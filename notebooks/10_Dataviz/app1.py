import plotly.express as px
import streamlit as st
df = px.data.gapminder()


paises = df['country'].unique()

pais = st.selectbox(label='Seleccione pais', options=paises)


mask = df['country'] == pais
dff = df[mask]
fig = px.line(data_frame=dff, x='year', y='lifeExp')
st.plotly_chart(fig)
color="rojo"

