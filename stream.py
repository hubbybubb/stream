import streamlit as st

import pandas as pd

import plotly.express as px

import xlrd as xl

import xlsxwriter

import os

from PIL import Image

import plotly.figure_factory as ff

dataframe1 = pd.read_excel('1.xlsx')
st.selectbox("Meni",dataframe1.Name)
