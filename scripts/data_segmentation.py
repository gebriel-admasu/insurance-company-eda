import pandas as pd

def create_groups(data, feature, group_a_value, group_b_value):
    """
    Segment data into two groups based on a feature.
    """
    group_a = data[data[feature] == group_a_value]
    group_b = data[data[feature] == group_b_value]
    return group_a, group_b
