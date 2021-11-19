import streamlit as st
import pandas as pd
import plotly.express as px

st.title('SERVER TEST')
st.write("""Upload file!""")
uploaded_file = st.file_uploader('Excel')
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

x = df.Datum
y = df.ITRA

fig1 = px.line(y=y, x=x, template='plotly_dark', title='Grafik za Basova',
               labels={
                   'value': 'ITRA Bodovi',
                   'x': 'Datum',
                   'variable': 'Proizvodnja'
               })
st.write(fig1)
