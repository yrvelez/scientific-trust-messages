import importlib.util, pathlib
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

pathlib.Path('results').mkdir(exist_ok=True)
pathlib.Path('figures').mkdir(exist_ok=True)

d = pd.read_csv('data/clean.csv')
for c in d.columns:
    if c not in ('arm', 'arm_code', 'StartDate', 'EndDate', 'UserLanguage'):
        d[c] = pd.to_numeric(d[c], errors='coerce')

H1 = reg.HYPOTHESES[0]
out = []

# E1: component item as outcome. Rationale: shows whether the planned trust effect
# is mirrored in a separate post-treatment science item (post_science_1, label not in codebook).
try:
    h = dict(H1, outcome="post_science_1")
    r = reg.reestimate(h, d)
    r.to_csv('results/E1_component_post_science_1.csv', index=False)
    n_sig = int((r['p_value'] < 0.05).sum())
    print(f"E1 Component item post_science_1 as outcome: {n_sig} of {len(r)} arm estimates have p<0.05 "
          f"(range of estimates {r['estimate'].min():.3f} to {r['estimate'].max():.3f}; "
          f"{len(r)} arm estimates tested)")
    out.append(dict(id="E1", title="Component item post_science_1 as outcome",
                    rationale="Shows whether the planned trust effect is mirrored in a separate post-treatment science item.",
                    method="Each message arm was compared with the control using the planned model, with a separate post-treatment science item as the outcome.",
                    table="results/E1_component_post_science_1.csv", figure=None,
                    finding=f"{n_sig} of {len(r)} arm estimates have p<0.05, estimates range {r['estimate'].min():.3f} to {r['estimate'].max():.3f}"))
except Exception as e:
    print("E1 failed:", e)

# E2: heterogeneity by party identification (rep column, 0/1).
# Rationale: partisanship is the most likely source of differential response to trust messages.
try:
    r = reg.reestimate(H1, d, moderator="rep")
    r.to_csv('results/E2_heterogeneity_rep.csv', index=False)
    n_sig = int((r['p_value'] < 0.05).sum())
    print(f"E2 Heterogeneity by rep: {n_sig} of {len(r)} arm-by-moderator interactions have p<0.05 "
          f"(minimum p {r['p_value'].min():.3f}; {len(r)} interactions tested)")
    out.append(dict(id="E2", title="Heterogeneity of planned effects by Republican identification",
                    rationale="Partisanship is the most likely source of differential response to trust messages.",
                    method="The arm-by-subgroup difference in the planned model was estimated, comparing Republican-identifying respondents with others.",
                    table="results/E2_heterogeneity_rep.csv", figure=None,
                    finding=f"{n_sig} of {len(r)} arm-by-group interactions have p<0.05 (minimum p {r['p_value'].min():.3f})"))
except Exception as e:
    print("E2 failed:", e)

pd.DataFrame(out).to_csv('results/exploratory_index.csv', index=False)
