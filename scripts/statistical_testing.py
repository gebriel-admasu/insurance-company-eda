from scipy.stats import ttest_ind, chi2_contingency

def t_test(group_a, group_b, kpi):
    """
    Perform t-test on two numerical datasets.
    """
    stat, p_value = ttest_ind(group_a[kpi], group_b[kpi], equal_var=False)
    return stat, p_value

def chi_square_test(data, feature_a, feature_b):
    """
    Perform Chi-Square test for categorical features.
    """
    contingency_table = pd.crosstab(data[feature_a], data[feature_b])
    stat, p_value, _, _ = chi2_contingency(contingency_table)
    return stat, p_value
