import re

def renombrar_columnas(df):
    """Renombra las columnas originales del DataFrame a nombres más simples."""
    mapping = {
        "Dia": "dia",
        "Estació": "estacio",
        "Nivell absolut (msnm)": "nivell_msnm",
        "Percentatge volum embassat (%)": "nivell_perc",
        "Volum embassat (hm3)": "volum"
    }
    df = df.rename(columns=mapping)
    print(f"\nColumnas renombradas: {list(df.columns)}")
    return df

def normalizar_nombres_pantano(df):
    """Elimina 'Embassament de' y el municipio entre paréntesis del nombre del pantano."""
    df["estacio"] = df["estacio"].str.replace(r"Embassament de ", "", regex=True)
    df["estacio"] = df["estacio"].str.replace(r"\s*\(.*\)", "", regex=True)
    print(f"\nNombres normalizados. Valores únicos: {df['estacio'].unique()[:5]}")
    return df

def filtrar_labaells(df):
    """Filtra los datos correspondientes al embalse de La Baells (sin importar mayúsculas)."""
    df_filtrado = df[df["estacio"].str.lower() == "la baells".lower()].copy()
    print(f"\nFiltrado 'La Baells': {df_filtrado.shape[0]} registros encontrados.")
    return df_filtrado