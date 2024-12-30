def create_insightful_plots(df):
    """Generate creative plots for insights."""
    sns.boxplot(data=df, x='Province', y='TotalClaims')
    plt.title("Total Claims by Province")
    plt.show()

    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()
