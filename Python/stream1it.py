import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

def main():
    st.title("Análisis de Datos con Streamlit")

    uploaded_file = st.file_uploader("Sube un archivo CSV o Excel", type=["csv", "xlsx", "xls"])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.write("### Datos del archivo")
            st.write(df)
            
            st.write("### Resumen Estadístico")
            st.write(df.describe().transpose())

            st.write("### Visualización de Datos")
            
            chart_type = st.selectbox("Selecciona el tipo de gráfico", ["Histogram", "Boxplot", "D. de Dispersión", "Ojiva", "Regresión Lineal"])

            if chart_type == "Histogram":
                column = st.selectbox("Selecciona la columna para el histograma", df.columns)
                plt.figure(figsize=(10, 6))
                sns.histplot(df[column], kde=True)
                st.pyplot(plt)
            
            elif chart_type == "Boxplot":
                column = st.selectbox("Selecciona la columna para el boxplot", df.columns)
                plt.figure(figsize=(10, 6))
                sns.boxplot(y=df[column])
                st.pyplot(plt)
            
            elif chart_type == "D. de Dispersión":
                col1 = st.selectbox("Selecciona la columna para el eje X", df.columns)
                col2 = st.selectbox("Selecciona la columna para el eje Y", df.columns)
                plt.figure(figsize=(10, 6))
                sns.scatterplot(x=df[col1], y=df[col2])
                st.pyplot(plt)
                
            elif chart_type == "Ojiva":
                column = st.selectbox("Selecciona la columna para la ojiva", df.columns)
                plt.figure(figsize=(10, 6))
                sns.histplot(df[column], kde=False, cumulative=True, stat="density", bins=30)
                plt.xlabel(column)
                plt.ylabel("Frecuencia acumulada")
                plt.title("Ojiva")
                st.pyplot(plt)

            elif chart_type == "Regresión Lineal":
                col1 = st.selectbox("Selecciona la columna para el eje X", df.columns)
                col2 = st.selectbox("Selecciona la columna para el eje Y", df.columns)
                
                X = df[[col1]]
                Y = df[col2]
                model = LinearRegression()
                model.fit(X, Y)
                Y_pred = model.predict(X)
                
                plt.figure(figsize=(10, 6))
                sns.scatterplot(x=df[col1], y=df[col2], label='Datos')
                plt.plot(df[col1], Y_pred, color='red', label='Regresión Lineal')
                st.pyplot(plt)
                
                st.write("### Resultados de la Regresión Lineal")
                st.write(f"Intercepto: {model.intercept_}")
                st.write(f"Coeficiente: {model.coef_[0]}")
                
                X2 = sm.add_constant(X)
                est = sm.OLS(Y, X2)
                est2 = est.fit()
                st.write(est2.summary())
            
            st.write("### Cálculos Estadísticos")
            stats_col = st.selectbox("Selecciona la columna para cálculos estadísticos", df.columns)
            if df[stats_col].dtype in ['float64', 'int64']:
                mean = df[stats_col].mean()
                median = df[stats_col].median()
                var = df[stats_col].var()
                std = df[stats_col].std()
                min_val = df[stats_col].min()
                max_val = df[stats_col].max()
                range_val = max_val - min_val
                iqr = df[stats_col].quantile(0.75) - df[stats_col].quantile(0.25)
                skewness = df[stats_col].skew()
                kurtosis = df[stats_col].kurt()

                st.write(f"Media: {mean}")
                st.write(f"Mediana: {median}")
                st.write(f"Varianza: {var}")
                st.write(f"Desviación Estándar: {std}")
                st.write(f"Mínimo: {min_val}")
                st.write(f"Máximo: {max_val}")
                st.write(f"Rango: {range_val}")
                st.write(f"Rango Intercuartílico: {iqr}")
                st.write(f"Simetría: {skewness}")
                st.write(f"Curtosis: {kurtosis}")

                numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
                if len(numeric_cols) > 1:
                    st.write("### Matriz de Correlación")
                    corr_matrix = df[numeric_cols].corr()
                    st.write(corr_matrix)
                    plt.figure(figsize=(10, 6))
                    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
                    st.pyplot(plt)
        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    main()