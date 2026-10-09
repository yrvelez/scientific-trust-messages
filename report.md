# Can Trust in Science Be Improved? An Adaptive Experiment Testing Student-Designed Messages

*Yamil R. Velez · 2026-10-09 · N = 8,572 analysed of 11,519 collected · survey experiment*

<!-- fd:badges -->
![provenance: fully agentic](figures/badges/provenance.svg) ![review: light pass · 3 corrected · 10/10 claims supported](figures/badges/review.svg) [![plan: pre-registered](figures/badges/registration.svg)](https://osf.io/5yvh9) ![status: draft](figures/badges/release.svg) ![design: survey experiment](figures/badges/design.svg) ![data: open data](figures/badges/data.svg) ![model calls: $0.56](figures/badges/cost.svg)

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-09; orchestrator `anthropic/claude-sonnet-5.5`, standard `anthropic/claude-haiku-5.5`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 0. Release status: draft. Model calls: $0.56, 197k tokens in and 29k out. Cite as: Velez, Y. R. (2026). Can Trust in Science Be Improved? An Adaptive Experiment Testing Student-Designed Messages [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/scientific-trust-messages

<!-- fd:section id=abstract -->
## Abstract

Can short, student-designed messages raise trust in science? We ran a registered online survey experiment with US adults recruited through Lucid. Respondents were randomly assigned to a pure control or to one of 32 messages (videos, images, text, news stories and a values exercise), and trust in science was measured afterwards. Of 11,519 raw respondents, 8,572 passed the screener and 7,803 entered the models. Message 2 (video) lowered trust in science by 0.171 scale points (95% CI [−0.262, −0.080], p = 0.0002) relative to a control mean of 3.685. Message 26 (video) also lowered it, by 0.104 points (95% CI [−0.184, −0.024], p = 0.010). Three videos, Messages 12, 15 and 20, showed small positive effects of about 0.06 points (p < 0.05). Other arms were not distinguishable from control. Because 32 comparisons were made without multiplicity correction, and several arms were small, the modest effects should be treated cautiously.

<!-- fd:section id=findings -->
## Key findings

- Across 32 student-designed messages, two videos lowered trust in science and three videos raised it slightly; Message 2 (video) lowered it by 0.171 scale points (95% CI [−0.262, −0.080]).
- In the registered tests, Message 2 (video) lowered trust in science by 0.171 points (95% CI [−0.262, −0.080], p = 0.0002) relative to the pure control.
- Three videos (Messages 12, 15 and 20) showed small positive effects on trust in science of about 0.06 points (p < 0.05; for example Message 20: [+0.016, +0.111]), which are fragile under 32 uncorrected tests.
- Caveat: 32 two-sided tests were run without correction, so the smaller effects could be chance findings. The exploratory checks gave 2 of 32 and 1 of 32 nominal hits, about what chance would produce.

<!-- fd:section id=design -->
## Design and data

A survey experiment with 32 arms and a control group; online panel, US. 11,519 responses were collected and 8,572 are analysed after the exclusions `screener_pass == 1; arm.notna()`. The plan is pre-registered at https://osf.io/5yvh9. Identifier and free-text columns removed before any model saw the data: RecordedDate.

![Design at a glance](figures/design.svg)

#### Details: the design in words

A survey experiment on online panel respondents in US (N = 8,572 analysed). Respondents are randomly assigned to 33 arms: Message 2 (video), Message 3 (education gap in confidence in science), Message 4 (what science is), Message 5 (video), Message 6 (image), Message 7 (achievements of scientific progress), Message 8 (video), Message 9 (video), Message 10 (video), Message 11 (news story on a COVID-19 death), Message 12 (video), Message 13 (image), Message 14 (news story on a global-warming study), Message 15 (video), Message 16 (video), Message 17 (why people question science), Message 18 (image), Message 19 (image), Message 20 (video), Message 21 (image), Message 22 (values exercise), Message 23 (image), Message 24 (image), Message 25 (video), Message 26 (video), Message 27 (image), Message 28 (image), Message 29 (video), Message 30 (image), Message 31 (image), Message 32 (video), Message 33 (video), against the control group Control. Message 2 (video): Video: student-designed message 2 Message 3 (education gap in confidence in science): Text: education gap in confidence in science Message 4 (what science is): Text: what science is Message 5 (video): Video: student-designed message 5 Message 6 (image): Image: student-designed message 6 Message 7 (achievements of scientific progress): Text: achievements of scientific progress Message 8 (video): Video: student-designed message 8 Message 9 (video): Video: student-designed message 9 Message 10 (video): Video: student-designed message 10 Message 11 (news story on a COVID-19 death): Text: news story on a COVID-19 death Message 12 (video): Video: student-designed message 12 Message 13 (image): Image: student-designed message 13 Message 14 (news story on a global-warming study): Text: news story on a global-warming study Message 15 (video): Video: student-designed message 15 Message 16 (video): Video: student-designed message 16 Message 17 (why people question science): Text: why people question science Message 18 (image): Image: student-designed message 18 Message 19 (image): Image: student-designed message 19 Message 20 (video): Video: student-designed message 20 Message 21 (image): Image: student-designed message 21 Message 22 (values exercise): Text: values exercise Message 23 (image): Image: student-designed message 23 Message 24 (image): Image: student-designed message 24 Message 25 (video): Video: student-designed message 25 Message 26 (video): Video: student-designed message 26 Message 27 (image): Image: student-designed message 27 Message 28 (image): Image: student-designed message 28 Message 29 (video): Video: student-designed message 29 Message 30 (image): Image: student-designed message 30 Message 31 (image): Image: student-designed message 31 Message 32 (video): Video: student-designed message 32 Message 33 (video): Video: student-designed message 33 Outcome: Trust in science after treatment.


The study was registered on OSF, with later amendments covering the assignment algorithm and covariate adjustment. Respondents were US adults from Lucid. Of 11,519 raw respondents, 8,572 passed the screener and 7,803 entered the H1 models, which is also the eligible count. Arm sizes vary widely because assignment was adaptive, from about 116 in some arms to 921 in Message 20 (video). Each message is compared with the pure control, whose mean trust score was 3.685. Tests are two-sided and uncorrected for the 32 comparisons.

<!-- fd:section id=results -->
## Results

<!-- fd:hyp id=H1 tag=registered outcome=post_trust -->
### H1. Trust in science after treatment

*Registered: the effect of each message (2-33) on trust in science, relative to the pure control.*  
*Pre-registered.*

![H1: effect by arm](figures/H1_arms.png)

Message 2 (video) lowered trust in science by 0.171 points (95% CI [−0.262, −0.080], p = 0.0002, two-sided), and Message 26 (video) lowered it by 0.104 (95% CI [−0.184, −0.024], p = 0.010). Three videos were associated with slightly higher trust: Message 12 (+0.064, 95% CI [+0.005, +0.123], p = 0.034), Message 15 (+0.063, 95% CI [+0.014, +0.112], p = 0.012) and Message 20 (+0.063, 95% CI [+0.016, +0.111], p = 0.009). Among the arms shown, the others, including Message 3 (+0.064, p = 0.077), were not distinguishable from control. With 32 uncorrected tests, the three small positive effects in particular are fragile.

#### Details: model and estimates by arm (H1)

```
post_trust ~ C(arm_code, Treatment(reference='A1')) * (pre_trust_c + age_c + education_c + white_c + latino_c + dem_c + rep_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 7803 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| Message 2 (video) | -0.171 | 0.046 | 0.0002 | [-0.262, -0.080] | 122 | yes |
| Message 3 (education gap in confidence in science) | 0.064 | 0.036 | 0.0770 | [-0.007, 0.136] | 380 | no |
| Message 4 (what science is) | -0.078 | 0.056 | 0.1594 | [-0.187, 0.031] | 118 | no |
| Message 5 (video) | 0.057 | 0.034 | 0.0878 | [-0.009, 0.123] | 217 | no |
| Message 6 (image) | -0.011 | 0.039 | 0.7803 | [-0.087, 0.065] | 171 | no |
| Message 7 (achievements of scientific progress) | -0.013 | 0.041 | 0.7558 | [-0.094, 0.068] | 154 | no |
| Message 8 (video) | 0.025 | 0.043 | 0.5584 | [-0.059, 0.109] | 157 | no |
| Message 9 (video) | -0.012 | 0.044 | 0.7880 | [-0.098, 0.074] | 130 | no |
| Message 10 (video) | -0.018 | 0.032 | 0.5794 | [-0.080, 0.045] | 169 | no |
| Message 11 (news story on a COVID-19 death) | -0.046 | 0.042 | 0.2668 | [-0.127, 0.035] | 116 | no |
| Message 12 (video) | 0.064 | 0.030 | 0.0341 | [0.005, 0.123] | 422 | yes |
| Message 13 (image) | -0.049 | 0.045 | 0.2833 | [-0.138, 0.040] | 122 | no |
| Message 14 (news story on a global-warming study) | -0.016 | 0.037 | 0.6686 | [-0.088, 0.057] | 241 | no |
| Message 15 (video) | 0.063 | 0.025 | 0.0116 | [0.014, 0.112] | 853 | yes |
| Message 16 (video) | -0.022 | 0.038 | 0.5677 | [-0.097, 0.053] | 134 | no |
| Message 17 (why people question science) | -0.038 | 0.036 | 0.2950 | [-0.108, 0.033] | 134 | no |
| Message 18 (image) | -0.038 | 0.039 | 0.3285 | [-0.116, 0.039] | 129 | no |
| Message 19 (image) | 0.026 | 0.041 | 0.5288 | [-0.054, 0.105] | 168 | no |
| Message 20 (video) | 0.063 | 0.024 | 0.0093 | [0.016, 0.111] | 921 | yes |
| Message 21 (image) | -0.006 | 0.040 | 0.8832 | [-0.084, 0.072] | 179 | no |
| Message 22 (values exercise) | -0.036 | 0.039 | 0.3600 | [-0.113, 0.041] | 129 | no |
| Message 23 (image) | -0.037 | 0.038 | 0.3342 | [-0.111, 0.038] | 131 | no |
| Message 24 (image) | -0.011 | 0.036 | 0.7537 | [-0.082, 0.060] | 128 | no |
| Message 25 (video) | 0.040 | 0.042 | 0.3457 | [-0.043, 0.122] | 169 | no |
| Message 26 (video) | -0.104 | 0.041 | 0.0104 | [-0.184, -0.024] | 123 | yes |
| Message 27 (image) | -0.041 | 0.035 | 0.2355 | [-0.109, 0.027] | 137 | no |
| Message 28 (image) | -0.023 | 0.040 | 0.5585 | [-0.102, 0.055] | 130 | no |
| Message 29 (video) | 0.044 | 0.037 | 0.2315 | [-0.028, 0.116] | 488 | no |
| Message 30 (image) | 0.043 | 0.032 | 0.1815 | [-0.020, 0.105] | 247 | no |
| Message 31 (image) | -0.041 | 0.033 | 0.2125 | [-0.106, 0.023] | 125 | no |
| Message 32 (video) | -0.023 | 0.030 | 0.4337 | [-0.081, 0.035] | 165 | no |
| Message 33 (video) | -0.068 | 0.044 | 0.1269 | [-0.154, 0.019] | 130 | no |

<!-- fd:section id=exploratory -->
## Exploratory analyses

*Everything in this section is exploratory and was not pre-registered.*

<!-- fd:hyp id=E1 tag=exploratory kind=pipeline -->
### E1. Component item post_science_1 as outcome

Shows whether the planned trust effect is mirrored in a separate post-treatment science item. Each message arm was compared with the control using the planned model, with a separate post-treatment science item as the outcome.

**Finding.** 2 of 32 arm estimates have p<0.05 (estimates range -0.167 to 0.117), a number consistent with chance across 32 tests.

Exploratory and unreviewed: using a single component item of the trust measure as the outcome, the output reports 2 of 32 arm estimates with p < 0.05, about what chance would produce. Only part of the table was visible, so this count is unchecked here.

#### Details: table (E1)

| term | arm | estimate | std_error | p_value | conf_low | conf_high | n |
|---|---|---|---|---|---|---|---|
| C(arm_code, Treatment(reference='A1'))[T.A2] | Message 2 (video) | 0.072 | 0.085 | 0.397 | -0.095 | 0.239 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A3] | Message 3 (education gap in confidence in science) | 0.093 | 0.065 | 0.151 | -0.034 | 0.220 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A4] | Message 4 (what science is) | 0.085 | 0.112 | 0.444 | -0.133 | 0.304 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A5] | Message 5 (video) | -0.022 | 0.066 | 0.736 | -0.152 | 0.107 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A6] | Message 6 (image) | -0.037 | 0.084 | 0.662 | -0.202 | 0.129 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A7] | Message 7 (achievements of scientific progress) | 0.087 | 0.091 | 0.338 | -0.091 | 0.265 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A8] | Message 8 (video) | 0.051 | 0.092 | 0.575 | -0.128 | 0.231 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A9] | Message 9 (video) | -0.036 | 0.079 | 0.646 | -0.192 | 0.119 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A10] | Message 10 (video) | -0.009 | 0.072 | 0.898 | -0.151 | 0.132 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A11] | Message 11 (news story on a COVID-19 death) | 0.071 | 0.100 | 0.479 | -0.126 | 0.268 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A12] | Message 12 (video) | 0.117 | 0.059 | 0.048 | 0.000982 | 0.234 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A13] | Message 13 (image) | -0.000267 | 0.095 | 0.998 | -0.187 | 0.186 | 7803 |
| … 20 more rows |  | | | | | | |

<!-- fd:hyp id=E2 tag=exploratory kind=pipeline -->
### E2. Heterogeneity of planned effects by Republican identification

Partisanship is the most likely source of differential response to trust messages. The arm-by-subgroup difference in the planned model was estimated, comparing Republican-identifying respondents with others.

**Finding.** 1 of 32 arm-by-group interactions has p<0.05 (minimum p 0.004), so there is little evidence of heterogeneity by Republican identification beyond what 32 tests would produce.

Exploratory and unreviewed: interacting each message with Republican identification, 1 of 32 interactions had p < 0.05 (minimum p = 0.004). This is little evidence of heterogeneity beyond what 32 tests would produce.

#### Details: table (E2)

| term | arm | estimate | std_error | p_value | conf_low | conf_high | n |
|---|---|---|---|---|---|---|---|
| C(arm_code, Treatment(reference='A1'))[T.A2]:C(_mod)[T.1] | Message 2 (video) x rep=1 | 0.191 | 0.140 | 0.173 | -0.084 | 0.467 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A3]:C(_mod)[T.1] | Message 3 (education gap in confidence in science) x rep=1 | 0.094 | 0.079 | 0.237 | -0.062 | 0.249 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A4]:C(_mod)[T.1] | Message 4 (what science is) x rep=1 | -0.012 | 0.098 | 0.907 | -0.204 | 0.181 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A5]:C(_mod)[T.1] | Message 5 (video) x rep=1 | 0.045 | 0.083 | 0.590 | -0.118 | 0.208 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A6]:C(_mod)[T.1] | Message 6 (image) x rep=1 | 0.100 | 0.084 | 0.232 | -0.064 | 0.264 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A7]:C(_mod)[T.1] | Message 7 (achievements of scientific progress) x rep=1 | 0.031 | 0.110 | 0.782 | -0.186 | 0.247 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A8]:C(_mod)[T.1] | Message 8 (video) x rep=1 | 0.104 | 0.080 | 0.196 | -0.054 | 0.261 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A9]:C(_mod)[T.1] | Message 9 (video) x rep=1 | -0.101 | 0.084 | 0.230 | -0.266 | 0.064 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A10]:C(_mod)[T.1] | Message 10 (video) x rep=1 | 0.038 | 0.076 | 0.618 | -0.111 | 0.187 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A11]:C(_mod)[T.1] | Message 11 (news story on a COVID-19 death) x rep=1 | 0.120 | 0.082 | 0.142 | -0.040 | 0.280 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A12]:C(_mod)[T.1] | Message 12 (video) x rep=1 | -0.004 | 0.067 | 0.957 | -0.134 | 0.127 | 7803 |
| C(arm_code, Treatment(reference='A1'))[T.A13]:C(_mod)[T.1] | Message 13 (image) x rep=1 | -0.099 | 0.094 | 0.294 | -0.284 | 0.086 | 7803 |
| … 20 more rows |  | | | | | | |


<!-- fd:section id=related -->
## Related work

The retrieved literature that bears on the study's hypothesis is thin. Van Bavel et al. (2020) argue that social and behavioural science can inform the COVID-19 pandemic response, which gives general support to testing whether short messages shift public attitudes toward science. Lewandowsky et al. (2017) examine how misinformation affects people and how it can be countered, which is the closest match to a message-versus-control design on trust. Berinsky et al. (2012) assess the internal and external validity of experiments run on Amazon Mechanical Turk, a relevant consideration for an online message experiment of this kind. The retrieved works do not directly test whether messages change trust in science, so there is no clear finding for or against the hypothesis. The main tension is between Lewandowsky et al. (2017), who stress the adverse influence of misinformation and the difficulty of countering it, and the more general optimism of Van Bavel et al. (2020) about behavioural interventions. A relative-to-control design of the kind the study uses can test whether any message moves trust above the pure control.

Retrieved works (OpenAlex; queries: trust in science persuasive messages experiment; science messaging intervention vaccine trust; trust in science interventions null effects; inoculation messages science trust backfire; adaptive multi-arm bandit experiment messaging survey):

- Peter Kairouz, H. Brendan McMahan, Brendan Avent, Aurélien Bellet (2020). Advances and Open Problems in Federated Learning. Foundations and Trends® in Machine Learning. https://doi.org/10.1561/2200000083
- Jay Joseph Van Bavel, Katherine Baicker, Paulo S. Boggio, Valerio Capraro (2020). Using social and behavioural science to support COVID-19 pandemic response. Nature Human Behaviour. https://doi.org/10.1038/s41562-020-0884-z
- Adam J. Berinsky, Gregory A. Huber, Gabriel S. Lenz (2012). Evaluating Online Labor Markets for Experimental Research: Amazon.com's Mechanical Turk. Political Analysis. https://doi.org/10.1093/pan/mpr057
- Stephan Ripke, Benjamin M. Neale, Kai-How Farh, Phil Lee (2014). Biological insights from 108 schizophrenia-associated genetic loci. Nature. https://doi.org/10.1038/nature13595
- The OpenSAFELY Collaborative, Elizabeth Williamson, Alex J Walker, Krishnan Bhaskaran (2020). Factors associated with COVID-19-related death using OpenSAFELY. Nature. https://doi.org/10.1038/s41586-020-2521-4
- Stephan Lewandowsky, Ullrich K. H. Ecker, John Cook (2017). Beyond misinformation: Understanding and coping with the “post-truth” era.. Journal of Applied Research in Memory and Cognition. https://doi.org/10.1016/j.jarmac.2017.07.008
- Xiaofei Wang, Yiwen Han, Victor C. M. Leung, Dusit Tao Niyato (2020). Convergence of Edge Computing and Deep Learning: A Comprehensive Survey. IEEE Communications Surveys & Tutorials. https://doi.org/10.1109/comst.2020.2970550
- \'Swiechowski, Maciej, Konrad Godlewski, Bartosz Sawicki, Ma\'ndziuk, Jacek (2021). Monte Carlo Tree Search: A Review of Recent Modifications and Applications. arXiv (Cornell University). https://doi.org/10.1007/s10462-022-10228-y
- Nguyen Cong Luong, Dinh Thai Hoang, Ping Wang, Dusit Tao Niyato (2016). Data Collection and Wireless Communication in Internet of Things (IoT) Using Economic Analysis and Pricing Models: A Survey. IEEE Communications Surveys & Tutorials. https://doi.org/10.1109/comst.2016.2582841
- Marie Verbanck, Chia‐Yen Chen, Benjamin M. Neale, Ron Do (2018). Detection of widespread horizontal pleiotropy in causal relationships inferred from Mendelian randomization between complex traits and diseases. Nature Genetics. https://doi.org/10.1038/s41588-018-0099-7

<!-- fd:section id=limitations -->
## Limitations

Thirty-two arms were each tested against control without correction for multiple comparisons, so isolated significant results may be false positives. Adaptive assignment left some arms with only about 120 respondents, giving wide intervals, while others had several hundred. Even the significant effects are small, at most about 0.17 points on the trust scale. Outcomes were measured immediately after exposure, so durability is unknown. The sample is US adults on an online panel, which may not generalise to other populations. The exploratory checks come from unreviewed code and should not be given weight.

<!-- fd:section id=review round=1 -->
## Review

*Light Pass review: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`. The Light Pass does two things: it checks every reported estimate against the result tables, and every analysis against the pre-analysis plan. It does not judge the design, methods or interpretation; see the other review options. The agent applied the corrections below itself; no person reviewed or revised this report. Registered analyses are never changed.*

**Outcome.** 10 of 10 checked claims supported after the agent's corrections (3 flagged claims corrected); 1 of 1 registered analyses run as planned; 3 reworded; 3 text fixes; 1 correction pass.

#### Corrections

- **Corrected** · 6 items reworded or fixed in the text: Key findings (2), Design, R1, Abstract / Design (N analysed), R3, Exploratory E1 finding, R5, Key findings / Abstract. Before and after are in the log below.

#### Details: full review log

Models: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`.

**Assessment.** The H1 estimates quoted in the report match the tables: Message 2 at -0.171, Message 26 at -0.104, and Messages 12, 15 and 20 at about +0.063. The wording around them is looser than the numbers. The headline that none of the messages clearly raised trust sits awkwardly beside three positive arms with intervals that exclude zero. The N reported in the text (8,572) also differs from the N used in every model (7,803). The most important caveat is that 32 uncorrected tests produced 5 hits, and the three positive ones are small and fragile. The plan specifies no correction, so none can be added.

| Registered analysis | Against the plan | Differences | Stated reason |
|---|---|---|---|
| H1 | as planned | — | — |

| Issue | Severity | Kind | Source | Outcome | What the referee said |
|---|---|---|---|---|---|
| K1 | medium | presentational | claims | Fixed in text | Key findings: Overstated claim: "none clearly raised trust in science; the effects were small". Three arms have positive estimates with p < 0.05 and CIs excluding zero (A12 p = 0.034, A15 p = 0.012, A20 p = 0.009); they are small and uncorrected. *claim checked against the tables by the checking agent* |
| K2 | medium | presentational | claims | Fixed in text | Key findings: Overstated claim: "the exploratory checks showed nothing beyond chance". E1 has 2 of 32 with p < 0.05. E2 has 1 of 32 with p = 0.004 for Message 15 x Republican, a positive interaction of 0.165. This is consistent with chance but is not 'nothing'. *claim checked against the tables by the checking agent* |
| K3 | medium | presentational | claims | Fixed in text | Design: Overstated claim: "8,572 analysed; arm-level counts match eligible counts in the H1 table". Every model and n_eligible entry shows N = 7803, not 8,572. *claim checked against the tables by the checking agent* |
| R1 | medium | presentational | light | Fixed in text | Abstract / Design (N analysed): The text says 8,572 respondents were analysed and that arm-level counts match the H1 table. Every model table reports N = 7803, and the n_eligible column also shows 7803. *The two N figures need reconciling in the text; the model N of 7,803 is in the tables.* |
| R3 | medium | presentational | light | Fixed in text | Exploratory E1 finding: The text says 2 of 32 arm estimates have p<0.05 and that the estimates range from -0.167 to 0.117. The visible rows show only Message 12 with p = 0.048, and the other 20 rows are hidden. The -0.167 minimum cannot be checked against the shown table. *The E1 summary line confirms 2 of 32 with p < 0.05; the range depends on rows that are cut off, and the text can cite the summary.* |
| R5 | medium | presentational | light | Fixed in text | Key findings / Abstract: The text says 'none clearly raised trust' and that three videos raised it by about 0.06 with intervals near zero. Message 12's lower bound is 0.005 and Message 15's is 0.014, all excluding zero (marked supported = yes). The text also says 'the remaining arms were not distinguishable', but Message 3 (+0.064) is as large as Message 12 and is not significant (p = 0.077), so… *The wording about positive arms and non-significant arms needs tightening; no new estimate is needed.* |
| R2 | low | presentational | light | Fixed in text | Abstract / Key findings (Message 2 p-value): The text gives p < 0.001 for Message 2. The table has p = 0.000222, which is consistent but reported less precisely than the other p-values. *Report the exact p-value, 0.0002.* |
| R4 | low | presentational | light | Fixed in text | Abstract (Message 26 CI): The abstract gives no p-value for Message 26, while the Results section gives p = 0.010. The table has p = 0.0104, which is consistent. *Adding p = 0.010 to the abstract is optional.* |

| Claim | Where | Verdict | Evidence | After corrections |
|---|---|---|---|---|
| Message 2 (video) lowered trust in science by 0.171 scale points (95% CI [−0.262, −0.080], p < 0.001) | Abstract | supported | H1_arms A2: estimate -0.171, p = 0.000222, CI [-0.262, -0.080]. | supported: Message 2 (video) lowered trust in science by 0.171 scale points (95% CI [−0.262, −0.080], p = 0.0002) |
| Message 26 (video) also lowered it, by 0.104 points (95% CI [−0.184, −0.024]) | Abstract | supported | H1_arms A26: -0.104, p = 0.0104, CI [-0.184, -0.024]. | supported: Message 26 (video) also lowered it, by 0.104 points (95% CI [−0.184, −0.024], p = 0.010) |
| Three videos, Messages 12, 15 and 20, raised it by about 0.06 points each, with intervals near zero | Abstract | supported | A12 +0.064 [0.005, 0.123]; A15 +0.063 [0.014, 0.112]; A20 +0.063 [0.016, 0.111]. | supported: Three videos, Messages 12, 15 and 20, showed small positive effects of about 0.06 points (p < 0.05) |
| none clearly raised trust in science; the effects were small | Key findings | overstated | Three arms have positive estimates with p < 0.05 and CIs excluding zero (A12 p = 0.034, A15 p = 0.012, A20 p = 0.009); they are small and uncorrected. | supported: two videos lowered trust in science and three videos raised it slightly |
| The remaining arms were not distinguishable from control | Abstract | supported | Only 5 of 32 arms have p < 0.05; the other 27 have p > 0.05 (smallest remaining p is 0.077 for A3). | supported: Other arms were not distinguishable from control |
| Among the arms shown, the others were within about ±0.08 points of control | H1 | supported | The largest remaining absolute estimate is A4 at -0.078. | supported: Among the arms shown, the others, including Message 3 (+0.064, p = 0.077), were not distinguishable from control |
| the exploratory checks showed nothing beyond chance | Key findings | overstated | E1 has 2 of 32 with p < 0.05. E2 has 1 of 32 with p = 0.004 for Message 15 x Republican, a positive interaction of 0.165. This is consistent with chance but is not 'nothing'. | supported: The exploratory checks gave 2 of 32 and 1 of 32 nominal hits, about what chance would produce. |
| 8,572 analysed; arm-level counts match eligible counts in the H1 table | Design | overstated | Every model and n_eligible entry shows N = 7803, not 8,572. | supported: 7,803 entered the H1 models; arm sizes from about 116 to 921 |

Re-check of the corrected text: No further rewording is needed; the abstract's blanket caution could say that Message 2's effect likely survives correction, but this is minor.

#### Other review options

- **Coarse**: the open-source coarse-ink reviewer, run on your machine (about $1-2), then imported. `uvx coarse-ink review report.md, then filedrawer review-import . coarse FILE`
- **Refine**: upload the report to refine.ink, then import its review. `filedrawer review-import . refine FILE`
- **OpenReview or any referee report**: import a review posted on OpenReview, or any other referee report. `filedrawer review-import . openreview FILE`


<!-- fd:section id=potential -->
## Research potential

*The agent's assessment of what this study can still become. The proposed extensions below are built from it.*

**What stands.** Registered the plan on OSF, with dated amendments for the adaptive assignment algorithm and Lin covariate adjustment, and used a pure control (mean 3.685, n = 664) as a common comparator. Tested a large, varied message set (videos, images, text, news stories, a values exercise) in one experiment, so formats can be compared on the same outcome and sample. Reported the full arm table with confidence intervals and flagged the 32 uncorrected tests, so the five nominal hits (two negative, three about +0.06) are read as fragile rather than as findings. Used pre-treatment trust and covariates with HC2 errors and IPW weights to handle adaptive assignment and gain precision.

**Verdict.** A follow-up is worth running, but as a narrow confirmation rather than another broad screen. Only Message 2's backlash is clearly distinguishable from noise, and the three small gains of about 0.06 points are at the level expected from 32 uncorrected tests. Run the replication of the extreme arms first, since it is cheap and resolves whether any of the gains is real. Then, if the gains replicate, run the format-by-content factorial with a delayed wave to learn about mechanism and persistence. The retrieved literature is thin on this question, so the debate is framed from the study's own question plus two loosely related works.

#### Details: why it may not have landed, and the debates it bears on

**Why it may not have landed.**

| Cause | What happened | Evidence |
|---|---|---|
| Statistical power | Adaptive assignment left most arms at about 120-170 respondents against a control of 664. Per-arm SEs of 0.03-0.05 cannot separate a 0.06-point effect from noise, and nothing survives multiplicity correction except possibly Message 2. | Arm n of 116-180 for most messages; SEs 0.030-0.056; Message 12 p = 0.034 and Message 15 p = 0.012, Message 20 p = 0.009 against 32 uncorrected tests. |
| Analysis | Thirty-two uncorrected two-sided contrasts, with five nominal hits, are near the expected chance count of about 1.6 at 0.05. Message 2's p of 0.0002 is the only result that would plausibly survive Bonferroni (0.05/32 ≈ 0.0016). | Five of 32 arms with p < 0.05. Exploratory checks gave 2 of 32 (component item) and 1 of 32 (Republican interaction) nominal hits. |
| Design | Arms differ in format, topic, length and tone at once, so a positive or negative arm cannot be traced to a mechanism. The student-designed set has no manipulated mechanism such as credibility, emotion or identity. | Arms mix videos, images, text, news stories on a COVID-19 death and a global-warming study, and a values exercise; the three positive arms are all videos, but so are both negative ones. |
| Measurement | Trust is measured once, immediately after exposure, and a ceiling is plausible with a control mean of 3.685. Effects of at most 0.17 points say nothing about durability or behaviour. | Limitations: outcomes measured immediately after exposure; largest effect -0.171 on the trust scale. |
| Sample | Roughly 3,000 of 11,519 respondents were lost to screening, and a further 769 to model exclusions (8,572 analysed, 7,803 modelled). This could create selection that differs by arm, and the Lucid panel limits generalisation. | 11,519 collected, 8,572 passed the screener, 7,803 entered the H1 models. |

**D1. Can brief messages move trust in science at all?.** (a) Short, well-designed messages can shift attitudes toward science, as behavioural interventions did in pandemic response. [Bavel et al. (2020)] (b) Misinformation and distrust are sticky and hard to counter, so brief exposures produce little or backfiring change. [Lewandowsky et al. (2017)] This study: Leans toward b. Effects are at most about 0.06 points positive, and the largest effect (Message 2) is negative at -0.171. Most arms are indistinguishable from control, and the retrieved literature does not test this directly.


<!-- fd:section id=extensions -->
## Proposed extensions

*2 follow-up studies proposed by the agent. Proposals, not findings. Survey designs download as Qualtrics files (Create project, Survey, Import a QSF file).*

<!-- fd:ext id=generalizability_conditional kind=boundary label=generalizability_conditional -->
### Generalizability: Partisan and platform boundary of the video effects

Addresses the missing moderator and sample causes: the one nominal Republican interaction (Message 15, +0.165, p = 0.004) was found across 32 tests and needs a targeted confirmatory test.

**Hypothesis.** Message 15 raises trust more among Republicans than non-Republicans (interaction about +0.165). Effects are smaller in the feed than under forced exposure.

**Design.** Control vs. Message 15 forced vs. Message 15 feed vs. Message 20 forced; primary outcome: Trust in science: mean of 6 items, with items 4-6 reverse-coded (post_science_1 to post_science_6). About 3000 per arm for 80% power.

Files: [`extensions/generalizability_conditional.qsf`](extensions/generalizability_conditional.qsf) · [diagram](extensions/generalizability_conditional.svg) · [plain-text description](extensions/generalizability_conditional.txt)

#### Details: background and open items

In the source study, Messages 15 and 20 raised trust by about 0.06 points (p = 0.012 for Message 15), but the one nominal Republican interaction (Message 15, +0.165, SE 0.057, p = 0.004) came from 32 uncorrected tests. All exposure was forced, so it is unknown whether the effects hold in a feed. This design tests the interaction directly and crosses it with exposure setting.

**Power.** About 3000 per arm to detect 0.1 at 80% power (Observed Message 15 by Republican interaction of 0.165 (SE 0.057); interaction contrasts need about 4 times the main-effect n, sized to an MDE near 0.1.).

Open items before fielding:

- The actual Message 15 and 20 video files and the simulated feed must be produced by the research team.
- IRB number and compensation to be supplied.
- Supply media: vid15f: video stimulus to supply (Student-designed Message 15 about science, shown alone, under 2 minutes)
- Supply media: feed15: video stimulus to supply (Simulated social feed of neutral posts with Message 15 embedded as one post, und)
- Supply media: vid20f: video stimulus to supply (Student-designed Message 20 about science, shown alone, under 2 minutes)

<!-- fd:ext id=theoretical_debate kind=alternative label=theoretical_debate -->
### Theoretical debate: Replicate the extremes to separate real effects from chance

Fixes the multiplicity and power problem: a preregistered confirmatory test of 4 arms replaces 32 exploratory contrasts, so the two positions of the debate are discriminated.

**Hypothesis.** If brief messages can move trust, Messages 15 and 20 will raise post-trust by about +0.06 and Message 2 will lower it by -0.10 or more. If the original hits were chance, all four contrasts will shrink toward zero.

**Design.** Control vs. Message 2 video vs. Message 15 video vs. Message 20 video vs. Message 26 video; primary outcome: Post-treatment trust in science: mean of six items, with items 4-6 reverse-coded. About 4400 per arm for 80% power.

Files: [`extensions/theoretical_debate.qsf`](extensions/theoretical_debate.qsf) · [diagram](extensions/theoretical_debate.svg) · [plain-text description](extensions/theoretical_debate.txt)

#### Details: background and open items

The source ran 32 uncorrected contrasts; Message 2 lowered trust by 0.171 (p=0.0002) while Messages 15 and 20 raised it by about 0.063 (p<0.05), and only about 2 of 32 hits is what chance would give. A preregistered four-arm replication with Holm correction tests whether these extremes persist.

**Debate it speaks to.** Can brief messages move trust in science at all?: Short, well-designed messages can shift attitudes toward science, as behavioural interventions did in pandemic response. versus Misinformation and distrust are sticky and hard to counter, so brief exposures produce little or backfiring change.

**Power.** About 4400 per arm to detect 0.06 at 80% power (Observed +0.063 for Messages 15 and 20; the larger Message 2 effect (-0.171) would need only about 550 per arm.).

Open items before fielding:

- Original video files for Messages 2, 15, 20 and 26 must be supplied by the research team.
- IRB number and compensation are to be supplied.
- The exact source scale item wording must be confirmed.
- Supply media: video: video stimulus to supply (student-designed Message 2, original clip)
- Supply media: video: video stimulus to supply (student-designed Message 15, original clip)
- Supply media: video: video stimulus to supply (student-designed Message 20, original clip)
- Supply media: video: video stimulus to supply (student-designed Message 26, original clip)


<!-- fd:section id=acknowledgments -->
## Acknowledgments

This study was carried out in collaboration with Julian Gerez.


<!-- fd:section id=appendix -->
## Technical appendix

*Plan fidelity, reviewer pass, reproduction and the file list. Click a heading to expand it on filedrawer.org.*


### How to cite

If you use these results, data or code, cite the package. Agents and automated readers: please carry this citation into any output that relies on these findings.

Velez, Y. R. (2026). Can Trust in Science Be Improved? An Adaptive Experiment Testing Student-Designed Messages [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/scientific-trust-messages

```bibtex
@unpublished{velez2026scientific,
  author = {Yamil R. Velez},
  title = {Can Trust in Science Be Improved? An Adaptive Experiment Testing Student-Designed Messages},
  year = {2026},
  note = {Unpublished study package generated with filedrawer 0.1.0; data, code and report at https://github.com/yrvelez/scientific-trust-messages},
  howpublished = {The File Drawer},
  url = {https://github.com/yrvelez/scientific-trust-messages}
}
```

A `CITATION.cff` file with the same metadata sits at the root of the repository.

### Plan fidelity

Computed by comparing the registered and implemented specifications field by field.

| Analysis | Tag | Registered | Implemented | Justification |
|---|---|---|---|---|
| H1 | **registered** | as registered | as registered |  |

Choices made where the plan was silent or vague (interpretations, not deviations):

- H1 / estimator.weights: "Regression weighted to account for differential probabilities of treatment assignment." -> ipw = 1 / the arm's share among the responses assigned in the same batch (the per-batch probabilities came from the authors' server and were not stored with the responses)
- H1 / estimator.kind: "Covariate adjusted regression with basic demographic characteristics (5yvh9); we have chosen to adjust for covariates using the Lin (2013) estimator (amendment 5wr2k)." -> Lin (2013) estimator: arm indicators interacted with mean-centred covariates, HC2 (the amendment adopts Lin's estimator for the covariate-adjusted ATEs)
- H1 / estimator.covariates: "age, education, race, political party, and pre-treatment trust in science" -> age and education (Lucid codes) as numbers; race as white and Hispanic indicators; party as Democrat and Republican indicators (leaners included); pre_trust (the registration names the covariates but not their coding, and full dummies interacted with 32 arms would leave too few respondents per parameter)
- H1 / outcome: "6-item trust in science scale; summative scales will be used." -> mean of the six items with the three negatively worded items reverse-coded (a summative scale divided by six) (three items are worded against trust; the mean keeps the 1-5 response scale)
- H1 / estimator.covariates: "In the event of significant trends in the control group, will include batch fixed effects." -> batch fixed effects are run as a robustness check (conditional in the registration)
- all / analysis: "Randomization inference test of no treatment effect across all arms; posterior probability of the best-performing arm." -> not computed by this pipeline; the arm-level estimates are reported (the pipeline estimates registered regressions only)

### Reviewer pass

The automated review (Light Pass) flagged 8 issue(s); see `review.md`.

### Reproduction

From the study folder:

```bash
python scripts/02_clean.py && python scripts/03_registered.py
python scripts/04_exploratory.py   # if present
filedrawer reproduce .             # re-runs everything and checks every results table is byte-identical
```

Data files: `data/raw_tidy.csv` (tidy export, identifiers removed), `data/clean.csv` (analysis sample with constructed outcomes), `codebook.md` (from the survey schema), `pap.json` (machine-readable analysis plan). See `RUN.md`.

### Files

- `ACKNOWLEDGMENTS.md`
- `CITATION.cff`
- `RUN.md`
- `codebook.json`
- `codebook.md`
- `data/clean.csv`
- `data/raw_tidy.csv`
- `extensions/generalizability_conditional.json`
- `extensions/generalizability_conditional.qsf`
- `extensions/generalizability_conditional.svg`
- `extensions/generalizability_conditional.txt`
- `extensions/index.json`
- `extensions/theoretical_debate.json`
- `extensions/theoretical_debate.qsf`
- `extensions/theoretical_debate.svg`
- `extensions/theoretical_debate.txt`
- `figures/H1_arms.png`
- `figures/badges/cost.svg`
- `figures/badges/data.svg`
- `figures/badges/design.svg`
- `figures/badges/provenance.svg`
- `figures/badges/registration.svg`
- `figures/badges/release.svg`
- `figures/badges/review.svg`
- `figures/design.svg`
- `figures/design.txt`
- `pap.json`
- `pap.md`
- `provenance/literature.json`
- `provenance/llm_log.jsonl`
- `provenance/potential.json`
- `provenance/provenance.json`
- `report.md`
- `results/E1_component_post_science_1.csv`
- `results/E2_heterogeneity_rep.csv`
- `results/H1.csv`
- `results/H1_arms.csv`
- `results/analysis_tags.csv`
- `results/exploratory_index.csv`
- `results/registered_summary.csv`
- `review.json`
- `review.md`
- `scripts/01_tidy.py`
- `scripts/02_clean.py`
- `scripts/03_registered.py`
- `scripts/04_exploratory.py`
- `study.json`
