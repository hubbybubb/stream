import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Primer Dashboard-a')
st.write("""Upload file!""")
df = pd.read_excel(r'\\SNS06CFSH01\HomeFolderR\miodrag.sljapic\Desktop\Bas.xlsx')
