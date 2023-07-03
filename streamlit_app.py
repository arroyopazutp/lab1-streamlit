import streamlit as st
import pandas as pd

df = pd.read_csv("https://gist.github.com/jaidevd/23aef12e9bf56c618c41#file-books-csv")

# Encabezado de la aplicación
st.header("Visualización de datos - Libros")

# Sección para filtrar los datos
st.sidebar.header("Filtros")
author = st.sidebar.selectbox("Autor", df["author"].unique())
year = st.sidebar.slider("Año de publicación", 1900, 2022, 2020)
price = st.sidebar.slider("Precio", 0.0, 100.0, (0.0, 100.0))

# Filtrar los datos en base a los filtros establecidos
filtered_df = df[(df["author"] == author) & (df["year"] == year) & (df["price"] >= price[0]) & (df["price"] <= price[1])]

# Mostrar los resultados
st.write(filtered_df)
