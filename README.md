# Proyecto: Análisis del embalse La Baells

Autor: Mario Aroca Páez (marocap)

Este proyecto analiza los datos históricos del volumen de agua en el embalse de La Baells (Catalunya). El análisis permite:

- Cargar y explorar los datos.
- Limpiar y transformar el dataset.
- Visualizar gráficamente la evolución del volumen.
- Aplicar suavizado para detectar tendencias.
- Identificar periodos de sequía.

Los datos se obtienen del portal de datos abiertos de la Generalitat de Catalunya:

[Quantitat d'aigua als embassaments - Generalitat de Catalunya](https://analisi.transparenciacatalunya.cat/Medi-Ambient/Quantitat-d-aigua-als-embassaments-de-les-Conques-/gn9e-3qhr/about_data)

## Estructura

```
PEC4-PantanoBaells/
├── src/
│   ├── main.py
│   └── modules/
│       ├── load.py
│       ├── clean.py
│       ├── transform.py
│       ├── visualize.py
│       └── drought.py
├── tests/
├── img/
├── doc/
├── screenshots/
├── setup.py
├── requirements.txt
├── .pylintrc
```

## Instalación

```bash
python -m venv venv
source venv/bin/activate   # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt
```

## Ejecución

```bash
python src/main.py             # Ejecuta todos los ejercicios
python src/main.py -ex 3       # Ejecuta hasta el ejercicio 3
```

## Tests

```bash
pytest --cov=src/modules tests/
```

## Documentación

```bash
pdoc src/modules --html -o doc
```

## Estilo de código

```bash
pylint src/modules
```

Capturas de pantalla de tests, cobertura, documentación y linter deben estar en la carpeta `screenshots/`.

## Licencia

MIT License.
