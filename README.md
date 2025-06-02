# Proyecto: Análisis del embalse La Baells

Este proyecto analiza los datos históricos del volumen de agua en el pantano de La Baells. Permite visualizar la evolución del nivel, aplicar un suavizado y detectar periodos de sequía.

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
