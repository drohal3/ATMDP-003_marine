import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import MaxNLocator

path = "./local/Tvarminne/Trace_gases/preprocessed/CO.parquet"

def main():
    df = pd.read_parquet(path, engine="pyarrow")
    monthly_groups = df.groupby(df.index.to_period("M"))
    print(monthly_groups)

if __name__ == "__main__":
    main()
