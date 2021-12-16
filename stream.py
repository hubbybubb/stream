import streamlit as st

import pandas as pd

import plotly.express as px

import xlrd as xl

import xlsxwriter

import os

from PIL import Image

import plotly.figure_factory as ff

dataframe1 = pd.read_excel('1.xlsx')
df = dataframe1.drop_duplicates(subset ="First Name",
                     keep = False, inplace = True)
st.selectbox("Meni",df)
