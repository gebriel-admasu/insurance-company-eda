from scipy.stats import pearsonr, chi2_contingency

def calculate_correlation(df, col1, col2):
    """Calculate Pearson correlation between two columns."""
    correlation, p_value = pearsonr(df[col1], df[col2])
    return correlation, p_value

def chi_square_test(df, col1, col2):
    """Perform Chi-Square test between two categorical variables."""
    contingency_table = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    return chi2, p
