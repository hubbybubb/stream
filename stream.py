import streamlit as st

import pandas as pd

import plotly.express as px

import xlrd as xl

import xlsxwriter

import os

from PIL import Image

import plotly.figure_factory as ff

dataframe1 = pd.read_excel('1.xlsx')
df = dataframe1.drop_duplicates(subset ="Name",
                     keep = False)
x = st.selectbox("Meni",df)
st.write(x)
rslt_df = dataframe1[dataframe['Name'].isin(x)]
