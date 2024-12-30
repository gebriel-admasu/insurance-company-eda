import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(df, numeric_cols, output_path):
    """Plot histograms for numeric columns."""
    for col in numeric_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f"Histogram of {col}")
        plt.savefig(f"{output_path}/{col}_histogram.png")
        plt.close()

def plot_bar_charts(df, categorical_cols, output_path):
    """Plot bar charts for categorical columns."""
    for col in categorical_cols:
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x=col)
        plt.title(f"Bar Chart of {col}")
        plt.xticks(rotation=45)
        plt.savefig(f"{output_path}/{col}_barchart.png")
        plt.close()
