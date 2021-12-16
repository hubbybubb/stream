import streamlit as st

import pandas as pd

import plotly.express as px

import xlrd as xl

import xlsxwriter

import os

from PIL import Image

import plotly.figure_factory as ff

dataframe1 = pd.read_excel('1.xlsx', index_col=False)
df = dataframe1.drop_duplicates(subset ="Name")
x = st.selectbox("Meni",df)
st.write(x)
y = []
y.append(x)
rslt_df = dataframe1[dataframe1['Name'].isin(y)]
st.table(rslt_df)
x1 = rslt_df.Datum
st.write()
x2 = st.selectbox("Meni",x1)
y2=[]
y2.append(x2)
rslt_df2 = rslt_df[rslt_df['Datum'].isin(y2)]
st.table(rslt_df2)
st.write(str(rslt_df2.tacni))
st.write(str(rslt_df2.netacni))

table = rslt_df2

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
