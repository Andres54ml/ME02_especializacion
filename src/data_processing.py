"""
Módulo para el procesamiento y limpieza de datos.
Contiene funciones reutilizables para limpiar y preparar los datos.
"""

import pandas as pd
import numpy as np


def clean_macro_data(df, replace_chars=None):
    """
    Limpia los datos macroeconómicos reemplazando valores inválidos con NaN.
    
    Args:
        df: DataFrame a limpiar
        replace_chars: Lista de caracteres a reemplazar por NaN (default: ["-", ""])
    
    Returns:
        DataFrame limpio
    """
    if replace_chars is None:
        replace_chars = ["-", ""]
    
    df_clean = df.copy()
    for char in replace_chars:
        df_clean = df_clean.replace(char, np.nan)
    
    return df_clean


def convert_to_numeric(series, errors='coerce'):
    """
    Convierte una serie a numérica de forma robusta.
    
    Args:
        series: Serie de pandas a convertir
        errors: Cómo manejar errores ('raise', 'coerce', 'ignore')
    
    Returns:
        Serie convertida a numérica
    """
    return pd.to_numeric(series, errors=errors)


def normalize_column_names(df):
    """
    Normaliza los nombres de columnas (minúsculas, sin espacios).
    
    Args:
        df: DataFrame a normalizar
    
    Returns:
        DataFrame con nombres normalizados
    """
    df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
    return df
