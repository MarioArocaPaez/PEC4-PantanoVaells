import pandas as pd

def load_data(ruta):
    """Cargar el dataset desde un CSV y devuelve un DataFrame"""
    return pd.read_csv(ruta)

def explora_datos(df):
    """Muestra primeras filas, columnas e infor general del DataFrame"""
    print("Primeras Filas:")
    print(df.head())
    print("\nColumnas:")
    print(df.columns)
    print("\nInfo:")
    print(df.info())