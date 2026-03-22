# Estructura del Proyecto - ME02 Especialización

## 📁 Árbol de Directorios

```
ME02_especializacion/
│
├── 📁 data/                           # Datos del proyecto
│   ├── raw/                           # Datos originales sin procesar
│   │   └── (archivos fuente originales)
│   │
│   └── processed/                     # Datos después del preprocesamiento
│       ├── X_train_flat.csv          # Features procesadas
│       └── y_train.csv               # Target variable
│
├── 📁 notebooks/                      # Jupyter Notebooks (análisis iterativo)
│   ├── 01_EDA.ipynb                  # Análisis Exploratorio de Datos
│   └── 02_Preprocesamiento.ipynb    # Limpieza y Preparación de Datos
│
├── 📁 src/                            # Código fuente reutilizable
│   ├── __init__.py                   # Inicializador del módulo
│   ├── data_processing.py            # Funciones de procesamiento de datos
│   └── analysis.py                   # Funciones de análisis estadístico
│
├── 📁 results/                        # Resultados y salidas
│   ├── figures/                       # Gráficos y visualizaciones
│   │   └── (archivos .png, .jpg, etc.)
│   │
│   └── metrics/                       # Métricas y reportes
│       └── (archivos .json, .csv, etc.)
│
├── 📁 docs/                           # Documentación del proyecto
│   └── (archivos markdown, documentación)
│
├── .gitignore                         # Archivos a ignorar en Git
├── requirements.txt                   # Dependencias de Python
├── README.md                          # Descripción general del proyecto
└── ESTRUCTURA.md                      # Este archivo
```

## 📋 Descripción de Directorios

### `data/`
- **raw/**: Almacena datos originales sin modificar. Útil para mantener referencia de los datos originales.
- **processed/**: Contiene datos limpios y preparados listos para análisis.

### `notebooks/`
- Jupyter Notebooks numerados en orden de ejecución
- Cada notebook documenta el proceso con explicaciones detalladas
- Ideal para exploración iterativa y documentación de análisis

### `src/`
- Módulo Python con código reutilizable
- `data_processing.py`: Funciones para limpiar y normalizar datos
- `analysis.py`: Funciones para análisis estadístico y pruebas
- Permite importar funciones en otros notebooks/scripts

### `results/`
- **figures/**: Gráficos, visualizaciones, plots
- **metrics/**: Métricas, reportes, resultados numéricos

### `docs/`
- Documentación técnica del proyecto
- Explicaciones de metodología
- Notas de investigación

## 🚀 Cómo Usar Este Proyecto

### 1. Configurar el Ambiente
```bash
# Crear ambiente virtual
python -m venv venv
source venv/Scripts/activate  # En Windows

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Ejecutar Análisis
```bash
# Abrir Jupyter Lab
jupyter lab

# Ejecutar notebooks en orden:
# 1. notebooks/01_EDA.ipynb
# 2. notebooks/02_Preprocesamiento.ipynb
```

### 3. Usar el Módulo `src/`
```python
from src import data_processing, analysis
import pandas as pd

# Limpiar datos
df_clean = data_processing.clean_macro_data(df)

# Realizar análisis
stats = analysis.descriptive_statistics(series)
```

## 📦 Dependencias Principales

Ver `requirements.txt` para la lista completa:
- **pandas**: Manipulación de datos
- **numpy**: Cálculos numéricos
- **matplotlib/seaborn**: Visualización
- **jupyter**: Notebooks interactivos
- **yfinance**: Descarga de datos financieros
- **statsmodels**: Análisis de series temporales
- **scikit-learn**: Machine Learning

## 📝 Convenciones del Proyecto

- Nombres de directorios: minúsculas, separados por guión bajo
- Nombres de archivos: descriptivos, numerados si hay orden
- Notebooks: `NN_descripcion.ipynb` (NN = número de orden)
- Código Python: PEP 8 compliant
- Datos: CSV para processados, formatos originales en raw/

---

**Última actualización**: Marzo 2026
