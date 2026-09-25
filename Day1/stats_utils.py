"""
stats_utils.py
---------------
Small helper library for the "Day 1 -- Descriptive Statistics" notebook.

Functions
---------
central_tendency(series)   -> pd.Series with mean / median / mode
dispersion(series)         -> pd.Series with variance / std_dev / range / IQR
skew_report(series)        -> printable string describing skew direction/size
summarize(series)          -> pd.Series combining central tendency + dispersion
plot_distribution(series, title=None, bins=20) -> matplotlib Axes
group_dispersion(df, group_col, value_col)     -> pd.DataFrame per-group stats
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def central_tendency(series: pd.Series) -> pd.Series:
    """Mean, median and mode of a numeric series."""
    series = series.dropna()
    mode_vals = series.mode()
    mode_val = mode_vals.iloc[0] if not mode_vals.empty else np.nan

    return pd.Series(
        {
            "mean": series.mean(),
            "median": series.median(),
            "mode": mode_val,
        },
        name="central_tendency",
    )


def dispersion(series: pd.Series) -> pd.Series:
    """Variance, standard deviation, range and IQR of a numeric series."""
    series = series.dropna()
    q1, q3 = series.quantile([0.25, 0.75])

    return pd.Series(
        {
            "variance": series.var(),
            "std_dev": series.std(),
            "range": series.max() - series.min(),
            "iqr": q3 - q1,
        },
        name="dispersion",
    )


def skew_report(series: pd.Series) -> str:
    """Human-readable summary of how mean, median and skewness relate."""
    series = series.dropna()
    mean_val = series.mean()
    median_val = series.median()
    skewness = series.skew()

    diff = mean_val - median_val
    if skewness < -0.1:
        direction = "left-skewed (a low tail is pulling the mean down)"
    elif skewness > 0.1:
        direction = "right-skewed (a high tail is pulling the mean up)"
    else:
        direction = "roughly symmetric"

    return (
        f"mean={mean_val:.2f}, median={median_val:.2f}, "
        f"skewness={skewness:.2f} -> distribution looks {direction}. "
        f"(mean - median = {diff:+.2f})"
    )


def summarize(series: pd.Series) -> pd.Series:
    """Combined central tendency + dispersion summary for a numeric series."""
    return pd.concat([central_tendency(series), dispersion(series)])


def plot_distribution(series: pd.Series, title: str | None = None, bins: int = 20):
    """Histogram of `series` with mean and median marked, returns the Axes."""
    series = series.dropna()
    mean_val = series.mean()
    median_val = series.median()

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(series, bins=bins, color="#4C72B0", edgecolor="white", alpha=0.85)
    ax.axvline(mean_val, color="#F96167", linestyle="--", linewidth=2, label=f"Mean = {mean_val:.2f}")
    ax.axvline(median_val, color="#2E7D32", linestyle="-", linewidth=2, label=f"Median = {median_val:.2f}")
    ax.set_ylabel("Number of titles")
    if title:
        ax.set_title(title)
    ax.legend()
    return ax


def group_dispersion(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Per-group mean, median, std_dev and count, sorted by std_dev descending."""
    grouped = df.groupby(group_col)[value_col].agg(
        mean="mean",
        median="median",
        std_dev="std",
        count="count",
    )
    return grouped.sort_values("std_dev", ascending=False)
