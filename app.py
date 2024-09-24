import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV con los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado
st.header('Aplicación de Gráficos de Vehículos Usados')

# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

# Acción a realizar si se selecciona la casilla de verificación para el histograma
if build_histogram:
    # Escribir un mensaje
    st.write('Creación de un histograma para la columna odómetro')
    
    # Crear el histograma con Plotly
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Acción a realizar si se selecciona la casilla de verificación para el gráfico de dispersión
if build_scatter:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión de precio vs kilometraje')
    
    # Crear el gráfico de dispersión con Plotly
    fig = px.scatter(car_data, x="odometer", y="price", title='Relación entre kilometraje y precio')
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)