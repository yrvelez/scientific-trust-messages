# Analysis plan (pre-registered: OSF 5yvh9, amended by w82xv and 5wr2k)

Transcribed from the OSF Preregistration "Can Trust in Science Be Improved? An Adaptive Experimental Approach"
(https://osf.io/5yvh9, DOI 10.17605/OSF.IO/5YVH9, registered 2021-11-20, before any human observation of the data)
and its two open-ended amendments: https://osf.io/w82xv (DOI 10.17605/OSF.IO/W82XV, 2021-11-28: the assignment
algorithm) and https://osf.io/5wr2k (2021-11-29: covariate adjustment with the Lin estimator). Associated project:
https://osf.io/9axfc.

## Design

Adaptive survey experiment on Lucid testing brief messages designed by students in an undergraduate experiments
course to raise trust in science. Each respondent sees one message (`arm`): A1 is a pure control ("Please continue
to the next page."), A2-A33 are the 32 student messages (text, images and videos). Before the message,
respondents write a few sentences about a situation where they acted on an important value.

Assignment (Offer-Westort, Coppock & Green 2021): equal probabilities during a burn-in of about 2,000 respondents,
then batches with more probability on promising arms. Following w82xv, the best arm is defined relative to control,
with a probability floor of .01, and from batch 3 a control-augmented design lets the control group "catch up" to
the best-performing arm. Following 5wr2k, the arm effects that set the next batch's probabilities are
covariate-adjusted with the Lin (2013) estimator, because large probabilities were going to arms with chance
covariate imbalance. Registered sample: 8,000 respondents in 8 batches.

Batches (`batch`) correspond to the Qualtrics surveys fielded in sequence: "Scientific Trust Messages (Final)"
(batch 1, the equal-probability burn-in, from 2021-11-21), "(Batches 2+)" (2), "(Batch 3)" through "(Batch 7)"
(3-7). Two earlier surveys, "Scientific Trust Messages" and "(Abbreviated)", predate the registration and are not
part of the registered study.

## Outcome

`post_trust`: the registered 6-item trust-in-science scale after the message, as a summative scale (the mean of
the six items, 1-5) with the three negatively worded items reverse-coded:

1. We can trust scientists to share their discoveries even if they don't like their findings.
2. I trust that the work of scientists to make life better for people.
3. We should trust the work of scientists.
4. Scientific theories are not trustworthy. (reversed)
5. We cannot trust scientists because they are biased in their perspectives. (reversed)
6. We cannot trust science because it moves too slowly. (reversed)

The same scale before the message is `pre_trust`.

## Sample and exclusions (registered)

- Respondents who fail the pre-treatment attention check are dropped: keep `screener_pass == 1` (the screener asks
  for both "extremely interested" and "very interested").
- Finished responses with an assigned arm.
- Missing data: listwise deletion on the outcome and covariates.

## Hypotheses

The registration's aim is to identify the most effective message.

- H1: the effect of each message (A2-A33) on `post_trust`, relative to the pure control (A1), two-sided.

## Estimation (registered)

Regression weighted to account for the differential probabilities of assignment, adjusting for age, education,
race, political party and pre-treatment trust in science, with HC2 standard errors (as in `estimatr`). Following
amendment 5wr2k, covariates enter through the Lin (2013) estimator (arm indicators interacted with mean-centred
covariates). Two-sided tests at alpha = 0.05; the registration specifies no multiple-testing correction.

- Weights: `ipw` = 1 / the arm's share among the responses assigned in the same batch. The probabilities the
  assignment server used were not stored with the responses, so each batch's realized shares stand in for them.
- Covariates: `age`; `education` (Lucid codes); `white` and `latino` indicators for race and Hispanic origin;
  `dem` and `rep` indicators for party (leaners included); `pre_trust`.

## Registered but conditional or not run here

- Batch fixed effects are registered "in the event of significant trends in the control group": run as a
  robustness check on H1.
- The randomization-inference test of no effect across all arms and the posterior probability of the
  best-performing arm (priors mean 0, SD 1; 5,000 posterior draws) are registered but not computed by this
  pipeline.

## Exploratory (not registered)

- COVID-19 vaccine attitudes after the message (`vax_safe`, `vax_effective`, `vax_fear`, 1-5): not among the
  registered measures.
- The covariate-adjusted estimates with additive covariates (OLS) instead of Lin's estimator.
