import streamlit as st
import pandas as pd
import plotly.express as px

# def clicky():
# #     if genre == 'Уклањање асфалтно-смоластих и парафинских наслага':
# #         st.write('Tačan odgovor!')
# #         st.balloons()
        
# #     else:
# #         st.write('Netacan odgovor!')
#       st.title('Test kompetencija')
#       st.write('Radi kod sad')


st.title('Test kompetencija')

add_selectbox = st.sidebar.selectbox(
    "Ime i prezime učesnika: ",
    ("Nikola Nikolic", "Petar Petrovic", "Mika Mikic")
)

st.sidebar.button('Potvrdi')

genre = st.radio(
'Топлотне методе се примењују за ',
('Уклањање калцита', 'Уклањање хидрата', 'Уклањање асфалтно-смоластих и парафинских наслага', 'Уклањање каменца '))

# option = st.selectbox('Odaberite naftno polje: ',
#     ('Velebit', 'Turija', 'Iđoš'))

# st.write('Odabrali ste naftno polje ', option)

# # st.write("""Upload file!""")
# # uploaded_file = st.file_uploader('Excel')
# # if uploaded_file is not None:
# #     df = pd.read_excel(uploaded_file)
# #     try:
# #         x = df.x
# #         y1 = df.y1
# #         y12 = df.y12
# #         y2 = df.y2
# #         y22 = df.y22

# #         fig1 = px.line(y=[y1,y12], x=x, template='plotly_dark', title='Среднее количество нефти в резервуарах', line_shape='spline',
# #                        labels={
# #                            'value': 'Среднее количество нефти в резервуарах',
# #                            'x': 'Дата',
# #                            'wide_variable_0':'Nafta',
# #                            'wide_variable_1':'Nafta2',
# #                            'variable': 'Proizvodnja'
# #                        })

        
# #         st.write(fig1)


# #         fig2 = px.line(y=[y2,y22], x=x, template='plotly_dark', title='Добыча нефти',line_shape='spline',
# #                        labels={
# #                            'value': 'Добыча нефти',
# #                            'x': 'Дата',
# #                            'variable': 'Proizvodnja'
# #                        })
# #         st.write(fig2)
        
# #     except:
# #         st.write('Try again!')
