def calcula_periodos(df):
    """
    Detecta periodos de sequía a partir de la columna 'nivell_suavizado'.

    Se define sequía como aquellos periodos donde el volumen suavizado
    está por debajo del 60% de forma continua.

    Args:
        df (DataFrame): DataFrame con columnas 'dia_decimal' y 'nivell_suavizado'.

    Returns:
        List[List[float, float]]: Lista de periodos de sequía, con fechas en formato decimal.
    """
    print("\nBuscando periodos de sequía...")

    bajo = df["nivell_suavizado"] < 60
    periodos = []
    inicio = None

    for i, es_bajo in enumerate(bajo):
        if es_bajo and inicio is None:
            inicio = float(df["dia_decimal"].iloc[i])
        elif not es_bajo and inicio is not None:
            fin = float(df["dia_decimal"].iloc[i - 1])
            periodos.append([round(inicio, 2), round(fin, 2)])
            inicio = None

    if inicio is not None:
        fin = float(df["dia_decimal"].iloc[-1])
        periodos.append([round(inicio, 2), round(fin, 2)])

    return periodos
