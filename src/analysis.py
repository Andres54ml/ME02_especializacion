"""
Módulo para análisis de series temporales.
Contiene funciones para análisis univariado, correlaciones y visualizaciones.
"""

import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def descriptive_statistics(series, name=None):
    """
    Calcula estadísticas descriptivas de una serie.
    
    Args:
        series: Serie de pandas
        name: Nombre de la serie (opcional)
    
    Returns:
        Series con estadísticas descriptivas
    """
    stats = {
        'mean': series.mean(),
        'std': series.std(),
        'min': series.min(),
        'max': series.max(),
        'q25': series.quantile(0.25),
        'q50': series.quantile(0.50),
        'q75': series.quantile(0.75),
        'count': series.count(),
        'missing': series.isna().sum()
    }
    return pd.Series(stats, name=name)


def adf_test(series, name=None):
    """
    Realiza la prueba de Dickey-Fuller aumentada para estacionariedad.
    
    Args:
        series: Serie de pandas
        name: Nombre de la serie (opcional)
    
    Returns:
        Diccionario con resultados de la prueba
    """
    result = adfuller(series.dropna(), autolag='AIC')
    
    output = {
        'ADF Statistic': result[0],
        'p-value': result[1],
        'Lags Used': result[2],
        'Observations': result[3],
        'Critical Value (1%)': result[4]['1%'],
        'Critical Value (5%)': result[4]['5%'],
        'Critical Value (10%)': result[4]['10%'],
        'Is Stationary': 'Yes' if result[1] < 0.05 else 'No'
    }
    
    return output
