# Day 3 — Data Distributions
### 30 Days of Machine Learning · Data Analyst / Data Scientist track

Everything needed to post Day 3 and back it up with real, executed code.

## What's in here

| File | What it is | What to do with it |
|---|---|---|
| `Day3_Data_Distributions_Carousel.pdf` | The **11-slide** LinkedIn carousel (same "Coral Energy" palette as Day 1 & 2) | Upload directly to LinkedIn as a document post |
| `Day3_Data_Distributions_Carousel.pptx` | Editable source for the carousel | Open in PowerPoint/Keynote to tweak text or colors |
| `Day3_Data_Distributions.ipynb` | The companion Jupyter notebook — **already executed**, every stat and chart is saved inside it | Open in Jupyter/VS Code to read top-to-bottom, or re-run it yourself |
| `dist_normal.png`, `dist_uniform.png`, `dist_binomial.png`, `dist_poisson.png`, `dist_skewed.png` | The five individual distribution charts from the notebook | Use any of these standalone — e.g. as a comment reply or a follow-up post |
| `dist_comparison_grid.png` | All five side-by-side, embedded in carousel slide 8 | Same — post standalone if useful |
| `requirements.txt` | Exact Python packages needed to re-run the notebook | `pip install -r requirements.txt` |

## Carousel structure (11 slides)

1. Hook — "Your dataset probably isn't a bell curve"
2. The basics — Shape, Center, Density
3. Normal distribution
4. Uniform distribution
5. Binomial distribution
6. Poisson distribution
7. Skewed (log-normal) distribution
8. All five, side by side (real chart from the notebook)
9. "Identify yours in 3 steps"
10. 60-second cheat sheet
11. CTA + Day 4 teaser

## What the notebook covers

1. **Normal** — exam scores, mean ≈ median, skewness ≈ 0
2. **Uniform** — random arrival time in a 60-minute window
3. **Binomial** — heads out of 20 coin flips, repeated 5,000 times
4. **Poisson** — signups per hour, showing variance ≈ mean
5. **Skewed (log-normal)** — session duration, mean well above median, skewness ≈ 5.4
6. **Side-by-side comparison grid** — all four generated distributions in one figure
7. **Cheat sheet + 3-step identification checklist** (markdown, mirrors the carousel)

All data is **synthetic**, generated with `np.random.seed(42)` for reproducibility — built to show each shape cleanly, not pulled from a real company. Swap in your own column by replacing any of the `np.random.*` calls with your actual data (e.g. `df['session_duration']` instead of the simulated `session_minutes`).

## How to run it yourself

```bash
pip install -r requirements.txt
jupyter notebook Day3_Data_Distributions.ipynb
```

Or re-run and re-save all outputs from the command line:

```bash
jupyter nbconvert --to notebook --execute --inplace Day3_Data_Distributions.ipynb
```

