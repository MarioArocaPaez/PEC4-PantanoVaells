import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import os

def graficar_evolucion(df, nombre):
    """
    Genera una gráfica de la evolución del volumen de agua (%)
    y la guarda como imagen PNG en la carpeta 'img/'.

    Args:
        df (DataFrame): Datos del embalse La Baells.
        nombre (str): Nombre del alumno para el subtítulo y nombre del archivo.
    """
    os.makedirs("img", exist_ok=True)
    ruta_salida = f"img/labaells_{nombre}.png"

    plt.figure(figsize=(10, 5))
    plt.plot(df["dia"], df["nivell_perc"], label="Volumen (%)")
    plt.title(f"Volumen La Baells - {nombre}")
    plt.xlabel("Fecha")
    plt.ylabel("Volumen (%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close()

    print(f"\nGráfico de evolución guardado en: {ruta_salida}")

def graficar_suavizado(df, nombre):
    """
    Aplica suavizado con Savitzky-Golay sobre el volumen (%),
    genera gráfica comparativa y guarda como PNG.

    Args:
        df (DataFrame): Datos del embalse con columna 'dia_decimal'.
        nombre (str): Nombre del alumno para el subtítulo y nombre del archivo.
    
    Returns:
        DataFrame: Mismo DataFrame con nueva columna 'nivell_suavizado'.
    """
    os.makedirs("img", exist_ok=True)
    ruta_salida = f"img/labaells_smoothed_{nombre}.png"

    y = df["nivell_perc"]

    if len(y) < 1500:
        raise ValueError("El número de registros debe ser al menos 1500 para aplicar Savitzky-Golay.")

    y_smooth = savgol_filter(y, window_length=1500, polyorder=3)

    plt.figure(figsize=(10, 5))
    plt.plot(df["dia_decimal"], y, alpha=0.5, label="Original")
    plt.plot(df["dia_decimal"], y_smooth, linewidth=2.5, label="Suavizado")
    plt.title(f"Volumen suavizado - {nombre}")
    plt.xlabel("Año (decimal)")
    plt.ylabel("Volumen (%)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close()

    print(f"Gráfico suavizado guardado en: {ruta_salida}")
    print(f"Columna 'nivell_suavizado' añadida al DataFrame.")

    df["nivell_suavizado"] = y_smooth
    return df
