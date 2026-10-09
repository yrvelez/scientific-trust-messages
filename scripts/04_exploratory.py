import importlib.util, pathlib
import numpy as np
import pandas as pd

_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

ROOT = pathlib.Path(__file__).resolve().parent.parent
RES = ROOT / 'results'
RES.mkdir(exist_ok=True)

d = pd.read_csv(ROOT / 'data' / 'clean.csv', low_memory=False)
for c in ['Finished', 'gender', 'post_science_1', 'post_trust', 'pre_trust']:
    d[c] = pd.to_numeric(d[c], errors='coerce')

H1 = [h for h in reg.HYPOTHESES if h['id'] == 'H1'][0]


def n_sig(df, pcol='p_value'):
    return int((pd.to_numeric(df[pcol], errors='coerce') < 0.05).sum())


# E1: robustness to dropping respondents who did not finish the survey
try:
    orig = reg.reestimate(H1, d)
    sub = d[d['Finished'] == 1]
    rob = reg.reestimate(H1, sub)
    keep = ['term', 'arm', 'estimate', 'std_error', 'p_value', 'conf_low', 'conf_high', 'n']
    o = orig[keep].rename(columns={c: f'orig_{c}' for c in keep if c not in ('term', 'arm')})
    r = rob[keep].rename(columns={c: f'compl_{c}' for c in keep if c not in ('term', 'arm')})
    t = o.merge(r, on=['term', 'arm'], how='outer')
    t.insert(0, 'analysis', 'E1')
    t.to_csv(RES / 'E1_completers_robustness.csv', index=False)
    ratio = (t['compl_std_error'] / t['orig_std_error']).dropna()
    nchg = 1 - len(sub) / len(d)
    print(f"E1 Robustness to finishers-only sample: {n_sig(rob)} of {len(rob)} arm estimates p<0.05 "
          f"(original {n_sig(orig)}); sample change {nchg:.1%}, SE ratio range {ratio.min():.2f}-{ratio.max():.2f}")
except Exception as e:
    print(f"E1 Robustness to finishers-only sample: failed ({e})")

# E2: heterogeneity by the gender column (0/1 coded: 1 = first code, 2 = second code)
try:
    d['gender_second'] = (d['gender'] == 2).astype(int)
    het = reg.reestimate(H1, d, moderator='gender_second')
    het.insert(0, 'analysis', 'E2')
    het.to_csv(RES / 'E2_gender_heterogeneity.csv', index=False)
    print(f"E2 Heterogeneity by gender column: {n_sig(het)} of {len(het)} arm-by-group interactions p<0.05 "
          f"across 32 arms tested (no correction)")
except Exception as e:
    print(f"E2 Heterogeneity by gender column: failed ({e})")

# E3: component item post_science_1 as outcome, same registered specification
try:
    h = dict(H1, outcome='post_science_1')
    comp = reg.reestimate(h, d)
    comp.insert(0, 'analysis', 'E3')
    comp.to_csv(RES / 'E3_component_post_science_1.csv', index=False)
    tr = comp[comp['term'].astype(str).str.contains('T\\.')]
    print(f"E3 Component item post_science_1: {n_sig(tr)} of {len(tr)} arm estimates p<0.05 "
          f"(mean estimate {pd.to_numeric(tr['estimate'], errors='coerce').mean():.3f})")
except Exception as e:
    print(f"E3 Component item post_science_1: failed ({e})")
