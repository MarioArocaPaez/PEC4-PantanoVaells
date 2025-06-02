import pandas as pd
from src.modules import clean

def test_renombrar_columnas():
    df = pd.DataFrame({
        "Dia": ["01/01/2020"],
        "Estació": ["Embassament de La Baells (Cercs)"],
        "Nivell absolut (msnm)": [500],
        "Percentatge volum embassat (%)": [60],
        "Volum embassat (hm3)": [100]
    })
    df = clean.renombrar_columnas(df)
    assert "estacio" in df.columns

def test_filtrar_labaells():
    df = pd.DataFrame({
        "estacio": ["La Baells", "Susqueda"],
        "volum": [50, 60]
    })
    df_filtrado = clean.filtrar_labaells(df)
    assert df_filtrado.shape[0] == 1
    assert df_filtrado["estacio"].iloc[0].lower() == "la baells"
