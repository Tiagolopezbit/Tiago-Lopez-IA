from sklearn.preprocessing import LabelEncoder, StandardScaler

def codificar(df, le_provincia, le_target):
    df = df.copy()
    df['stateProvince_enc'] = le_provincia.fit_transform(df['stateProvince'])
    df['target'] = le_target.fit_transform(df['scientificName'])
    return df

def escalar(df, features, scaler):
    df = df.copy()
    df[features] = scaler.fit_transform(df[features])
    return df
