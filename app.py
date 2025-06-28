import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="EDA Titanic", layout="wide")

st.title("Analisis De Datos del Titanic")

#cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
    
df = load_data()

st.dataframe(df)

st.subheader("Informacion Basica")
col1, col2, col3 = st.columns(3)
col1.metric("Filas: ", df.shape[0])
col1.metric("Columnas:  ", df.shape[1])
col1.metric("Nulos Totales:  ",df.isnull().sum().sum())

st.subheader("Valores Nulos")
st.write(df.isnull().sum())

st.subheader("Estadisticas")
st.write(df.describe())

st.subheader("Visualizaciones")

with st.expander("Distribucion de las Edades"):
    fig, ax = plt.subplots()
    sns.histplot(df['Age'].dropna(), kde=True, ax=ax)
    st.pyplot(fig)