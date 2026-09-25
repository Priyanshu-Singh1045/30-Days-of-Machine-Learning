# Day 2 — Probability Basics
### 30 Days of Machine Learning · Data Analyst / Data Scientist track

This folder is everything you need to post Day 2 and back it up with real, working code.

## What's in here

| File | What it is | What to do with it |
|---|---|---|
| `Day2_Probability_Basics_Carousel.pdf` | The 8-slide LinkedIn carousel (same "Coral Energy" palette as Day 1) | Upload directly to LinkedIn as a document post — this is the native carousel format |
| `Day2_Probability_Basics_Carousel.pptx` | Editable source for the carousel | Open in PowerPoint/Keynote if you want to tweak any text or colors before posting |
| `Day2_Probability_Basics.ipynb` | The companion Jupyter notebook — **already executed**, every output (numbers + the chart) is saved inside it | Open in Jupyter/VS Code to read top-to-bottom, or re-run it yourself |
| `churn_by_support_contact.png` | The chart from the notebook, also embedded in carousel slide 6 | Use as a standalone image if you want to post it separately, e.g. as a comment reply or a follow-up post |
| `requirements.txt` | The exact Python packages needed to re-run the notebook | `pip install -r requirements.txt` |

## What the notebook covers

1. **Basic probability** — theoretical vs. empirical, using a 10,000-flip coin simulation
2. **Conditional probability** — a synthetic 2,000-customer churn/support dataset, computing `P(churn)`, `P(churn | support)`, `P(churn | no support)`
3. **Independence** — checking whether `P(churn | support) == P(churn)` (it doesn't — that gap is the story)
4. **Bayes' Theorem** — flipping the question to `P(support | churn)`, computed two ways (via the formula, and directly from the data) to prove they match
5. **Visualization** — the bar chart used in slide 6 of the carousel, styled in the same navy/coral palette

The dataset is **synthetic** (built inside the notebook with `np.random.seed(42)` for reproducibility) — it's designed to illustrate the concepts clearly, not to represent a real company's numbers. Swap in your own data by replacing the `contacted_support` / `churned` columns with any two binary columns you actually track.

## How to run it yourself

```bash
pip install -r requirements.txt
jupyter notebook Day2_Probability_Basics.ipynb
```

Or, to re-run and re-save all outputs from the command line:

```bash
jupyter nbconvert --to notebook --execute --inplace Day2_Probability_Basics.ipynb
```


