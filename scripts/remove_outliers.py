# Detect and remove outliers for each numeric column
from .check_for_outliers import detect_outliers
def remove_outliers(df):
    numeric_columns = df.select_dtypes(include=['int64', 'float64'])
    for column in numeric_columns:
        outliers = detect_outliers(df, column)
        df = df.drop(outliers.index)
    return df