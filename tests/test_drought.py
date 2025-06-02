import pandas as pd
from src.modules import drought

def test_calcula_periodos():
    df = pd.DataFrame({
        "dia_decimal": [2000.0, 2001.0, 2002.0, 2003.0, 2004.0],
        "nivell_suavizado": [70, 50, 50, 65, 70]
    })
    periodos = drought.calcula_periodos(df)
    assert periodos == [[2001.0, 2002.0]]
