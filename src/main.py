import argparse
from modules import load, clean, transform, visualize, drought

def main():
    parser = argparse.ArgumentParser(description="Analiza los datos del embalse La Baells")
    parser.add_argument("-ex", type=int, help="Ejercicio a ejectuar (1-5). Por defecto, todos.")
    args = parser.parse_args()

    # Ruta del dataset
    csv_path = "data/embassaments.csv"

    if not args.ex or args.ex >= 1:
        df = load.load_data(csv_path)
        load.explora_datos(df)

    if not args.ex or args.ex >= 2:
        df = clean.renombrar_columnas(df)
        df = clean.normalizar_nombres_pantano(df)
        df = clean.filtrar_labaells(df)

    if not args.ex or args.ex >= 3:
        df = transform.convertir_fecha(df)
        df = transform.agregar_decimal(df)
        transform.mostrar_fechas(df)

    if not args.ex or args.ex >= 4:
        visualize.graficar_evolucion(df, "Mario Aroca Páez")
        df = visualize.graficar_suavizado(df, "Mario Aroca Páez")

    if not args.ex or args.ex >= 5:
        periodos = drought.calcula_periodos(df)
        print("Periodos de sequía detectados:", periodos)

if __name__ == "__main__":
    main()