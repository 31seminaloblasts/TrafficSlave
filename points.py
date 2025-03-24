import pandas as pd
def locations(file_path):
    df = pd.read_csv(file_path)
    return [
        {"coordinates": (row['latitude'], row['longitude']), "customers": row['customers']}
        for _, row in df.iterrows()
    ]
def population(file_path):
    df = pd.read_csv(file_path)
    return [
        {"coordinates": (row['latitude'], row['longitude']), "population": row['population']}
        for _, row in df.iterrows()
    ]
