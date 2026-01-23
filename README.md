# sprint_7

# Análisis de Datos de Vehículos - Aplicación Web

## Descripción del Proyecto

Esta aplicación web interactiva permite explorar un conjunto de datos de anuncios de venta de coches. La aplicación está construida con Streamlit y proporciona visualizaciones interactivas para analizar las características de los vehículos en venta.

## Funcionalidades

- **Histograma interactivo**: Visualiza la distribución del odómetro de los vehículos
- **Gráfico de dispersión**: Explora la relación entre el kilometraje (odómetro) y el precio de los vehículos
- **Interfaz intuitiva**: Botones interactivos para generar las visualizaciones bajo demanda

## Archivos del Proyecto

- `app.py`: Aplicación principal de Streamlit
- `vehicles_us.csv`: Conjunto de datos de vehículos
- `EDA.ipynb`: Análisis exploratorio de datos
- `requirements.txt`: Dependencias del proyecto

## Tecnologías Utilizadas

- Python
- Streamlit
- Plotly Express
- Pandas

## Cómo Ejecutar la Aplicación

```bash
streamlit run app.py
```

Dependencias del Proyecto
El archivo requirements.txt incluye las siguientes librerías:

pandas: Manipulación y análisis de datos
plotly_express: Creación de gráficos interactivos
streamlit: Framework para crear aplicaciones web de datos

## Instalación

bash
pip install -r requirements.txt
