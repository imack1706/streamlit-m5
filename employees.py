import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

# Cargar el archivo CSV en un DataFrame (employees)
@st.cache
def datos(nrows=500):
    data = pd.read_csv('Employees.csv', nrows=nrows)
    return data

employees = datos()

# Crear título y descripciones
st.title('Datos de Empleados')
st.header('Análisis de Datos de Empleados')
st.write('Esta información resultará explicativa del fenómeno de deserción laboral que tanto afecta en la actualidad a las empresas y organizaciones.')

# Crear sidebar
st.sidebar.header('Menú')

# Mostrar DataFrame con checkbox
show_dataframe = st.sidebar.checkbox('Mostrar DataFrame completo')
if show_dataframe:
    st.write('DataFrame completo:')
    st.write(employees)

# Buscador de empleados
st.sidebar.subheader('Buscador')
search_term = st.sidebar.text_input('Buscar por Employee_ID, Hometown o Unit')
filtro_employees = employees[employees.apply(lambda row: search_term.lower() in row.to_string().lower(), axis=1)]
st.sidebar.write('Resultados encontrados:', len(filtro_employees))
if len(filtro_employees) > 0:
    st.write('Resultados:')
    st.write(filtro_employees)

# Filtrar por nivel educativo
education_levels = employees['Education_Level'].unique()
education = st.sidebar.selectbox('Seleccionar Nivel Educativo', education_levels)
education_employees = employees[employees['Education_Level'] == education]
st.sidebar.write('Total de empleados con nivel educativo {}:'.format(education), len(education_employees))
if len(education_employees) > 0:
    st.write('Empleados con nivel educativo', education)
    st.write(education_employees)

# Filtrar por ciudad 
cities = employees['Hometown'].unique()
city = st.sidebar.selectbox('Seleccionar Ciudad', cities)
city_employees = employees[employees['Hometown'] == city]
st.sidebar.write('Total de empleados en', city + ':', len(city_employees))
if len(city_employees) > 0:
    st.write('Empleados en', city)
    st.write(city_employees)

# Filtrar por unidad funcional 
units = employees['Unit'].unique()
unit = st.sidebar.selectbox('Seleccionar Unidad Funcional', units)
unit_employees = employees[employees['Unit'] == unit]
st.sidebar.write('Total de empleados en la unidad', unit + ':', len(unit_employees))
if len(unit_employees) > 0:
    st.write('Empleados en la unidad', unit)
    st.write(unit_employees)

# Histograma de edades
st.header('Histograma de Edades')
plt.figure(figsize=(8, 6))
sns.histplot(data=employees, x='Age', bins=20, kde=True)
st.pyplot()

# Gráfica de frecuencias por unidades funcionales
st.header('Gráfica de Frecuencias por Unidades Funcionales')
plt.figure(figsize=(10, 6))
sns.countplot(data=employees, y='Unit')
st.pyplot()

# Análisis de deserción por ciudades (Hometown)
st.header('Análisis de Deserción por Ciudades')
desertion_by_city = employees.groupby('Hometown')['Attrition_rate'].mean()
plt.figure(figsize=(10, 6))
sns.barplot(x=desertion_by_city.index, y=desertion_by_city.values)
plt.xticks(rotation=45)
st.pyplot()

# Análisis de deserción por edad
st.header('Análisis de Deserción por Edad')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=employees, x='Age', y='Attrition_rate')
st.pyplot()

# Análisis de relación entre tiempo de servicio y deserción
st.header('Análisis de Relación entre Tiempo de Servicio y Deserción')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=employees, x='Time_of_service', y='Attrition_rate')
st.pyplot()
