import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import MaxNLocator


DATA_BASE_PATH = "./local/Tvarminne/Trace_gases"
DATA_GASSES = ["CO", "NO", "O3", "SO2"]
# DATA_GASSES = ["SO2"]

PREPROCESS_SUBPATH = "preprocessed"

PREPROCESSED_DATA_PATH = f"{DATA_BASE_PATH}/{PREPROCESS_SUBPATH}"

def main():
    dfs = []

    for gas in DATA_GASSES:
        df = pd.read_parquet(f"{PREPROCESSED_DATA_PATH}/{gas}.parquet", engine="pyarrow")
        dfs.append(df)

    fig, axes = plt.subplots(
        len(dfs),
        1,
        figsize=(10, 8),
        sharex=True,
    )

    for ax, df, gas in zip(axes, dfs, DATA_GASSES):
        ax.plot(df.index, df[gas])
        ax.set_title(gas)
        ax.grid(True)
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5))

    plt.xlabel("Time")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
