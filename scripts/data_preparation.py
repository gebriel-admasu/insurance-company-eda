import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def handle_missing_data(df, strategy="mean", threshold=0.3):
    """
    Handle missing data by removing or imputing based on strategy.
    """
    # Drop columns with too many missing values
    for col in df.columns:
        if df[col].isnull().mean() > threshold:
            df = df.drop(columns=[col])
    
    # Impute missing values
    if strategy == "mean":
        df = df.fillna(df.mean())
    elif strategy == "median":
        df = df.fillna(df.median())
    elif strategy == "mode":
        df = df.fillna(df.mode().iloc[0])
    return df

def encode_categorical_data(df, categorical_columns, method="onehot"):
    """
    Encode categorical columns using one-hot or label encoding.
    """
    if method == "onehot":
        return pd.get_dummies(df, columns=categorical_columns)
    elif method == "label":
        for col in categorical_columns:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
    return df

def split_data(df, target, test_size=0.3, random_state=42):
    """
    Split the data into training and test sets.
    """
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
