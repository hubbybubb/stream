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

table = rslt_df2.T.tail(3)
st.write(table)
l = ["Osnove","Zakonska","Mehanicke"]
fig1=px.bar(table, x=l, y=[1,2,3], orientation="v",title="<b>Pracenje uspesnosti po testu</b>",color_discrete_sequence=["#0083B8"]*len(m),template="plotly_white",)
