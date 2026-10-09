"""Pool the adaptive batches of "Scientific Trust Messages" into the filedrawer pipeline input.

Reads the raw Qualtrics exports in inputs/raw/ (gitignored: they carry Lucid respondent ids, ZIP codes and
free text), drops every identifier and free-text column, and writes inputs/pipeline_input.csv with:

- batch: the fielding batch, from the survey each response came from (see BATCHES);
- arm: the message, A1 = pure control ("Please continue to the next page."), A2-A33 = the student messages;
- screener_pass: passed the pre-treatment attention check (registered exclusion);
- pre_trust / post_trust: the registered 6-item trust-in-science scale, mean of the items with the three
  negatively worded items (4-6) reverse-coded, 1-5;
- covariates named in the registration (age, education, race, party), coded from Lucid's standard codes;
- ipw: 1 / the arm's share among the responses assigned in the same batch. The per-batch assignment
  probabilities came from the authors' server and were not stored with the responses, so each batch's realized
  shares stand in for them.
"""
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).parent
RAW = HERE / "inputs" / "raw"
# Qualtrics survey -> batch. "Final" is the equal-probability burn-in that opened the registered study
# (osf.io/5yvh9, registered 2021-11-20); the earlier "Scientific Trust Messages" and "(Abbreviated)" surveys
# predate the registration and are not part of it.
BATCHES = [("stm_final.csv", 1), ("stm_batches2plus.csv", 2), ("stm_batch3.csv", 3), ("stm_batch4.csv", 4),
           ("stm_batch5.csv", 5), ("stm_batch6.csv", 6), ("stm_batch7.csv", 7)]
DROP = ["IPAddress", "RecipientLastName", "RecipientFirstName", "RecipientEmail", "ExternalReference",
        "LocationLatitude", "LocationLongitude", "ResponseId", "rid", "zip", "text1", "text_2", "student",
        "content", "random", "DistributionChannel"]
VAX = {"vax_attitudes_1": "vax_safe", "vax_attitudes_2": "vax_effective", "vax_attitudes_3": "vax_fear"}

frames, missing = [], []
for name, b in BATCHES:
    f = RAW / name
    if not f.exists():
        missing.append(name)
        continue
    d = pd.read_csv(f, skiprows=[1, 2], dtype=str, keep_default_na=True)
    d.insert(0, "batch", b)
    frames.append(d.drop(columns=[c for c in DROP if c in d.columns]))
if missing:
    print(f"missing exports (not pooled): {', '.join(missing)}")
df = pd.concat(frames, ignore_index=True).rename(columns=VAX)      # the pipeline adds row_id itself

num = pd.to_numeric(df["num"], errors="coerce")
df["arm"] = np.where(num.notna(), "A" + num.astype("Int64").astype(str), None)
df = df.drop(columns=["num"])

pick = df[[f"screener_{i}" for i in range(1, 6)]].notna()
df["screener_pass"] = (pick["screener_1"] & pick["screener_2"] & ~pick[["screener_3", "screener_4", "screener_5"]].any(axis=1)).astype(int)

for t in ("pre", "post"):
    items = df[[f"{t}_science_{i}" for i in range(1, 7)]].apply(pd.to_numeric, errors="coerce")
    for i in (4, 5, 6):
        items[f"{t}_science_{i}"] = 6 - items[f"{t}_science_{i}"]
    df[f"{t}_trust"] = items.mean(axis=1, skipna=False)        # complete items only (listwise, as registered)

# Lucid standard codes: ethnicity 1 = White; hispanic 1 = not Hispanic, 2-14 = a Hispanic origin;
# political_party 1-3 = Democrat (strong, not strong, leaning), 5-7 = Republican, 4 = independent, 8+ = other/none
eth, hisp, party = (pd.to_numeric(df[c], errors="coerce") for c in ("ethnicity", "hispanic", "political_party"))
df["white"] = np.where(eth.notna(), (eth == 1).astype(float), np.nan)
df["latino"] = np.where(hisp.notna(), hisp.between(2, 14).astype(float), np.nan)
df["dem"] = np.where(party.notna(), party.between(1, 3).astype(float), np.nan)
df["rep"] = np.where(party.notna(), party.between(5, 7).astype(float), np.nan)
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["education"] = pd.to_numeric(df["education"], errors="coerce").where(lambda s: s > 0)

assigned = df["arm"].notna()
share = df[assigned].groupby("batch")["arm"].value_counts(normalize=True)
df["ipw"] = [1 / share[(b, a)] if a is not None else np.nan for b, a in zip(df["batch"], df["arm"])]

out = HERE / "inputs" / "pipeline_input.csv"
df.to_csv(out, index=False)
sample = (df.Finished == "1") & (df.screener_pass == 1) & assigned & df.post_trust.notna()
print(f"wrote {out.relative_to(HERE)}: {len(df)} rows from {len(frames)} batches; "
      f"finished, attentive and assigned with the outcome: {int(sample.sum())}")
print(df[assigned].groupby("batch")["arm"].agg(["size", "nunique"]).to_string())
