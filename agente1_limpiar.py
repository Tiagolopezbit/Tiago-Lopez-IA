import pandas as pd

def limpiar(df):
    filas_antes = len(df)
    df = df.drop_duplicates()
    df = df.dropna()
    print(f'Filas antes: {filas_antes} | Despues: {len(df)}')
    return df
