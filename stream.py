import streamlit as st
import pandas as pd
import plotly.express as px
import xlrd as xl
import xlsxwriter
import os
from PIL import Image
import plotly.figure_factory as ff

def admin():
#   results=view_all_results()
# OVDE TREBA DA SE ZAMENI DATA FRAME
  total_result = pd.read_excel('1.xlsx', index_col=False)
  name_search = total_result.drop_duplicates(subset ="Name")
  name = st.selectbox("Meni",name_search)
  st.write(name)
  name_list = []
  name_list.append(name)
  name_result = total_result[total_result['Name'].isin(name_list)]
  st.table(name_result)
  date_search = name_result.Datum
  date = st.selectbox("Meni",date_search)
  date_list=[]
  date_list.append(date)
  result_final = name_result[name_result['Datum'].isin(y2)]
  st.table(result_final)

  table = result_final

  osnove = table.iat[0,4]
  zakonska = table.iat[0,5]
  mehanicke = table.iat[0,6]

  r = []
  r.append(int(osnove))
  r.append(int(zakonska))
  r.append(int(mehanicke))

  r2=['Osnove', 'Zakon', 'Meh']
  df = pd.DataFrame(list(zip(r2, r)),
                 columns =['Name', 'val'])

  fig1=px.bar(df, x='Name',y='val',orientation="v",title="<b>Pracenje uspesnosti po testu</b>",template="plotly_white")
  st.plotly_chart(fig1)
  
admin()
