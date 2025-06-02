import pandas as pd
from datetime import datetime

def convertir_fecha(df):
    """Convierte la columna 'dia' a formato datetime y ordena por fecha ascendente."""
    df["dia"] = pd.to_datetime(df["dia"], format="%d/%m/%Y")
    df = df.sort_values("dia")
    print("\nColumna 'dia' convertida a datetime.")
    print(f"Tipo de dato de 'dia': {df['dia'].dtype}")
    return df

def mostrar_fechas(df):
    """Muestra información temporal del dataset."""
    fecha_min = df["dia"].min()
    fecha_max = df["dia"].max()
    total = len(df)
    print(f"\nFecha más antigua: {fecha_min.strftime('%d/%m/%Y')}")
    print(f"Fecha más reciente: {fecha_max.strftime('%d/%m/%Y')}")
    print(f"Número total de registros: {total}")

def toYearFraction(date):
    """
    Convierte un datetime a un número decimal de año.
    Ejemplo: 01/07/2025 → 2025.5 aproximadamente
    """
    def sinceEpoch(date):
        return (date - datetime(1970, 1, 1)).total_seconds()

    s = sinceEpoch
    year = date.year
    start = datetime(year=year, month=1, day=1)
    end = datetime(year=year + 1, month=1, day=1)

    return year + ((s(date) - s(start)) / (s(end) - s(start)))

def agregar_decimal(df):
    """Agrega una columna 'dia_decimal' con la fecha en formato decimal."""
    df["dia_decimal"] = df["dia"].apply(toYearFraction)
    print("\nColumna 'dia_decimal' añadida al DataFrame.")
    print("Ejemplo de valores:")
    print(df[["dia", "dia_decimal"]].head())
    return df
