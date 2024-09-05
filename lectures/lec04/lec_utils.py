"""
Imports and helpful functions that we use in Practical Data Science lectures.

Usage:

from lec_utils import *
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_inline.backend_inline import set_matplotlib_formats
from IPython.display import display, IFrame, HTML

from pathlib import Path

import plotly
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio

# Preferred styles
pio.templates["pds"] = go.layout.Template(
    layout=dict(
        margin=dict(l=30, r=30, t=30, b=30),
        autosize=True,
        width=600,
        height=400,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        title=dict(x=0.5, xanchor="center"),
    )
)
pio.templates.default = "simple_white+pds"

set_matplotlib_formats("svg")
sns.set_context("poster")
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# display options for numpy and pandas
np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

# Use plotly as default plotting engine
pd.options.plotting.backend = "plotly"


def display_df(
    df, rows=pd.options.display.max_rows, cols=pd.options.display.max_columns
):
    """Displays n rows and cols from df"""
    with pd.option_context(
        "display.max_rows", rows, "display.max_columns", cols
    ):
        display(df)


def dfs_side_by_side(*dfs):
    """
    Displays two or more dataframes side by side.
    """
    display(
        HTML(
            f"""
        <div style="display: flex; gap: 1rem;">
        {''.join(df.to_html() for df in dfs)}
        </div>
    """
        )
    )
