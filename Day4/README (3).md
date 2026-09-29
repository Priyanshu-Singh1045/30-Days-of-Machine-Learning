# Day 4 · Hypothesis Testing — *Is it real, or just luck?*

Part of the **30 Days of Machine Learning** series (companion to [Day 3 — Data Distributions](../day-03-data-distributions)).

A from-scratch, fully-executed walkthrough of the five hypothesis tests that cover most day-to-day analytics work — built for the LinkedIn carousel in this repo, and safe to run end-to-end on your own machine.

<p align="center">
  <img src="images/welch_ttest.png" width="32%" />
  <img src="images/proportion_test.png" width="32%" />
  <img src="images/power_curve.png" width="32%" />
</p>

---

## 📂 What's in this repo

```
day-04-hypothesis-testing/
├── Day4_Hypothesis_Testing.ipynb     # the notebook — every cell already executed
├── Day4_Hypothesis_Testing_Carousel.pdf   # the 11-slide LinkedIn carousel
├── requirements.txt                  # exact package versions used
├── data/                             # CSVs the notebook generates (simulated data)
│   ├── onboarding_engagement.csv
│   ├── latency_before_after.csv
│   ├── ab_conversions.csv
│   ├── session_duration.csv
│   └── channel_revenue.csv
├── images/                           # PNG charts exported by the notebook
└── results/
    └── results.json                  # every headline number, machine-readable
```

## 🧠 What the notebook covers

| # | Section | Test / idea | SciPy call |
|---|---|---|---|
| 1 | Setup | Reproducible environment, seed, helpers | — |
| 2 | The p-value from scratch | Simulate a null distribution and compare it to the exact test | `stats.binomtest` |
| 3 | Test 1 | **Welch t-test** — two independent group means | `stats.ttest_ind(equal_var=False)` |
| 4 | Test 2 | **Paired t-test** — same units, before vs. after | `stats.ttest_rel` |
| 5 | Test 3 | **Two-proportion / chi-square** — did a rate change? | `stats.chi2_contingency` |
| 6 | Test 4 | **Mann-Whitney U** — skewed or ordinal data | `stats.mannwhitneyu` |
| 7 | Test 5 | **One-way ANOVA + Tukey HSD** — 3+ groups | `stats.f_oneway`, `stats.tukey_hsd` |
| 8 | Type I / II errors & power | A/A test proving α is the false-positive rate; power curves; sample-size planning | `stats.nct`, simulation |
| 9 | Two traps | Multiple testing (Bonferroni, Benjamini-Hochberg) and "significant ≠ important" | `stats.false_discovery_control` |
| 10 | Cheat sheet | A `recommend_test()` helper + situation → test lookup table | — |
| 11 | Save results | Exports every number to `results/results.json` | — |

Every dataset is **simulated with a fixed random seed (`42`)**, so re-running the notebook reproduces the exact numbers, tables and charts shown here — nothing is hard-coded or faked.

## 📊 Headline numbers from this run

| Test | Result |
|---|---|
| Welch t-test (onboarding) | +4.25 min lift, 95% CI [1.68, 6.82], *p* = 0.0013, Cohen's *d* = 0.32 |
| Paired t-test (latency) | −22.7 ms, 95% CI [−28.8, −16.7], *p* < 0.0001 — ignoring the pairing drops it to *p* = 0.096 |
| Two-proportion test (conversion) | +1.66 pp (+16.7% relative), *p* = 0.0074 |
| Mann-Whitney U (session duration) | medians 4.08 → 4.76 min, *p* = 0.124 (not significant here) |
| One-way ANOVA (channel revenue) | F = 10.61, *p* < 0.0001, η² = 0.08; Tukey flags Search − Email as the clearest gap |
| A/A false-positive check | 10,000 no-effect simulations → 4.76% flagged "significant" at α = 0.05 (theory: 5%) |
| Multiple testing (20 metrics, all noise) | 64.0% chance of ≥1 false alarm uncorrected, vs. ~5% with Bonferroni or Benjamini-Hochberg |

Full numbers, including confidence intervals and sample sizes, are in [`results/results.json`](results/results.json).

## ▶️ Running it yourself

```bash
git clone <this-repo-url>
cd day-04-hypothesis-testing
python -m venv .venv && source .venv/bin/activate      # optional but recommended
pip install -r requirements.txt
jupyter notebook Day4_Hypothesis_Testing.ipynb
```

Run all cells top-to-bottom (`Kernel → Restart & Run All`). Because the random seed is fixed, you should get **identical** numbers, tables and charts to the ones already saved in the notebook and in `results/results.json`.

## 🧩 Requirements

```
numpy
pandas
scipy
matplotlib
jupyter
```

See [`requirements.txt`](requirements.txt) for the exact versions this was built and tested against.

## 🔑 Key takeaways

1. **A p-value is just the tail area of the null distribution** — how surprising your data would be if nothing were going on.
2. **Match the test to the data**: numeric vs. binary outcome, two groups vs. many, paired vs. independent, normal vs. skewed.
3. **Report more than *p***: effect size and a confidence interval tell you *how much*, not just *whether*.
4. **Plan power up front.** Small effects need big samples — a "not significant" result from an under-powered test means very little.
5. **Testing many metrics inflates false alarms.** Correct for it (Bonferroni / Benjamini-Hochberg).
6. **Statistically significant ≠ practically important.** Statistics detects an effect; you decide whether it's worth acting on.

## 🗺️ Series

- ✅ Day 3 — Data Distributions
- ✅ **Day 4 — Hypothesis Testing** (this repo)
- ⏭️ Day 5 — Correlation vs. Causation

---

*Built as part of the "30 Days of Machine Learning" LinkedIn series. Feedback and pull requests welcome.*
