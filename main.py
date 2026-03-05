import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import MaxNLocator

path = "./local/Tvarminne/Trace_gases/preprocessed/CO.parquet"

BOX_PLOT_GROUP_MONTH_MAP = {
    "winter 2022": {
        "months": ["2021-12", "2022-01", "2022-02"],
    },
    "spring 2022": {
        "months": ["2022-03", "2022-04", "2022-05"],
    },
    "summer 2022": {
        "months": ["2022-06", "2022-07", "2022-08"],
    },
    "autumn 2022": {
        "months": ["2022-09", "2022-10", "2022-11"],
    },
    "winter 2023": {
        "months": ["2022-12", "2023-01", "2023-02"],
    },
    "spring 2023": {
        "months": ["2023-03", "2023-04", "2023-05"],
    },
    "summer 2023": {
        "months": ["2023-06", "2023-07", "2023-08"],
    },
    "autumn 2023": {
        "months": ["2023-09", "2023-10", "2023-11"],
    },
    "winter 2024": {
        "months": ["2023-12", "2024-01", "2024-02"],
    },
    "spring 2024": {
        "months": ["2024-03", "2024-04", "2024-05"],
    },
    "summer 2024": {
        "months": ["2024-06", "2024-07", "2024-08"],
    },
    "autumn 2024": {
        "months": ["2024-09", "2024-10", "2024-11"],
    },
    "winter 2025": {
        "months": ["2024-12", "2025-01", "2025-02"],
    },
    "spring 2025": {
        "months": ["2025-03", "2025-04", "2025-05"],
    },
    "summer 2025": {
        "months": ["2025-06", "2025-07", "2025-08"],
    },
    "autumn 2025": {
        "months": ["2025-09", "2025-10", "2025-11"],
    },
}

# TODO: produce from map above
BOX_PLOT_SEASON_GROUP_MAP = {

  "2022-03": "spring 2022",
  "2022-04": "spring 2022",
  "2022-05": "spring 2022",
  "2022-06": "summer 2022",
  "2022-07": "summer 2022",
  "2022-08": "summer 2022",
  "2022-09": "autumn 2022",
  "2022-10": "autumn 2022",
  "2022-11": "autumn 2022",
  "2022-12": "winter 2023",
  "2023-01": "winter 2023",
  "2023-02": "winter 2023",
  "2023-03": "spring 2023",
  "2023-04": "spring 2023",
  "2023-05": "spring 2023",
  "2023-06": "summer 2023",
  "2023-07": "summer 2023",
  "2023-08": "summer 2023",
  "2023-09": "autumn 2023",
  "2023-10": "autumn 2023",
  "2023-11": "autumn 2023",
  "2023-12": "winter 2024",
  "2024-01": "winter 2024",
  "2024-02": "winter 2024",
  "2024-03": "spring 2024",
  "2024-04": "spring 2024",
  "2024-05": "spring 2024",
  "2024-06": "summer 2024",
  "2024-07": "summer 2024",
  "2024-08": "summer 2024",
  "2024-09": "autumn 2024",
  "2024-10": "autumn 2024",
  "2024-11": "autumn 2024",
  "2024-12": "winter 2025",
  "2025-01": "winter 2025",
  "2025-02": "winter 2025",
  "2025-03": "spring 2025",
  "2025-04": "spring 2025",
  "2025-05": "spring 2025",
  "2025-06": "summer 2025",
  "2025-07": "summer 2025",
  "2025-08": "summer 2025",
  "2025-09": "autumn 2025",
  "2025-10": "autumn 2025",
  "2025-11": "autumn 2025",
}

def main():
    df = pd.read_parquet(path, engine="pyarrow")
    monthly_groups = df.groupby(df.index.to_period("M"))
    data = {}
    labels = []

    for period, group in monthly_groups:
        season_group = BOX_PLOT_SEASON_GROUP_MAP.get(str(period), None)
        if season_group is None:
            print(f"Season not found for period: {period}")
            continue

        print(f"Processing period: {period}, season group: {season_group}")

        continue

        group_name = f"{season_group} {year}"
        existing_data = data.get(group_name, np.array())
        existing_data.extend(group[df.columns[0]].values)  # change column if needed
        data[group_name] = existing_data
        print(group)

        # data.append(group[df.columns[0]].values)   # change column if needed
        # labels.append(str(period))

    return
    plt.figure()
    plt.boxplot(data)
    plt.xticks(range(1, len(labels) + 1), labels, rotation=45)
    plt.xlabel("Month")
    plt.ylabel("Value")
    plt.title("Monthly Boxplots")
    plt.tight_layout()
    plt.show()
    print(monthly_groups)

if __name__ == "__main__":
    main()
