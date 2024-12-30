import pandas as pd

def load_data(file_path):
    """Load dataset from the given file path."""
    return pd.read_csv(file_path)

def summarize_data(df):
    """Summarize data by providing column info and basic statistics."""
    return {
        "info": df.info(),
        "head": df.head(),
        "describe": df.describe(include="all")
    }
