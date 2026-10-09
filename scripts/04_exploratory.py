import importlib.util, pathlib
import pandas as pd
import numpy as np

_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

root = pathlib.Path(__file__).resolve().parent.parent
pathlib.Path(root / 'results').mkdir(exist_ok=True)

d = pd.read_csv(root / 'data' / 'clean.csv')
for c in ['Finished', 'rep', 'dem', 'post_trust', 'pre_trust']:
    d[c] = pd.to_numeric(d[c], errors='coerce')

h1 = reg.HYPOTHESES[0]

# E1: robustness of the planned H1 estimates to dropping unfinished responses
orig = reg.reestimate(h1, d)
fin = d[d['Finished'] == 1]
alt = reg.reestimate(h1, fin)
m = orig[['term', 'arm', 'estimate', 'std_error', 'p_value', 'n']].merge(
    alt[['arm', 'estimate', 'std_error', 'p_value', 'n']],
    on='arm', suffixes=('_original', '_finished_only'))
m = m[m['arm'].notna()].copy()
m['se_ratio'] = m['std_error_finished_only'] / m['std_error_original']
sample_change = 1 - len(fin) / len(d)
if (m['se_ratio'].max() > 2 or m['se_ratio'].min() < 0.5) and sample_change < 0.10:
    print('E1 dropped: standard errors changed by more than a factor of two')
else:
    m.to_csv(root / 'results' / 'E1_finished_only.csv', index=False)
    r = np.corrcoef(m['estimate_original'], m['estimate_finished_only'])[0, 1]
    nsig_o = int((m['p_value_original'] < 0.05).sum())
    nsig_a = int((m['p_value_finished_only'] < 0.05).sum())
    print(f"E1 Planned H1 with unfinished responses dropped: {len(m)} arm estimates; "
          f"correlation of arm estimates with the original {r:.3f}; "
          f"{nsig_o} arms significant at p<0.05 originally versus {nsig_a} after dropping "
          f"{sample_change*100:.1f}% of rows; median SE ratio {m['se_ratio'].median():.2f}")

# E2: heterogeneity of the planned H1 effects by Republican party identification
het = reg.reestimate(h1, d, moderator='rep')
het = het[het['arm'].notna()].copy() if 'arm' in het.columns else het
het.to_csv(root / 'results' / 'E2_party_interaction.csv', index=False)
pcol = 'p_value' if 'p_value' in het.columns else het.columns[-1]
n_tot = len(het)
n_sig = int((het[pcol] < 0.05).sum())
print(f"E2 Arm-by-Republican interactions on trust in science: {n_sig} of {n_tot} "
      f"interaction estimates have p<0.05, about what chance alone would give at 5% "
      f"(planned H1 arm contrasts only, no further tests)")
