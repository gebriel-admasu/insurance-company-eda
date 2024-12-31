def analyze_results(stat, p_value, alpha=0.05):
    """
    Analyze statistical test results.
    """
    if p_value < alpha:
        return "Reject the null hypothesis: Significant effect detected."
    else:
        return "Fail to reject the null hypothesis: No significant effect detected."
