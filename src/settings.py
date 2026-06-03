import pandas as pd
from pathlib import Path

# Path Configuration
BASE = Path(__file__).resolve().parents[1]

PATHS = {"raw_customers": BASE/"data"/"raw"/"customers.csv",
         "raw_loans": BASE/"data"/"raw"/"loans.csv",
         "raw_transactions": BASE/"data"/"raw"/"transactions.csv",
         "clean_customers": BASE/"data"/"cleaned"/"customers_clean.csv",
         "clean_loans": BASE/"data"/"cleaned"/"loans_clean.csv",
         "clean_transactions": BASE/"data"/"cleaned"/"transactions_clean.csv",
         "features": BASE/"data"/"processed"/"features.csv",
         "segments": BASE/"data"/"processed"/"segments.csv",
         }

# Settings Functions
def apply_pandas_settings():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.float_format', '{:.2f}'.format)

def apply_plot_settings():
    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.set_style('whitegrid')

    plt.rcParams['figure.figsize'] = (10,6)
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.labelsize'] = 12


    