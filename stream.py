import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Primer Dashboard-a')
st.write("""Upload file!""")
df = pd.read_excel(r'T:\DB\Drilling\01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa\STPNiG\1. Analitika\Streamlit\Bas.xlsx')
