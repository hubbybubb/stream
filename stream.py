import streamlit as st

import pandas as pd

import plotly.express as px

import xlrd as xl

import xlsxwriter

import os

from PIL import Image

import plotly.figure_factory as ff

slika=Image.open('1.png')
st.set_page_config(page_title='CUP Dashboard',page_icon=slika)


#[theme]

# FUNKCIJA U KOJOJ TREBAS DA DEFINISES GRAFIK ZA DATO POLJE
#path = 'C:\Users\darja\OneDrive\Desktop\DI 30 09 2021.xls'
#df = pd.read_excel(r''+path+'', sheet_name='SEVERNI BANAT')
mesec = ""
dan = ""
m = ""
name = "DI 01 01 2021.xls"
path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/01.Januar'
def Excel():
    global mesec
    global dan
    global m
    global name
    global path
    d = str(dan)
    #mesec = Januar, februaru...
    #option = da
    if mesec == "Januar":
        if dan<10:
          name = '/DI 0' + d + ' 01 2021.xlsm'
        elif dan>=10:
          name = '/DI ' + d + ' 01 2021.xlsm'
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/01 Januar'+name
    elif mesec == "Februar":
        if dan<10:
          name = '/DI 0' + d + ' 02 2021.xlsm'
        elif dan>=10:
          name = '/DI ' + d + ' 02 2021.xlsm'
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/02 Februar'+name
    elif mesec == "Mart":
        if dan<10:
          name = '/DI 0' + d + ' 03 2021.xlsm'
        elif dan>=10:
          name = '/DI ' + d + ' 03 2021.xlsm'
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/03 Mart'+name
    elif mesec == "April":
        if dan<10:
          name = '/DI 0' + d + ' 04 2021.xlsm'
        elif dan>=10:
          name = ('/DI ' + d + ' 04 2021.xlsm')  
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/04 April' + name
    elif mesec == "Maj":
        if dan<10:
          name = ('/DI 0' + d + ' 05 2021.xlsm')
        elif dan>=10:
          name = ('/DI ' + d + ' 05 2021.xlsm')
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/05 Maj' + name
    elif mesec == "Jun":
        if dan<10:
          name = ('/DI 0' + d + ' 06 2021.xlsm')
        elif dan>=10:
          name = ('/DI ' + d + ' 06 2021.xlsm')
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/06 Jun' + name
    elif mesec == "Jul":
        if dan<10:
          name = ('/DI 0' + d + ' 07 2021.xlsm')
        elif dan>=10:
          name = ('/DI ' + d + ' 07 2021.xlsm')
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/07 Jul' + name
    elif mesec == "Avgust":
        if dan<10:
          name = ('/DI 0' + d + ' 08 2021.xlsm')
        elif dan>=10:
          name = ('/DI ' + d + ' 08 2021.xlsm')
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/08 Avgust' + name
    elif mesec == "Septembar":
        if dan<10:
          name = ('/DI 0' + d + ' 09 2021.xlsm')
        elif dan>=10:
          name = ('/DI ' + d + ' 09 2021.xlsm')
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/09 Septembar' + name
    elif mesec == "Oktobar":
        if dan<10:
          name = ('/DI 0' + d + ' 10 2021.xlsm')
        elif dan>=10:
          name = ('/DI ' + d + ' 10 2021.xlsm')
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/10 Oktobar' + name
    elif mesec == "Novembar":
        if dan<10:
          name = ('\DI 0' + d + ' 11 2021.xlsm')
        elif dan>=10:
          name = ('\DI ' + d + ' 11 2021.xlsm')
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/11 Novembar' + name
    elif mesec == "Decembar":
        if dan<10:
          name = ('/DI 0' + d + ' 12 2021.xlsm')
        elif dan>=10:
          name = ('/DI ' + d + ' 12 2021.xlsm')
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/12 Decembar' + name
    basov = xl.open_workbook(path)
   
    sheet = basov.sheet_by_name('SEVERNI BANAT')
    n=sheet.ncols
    sheet2 = basov.sheet_by_name('SREDNJI BANAT')
    m=sheet2.ncols
    label = ['Zalihe_Fluid_na_dan_m3'  , 'Zalihe_Vode_na_dan_m3', 'Zalihe_Nafte_na_dan_m3',  'Zalihe_nafte_na_dan_t',   'Zalihe_Nafta_u_pripremi_t'    ,'Zalihe_Nafta_za_otpremu_t',
            'Zalihe_Nafta_u_sistemu_i_cevima_t',   'Zalihe_Voda_za_odlaganje_m3', 'Otprema_Fluid_m3',    'Otprema_Sadržaj_vode_%',  'Otprema_Nafta_m3',    'Otprema_Nafta_t',
             'Odlaganje_slojne_vode_m3', 'Otprema_na_druga_Fluid_m3'   ,'Otprema_na_druga_nafta_t'    ,'Sopstvena_potrošnja_Nafta_m3'    ,
            'Sopstvena_potrošnja_Nafta_t'  ,'Proizvodnja_Fluida_m3','Proizvodnja_Voda_m3',    'Proizvodnja_nafte_m3' ,'Proizvodnja_Nafte_t',
            'Prijem_sa_drugih_objekata_Fluida_m3', 'Prijem_sa_drugih_objekata_Voda_m3',   'Prijem_sa_drugih_objekata_nafte_m3',  'Prijem_sa_drugih_objekata_Nafte_t']

    label2 = ['Srednje_Zalihe_Fluid_na_dan_m3' , 'Srednje_Zalihe_Vode_na_dan_m3', 'Srednje_Zalihe_Nafte_na_dan_m3',  'Srednje_Zalihe_nafte_na_dan_t',   'Srednje_Zalihe_Nafta_u_pripremi_t'    ,'Srednje_Zalihe_Nafta_za_otpremu_t',
            'Srednje_Zalihe_Nafta_u_sistemu_i_cevima_t',   'Srednje_Zalihe_Voda_za_odlaganje_m3', 'Srednje_Otprema_Fluid_m3',    'Srednje_Otprema_Sadržaj_vode_%',  'Srednje_Otprema_Nafta_m3',    'Srednje_Otprema_Nafta_t',
             'Srednje_Odlaganje_slojne_vode_m3', 'Srednje_Otprema_na_druga_Fluid_m3'   ,'Srednje_Otprema_na_druga_nafta_t'    ,'Srednje_Sopstvena_potrošnja_Nafta_m3'    ,
            'Srednje_Sopstvena_potrošnja_Nafta_t'  ,'Srednje_Proizvodnja_Fluida_m3','Srednje_Proizvodnja_Voda_m3',    'Srednje_Proizvodnja_nafte_m3' ,'Srednje_Proizvodnja_Nafte_t',
            'Srednje_Prijem_sa_drugih_objekata_Fluida_m3', 'Srednje_Prijem_sa_drugih_objekata_Voda_m3',   'Srednje_Prijem_sa_drugih_objekata_nafte_m3', 'Srednje_Prijem_sa_drugih_objekata_Nafte_t',
             'Suma_Zaliha_Fluid_na_dan_m3',    'Suma_Zalihe_Vode_na_dan_m3',  'Suma_Zalihe_Nafte_na_dan_m3', 'Suma_Zalihe_nafte_na_dan_t',
             'Suma_Zalihe_u_pripremi_t',   'Suma_Zalihe_Nafta_za_otpremu_t',  'Suma_Zalihe_Nafta_u_sistemu_i_cevima_t',  'Suma_Zalihe_Voda_za_odlaganje_m3',
             'Suma_Otprema_Fluid_m3',  'Suma_Otprema_Sadržaj_vode_%', 'Suma_Otprema_Nafta_m3',   'Suma_Otprema_Nafta_t',
             'Suma_Odlaganje_slojne_vode_m3',  'Suma_Otprema_na_druga_Fluid_m3',  'Suma_Otprema_na_druga_nafta_t',   'Suma_Sopstvena_potrošnja_Nafta_m3',
             'Suma_Sopstvena_potrošnja_Nafta_t',   'Suma_Proizvodnja_Fluida_m3',  'Suma_Proizvodnja_Voda_m3',    'Suma_Proizvodnja_nafte_m3',
             'Suma_Proizvodnja_Nafte_t',   'Suma_Prijem_sa_drugih_objekata_Fluida_m3',    'Suma_Prijem_sa_drugih_objekata_Voda_m3',
             'Suma_Prijem_sa_drugih_objekata_nafte_m3',    'Suma_Prijem_sa_drugih_objekata_Nafte_t'
             ]
    mesec_list = ['Januar','Februar','Mart','April','Maj','Jun','Jul','Avgust','Septembar', 'Oktobar', 'Novembar', 'Decembar']
    workbook = xlsxwriter.Workbook('Novifajl.xlsx')
    #workbook1 = xlsxwriter.Workbook('B.xlsx')
    worksheet1 = workbook.add_worksheet('Mokrin')
    #worksheet11 = workbook1.add_worksheet('Mokrin')
    for i in range(26):
        worksheet1.write(0,i, label[i-1])
    for i in range(1,32):
        worksheet1.write(0, 0, 'Dani')
        worksheet1.write(i, 0, i)
    sum = 0
    sr= 0
    for i in range(10,n):
        for j in range(9,n):
            val = sheet.cell_value(j,i)
            worksheet1.write(i-9,j-8,val)
 


    worksheet2 = workbook.add_worksheet('MOKRIN GAZOLIN')
    #worksheet12 = workbook1.add_worksheet('MOKRIN GAZOLIN')
    for i in range(26):
        worksheet2.write(0,i, label[i-1])
    for i in range(1,32):
        worksheet2.write(0, 0, 'Dani')
        worksheet2.write(i, 0, i)

    for i in range(10,n):
        for j in range(34,59):
            val = sheet.cell_value(j,i)
            worksheet2.write(i-9,j-33,val)

    worksheet3 = workbook.add_worksheet('KIKINDA GORNJE')
    #worksheet13 = workbook1.add_worksheet('KIKINDA GORNJE')
    for i in range(26):
        worksheet3.write(0,i, label[i-1])
    for i in range(1,32):
        worksheet3.write(0, 0, 'Dani')
        worksheet3.write(i, 0, i)
    for i in range(10,n):
        for j in range(59,84):
            val = sheet.cell_value(j,i)
            worksheet3.write(i-9,j-58,val)

    worksheet4 = workbook.add_worksheet('KIKINDA POLJE')
    #worksheet14 = workbook1.add_worksheet('KIKINDA POLJE')
    for i in range(26):
        worksheet4.write(0, i, label[i - 1])
    for i in range(1, 32):
        worksheet4.write(0, 0, 'Dani')
        worksheet4.write(i, 0, i)
    for i in range(10, n):
        for j in range(84, 109):
            val = sheet.cell_value(j, i)
            worksheet4.write(i - 9, j - 83, val)

    worksheet5 = workbook.add_worksheet('VELEBIT')
    #worksheet15 = workbook1.add_worksheet('VELEBIT')
    for i in range(26):
        worksheet5.write(0, i, label[i - 1])
    for i in range(1, 32):
        worksheet5.write(0, 0, 'Dani')
        worksheet5.write(i, 0, i)
    for i in range(10, n):
        for j in range(184, 209):
            val = sheet.cell_value(j, i)
            worksheet5.write(i - 9, j - 183, val)

    worksheet6 = workbook.add_worksheet('TURIJA')
    #worksheet16 = workbook1.add_worksheet('TURIJA')
    for i in range(26):
        worksheet6.write(0, i, label[i - 1])
    for i in range(1, 32):
        worksheet6.write(0, 0, 'Dani')
        worksheet6.write(i, 0, i)
    for i in range(10, m):
        for j in range(513, 538):
            val = sheet2.cell_value(j, i)
            worksheet6.write(i - 9, j - 512, val)

    worksheet7 = workbook.add_worksheet('IDJOS')
    #worksheet17 = workbook1.add_worksheet('IDJOS')
    for i in range(26):
        worksheet7.write(0, i, label[i - 1])
    for i in range(1, 32):
        worksheet7.write(0, 0, 'Dani')
        worksheet7.write(i, 0, i)
    for i in range(10, n):
        for j in range(259, 284):
            val = sheet.cell_value(j, i)
            worksheet7.write(i - 9, j - 258, val)

    workbook.close()
#po mesecima

def Velebit():
    df = pd.read_excel('B.xlsx', sheet_name='velebit')
    x = df.Mesec
    y1 = df.Zalihe_Fluid_na_dan_m3
    y2 = df.Zalihe_nafte_na_dan_t
    y3 = df.Suma_Zaliha_Fluid_na_dan_m3
    y4 = df.Suma_Zalihe_Vode_na_dan_m3
    y5 = df.Suma_Zalihe_Nafte_na_dan_m3
    y6 = df.Suma_Zalihe_Voda_za_odlaganje_m3
    y7 = df.Suma_Otprema_Nafta_t
    y8 = df.Suma_Proizvodnja_Nafte_t
    y9 = df.Suma_Zalihe_nafte_na_dan_t
    y10 = df.Zalihe_воды_в_оставшейся_эмульсии_после_сброса
    y11 = df.Suma_Proizvodnja_nafte_m3
    y12 = df.Suma_Proizvodnja_Voda_m3
    y13 = df.Suma_Proizvodnja_Fluida_m3
    y14 = df.ШТР_Замерная_из_ШТР_m3
    y15 = df.ШТР_Замерная_из_ШТР_тн
    y16 = df.TERA_Добыча_нефти_и_газоконденсата_тн_МЭР
    y17 = df.TERA_BP_План_Добыча_нефти_и_газоконденсата_тыс
    st.title('Velebit grafici')

    

    fig1 = px.line(df, y=[y1, y2], x=x, template='plotly_white',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                       line_shape='spline', width= 1500, height=500, markers=True,
                       labels={
                           'y': 'Среднее количество нефти в резервуарах',
                           'x': 'Datum',
                           'variable': '',
                        'value': 'Proizvodnja'})
   
    st.plotly_chart(fig1)
    st.markdown("-------------------------")
    # # st.write(fig1)
    

    fig2 = px.line(df, y=[y3,y4,y5,y6], x=x, template='ggplot2',
                   title='2. Запасы жидкости, воды, эмульсии в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': 'Proizvodnja'})
    st.plotly_chart(fig2)
    st.markdown("-------------------------")
    
    fig4 = px.line(df, y=[y5,y9,y10], x=x, template='ggplot2',
                   title='3.Запасы эмульсии и нефти в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': 'Proizvodnja'})
    st.plotly_chart(fig4)
    st.markdown("-------------------------")

    fig3 = px.line(df, y=[y7,y8,y4], x=x, template='ggplot2',
                   title='4. Добыча нефти и сдача нефти (сумма за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': 'Proizvodnja'})
    st.plotly_chart(fig3)
    st.markdown("-------------------------")
    fig5 = px.line(df, y=[y8,y12,y13], x=x, template='ggplot2',
                   title='5. Добыча жидкости, нефти (сумма за месяц',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': 'Proizvodnja'})
    st.plotly_chart(fig5)
    st.markdown("-------------------------")
    fig6 = px.line(df, y=[y8,y12,y13,y14,y15,y16,y17], x=x, template='ggplot2',
                   title='(сумма за месяц) Добыча жидкости, нефти по резервуарам, Добыча жидкости, нефти по замерной, Добыча жидкости, нефти по МЭРам',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': 'Proizvodnja'})
    st.plotly_chart(fig6)

#     KOD ZA GRAFIK VELEBIT


def KikindaPolje():
    st.title('Kikinda Polje grafici')
    df = pd.read_excel(r'B.xlsx', sheet_name='kikinda polje')
    x = df.Mesec
    y1 = df.Zalihe_Fluid_na_dan_m3
    y2 = df.Zalihe_nafte_na_dan_t
    y3 = df.Suma_Zaliha_Fluid_na_dan_m3
    y4 = df.Suma_Zalihe_Vode_na_dan_m3
    y5 = df.Suma_Zalihe_Nafte_na_dan_m3
    y6 = df.Suma_Zalihe_Voda_za_odlaganje_m3
    y7 = df.Suma_Otprema_Nafta_t
    y8 = df.Suma_Proizvodnja_Nafte_t
    y9 = df.Suma_Zalihe_nafte_na_dan_t
    y10 = df.Zalihe_воды_в_оставшейся_эмульсии_после_сброса
    y11 = df.Suma_Proizvodnja_nafte_m3
    y12 = df.Suma_Proizvodnja_Voda_m3
    # y13 = df.Suma_Proizvodnja_Fluida_m3
    # y14 = df.ШТР_Замерная_из_ШТР_m3
    # y15 = df.ШТР_Замерная_из_ШТР_тн
    # y16 = df.TERA_Добыча_нефти_и_газоконденсата_тн_МЭР
    # y17 = df.TERA_BP_План_Добыча_нефти_и_газоконденсата_тыс

    fig1 = px.line(df, y=[y1, y2], x=x, template='ggplot2', color = 'variable',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                       },
                   category_orders={'z_fluidm3':'Zalihe fluida na dan (m3)'})

    st.plotly_chart(fig1)
    st.markdown("-------------------------")        
    fig2 = px.line(df, y=[y3, y4, y5, y6], x=x, template='ggplot2', color = 'variable',
                   title='2. Запасы жидкости, воды, эмульсии в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value':''
                       },
                   category_orders={'z_fluidm3':'Zalihe fluida na dan (m3)'})
    st.plotly_chart(fig2)
    st.markdown("-------------------------")
    fig4 = px.line(df, y=[y9,y5,y10], x=x, template='ggplot2',
                   title='Добыча нефти и сдача нефти (сумма за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                       })
    st.plotly_chart(fig4)
    st.markdown("-------------------------")

    fig3 = px.line(df, y=[y7, y8], x=x, template='ggplot2',
                   title='Добыча нефти и сдача нефти (сумма за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                       })
    st.plotly_chart(fig3)
    st.markdown("-------------------------")
    fig5 = px.line(df, y=[y11, y12, y8], x=x, template='ggplot2',
                   title='5. Добыча жидкости, нефти (сумма за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                       })
    st.plotly_chart(fig5)
    st.markdown("-------------------------")

def Turija():
    st.title('Turija grafici')
    df = pd.read_excel(r'B.xlsx', sheet_name='turija')
    x = df.Mesec
    y1 = df.Zalihe_Fluid_na_dan_m3
    y2 = df.Zalihe_nafte_na_dan_t
    y3 = df.Suma_Zaliha_Fluid_na_dan_m3
    y4 = df.Suma_Zalihe_Vode_na_dan_m3
    y5 = df.Suma_Zalihe_Nafte_na_dan_m3
    y6 = df.Suma_Zalihe_Voda_za_odlaganje_m3
    y7 = df.Suma_Otprema_Nafta_t
    y8 = df.Suma_Proizvodnja_Nafte_t
    # y9 = df.Suma_Zalihe_nafte_na_dan_t
    # y10 = df.Zalihe_воды_в_оставшейся_эмульсии_после_сброса
    y11 = df.Suma_Proizvodnja_nafte_m3
    y12 = df.Suma_Proizvodnja_Voda_m3
    # y13 = df.Suma_Proizvodnja_Fluida_m3
    # y14 = df.ШТР_Замерная_из_ШТР_m3
    # y15 = df.ШТР_Замерная_из_ШТР_тн
    # y16 = df.TERA_Добыча_нефти_и_газоконденсата_тн_МЭР
    # y17 = df.TERA_BP_План_Добыча_нефти_и_газоконденсата_тыс.т

    fig1 = px.line(df, y=[y1, y2], x=x, template='ggplot2', color='variable',
                   title='1. Жидкость и нефть в резервуарах (среднее значение за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   },
                   category_orders={'z_fluidm3': 'Zalihe fluida na dan (m3)'})

    st.plotly_chart(fig1)
    st.markdown("-------------------------")
    fig2 = px.line(df, y=[y3, y4, y5, y6], x=x, template='ggplot2', color='variable',
                   title='2. Запасы жидкости, воды, эмульсии в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   },
                   category_orders={'z_fluidm3': 'Zalihe fluida na dan (m3)'})
    st.plotly_chart(fig2)
    st.markdown("-------------------------")
    fig3 = px.line(df, y=[y7, y8], x=x, template='ggplot2',
                   title='3. Запасы эмульсии и нефти в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   })
    st.plotly_chart(fig3)
    st.markdown("-------------------------")
    fig5 = px.line(df, y=[y11, y12, y8], x=x, template='ggplot2',
                   title='5. Добыча жидкости, нефти (сумма за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                       })
    st.plotly_chart(fig5)
    
    
def Idjos():
    st.title('Idjos grafici')
    df = pd.read_excel(r'B.xlsx', sheet_name='idjos')
    x = df.Mesec
    y1 = df.Zalihe_Fluid_na_dan_m3
    y2 = df.Zalihe_nafte_na_dan_t
    y3 = df.Suma_Zaliha_Fluid_na_dan_m3
    y4 = df.Suma_Zalihe_Vode_na_dan_m3
    y5 = df.Suma_Zalihe_Nafte_na_dan_m3
    y6 = df.Suma_Zalihe_Voda_za_odlaganje_m3
    y7 = df.Suma_Otprema_Nafta_t
    y8 = df.Suma_Proizvodnja_Nafte_t
    # y9 = df.Suma_Zalihe_nafte_na_dan_t
    # y10 = df.Zalihe_воды_в_оставшейся_эмульсии_после_сброса
    # y11 = df.Suma_Proizvodnja_nafte_m3
    # y12 = df.Suma_Proizvodnja_Voda_m3
    # y13 = df.Suma_Proizvodnja_Fluida_m3
    # y14 = df.ШТР_Замерная_из_ШТР_m3
    # y15 = df.ШТР_Замерная_из_ШТР_тн
    # y16 = df.TERA_Добыча_нефти_и_газоконденсата_тн_МЭР
    # y17 = df.TERA_BP_План_Добыча_нефти_и_газоконденсата_тыс.тt

    fig1 = px.line(df, y=[y1, y2], x=x, template='ggplot2', color='variable',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   },
                   category_orders={'z_fluidm3': 'Zalihe fluida na dan (m3)'})

    st.plotly_chart(fig1)
    st.markdown("-------------------------")
    fig2 = px.line(df, y=[y3, y4, y5, y6], x=x, template='ggplot2', color='variable',
                   title='2. Запасы жидкости, воды, эмульсии в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   },
                   category_orders={'z_fluidm3': 'Zalihe fluida na dan (m3)'})
    st.plotly_chart(fig2)
    st.markdown("-------------------------")
    fig3 = px.line(df, y=[y7, y8], x=x, template='ggplot2',
                   title='Добыча нефти и сдача нефти (сумма за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   })
    st.plotly_chart(fig3)
    st.markdown("-------------------------")
def VelebitPoMesecu():
    st.markdown('-----')
    st.title('VELEBIT')
    df = pd.read_excel(r'Novifajl.xlsx', sheet_name='VELEBIT')
    x = df.Dani
    y1 = df.Proizvodnja_Nafte_t

    fig1 = px.line(df, y=y1, x=x, template='ggplot2',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''})

    # st.metric(label = "Srednja proizvodnja u mesecu ", value = , delta = "12% u osnosu na prosli mesec" )

    st.plotly_chart(fig1)
    st.markdown("-------------------------")
def KikindaPoljePoMesecu():
        st.title('KIKINDA POLJE')
        df = pd.read_excel(r'Novifajl.xlsx', sheet_name='KIKINDA POLJE')
        x = df.Dani
        y1 = df.Proizvodnja_Nafte_t

        fig1 = px.line(df, y=y1, x=x, template='ggplot2',
                       title='1. Жидкость и нефть в резервуарах (среднее значение за месяц)',
                       line_shape='spline', width=1500, height=500, markers=True,
                       labels={
                           'y': 'Среднее количество нефти в резервуарах',
                           'x': 'Datum',
                           'variable': '',
                           'value': ''})
        st.metric(label="Srednja proizvodnja u mesecu ", value="623[t]", delta="12% u osnosu na prosli mesec")
        st.plotly_chart(fig1)
        st.markdown("-------------------------")
def TurijaPoMesecu():
        st.title('KIKINDA POLJE')
        df = pd.read_excel(r'Novifajl.xlsx', sheet_name='TURIJA')
        x = df.Dani
        y1 = df.Proizvodnja_Nafte_t

        fig1 = px.line(df, y=y1, x=x, template='ggplot2',
                       title='1. Жидкость и нефть в резервуарах (среднее значение за месяц)',
                       line_shape='spline', width=1500, height=500, markers=True,
                       labels={
                           'y': 'Среднее количество нефти в резервуарах',
                           'x': 'Datum',
                           'variable': '',
                           'value': ''})
        st.metric(label="Srednja proizvodnja u mesecu ", value="623[t]", delta="12% u osnosu na prosli mesec")
        st.plotly_chart(fig1)
        st.markdown("-------------------------")

def IdjosPoMesecu():
    st.title('Idjos')
    df = pd.read_excel(r'Novifajl.xlsx', sheet_name='IDJOS')
    x = df.Dani
    y1 = df.Proizvodnja_Nafte_t

    fig1 = px.line(df, y=y1, x=x, template='ggplot2',
                   title='1. Жидкость и нефть в резервуарах (среднее значение за месяц)',
                   line_shape='spline', width=1500, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''})
    st.metric(label="Srednja proizvodnja u mesecu ", value="623[t]", delta="12% u osnosu na prosli mesec")
    st.plotly_chart(fig1)
  


st.sidebar.image("slika.png")
st.sidebar.markdown('------------------')
#st.sidebar.text_area('')
# st.header('DOBRODOSLI U MONITORING PROIZVODNJE NAFTE I GASA')
n=st.sidebar.radio('Odaberite zeljeni prikaz',("Mesecni prikaz","Dnevni prikaz" ))


if n=="Mesecni prikaz":


    add_selectbox = st.sidebar.selectbox(

        "Odaberite naftno polje: ",

        ("Velebit", "Turija", "Kikinda Polje", "Idjos"))

    if add_selectbox == "Velebit":
        Velebit()

    if add_selectbox == "Turija":
        Turija()

    if add_selectbox == "Kikinda Polje":
        KikindaPolje()

    if add_selectbox == "Idjos":
        Idjos()

    if add_selectbox == "None":
        st.write("hello")

if n=="Dnevni prikaz":
    add_selectbox = st.sidebar.selectbox(

        "Svaki mesec posebno: ",

        ("Velebit", "Turija", "Kikinda Polje", "Idjos"))
    st.sidebar.markdown('------------------')

    if add_selectbox == "Velebit":
        mesec = st.sidebar.selectbox('Za koji mesec zelite prikaz podataka? ', ('Januar', 'Februar', 'April', 'Maj', 'Jun', 'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar'), )
        st.sidebar.markdown('------------------')
        # mesec = st.text_input("Za koji mesec zelite podatke?")
        dan = st.slider("Za koliko dana zelite podatke", 1, 31, 1)
        if mesec and dan:
            task = Excel()
            task = VelebitPoMesecu()
            # if ValueError == True:
            #     st.error('Podaci za datum nisu uneti')
            # else:
            #     st.error('')


    if add_selectbox == "Turija":
        mesec = st.sidebar.selectbox('Za koji mesec zelite prikaz podataka? ', ('Januar', 'Februar', 'April', 'Maj', 'Jun', 'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar'), )
        option = st.slider("Za koliko dana zelite podatke", 1, 31, 1)
        TurijaPoMesecu()

    if add_selectbox == "Kikinda Polje":
        mesec = st.sidebar.selectbox('Za koji mesec zelite prikaz podataka? ', ('Januar', 'Februar', 'April', 'Maj', 'Jun', 'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar'), )
        option = st.slider("Za koliko dana zelite podatke", 1, 31, 1)
        KikindaPoljePoMesecu()

    if add_selectbox == "Idjos":
        mesec = st.sidebar.selectbox('Za koji mesec zelite prikaz podataka? ', ('Januar', 'Februar', 'April', 'Maj', 'Jun', 'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar'), )
        option = st.slider("Za koliko dana zelite podatke", 1, 31, 1)
        IdjosPoMesecu()

  

