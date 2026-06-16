import pandas as pd

def extraer_features(df):
    df = df.copy()
    df['eventDate'] = pd.to_datetime(df['eventDate'], errors='coerce')
    df['año'] = df['eventDate'].dt.year
    df['mes'] = df['eventDate'].dt.month
    df = df.dropna(subset=['año', 'mes'])
    return df
