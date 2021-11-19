import streamlit as st
import pandas as pd
import plotly.express as px

st.title('SERVER TEST')
st.write("""Upload file!""")
uploaded_file = st.file_uploader('Excel')
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    try:
        x = df.x
        y1 = df.y1
        y12 = df.y12
        y2 = df.y2
        y22 = df.y22

        fig1 = px.line(y=[y1,y12], x=x, template='plotly_dark', title='Среднее количество нефти в резервуарах',
                       labels={
                           'y': 'Среднее количество нефти в резервуарах',
                           'x': 'Datum',
                           'wide_variable_0':'Nafta'
                           'wide_variable_1':'Nafta2'
                           'variable': 'Proizvodnja'
                       })
        st.write(fig1)


        fig2 = px.line(y=[y1,y12], x=x, template='plotly_dark', title='Среднее количество нефти в резервуарах',
                       labels={
                           'y': 'Среднее количество нефти в резервуарах',
                           'x': 'Datum',
                           'variable': 'Proizvodnja'
                       })
        st.write(fig2)
        
     except:
        st.write('Fajl nije u pravom formatu! Pokusajte ponovo')
