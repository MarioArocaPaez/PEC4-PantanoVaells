import pandas as pd
from src.modules import transform

def test_convertir_fecha():
    df = pd.DataFrame({"dia": ["01/01/2020", "02/01/2020"]})
    df = transform.convertir_fecha(df)
    assert pd.api.types.is_datetime64_any_dtype(df["dia"])

def test_agregar_decimal():
    df = pd.DataFrame({"dia": pd.to_datetime(["2020-01-01", "2020-07-01"])})
    df = transform.agregar_decimal(df)
    assert "dia_decimal" in df.columns
    assert isinstance(df["dia_decimal"].iloc[0], float)
