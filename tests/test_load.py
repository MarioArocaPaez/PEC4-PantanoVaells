import pandas as pd
from src.modules import load

def test_load_data():
    df = load.load_data("data/embassaments.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
