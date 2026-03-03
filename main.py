import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("./local/Tvarminne/CIApi_data/MION_NO3_WinterSchool.csv")
    # corr_df = df.drop(columns=["Time"])
    # corr = corr_df.corr()
    # print(df.head())
    # print(df.drop(columns=["Time"]).corr())
    plt.figure(figsize=(10,10))
    sns.heatmap(
        df.drop(columns=["Time"]).corr(),
        annot=True,
        vmin=-1, vmax=1, center=0, 
        xticklabels=1, 
        yticklabels=1)
    plt.show()

if __name__ == "__main__":
    main()
