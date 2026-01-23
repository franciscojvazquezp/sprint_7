import plotly.express as px
import streamlit as st
import pandas as pd
car_data = pd.read_csv('Notebooks/vehicles_us.csv')
print(car_data.head())
hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
disp_button = st.button('Construir gráfica de dispersión')
if disp_button:
    st.write('Creación de una gráfica de dispersión para el conjunto de datos de anuncio de venta de coches')
    fig_2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_2, use_container_width=True)
