import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Definimos el título de nuestra aplicación:
st.title('Mi aplicación de visualización de datos')
# Pedimos al usuario que cargue un archivo CSV con datos:
datafile = st.file_uploader('Cargar archivo CSV', type='csv')
if datafile:
  df = pd.read_csv(datafile)
# Si el usuario cargó un archivo CSV, mostramos los datos en una tabla:
if 'df' in locals():
    st.write(df)
# Añadimos algunas visualizaciones básicas, como un histograma y un gráfico de dispersión:
if 'df' in locals():
    st.subheader('Visualizaciones')
    # Histograma
    plt.hist(df['columna1'])
    st.pyplot()

    # Gráfico de dispersión
    plt.scatter(df['columna1'], df['columna2'])
    st.pyplot()
