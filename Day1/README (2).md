# Day 1 — Descriptive Statistics: The Mean Lied to Me

`#30DaysOfMachineLearning`

This project analyzes a synthetic StreamFlix catalogue (1,200 titles) to show
why the **mean** rating can mislead when the underlying distribution is
skewed, and breaks the picture down by genre.

## Files in this project

| File | Purpose |
|---|---|
| `day01_mean_lied_to_me_EXECUTED.ipynb` | Notebook with all cells already run — outputs and plots included, nothing to install. |
| `day01_mean_lied_to_me_DEBUGGED.ipynb` | Same notebook, unexecuted — run it yourself. |
| `stats_utils.py` | Helper functions: `central_tendency`, `dispersion`, `skew_report`, `summarize`, `plot_distribution`, `group_dispersion`. |
| `generate_dataset.py` | Generates the synthetic dataset (seeded, reproducible). |
| `data/streaming_ratings.csv` | The dataset itself (1,200 rows), already generated. |

## Fixing "module not found" in Google Colab

If `from stats_utils import ...` fails in Colab, it's almost always a **path
or filename mismatch** between where you uploaded the file and where your
code is looking for it.

**Check where the file actually is:**

```python
import os
print(os.path.exists('/content/stats_utils.py'))
print(os.path.exists('/stats_utils.py'))
```

**If the file is at `/stats_utils.py` (Colab's root) but your code does
`sys.path.append('/content')`**, either move the file into `/content`:

```python
import shutil
shutil.move('/stats_utils.py', '/content/stats_utils.py')
```

**or** point `sys.path` at wherever the file actually is:

```python
import sys
sys.path.append('/')
```

Then run the import cell as normal:

```python
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('/content')  # match this to wherever stats_utils.py lives

from stats_utils import (
    central_tendency,
    dispersion,
    skew_report,
    summarize,
    plot_distribution,
    group_dispersion,
)

plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
```

If you've already tried a broken import once, **restart the runtime**
(Runtime → Restart session) before re-running — Colab can cache a failed
import.

## Running this on your own machine (not Colab)

### 1. Get Python and the required packages

You need Python 3.9+ and these packages:

```bash
pip install pandas matplotlib numpy jupyter
```

(If you use `conda`, `conda install pandas matplotlib numpy jupyter` works
just as well.)

### 2. Set up the project folder

Put these files in the **same folder**:

```
day01-mean-lied-to-me/
├── day01_mean_lied_to_me_DEBUGGED.ipynb
├── stats_utils.py
├── generate_dataset.py
└── data/
    └── streaming_ratings.csv
```

`stats_utils.py` must sit next to the notebook (not in a subfolder) so the
plain `from stats_utils import ...` line finds it with no path juggling.

If you don't have `data/streaming_ratings.csv` yet, generate it from inside
that folder:

```bash
python generate_dataset.py
```

This creates `data/streaming_ratings.csv` with 1,200 rows (it's seeded, so
you'll get the same data every time you run it).

### 3. Launch the notebook

From inside the project folder:

```bash
jupyter notebook day01_mean_lied_to_me_DEBUGGED.ipynb
```

or, if you prefer JupyterLab:

```bash
jupyter lab day01_mean_lied_to_me_DEBUGGED.ipynb
```

Then run all cells (Cell → Run All, or Shift+Enter through each one). No
`sys.path.append(...)` or Colab-specific fixes are needed locally, since the
notebook, `stats_utils.py`, and `data/` are already in the right place
relative to each other.

### 4. VS Code instead of Jupyter (optional)

If you use VS Code with the Python/Jupyter extension, just open the folder
in VS Code and open the `.ipynb` file directly — it uses the same
kernel/working-directory logic as Jupyter, so no path changes are needed
there either.

## Common issues

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'stats_utils'` | `stats_utils.py` isn't in the same folder as the notebook (or isn't on `sys.path`) | Move it next to the notebook, or add the right folder with `sys.path.append(...)` |
| `FileNotFoundError: data/streaming_ratings.csv` | Dataset hasn't been generated, or you're running Jupyter from the wrong working directory | Run `python generate_dataset.py` from the project folder, and launch Jupyter from that same folder |
| `TypeError: NDFrame.describe() got an unexpected keyword argument 'numeric_only'` | Newer pandas (3.x) dropped `numeric_only` from `describe()` | Already fixed in these notebooks — they use `df.select_dtypes(include="number").describe()` instead |
