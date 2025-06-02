import os
import pandas as pd
from src.modules import visualize

def test_graficar_evolucion(tmp_path):
    df = pd.DataFrame({
        "dia": pd.date_range(start="2020-01-01", periods=10),
        "nivell_perc": [50, 55, 53, 60, 62, 61, 59, 58, 56, 54]
    })
    nombre = "test_evolucion"
    img_path = tmp_path / f"labaells_{nombre}.png"

    # Cambiar directorio de guardado temporalmente
    original_os_makedirs = os.makedirs
    os.makedirs = lambda path, exist_ok: None
    original_savefig = visualize.plt.savefig
    visualize.plt.savefig = lambda path: img_path.write_text("imagen")

    visualize.graficar_evolucion(df, nombre)

    # Restaurar funciones
    os.makedirs = original_os_makedirs
    visualize.plt.savefig = original_savefig

    assert img_path.exists()

def test_graficar_suavizado(tmp_path):
    df = pd.DataFrame({
        "dia_decimal": list(range(1500)),
        "nivell_perc": [50 + ((-1) ** i) * (i % 5) for i in range(1500)]
    })

    nombre = "test_suavizado"
    img_path = tmp_path / f"labaells_smoothed_{nombre}.png"

    # Simular la escritura del archivo sin necesidad de backend gráfico
    original_savefig = visualize.plt.savefig
    visualize.plt.savefig = lambda path: img_path.write_text("imagen")

    # Ejecutar función
    df_resultado = visualize.graficar_suavizado(df.copy(), nombre)

    # Restaurar savefig
    visualize.plt.savefig = original_savefig

    # Verificaciones
    assert img_path.exists()
    assert "nivell_suavizado" in df_resultado.columns
    assert len(df_resultado["nivell_suavizado"]) == 1500