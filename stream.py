import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Primer Dashboard-a')
st.write("""Upload file!""")
df = pd.read_csv(r'C:\Test\Bas.csv')
# uploaded_file = st.file_uploader('Excel')
# if uploaded_file is not None:
#     df = pd.read_excel(uploaded_file)
#     try:
#         x = df.x
#         y1 = df.y1
#         y12 = df.y12
#         y2 = df.y2
#         y22 = df.y22

#         fig1 = px.line(y=[y1,y12], x=x, template='plotly_dark', title='Среднее количество нефти в резервуарах',
#                        labels={
#                            'value': 'Среднее количество нефти в резервуарах',
#                            'x': 'Дата',
#                            'wide_variable_0':'Nafta',
#                            'wide_variable_1':'Nafta2',
#                            'variable': 'Proizvodnja'
#                        })

        
#         st.write(fig1)


#         fig2 = px.line(y=[y2,y22], x=x, template='plotly_dark', title='Добыча нефти',
#                        labels={
#                            'value': 'Добыча нефти',
#                            'x': 'Дата',
#                            'variable': 'Proizvodnja'
#                        })
#         st.write(fig2)
        
#     except:
#         st.write('Try again!')
