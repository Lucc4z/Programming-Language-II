import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

st.title("Análisis Estadístico Descriptivo y Gráficos de Normalidad")

uploaded_file = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.header("Vista previa de los datos")
    st.write(df.head())

    st.header("Resumen Estadístico Descriptivo")
    st.write(df.describe())

    st.header("Histogramas")
    column = st.selectbox("Selecciona una columna para el histograma", df.columns)
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    st.pyplot(plt)

    st.header("Gráfico Q-Q")
    plt.figure(figsize=(10, 6))
    stats.probplot(df[column], dist="norm", plot=plt)
    st.pyplot(plt)

    st.header("Pruebas de Normalidad")
    st.write("Prueba de Shapiro-Wilk:")
    shapiro_test = stats.shapiro(df[column])
    st.write(f"Estadístico: {shapiro_test.statistic}, p-valor: {shapiro_test.pvalue}")

    st.write("Prueba de D'Agostino y Pearson:")
    dagostino_test = stats.normaltest(df[column])
    st.write(f"Estadístico: {dagostino_test.statistic}, p-valor: {dagostino_test.pvalue}")

    st.write("Prueba de Anderson-Darling:")
    anderson_test = stats.anderson(df[column], dist='norm')
    st.write(f"Estadístico: {anderson_test.statistic}")
    for i in range(len(anderson_test.critical_values)):
        sl, cv = anderson_test.significance_level[i], anderson_test.critical_values[i]
        st.write(f"Nivel de significancia {sl}: valor crítico {cv}")
