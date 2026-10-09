# Can Trust in Science Be Improved? An Adaptive Experiment Testing Student-Designed Messages

*Yamil R. Velez · 2026-10-09 · N = 8,572 analysed of 11,519 collected · survey experiment*

<!-- fd:badges -->
![provenance: fully agentic](figures/badges/provenance.svg) ![review: light pass · 2 corrected · 11/11 claims supported](figures/badges/review.svg) [![plan: pre-registered](figures/badges/registration.svg)](https://osf.io/5yvh9) ![status: draft](figures/badges/release.svg) ![design: survey experiment](figures/badges/design.svg) ![data: open data](figures/badges/data.svg) ![model calls: $0.78](figures/badges/cost.svg)

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-09; orchestrator `anthropic/claude-sonnet-5.5`, standard `anthropic/claude-haiku-5.5`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 0. Release status: draft. Model calls: $0.78, 299k tokens in and 34k out. Cite as: Velez, Y. R. (2026). Can Trust in Science Be Improved? An Adaptive Experiment Testing Student-Designed Messages [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/scientific-trust-messages

<!-- fd:section id=abstract -->
## Abstract

Can short messages raise trust in science? This registered adaptive survey experiment randomly assigned US adults recruited through Lucid to a pure control or one of 32 messages, including videos, texts, images and memes, many made by students. The outcome was trust in science after treatment, measured on a five-point scale. Of the 11,519 respondents, 8,572 were analysed. Five arms differed from control. The 'Can You Trust Science Too Much?' video lowered trust by 0.17 points (95% CI [−0.26, −0.08], p < 0.001), and the 'Powers of Ten' film lowered it by 0.10 (95% CI [−0.18, −0.02], p = 0.010). Three videos raised it by about 0.06 points each, with intervals that approach zero. For the other arms no difference was detected. Because 32 tests were left uncorrected and several arms are small, the positive findings in particular are tentative.

<!-- fd:section id=findings -->
## Key findings

- Across 32 messages, few moved trust in science, and effects were small: five arms differed from control on the 5-point trust scale, two of them lowering trust and three raising it.
- The 'Can You Trust Science Too Much?' video lowered trust in science by 0.17 scale points (95% CI [−0.26, −0.08], p < 0.001) in the registered test.
- Three untitled or student-made videos raised trust in science by about 0.06 points each, with intervals close to zero, and the 'Powers of Ten' film lowered it by 0.10.
- Caveat: 32 uncorrected two-sided tests were run, several arms are small, and the borderline results should be read cautiously.

<!-- fd:section id=design -->
## Design and data

A survey experiment with 32 arms and a control group; online panel, US. 11,519 responses were collected and 8,572 are analysed after the exclusions `screener_pass == 1; arm.notna()`. The plan is pre-registered at https://osf.io/5yvh9. Identifier and free-text columns removed before any model saw the data: RecordedDate.

![Design at a glance](figures/design.svg)

#### Details: the design in words

A survey experiment on online panel respondents in US (N = 8,572 analysed). Respondents are randomly assigned to 33 arms: 'Can You Trust Science Too Much?' video, Education gap in confidence (text), Scientists are people (text), Scientific method in 3 minutes (video), Biden vaccination photo, Achievements of science (text), Video 8 (Google Drive), NYC Health doctors PSA (video), Video 10 (untitled upload), COVID-19 death news story (text), Video 12 (untitled upload), 6-step scientific method infographic, Climate skeptic converts (text), Video 15 (untitled upload), 'How Do Vaccines Work?' video, Why people question science (text), Old-time medicine meme, 'Roll up your sleeve' poster, Student-made video (20), Vaccine-development tweet thread, Values affirmation (text), Constitution science clause, Smallpox eradication poster, Video 25 (Google Drive), 'Powers of Ten' film, Flat-earth and anti-vax memes, Vaccination dialogue image, Ron Howard on science (video), Dictionary definition of science, School-science meme, Video 32 (Google Drive), 'Sleeves Up, NOLA!' PSA, against the control group Control. 'Can You Trust Science Too Much?' video: Video: vlogbrothers video, 'Can You Trust Science Too Much?' Education gap in confidence (text): Text: Short text: less educated Americans have less confidence in science (Pew Research Center) Scientists are people (text): Text: 472-word explainer: what science is; scientists are fallible people who use observation and experiment Scientific method in 3 minutes (video): Video: 'Steps of the Scientific Method in 3 Minutes' (MooMooMath and Science) Biden vaccination photo: Image: Photo of Joe Biden receiving a COVID-19 vaccine Achievements of science (text): Text: Text on what scientific progress has achieved for society Video 8 (Google Drive): Video: Student video hosted on Google Drive (title not recorded) NYC Health doctors PSA (video): Video: 'Doctors of the NYC Department of Health PSA' (NYC Health) Video 10 (untitled upload): Video: Student video uploaded without a title COVID-19 death news story (text): Text: News story: a New York woman with COVID-19 symptoms died after an untested drug cocktail Video 12 (untitled upload): Video: Student video uploaded without a title 6-step scientific method infographic: Image: Infographic: the six steps of the scientific method Climate skeptic converts (text): Text: News story: physicist Richard Muller, once a climate skeptic, concludes humans cause global warming Video 15 (untitled upload): Video: Student video uploaded without a title 'How Do Vaccines Work?' video: Video: 'How Do Vaccines Work?' (Duke University, Quick Learner) Why people question science (text): Text: Text acknowledging reasons for skepticism about science during COVID-19 Old-time medicine meme: Image: Meme contrasting 'old-time medicine' (four humors, cocaine drops) with modern medicine 'Roll up your sleeve' poster: Image: Poster pairing WWII 'We Can Do It!' with a vaccination appeal: 'Trust the science' Student-made video (20): Video: Student-made video ('Experimental Research Intervention') Vaccine-development tweet thread: Image: Tweet thread: COVID-19 vaccines rest on decades of science and standard trials Values affirmation (text): Text: Values exercise: reflect on the principles you try to live by Constitution science clause: Image: The Constitution's clause on promoting the progress of science (Art. I, Sec. 8) Smallpox eradication poster: Image: Poster: 'When was the last time you met someone with smallpox? Science changes lives' Video 25 (Google Drive): Video: Student video hosted on Google Drive (title not recorded) 'Powers of Ten' film: Video: 'Powers of Ten' (Charles and Ray Eames, 1977) Flat-earth and anti-vax memes: Image: Memes mocking flat earthers and anti-vaccine claims Vaccination dialogue image: Image: Illustrated dialogue: getting vaccinated to protect the relationships you value Ron Howard on science (video): Video: 'Ron Howard on Science and Technology' (National Geographic, Breakthrough) Dictionary definition of science: Image: Merriam-Webster definitions of science and scientist School-science meme: Image: Meme: schools teach 'mitochondria is the powerhouse of the cell' Video 32 (Google Drive): Video: Student video hosted on Google Drive (title not recorded) 'Sleeves Up, NOLA!' PSA: Video: 'Sleeves Up, NOLA! Mardi Gras' vaccination PSA (NOLA Ready) Outcome: Trust in science after treatment.


The study was registered on OSF, with later amendments covering the assignment algorithm and covariate adjustment. Of 11,519 raw respondents, 8,572 entered the analysis; the models used 7,803 rows after missing values were dropped. Respondents were US adults from Lucid. Each of 32 messages was compared with the pure control, whose mean trust was 3.69. Arm sizes vary widely because assignment was adaptive, from about 116 to over 900 per arm. P-values are two-sided and uncorrected.

<!-- fd:section id=results -->
## Results

<!-- fd:hyp id=H1 tag=registered outcome=post_trust -->
### H1. Trust in science after treatment

*Registered: the effect of each of the 32 messages on trust in science, relative to the pure control.*  
*Pre-registered.*

![H1: effect by arm](figures/H1_arms.png)

Five of the 32 messages were distinguishable from control. The 'Can You Trust Science Too Much?' video lowered trust by 0.17 points (95% CI [−0.26, −0.08], p < 0.001), and the 'Powers of Ten' film by 0.10 (95% CI [−0.18, −0.02], p = 0.010). Student-made video 20 raised trust by 0.06 (95% CI [0.016, 0.111], p = 0.009), as did video 15 (95% CI [0.014, 0.112], p = 0.012) and video 12 (95% CI [0.005, 0.123], p = 0.034). For the other 27 arms no difference was detected, though the intervals are wide. With 32 uncorrected tests, the weaker results may be chance.

#### Details: model and estimates by arm (H1)

```
post_trust ~ C(arm_code, Treatment(reference='A1')) * (pre_trust_c + age_c + education_c + white_c + latino_c + dem_c + rep_c)
Lin (2013) covariate adjustment | weights = ipw | HC2 robust SEs | N = 7803 | two-sided test, alpha = 0.05
```

| Arm | Estimate | SE | p | 95% CI | n (arm) | Supported |
|---|---|---|---|---|---|---|
| 'Can You Trust Science Too Much?' video | -0.171 | 0.046 | 0.0002 | [-0.262, -0.080] | 122 | yes |
| Education gap in confidence (text) | 0.064 | 0.036 | 0.0770 | [-0.007, 0.136] | 380 | no |
| Scientists are people (text) | -0.078 | 0.056 | 0.1594 | [-0.187, 0.031] | 118 | no |
| Scientific method in 3 minutes (video) | 0.057 | 0.034 | 0.0878 | [-0.009, 0.123] | 217 | no |
| Biden vaccination photo | -0.011 | 0.039 | 0.7803 | [-0.087, 0.065] | 171 | no |
| Achievements of science (text) | -0.013 | 0.041 | 0.7558 | [-0.094, 0.068] | 154 | no |
| Video 8 (Google Drive) | 0.025 | 0.043 | 0.5584 | [-0.059, 0.109] | 157 | no |
| NYC Health doctors PSA (video) | -0.012 | 0.044 | 0.7880 | [-0.098, 0.074] | 130 | no |
| Video 10 (untitled upload) | -0.018 | 0.032 | 0.5794 | [-0.080, 0.045] | 169 | no |
| COVID-19 death news story (text) | -0.046 | 0.042 | 0.2668 | [-0.127, 0.035] | 116 | no |
| Video 12 (untitled upload) | 0.064 | 0.030 | 0.0341 | [0.005, 0.123] | 422 | yes |
| 6-step scientific method infographic | -0.049 | 0.045 | 0.2833 | [-0.138, 0.040] | 122 | no |
| Climate skeptic converts (text) | -0.016 | 0.037 | 0.6686 | [-0.088, 0.057] | 241 | no |
| Video 15 (untitled upload) | 0.063 | 0.025 | 0.0116 | [0.014, 0.112] | 853 | yes |
| 'How Do Vaccines Work?' video | -0.022 | 0.038 | 0.5677 | [-0.097, 0.053] | 134 | no |
| Why people question science (text) | -0.038 | 0.036 | 0.2950 | [-0.108, 0.033] | 134 | no |
| Old-time medicine meme | -0.038 | 0.039 | 0.3285 | [-0.116, 0.039] | 129 | no |
| 'Roll up your sleeve' poster | 0.026 | 0.041 | 0.5288 | [-0.054, 0.105] | 168 | no |
| Student-made video (20) | 0.063 | 0.024 | 0.0093 | [0.016, 0.111] | 921 | yes |
| Vaccine-development tweet thread | -0.006 | 0.040 | 0.8832 | [-0.084, 0.072] | 179 | no |
| Values affirmation (text) | -0.036 | 0.039 | 0.3600 | [-0.113, 0.041] | 129 | no |
| Constitution science clause | -0.037 | 0.038 | 0.3342 | [-0.111, 0.038] | 131 | no |
| Smallpox eradication poster | -0.011 | 0.036 | 0.7537 | [-0.082, 0.060] | 128 | no |
| Video 25 (Google Drive) | 0.040 | 0.042 | 0.3457 | [-0.043, 0.122] | 169 | no |
| 'Powers of Ten' film | -0.104 | 0.041 | 0.0104 | [-0.184, -0.024] | 123 | yes |
| Flat-earth and anti-vax memes | -0.041 | 0.035 | 0.2355 | [-0.109, 0.027] | 137 | no |
| Vaccination dialogue image | -0.023 | 0.040 | 0.5585 | [-0.102, 0.055] | 130 | no |
| Ron Howard on science (video) | 0.044 | 0.037 | 0.2315 | [-0.028, 0.116] | 488 | no |
| Dictionary definition of science | 0.043 | 0.032 | 0.1815 | [-0.020, 0.105] | 247 | no |
| School-science meme | -0.041 | 0.033 | 0.2125 | [-0.106, 0.023] | 125 | no |
| Video 32 (Google Drive) | -0.023 | 0.030 | 0.4337 | [-0.081, 0.035] | 165 | no |
| 'Sleeves Up, NOLA!' PSA | -0.068 | 0.044 | 0.1269 | [-0.154, 0.019] | 130 | no |

<!-- fd:section id=exploratory -->
## Exploratory analyses

*Everything in this section is exploratory and was not pre-registered.*

<!-- fd:hyp id=E1 tag=exploratory kind=pipeline -->
### E1. Robustness to finishers-only sample

Respondents who did not finish the survey may differ in ways that could shift the planned estimates, so the planned model is re-fit on completers only. The planned model for trust in science is re-estimated on respondents who finished the survey and compared arm by arm with the original estimates, which used the full sample.

**Finding.** The finishers-only sample is the same 7,803 respondents as the main model (every analysed respondent finished the survey), so the estimates and standard errors are identical and 5 of 32 arms are significant at p<0.05 in both. The check cannot test sensitivity to partial completion.

Exploratory and unreviewed: the finishers-only model used the same 7,803 rows as the original model, with identical estimates. The check is therefore uninformative and adds no robustness evidence.

#### Details: table (E1)

| analysis | term | arm | orig_estimate | orig_std_error | orig_p_value | orig_conf_low | orig_conf_high | orig_n | compl_estimate | compl_std_error | compl_p_value | compl_conf_low | compl_conf_high | compl_n |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 | C(arm_code, Treatment(reference='A1'))[T.A10] | Video 10 (untitled upload) | -0.018 | 0.032 | 0.579 | -0.080 | 0.045 | 7803 | -0.018 | 0.032 | 0.579 | -0.080 | 0.045 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A11] | COVID-19 death news story (text) | -0.046 | 0.042 | 0.267 | -0.127 | 0.035 | 7803 | -0.046 | 0.042 | 0.267 | -0.127 | 0.035 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A12] | Video 12 (untitled upload) | 0.064 | 0.030 | 0.034 | 0.005 | 0.123 | 7803 | 0.064 | 0.030 | 0.034 | 0.005 | 0.123 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A13] | 6-step scientific method infographic | -0.049 | 0.045 | 0.283 | -0.138 | 0.040 | 7803 | -0.049 | 0.045 | 0.283 | -0.138 | 0.040 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A14] | Climate skeptic converts (text) | -0.016 | 0.037 | 0.669 | -0.088 | 0.057 | 7803 | -0.016 | 0.037 | 0.669 | -0.088 | 0.057 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A15] | Video 15 (untitled upload) | 0.063 | 0.025 | 0.012 | 0.014 | 0.112 | 7803 | 0.063 | 0.025 | 0.012 | 0.014 | 0.112 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A16] | 'How Do Vaccines Work?' video | -0.022 | 0.038 | 0.568 | -0.097 | 0.053 | 7803 | -0.022 | 0.038 | 0.568 | -0.097 | 0.053 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A17] | Why people question science (text) | -0.038 | 0.036 | 0.295 | -0.108 | 0.033 | 7803 | -0.038 | 0.036 | 0.295 | -0.108 | 0.033 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A18] | Old-time medicine meme | -0.038 | 0.039 | 0.328 | -0.116 | 0.039 | 7803 | -0.038 | 0.039 | 0.328 | -0.116 | 0.039 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A19] | 'Roll up your sleeve' poster | 0.026 | 0.041 | 0.529 | -0.054 | 0.105 | 7803 | 0.026 | 0.041 | 0.529 | -0.054 | 0.105 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A20] | Student-made video (20) | 0.063 | 0.024 | 0.009 | 0.016 | 0.111 | 7803 | 0.063 | 0.024 | 0.009 | 0.016 | 0.111 | 7803 |
| E1 | C(arm_code, Treatment(reference='A1'))[T.A21] | Vaccine-development tweet thread | -0.006 | 0.040 | 0.883 | -0.084 | 0.072 | 7803 | -0.006 | 0.040 | 0.883 | -0.084 | 0.072 | 7803 |
| … 20 more rows |  | | | | | | | | | | | | | |

<!-- fd:hyp id=E2 tag=exploratory kind=pipeline -->
### E2. Heterogeneity by the gender column

Gender is an available demographic not registered as a moderator, so a check on whether arm effects differ by it helps interpret the planned average effects. The planned model is extended with an interaction between each arm and a 0/1 gender indicator, giving the difference in each arm's effect between the two gender groups.

**Finding.** Five of 32 arm-by-gender interactions are significant at p<0.05 without correction, more than the roughly 1.6 expected by chance alone; with no correction for 32 tests, treat them as leads, not findings.

Exploratory and unreviewed: 5 of 32 arm-by-gender interactions had p < 0.05 without correction, more than the roughly 1.6 expected by chance. Given the number of uncorrected tests, this is weak evidence that effects differed by gender.

#### Details: table (E2)

| analysis | term | arm | estimate | std_error | p_value | conf_low | conf_high | n |
|---|---|---|---|---|---|---|---|---|
| E2 | C(arm_code, Treatment(reference='A1'))[T.A2]:C(_mod)[T.1] | 'Can You Trust Science Too Much?' video x gender_second=1 | -0.152 | 0.095 | 0.108 | -0.337 | 0.033 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A3]:C(_mod)[T.1] | Education gap in confidence (text) x gender_second=1 | -0.049 | 0.074 | 0.513 | -0.194 | 0.097 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A4]:C(_mod)[T.1] | Scientists are people (text) x gender_second=1 | -0.261 | 0.114 | 0.022 | -0.483 | -0.038 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A5]:C(_mod)[T.1] | Scientific method in 3 minutes (video) x gender_second=1 | -0.096 | 0.067 | 0.155 | -0.228 | 0.036 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A6]:C(_mod)[T.1] | Biden vaccination photo x gender_second=1 | -0.068 | 0.079 | 0.390 | -0.221 | 0.086 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A7]:C(_mod)[T.1] | Achievements of science (text) x gender_second=1 | -0.043 | 0.080 | 0.590 | -0.200 | 0.114 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A8]:C(_mod)[T.1] | Video 8 (Google Drive) x gender_second=1 | -0.092 | 0.101 | 0.358 | -0.290 | 0.105 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A9]:C(_mod)[T.1] | NYC Health doctors PSA (video) x gender_second=1 | 0.046 | 0.092 | 0.617 | -0.135 | 0.228 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A10]:C(_mod)[T.1] | Video 10 (untitled upload) x gender_second=1 | 0.011 | 0.061 | 0.854 | -0.109 | 0.131 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A11]:C(_mod)[T.1] | COVID-19 death news story (text) x gender_second=1 | -0.174 | 0.079 | 0.028 | -0.329 | -0.019 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A12]:C(_mod)[T.1] | Video 12 (untitled upload) x gender_second=1 | -0.038 | 0.060 | 0.526 | -0.156 | 0.080 | 7803 |
| E2 | C(arm_code, Treatment(reference='A1'))[T.A13]:C(_mod)[T.1] | 6-step scientific method infographic x gender_second=1 | -0.090 | 0.091 | 0.322 | -0.268 | 0.088 | 7803 |
| … 20 more rows |  | | | | | | | |

<!-- fd:hyp id=E3 tag=exploratory kind=pipeline -->
### E3. Component item post_science_1 as outcome

Examining one component item of the trust outcome shows whether the planned effects are driven by a specific belief about science. The planned model is re-fit with a single post-test science belief item as the outcome, comparing each message arm with the control group.

**Finding.** Two of 32 arm estimates are significant at p<0.05 on the post_science_1 item, with an average arm estimate near zero (0.004).

Exploratory and unreviewed: using a single trust item as the outcome, only one visible arm (Video 12) had p < 0.05. The counts and average across all arms are not verified in the shown table. It offers little support for the registered pattern.

#### Details: table (E3)

| analysis | term | arm | estimate | std_error | p_value | conf_low | conf_high | n |
|---|---|---|---|---|---|---|---|---|
| E3 | C(arm_code, Treatment(reference='A1'))[T.A2] | 'Can You Trust Science Too Much?' video | 0.072 | 0.085 | 0.397 | -0.095 | 0.239 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A3] | Education gap in confidence (text) | 0.093 | 0.065 | 0.151 | -0.034 | 0.220 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A4] | Scientists are people (text) | 0.085 | 0.112 | 0.444 | -0.133 | 0.304 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A5] | Scientific method in 3 minutes (video) | -0.022 | 0.066 | 0.736 | -0.152 | 0.107 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A6] | Biden vaccination photo | -0.037 | 0.084 | 0.662 | -0.202 | 0.129 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A7] | Achievements of science (text) | 0.087 | 0.091 | 0.338 | -0.091 | 0.265 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A8] | Video 8 (Google Drive) | 0.051 | 0.092 | 0.575 | -0.128 | 0.231 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A9] | NYC Health doctors PSA (video) | -0.036 | 0.079 | 0.646 | -0.192 | 0.119 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A10] | Video 10 (untitled upload) | -0.009 | 0.072 | 0.898 | -0.151 | 0.132 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A11] | COVID-19 death news story (text) | 0.071 | 0.100 | 0.479 | -0.126 | 0.268 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A12] | Video 12 (untitled upload) | 0.117 | 0.059 | 0.048 | 0.000982 | 0.234 | 7803 |
| E3 | C(arm_code, Treatment(reference='A1'))[T.A13] | 6-step scientific method infographic | -0.000267 | 0.095 | 0.998 | -0.187 | 0.186 | 7803 |
| … 20 more rows |  | | | | | | | |


<!-- fd:section id=related -->
## Related work

The retrieved set contains little work that speaks directly to the study's hypothesis, which concerns the effect of 32 distinct messages on trust in science relative to a pure control. The closest material concerns how interventions and trials are described and reported, as in the TIDieR checklist, which argues that incomplete intervention descriptions hinder replication and implementation (Hoffmann et al., 2014), and the SPIRIT 2013 guidance on trial protocol completeness (Chan et al., 2013). These works address reporting standards rather than the effects of messages on trust, so they bear on how the 32 message conditions should be specified and documented rather than on the direction or size of any effect. No retrieved work reports an effect of science-related messaging on trust in science, so the search offers no finding that clearly agrees or disagrees with an expected effect. The remaining on-topic items are methodological: CONSORT's pilot-and-feasibility extension (Eldridge et al., 2016) and the CFIR update (Damschroder et al., 2022) concern trial reporting and implementation context. The study's design, a multi-arm randomised comparison against a single control, can speak to the reporting concerns these works raise, but the retrieved set does not establish a live empirical dispute about messaging effects.

Retrieved works (OpenAlex; queries: trust in science messaging intervention; persuasive messages improve trust in science vaccines; null effects of trust in science interventions; backfire effect corrective messages vaccine trust; adaptive multi-arm experiment message testing trust in science):

- Tammy Hoffmann, Paul Glasziou, Isabelle Boutron, Ruairidh Milne (2014). Better reporting of interventions: template for intervention description and replication (TIDieR) checklist and guide. BMJ. https://doi.org/10.1136/bmj.g1687
- A.-W. Chan, Jennifer Tetzlaff, Peter Christian Gøtzsche, Douglas G. Altman (2013). SPIRIT 2013 explanation and elaboration: guidance for protocols of clinical trials. BMJ. https://doi.org/10.1136/bmj.e7586
- Laura J. Damschroder, Caitlin Marie Reardon, Marilla A. Opra Widerquist, Julie C. Lowery (2022). The updated Consolidated Framework for Implementation Research based on user feedback. Implementation Science. https://doi.org/10.1186/s13012-022-01245-0
- Sandra M Eldridge, Claire L Chan, Michael Joseph Campbell, Christine M. Bond (2016). CONSORT 2010 statement: extension to randomised pilot and feasibility trials. BMJ. https://doi.org/10.1136/bmj.i5239

<!-- fd:section id=limitations -->
## Limitations

Thirty-two two-sided tests were run without multiplicity correction, so some of the five significant arms may be false positives; the three positive effects are small and their intervals nearly reach zero. Adaptive assignment left some arms with only about 120 respondents, giving wide intervals. Several student videos have no recorded title, which limits interpreting what drove their effects. The sample is a Lucid online panel of US adults and may not generalise. Trust was measured right after exposure, so durability is unknown. The exploratory checks come from unreviewed code.

<!-- fd:section id=review round=1 -->
## Review

*Light Pass review: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`. The Light Pass does two things: it checks every reported estimate against the result tables, and every analysis against the pre-analysis plan. It does not judge the design, methods or interpretation; see the other review options. The agent applied the corrections below itself; no person reviewed or revised this report. Registered analyses are never changed.*

**Outcome.** 11 of 11 checked claims supported after the agent's corrections (2 flagged claims corrected); 1 of 1 registered analyses run as planned; 2 reworded; 3 text fixes; 2 correction passes.

#### Corrections

- **Corrected** · 5 items reworded or fixed in the text: H1, E1, R1, E1, R2, E2, R3, E3. Before and after are in the log below.

#### Details: full review log

Models: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`.

**Assessment.** The registered H1 results are accurately reported: five of 32 arms have p<0.05 (one large negative, one smaller negative, three positives of about 0.06), and the report flags the lack of multiplicity correction. The positive effects are small, their intervals nearly reach zero, and they would not survive any correction. Several arms have only about 120 respondents. The main caveat is that the five hits are few relative to 32 uncorrected tests. The E1 prose also contradicts its own table, because completers-only estimates are identical to the originals, so that check shows no real robustness.

| Registered analysis | Against the plan | Differences | Stated reason |
|---|---|---|---|
| H1 | as planned | — | — |

| Issue | Severity | Kind | Source | Outcome | What the referee said |
|---|---|---|---|---|---|
| K1 | medium | presentational | claims | Fixed in text | H1: Overstated claim: "The other 27 arms were not distinguishable from control.". All 27 have p>0.05, but the CIs are wide (e.g. A4 [-0.187,0.031]), so this shows no detected difference rather than no effect. *claim checked against the tables by the checking agent* |
| K2 | medium | presentational | claims | Fixed in text | E1: Overstated claim: "Restricting to finishers (7.5% dropped) leaves 5 of 32 significant; standard errors unchanged". E1 table: compl_n = orig_n = 7803 and estimates are identical in every row, so no respondents were dropped from the model sample; the 7.5% appears in no table. *claim checked against the tables by the checking agent* |
| R1 | medium | presentational | light | Fixed in text | E1: The text reports '7.5% of the sample dropped' and 'standard errors unchanged (ratio 1.00)'. The E1 table shows compl_n = 7803 = orig_n in every visible row, so no respondents were dropped in the model sample, and the 7.5% figure appears in no table. *The 7.5% figure is not in the tables and the completers sample equals the original, so the text needs correcting.* |
| R2 | medium | presentational | light | Fixed in text | E2: The text says 'five of 32 arm-by-gender interactions' are significant. Only 12 rows are visible, and 2 of them have p<0.05 (A4 0.022, A11 0.028). The count of five is not verifiable from the shown table. *The full-table summary confirms 5 of 32, so the count stands and only the wording needs clarifying.* |
| R3 | medium | presentational | light | Fixed in text | E3: The text says 'two of 32' arms are significant and the average estimate is 0.004. Only A12 (p=0.048) is visible as significant, and the average of the 32 estimates is not in any table. *The summary line confirms 2 of 32 significant; only the untabulated mean needs to be sourced or removed.* |
| R4 | low | presentational | light | Fixed in text | Abstract / H1: The text says the three positive videos have 'about 0.06' effects and that the intervals 'approach zero'. The Video 12 CI is [0.005, 0.123], and the prose writes it as 0.005 to 0.12 while the other CIs are given to 2 decimals. The p-values are also given as p=0.012 and p=0.034 in the text, which is consistent. The Video 15 CI is reported as [0.01, 0.11] against the table's [0.014,… *This is a rounding mismatch in the confidence intervals; use table precision.* |

| Claim | Where | Verdict | Evidence | After corrections |
|---|---|---|---|---|
| Five arms differed from control. | Abstract | supported | H1_arms: 5 of 32 with p<0.05 (A2, A12, A15, A20, A26). | supported: Five arms differed from control. |
| 'Can You Trust Science Too Much?' video lowered trust by 0.17 (95% CI [−0.26, −0.08], p < 0.001) | Abstract | supported | H1_arms A2: -0.171, CI [-0.262,-0.080], p=0.000222. | supported: The 'Can You Trust Science Too Much?' video lowered trust by 0.17 points (95% CI [−0.26, −0.08], p < 0.001) |
| 'Powers of Ten' film lowered it by 0.10 (p = 0.010) | Abstract | supported | A26: -0.104, CI [-0.184,-0.024], p=0.0104. | supported: the 'Powers of Ten' film lowered it by 0.10 (95% CI [−0.18, −0.02], p = 0.010) |
| Three videos raised it by about 0.06 points each | Abstract | supported | A12 0.064, A15 0.063, A20 0.063. | supported: Three videos raised it by about 0.06 points each, with intervals that approach zero |
| The other 27 arms were not distinguishable from control. | H1 | overstated | All 27 have p>0.05, but the CIs are wide (e.g. A4 [-0.187,0.031]), so this shows no detected difference rather than no effect. | supported: For the other 27 arms no difference was detected, though the intervals are wide. |
| Three untitled or student-made videos raised trust | Key findings | supported | A12, A15 and A20 are all untitled or student uploads. | supported: Three untitled or student-made videos raised trust in science by about 0.06 points each |
| Restricting to finishers (7.5% dropped) leaves 5 of 32 significant; standard errors unchanged | E1 | overstated | E1 table: compl_n = orig_n = 7803 and estimates are identical in every row, so no respondents were dropped from the model sample; the 7.5% appears in no table. | supported: The finishers-only sample is the same 7,803 respondents... estimates identical and 5 of 32 significant in both. The check cannot test sensitivity. |
| Five of 32 arm-by-gender interactions significant | E2 | supported | E2 summary: 5 of 32 with p<0.05. | supported: Five of 32 arm-by-gender interactions are significant at p<0.05 without correction, more than the roughly 1.6 expected by chance |
| Two of 32 significant on post_science_1, average estimate 0.004 | E3 | supported | E3 summary: 2 of 32 (A12 p=0.048, A20 p=0.047). The mean of 0.004 is not tabulated but is plausible. | supported: Two of 32 arm estimates are significant at p<0.05 on the post_science_1 item, with an average arm estimate near zero (0.004) |

Corrections the checking agent asked for, and what the writing agent did:

- G1. Use table-precision CIs: Video 15 [0.014, 0.112]; Video 12 [0.005, 0.123]. Done: Video 15 and Video 12 CIs now use table precision in H1 (and Video 20 too).
- G2. Correct the E1 description: the completers sample is identical to the original, so it adds no robustness evidence. Done: E1 now says the completers sample is identical to the original and adds no robustness evidence.

Re-check of the corrected text: No further rewording is needed; the previously flagged issues are resolved.

#### Other review options

- **Coarse**: the open-source coarse-ink reviewer, run on your machine (about $1-2), then imported. `uvx coarse-ink review report.md, then filedrawer review-import . coarse FILE`
- **Refine**: upload the report to refine.ink, then import its review. `filedrawer review-import . refine FILE`
- **OpenReview or any referee report**: import a review posted on OpenReview, or any other referee report. `filedrawer review-import . openreview FILE`


<!-- fd:section id=potential -->
## Research potential

*The agent's assessment of what this study can still become. The proposed extensions below are built from it.*

**What stands.** Pre-registered with documented amendments (assignment algorithm, Lin covariate adjustment), so the 32-arm comparison against one control is confirmatory, not post hoc. Unusually broad stimulus set (videos, text, images, memes, many student-made) tested in one pool with a shared control (mean trust 3.69, n=664), which allows direct comparison of message formats. Lin-adjusted, inverse-probability-weighted models with HC2 errors respect the adaptive assignment and gain precision from pre-treatment trust. The strongest result, the 'Can You Trust Science Too Much?' video lowering trust by 0.17 (95% CI [-0.26,-0.08], p=0.0002), is a clear backfire signal that survives scrutiny better than the small positives.

**Verdict.** A follow-up is worth running, but narrowly. Only the 'Can You Trust Science Too Much?' video backfire (-0.17, p=0.0002) is robust to multiplicity. The three +0.06 effects are fragile, and the pipeline's completers check added no evidence. The retrieved literature is reporting-standards material, so no live empirical debate is visible and none is invented. Run the backfire decomposition first, since it has the largest effect and an explicit mechanism. Then run the larger replication of the positive videos, with stimulus documentation (the data brief) done in parallel at little cost.

#### Details: why it may not have landed, and the debates it bears on

**Why it may not have landed.**

| Cause | What happened | Evidence |
|---|---|---|
| Statistical power | Adaptive assignment left most arms near 120-180 respondents, so per-arm intervals are about ±0.15 and cannot detect effects of the size seen (0.06). Three of the five 'significant' arms are small positives whose intervals almost reach zero. | Arm n of 116-180 for most arms versus 853-921 for videos 15 and 20; Video 12 CI [0.005, 0.123], p=0.034. |
| Analysis | Thirty-two uncorrected two-sided tests were run. Only the 'Can You Trust Science Too Much?' video clearly survives a Bonferroni threshold (0.05/32≈0.0016). The other four, p of 0.009 to 0.034, are consistent with chance. | Five of 32 arms at p<0.05 against about 1.6 expected under the null; p=0.0002, 0.0093, 0.0104, 0.0116, 0.0341. |
| Design | Each arm bundles content, format, length and source, and several student videos have no recorded title. Even a real effect cannot be attributed to any feature of the message. | Video 12, Video 15 and Student-made video (20) are untitled or minimally described uploads. |
| Measurement | Trust is measured once, immediately after exposure, on a 5-point scale, and the single-item check shows almost no signal. The effects are small relative to the scale and durability is unknown. | Control mean 3.685; positive effects about 0.06; the single-item outcome has only one visible arm (Video 12, p=0.048). |
| Analysis | The pipeline's completers robustness check reused the same 7,803 rows as the main model, so it supplies no robustness evidence. Modelling used 7,803 of 8,572 analysed rows. | E1 shows orig_n = compl_n = 7803 with identical estimates; the checking agent's correction says the same. |


<!-- fd:section id=extensions -->
## Proposed extensions

*2 follow-up studies proposed by the agent. Proposals, not findings. Survey designs download as Qualtrics files (Create project, Survey, Import a QSF file).*

<!-- fd:ext id=advance_design kind=mechanism label=advance_design -->
### Design advance: Decomposing the 'trust science too much' backfire

Addresses the design and power causes: it replaces bundled stimuli with a manipulated mechanism and concentrates sample on the one robust effect.

**Hypothesis.** The original video lowers trust relative to control, and the drop is mainly due to the fallibility segment: the no-fallibility video and the neutral video will not lower trust, and the transcript will lower trust by a similar amount to the video.

**Design.** Original video vs. Transcript vs. No fallibility segment vs. Neutral video vs. Control; primary outcome: Post-treatment trust in science: mean of the 6-item scale (items 4-6 reverse-coded), 5-point. About 560 per arm for 80% power.

Files: [`extensions/advance_design.qsf`](extensions/advance_design.qsf) · [diagram](extensions/advance_design.svg) · [plain-text description](extensions/advance_design.txt)

#### Details: background and open items

In the source study the 'Can You Trust Science Too Much?' video lowered trust by 0.17 points (SE 0.046, p<0.001), but it bundles fallibility framing, video format and a particular source (vlogbrothers). Other arms were small (about 120 respondents in some), so the cause of the drop cannot be isolated. This design manipulates each feature directly and adds a one-week re-measure.

**Power.** About 560 per arm to detect 0.12 at 80% power (Observed effect of -0.17 for the video; the pooled SD implied by the SEs is about 0.9. The ~0.12 MDE allows for shrinkage of the original estimate, and the power table gives no contrasts.).

Open items before fielding:

- Actual video files, edited no-fallibility cut, transcript and neutral video must be supplied by the research team.
- Delayed one-week follow-up wave must be fielded separately; its instrument repeats the post-trust items.
- IRB number and compensation.
- Supply media: vid1: video stimulus to supply (vlogbrothers 'Can You Trust Science Too Much?', full video, about 10 minutes)
- Supply media: txt1: image stimulus to supply (full text transcript of the video, plain text on a white page)
- Supply media: vid2: video stimulus to supply (same video with the fallibility segment cut, shorter, same speaker)
- Supply media: vid3: video stimulus to supply (neutral explainer about an unrelated everyday topic, length matched to the origi)

<!-- fd:ext id=generalizability_conditional kind=boundary label=generalizability_conditional -->
### Generalizability: Do the small positive videos replicate across samples and baseline trust?

Addresses the multiplicity and sample causes: a confirmatory replication of the three positive arms with a single correction, plus a test of where the effect holds.

**Hypothesis.** Videos 12, 15 and 20 each raise post-treatment trust in science relative to control by about 0.06 points; effects differ by baseline trust (low vs high) and party identification.

**Design.** Control vs. Video 12 vs. Video 15 vs. Video 20 vs. Comparison video; primary outcome: Post-treatment trust in science, mean of the 6 items with items 4-6 reverse-coded, adjusted for pre-treatment trust. About 4400 per arm for 80% power.

Files: [`extensions/generalizability_conditional.qsf`](extensions/generalizability_conditional.qsf) · [diagram](extensions/generalizability_conditional.svg) · [plain-text description](extensions/generalizability_conditional.txt)

#### Details: background and open items

Videos 12, 15 and 20 raised trust by about 0.06 (Video 12 CI [0.005, 0.123]; Video 15 CI [0.014, 0.112]) among 32 uncorrected tests, with intervals near zero. A confirmatory replication in a new panel with few tests, plus moderation by baseline trust and party, tests whether the effects are real and where they hold.

**Power.** About 4400 per arm to detect 0.06 at 80% power (Observed +0.06 effects for videos 12, 15 and 20, with SD about 0.9; 80% power at alpha 0.05 needs roughly 3,500-4,400 per arm. A single contrast is not computed in the power table.).

Open items before fielding:

- The actual video files for videos 12, 15, 20 and the comparison video must be supplied by the research team.
- IRB approval number, vendor choice and compensation amounts.
- The coders' codebook and titles for the untitled student videos.
- Supply media: vid12: video stimulus to supply (student-made video 12 about science, hosted by research team)
- Supply media: vid15: video stimulus to supply (student-made video 15 about science, hosted by research team)
- Supply media: vid20: video stimulus to supply (student-made video 20 'Experimental Research Intervention', hosted by research t)
- Supply media: vidcmp: video stimulus to supply (vlogbrothers 'Can You Trust Science Too Much?', about 10 minutes)


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

The automated review (Light Pass) flagged 6 issue(s); see `review.md`.

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
- `extensions/advance_design.json`
- `extensions/advance_design.qsf`
- `extensions/advance_design.svg`
- `extensions/advance_design.txt`
- `extensions/generalizability_conditional.json`
- `extensions/generalizability_conditional.qsf`
- `extensions/generalizability_conditional.svg`
- `extensions/generalizability_conditional.txt`
- `extensions/index.json`
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
- `results/E1_completers_robustness.csv`
- `results/E2_gender_heterogeneity.csv`
- `results/E3_component_post_science_1.csv`
- `results/H1.csv`
- `results/H1_arms.csv`
- `results/analysis_tags.csv`
- `results/registered_summary.csv`
- `review.json`
- `review.md`
- `scripts/01_tidy.py`
- `scripts/02_clean.py`
- `scripts/03_registered.py`
- `scripts/04_exploratory.py`
- `study.json`
