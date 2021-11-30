import streamlit as st

import pandas as pd

import plotly.express as px

import xlrd as xl

import xlsxwriter

import os



from datetime import datetime, timedelta

#[theme]

# FUNKCIJA U KOJOJ TREBAS DA DEFINISES GRAFIK ZA DATO POLJE
#path = 'C:\Users\darja\OneDrive\Desktop\DI 30 09 2021.xls'
#df = pd.read_excel(r''+path+'', sheet_name='SEVERNI BANAT')
mesec = ""
dan = ""
m = ""
name = "DI 01 01 2021.xlsm"
path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/01 Januar'
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
        name = '/DI ' + d + ' 01 2021.xlsm'
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/01 Januar'+name
    elif mesec == "April":
        name = ('/DI ' + d + ' 04 2021.xlsm')
        path = r'T:/DB/Drilling/01.Departman za tehniku i tehnologiju proizvodnje nafte i gasa/STPNiG/1. Analitika/18. USOI - 2021/04 April' + name
    basov = xl.open_workbook(path)
    sheet = basov.sheet_by_name('SEVERNI BANAT')
    sheet2 = basov.sheet_by_name('SREDNJI BANAT')
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
    # workbook1 = xlsxwriter.Workbook('B.xlsx')
    worksheet1 = workbook.add_worksheet('Mokrin')
    #worksheet11 = workbook1.add_worksheet('Mokrin')
    for i in range(26):
        worksheet1.write(0,i, label[i-1])
    for i in range(1,31):
        worksheet1.write(0, 0, 'Dani')
        worksheet1.write(i, 0, i)
    sum = 0
    sr= 0
    for i in range(10,41):
        for j in range(9,34):
            val = sheet.cell_value(j,i)
            worksheet1.write(i-9,j-8,val)
    #
    # for i in range(52):
    #     worksheet1.write(0,i, label2[i-1])
    # for i in range(1,13):
    #     worksheet1.write(0, 0, 'Mesec')
    #     worksheet1.write(i, 0, mesec_list[i])
    # for i in range(12):
    #     for j in range(56):




    worksheet2 = workbook.add_worksheet('MOKRIN GAZOLIN')
    #worksheet12 = workbook1.add_worksheet('MOKRIN GAZOLIN')
    for i in range(26):
        worksheet2.write(0,i, label[i-1])
    for i in range(1,31):
        worksheet2.write(0, 0, 'Dani')
        worksheet2.write(i, 0, i)

    for i in range(10,41):
        for j in range(34,59):
            val = sheet.cell_value(j,i)
            worksheet2.write(i-9,j-33,val)

    worksheet3 = workbook.add_worksheet('KIKINDA GORNJE')
    #worksheet13 = workbook1.add_worksheet('KIKINDA GORNJE')
    for i in range(26):
        worksheet3.write(0,i, label[i-1])
    for i in range(1,31):
        worksheet3.write(0, 0, 'Dani')
        worksheet3.write(i, 0, i)
    for i in range(10,41):
        for j in range(59,84):
            val = sheet.cell_value(j,i)
            worksheet3.write(i-9,j-58,val)

    worksheet4 = workbook.add_worksheet('KIKINDA POLJE')
    #worksheet14 = workbook1.add_worksheet('KIKINDA POLJE')
    for i in range(26):
        worksheet4.write(0, i, label[i - 1])
    for i in range(1, 31):
        worksheet4.write(0, 0, 'Dani')
        worksheet4.write(i, 0, i)
    for i in range(10, 41):
        for j in range(84, 109):
            val = sheet.cell_value(j, i)
            worksheet4.write(i - 9, j - 83, val)

    worksheet5 = workbook.add_worksheet('VELEBIT')
    #worksheet15 = workbook1.add_worksheet('VELEBIT')
    for i in range(26):
        worksheet5.write(0, i, label[i - 1])
    for i in range(1, 31):
        worksheet5.write(0, 0, 'Dani')
        worksheet5.write(i, 0, i)
    for i in range(10, 41):
        for j in range(184, 209):
            val = sheet.cell_value(j, i)
            worksheet5.write(i - 9, j - 183, val)

    worksheet6 = workbook.add_worksheet('TURIJA')
    #worksheet16 = workbook1.add_worksheet('TURIJA')
    for i in range(26):
        worksheet6.write(0, i, label[i - 1])
    for i in range(1, 31):
        worksheet6.write(0, 0, 'Dani')
        worksheet6.write(i, 0, i)
    for i in range(10, 41):
        for j in range(513, 538):
            val = sheet2.cell_value(j, i)
            worksheet6.write(i - 9, j - 512, val)

    worksheet7 = workbook.add_worksheet('IDJOS')
    #worksheet17 = workbook1.add_worksheet('IDJOS')
    for i in range(26):
        worksheet7.write(0, i, label[i - 1])
    for i in range(1, 31):
        worksheet7.write(0, 0, 'Dani')
        worksheet7.write(i, 0, i)
    for i in range(10, 41):
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

    st.title('Velebit grafici')

    fig1 = px.line(df, y=[y1, y2], x=x, template='ggplot2',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                       line_shape='spline', width= 1300, height=500, markers=True,
                       labels={
                           'y': 'Среднее количество нефти в резервуарах',
                           'x': 'Datum',
                           'variable': '',
                        'value': 'Proizvodnja'})
   # fig1.add_trace()
    st.write(fig1)

    fig2 = px.line(df, y=[y3,y4,y5,y6], x=x, template='ggplot2',
                   title='2. Запасы жидкости, воды, эмульсии в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': 'Proizvodnja'})
    st.write(fig2)

    fig3 = px.line(df, y=[y7,y8], x=x, template='ggplot2',
                   title='Добыча нефти и сдача нефти (сумма за месяц)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': 'Proizvodnja'})
    st.write(fig3)

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

    fig1 = px.line(df, y=[y1, y2], x=x, template='ggplot2', color = 'variable',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                       },
                   category_orders={'z_fluidm3':'Zalihe fluida na dan (m3)'})

    st.write(fig1)

    fig2 = px.line(df, y=[y3, y4, y5, y6], x=x, template='ggplot2', color = 'variable',
                   title='2. Запасы жидкости, воды, эмульсии в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value':''
                       },
                   category_orders={'z_fluidm3':'Zalihe fluida na dan (m3)'})
    st.write(fig2)

    fig3 = px.line(df, y=[y7, y8], x=x, template='ggplot2',
                   title='Добыча нефти и сдача нефти (сумма за месяц)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                       })
    st.write(fig3)


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

    fig1 = px.line(df, y=[y1, y2], x=x, template='ggplot2', color='variable',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   },
                   category_orders={'z_fluidm3': 'Zalihe fluida na dan (m3)'})

    st.write(fig1)

    fig2 = px.line(df, y=[y3, y4, y5, y6], x=x, template='ggplot2', color='variable',
                   title='2. Запасы жидкости, воды, эмульсии в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   },
                   category_orders={'z_fluidm3': 'Zalihe fluida na dan (m3)'})
    st.write(fig2)

    fig3 = px.line(df, y=[y7, y8], x=x, template='ggplot2',
                   title='Добыча нефти и сдача нефти (сумма за месяц)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   })
    st.write(fig3)

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

    fig1 = px.line(df, y=[y1, y2], x=x, template='ggplot2', color='variable',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   },
                   category_orders={'z_fluidm3': 'Zalihe fluida na dan (m3)'})

    st.write(fig1)

    fig2 = px.line(df, y=[y3, y4, y5, y6], x=x, template='ggplot2', color='variable',
                   title='2. Запасы жидкости, воды, эмульсии в резервуарах (данные на конец месяца)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   },
                   category_orders={'z_fluidm3': 'Zalihe fluida na dan (m3)'})
    st.write(fig2)

    fig3 = px.line(df, y=[y7, y8], x=x, template='ggplot2',
                   title='Добыча нефти и сдача нефти (сумма за месяц)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''
                   })
    st.write(fig3)

def VelebitPoMesecu():
    st.markdown('-----')
    st.title('VELEBIT')
    df = pd.read_excel(r'Novifajl.xlsx', sheet_name='VELEBIT')
    x = df.Dani
    y1 = df.Proizvodnja_Nafte_t

    fig1 = px.line(df, y=y1, x=x, template='ggplot2',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''})
    st.metric(label = "Srednja proizvodnja u mesecu ", value = "623[t]", delta = "12% u osnosu na prosli mesec" )
    st.write(fig1)

def KikindaPoljePoMesecu():
        st.title('KIKINDA POLJE')
        df = pd.read_excel(r'Novifajl.xlsx', sheet_name='KIKINDA POLJE')
        x = df.Dani
        y1 = df.Proizvodnja_Nafte_t

        fig1 = px.line(df, y=y1, x=x, template='ggplot2',
                       title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                       line_shape='spline', width=1300, height=500, markers=True,
                       labels={
                           'y': 'Среднее количество нефти в резервуарах',
                           'x': 'Datum',
                           'variable': '',
                           'value': ''})
        st.metric(label="Srednja proizvodnja u mesecu ", value="623[t]", delta="12% u osnosu na prosli mesec")
        st.write(fig1)

def TurijaPoMesecu():
        st.title('KIKINDA POLJE')
        df = pd.read_excel(r'Novifajl.xlsx', sheet_name='TURIJA')
        x = df.Dani
        y1 = df.Proizvodnja_Nafte_t

        fig1 = px.line(df, y=y1, x=x, template='ggplot2',
                       title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                       line_shape='spline', width=1300, height=500, markers=True,
                       labels={
                           'y': 'Среднее количество нефти в резервуарах',
                           'x': 'Datum',
                           'variable': '',
                           'value': ''})
        st.metric(label="Srednja proizvodnja u mesecu ", value="623[t]", delta="12% u osnosu na prosli mesec")
        st.write(fig1)


def IdjosPoMesecu():
    st.title('Idjos')
    df = pd.read_excel(r'Novifajl.xlsx', sheet_name='IDJOS')
    x = df.Dani
    y1 = df.Proizvodnja_Nafte_t

    fig1 = px.line(df, y=y1, x=x, template='ggplot2',
                   title='1. Жидкость и нефть в резервуарах Велебита (среднее значение за месяц)',
                   line_shape='spline', width=1300, height=500, markers=True,
                   labels={
                       'y': 'Среднее количество нефти в резервуарах',
                       'x': 'Datum',
                       'variable': '',
                       'value': ''})
    st.metric(label="Srednja proizvodnja u mesecu ", value="623[t]", delta="12% u osnosu na prosli mesec")
    st.write(fig1)
    # fig2 = px.line(df, y=[y3, y4, y5, y6], x=x, template='ggplot2', color='variable',
    #                title='2. Запасы жидкости, воды, эмульсии в резервуарах (данные на конец месяца)',
    #                line_shape='spline', width=1300, height=500, markers=True,
    #                labels={
    #                    'y': 'Среднее количество нефти в резервуарах',
    #                    'x': 'Datum',
    #                    'variable': '',
    #                    'value': ''
    #                },
    #                category_orders={'z_fluidm3': 'Zalihe fluida na dan (m3)'})
    # st.write(fig2)
    #
    # fig3 = px.line(df, y=[y7, y8], x=x, template='ggplot2',
    #                title='Добыча нефти и сдача нефти (сумма за месяц)',
    #                line_shape='spline', width=1300, height=500, markers=True,
    #                labels={
    #                    'y': 'Среднее количество нефти в резервуарах',
    #                    'x': 'Datum',
    #                    'variable': '',
    #                    'value': ''
    #                })
    # st.write(fig3)


# end = datetime(mesec, option).strftime('%d %m %Y')
# start = (datetime.today() - timedelta(option)).strftime('d %m %Y')
# print(end,start)
# def load_data(field, start_date, end_date):
#     df = data.DataReader(name=field,
#                          start=start_date,
#                          end=end_date,
#                         data_source='yahoo')
#     return df

# Excel()

# st.sidebar.image("slika.png")
#st.sidebar.text_area('')
st.sidebar.write('Kako biste prikazali grafike za dato polje prvo odaberite polje')

add_selectbox = st.sidebar.radio('',('Mesecni prikaz podataka', 'Dnevni prikaz podataka'))
st.sidebar.write('---------------------------------------')

if add_selectbox=='Mesecni prikaz podataka':
    st.sidebar.success('Izabrali ste mesecni prikaz')


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

if add_selectbox=='Dnevni prikaz podataka':
    st.sidebar.success('Izabrali ste dnevni prikaz')
    add_selectbox = st.sidebar.selectbox(

        "Odaberite naftno polje:",

        ("Velebit", "Turija", "Kikinda Polje", "Idjos"))

    if add_selectbox == "Velebit po danu":
        mesec = st.selectbox('Za koji mesec zelite prikaz podataka? ', ('','Januar', 'Februar', 'April', 'Maj', 'Jun', 'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar'), )
        # mesec = st.text_input("Za koji mesec zelite podatke?")
        dan = st.slider("Za koliko dana zelite podatke", 1, 31, 1)
        if mesec and dan:
            task = Excel()
            task = VelebitPoMesecu()
            # if ValueError == True:
            #     st.error('Podaci za datum nisu uneti')
            # else:
            #     st.error('')


    if add_selectbox == "Turija Po Danu":
        mesec = st.text_input("Za koji mesec zelite podatke?")
        option = st.slider("Za koliko dana zelite podatke", 1, 31, 1)
        TurijaPoMesecu()

    if add_selectbox == "Kikinda Polje Po Danu":
        mesec = st.text_input("Za koji mesec zelite podatke?")
        option = st.slider("Za koliko dana zelite podatke", 1, 31, 1)
        KikindaPoljePoMesecu()

    if add_selectbox == "Idjos Po Danu":
        mesec = st.text_input("Za koji mesec zelite podatke?")
        option = st.slider("Za koliko dana zelite podatke", 1, 31, 1)
        IdjosPoMesecu()

    if add_selectbox == "None":
        st.write("")
