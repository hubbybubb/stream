import streamlit as st
import pandas as pd
from PIL import Image
import json
import random
import datetime
import base64
import math
from plotly.subplots import make_subplots
# import win32com.client as client
import plotly.graph_objects as go  
import sqlite3

# Ikonica i naziv aplikacije--------------------------------------------
slika=Image.open('download.png')
st.set_page_config(page_title='Naftna fiskultura',page_icon=slika,layout='wide')

# Baza podataka--------------------------------------------------------------------

conn = sqlite3.connect('data.db')
c = conn.cursor()

# c.execute('CREATE TABLE IF NOT EXISTS admintable(username TEXT PRIMARY KEY,password TEXT)')
# conn.commit()

# c.execute('INSERT INTO  admintable(username,password) VALUES ("BojanM","1234")')
# conn.commit()

# c.execute('CREATE TABLE IF NOT EXISTS rezultati(name TEXT ,datum TEXT,tacni INTEGER,netacni INTEGER,Osnove INTEGER,Osnovenetacni INTEGER , Zakonska INTEGER,Zakonskanetacni INTEGER,Mehanicke INTEGER,Mehanickenetacni INTEGER,Eruptivna INTEGER,Eruptivnanetacni INTEGER,Struktura INTEGER,Strukturanetacni INTEGER,Hemizacija INTEGER, Hemizacijanetacni INTEGER,Priprema INTEGER,Pripremanetacni INTEGER, PRIMARY KEY (name,datum))')
# conn.commit()
def admin_user(u,n):
  c.execute('SELECT * FROM admintable WHERE username =? AND password = ?',(u,n))
  data = c.fetchall()
  return data

def create_usertable():
  c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT PRIMARY KEY,password TEXT,ime TEXT,prezime TEXT,email TEXT,broj_telefona TEXT, sap_broj TEXT,naziv_pozicije TEXT)')
       
def create_r():
  c.execute('CREATE TABLE IF NOT EXISTS rezultati(name TEXT ,datum TEXT,tacni INTEGER,netacni INTEGER,Osnove INTEGER,Osnovenetacni INTEGER , Zakonska INTEGER,Zakonskanetacni INTEGER,Mehanicke INTEGER,Mehanickenetacni INTEGER,Eruptivna INTEGER,Eruptivnanetacni INTEGER,Struktura INTEGER,Strukturanetacni INTEGER,Hemizacija INTEGER, Hemizacijanetacni INTEGER,Priprema INTEGER,Pripremanetacni INTEGER, PRIMARY KEY (name,datum))')

def add_userr(name,datum,tacni,netacni,Osnove,Osnovenetacni,Zakonska,Zakonskanetacni,Mehanicke,Mehanickenetacni,Eruptivna,Eruptivnanetacni,Struktura,Strukturanetacni,Hemizacija,Hemizacijanetacni, Priprema,Pripremanetacni):
  c.execute('INSERT INTO rezultati(name,datum,tacni,netacni,Osnove,Osnovenetacni,Zakonska,Zakonskanetacni,Mehanicke,Mehanickenetacni,Eruptivna,Eruptivnanetacni,Struktura,Strukturanetacni,Hemizacija,Hemizacijanetacni, Priprema,Pripremanetacni) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(name,datum,tacni,netacni,Osnove,Osnovenetacni,Zakonska,Zakonskanetacni,Mehanicke,Mehanickenetacni,Eruptivna,Eruptivnanetacni,Struktura,Strukturanetacni,Hemizacija,Hemizacijanetacni, Priprema,Pripremanetacni))
  conn.commit()

def add_userdata(username,password,ime,prezime,email,broj_telefona,sap_broj,naziv_pozicije):
  c.execute('INSERT INTO userstable(username,password,ime,prezime,email,broj_telefona,sap_broj,naziv_pozicije) VALUES (?,?,?,?,?,?,?,?)',(username,password,ime,prezime,email,broj_telefona,sap_broj,naziv_pozicije))
  conn.commit()

def login_user(username,password):
  c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
  data = c.fetchall()
  return data

def view_all_results():
  c.execute('SELECT * FROM rezultati')
  data = c.fetchall()
  return data

def view_last_results():
  c.execute('SELECT * FROM rezultati ORDER BY name DESC LIMIT 1')
  data = c.fetchall()
  return data

def view_all_users():
  c.execute('SELECT * FROM userstable')
  data = c.fetchall()
  return data

name1=""
     
# # stranica sa Testom, funkcija za Test-----------------------------------------------------------------

def total_broj_testa():
  results=view_all_results()
  clean_db=pd.DataFrame(results, columns=['Name','Datum','tacni','netacni','Osnove','Osnovenetacni','Zakonska',"Zakonskanetacni",'Mehanicke',"Mehanickenetacni",'Eruptivna',"Eruptivnanetacni",'Struktura',"Strukturanetacni",'Hemizacija',"Hemizacijanetacni",'Priprema',"Pripremanetacni"])
  clean_db1=clean_db[clean_db['Name']==name1]
  total=clean_db1.shape[0]

def rezultati1():
  results=view_all_results()
  clean_db=pd.DataFrame(results, columns=['Name','Datum','tacni','netacni','Osnove','Osnovenetacni','Zakonska',"Zakonskanetacni",'Mehanicke',"Mehanickenetacni",'Eruptivna',"Eruptivnanetacni",'Struktura',"Strukturanetacni",'Hemizacija',"Hemizacijanetacni",'Priprema',"Pripremanetacni"])
  clean_db1=clean_db[clean_db['Name']==name1]
  st.dataframe(clean_db1)
  
  st.bar_chart(clean_db1['netacni'])

def rezultati_admin():
  results=view_all_results()
  clean_db=pd.DataFrame(results, columns=['Name','Datum','tacni','netacni','Osnove','Osnovenetacni','Zakonska',"Zakonskanetacni",'Mehanicke',"Mehanickenetacni",'Eruptivna',"Eruptivnanetacni",'Struktura',"Strukturanetacni",'Hemizacija',"Hemizacijanetacni",'Priprema',"Pripremanetacni"])
  st.dataframe(clean_db)

# def slanje_maila():
#   outlook = client.Dispatch('Outlook.Application')
#   message = outlook.CreateItem(0) # 0 is the code for a mail item (see the enumerations)
#   message.Display()
#   message.To = 'bojan.martinovic@nis.rs'

#   message.Subject = 'Naftna fiskultura'
#   message.Body = 'Postovani, \n\nZavrsio sam test!'
#   message.Save() # save to drafts folder
#   message.Send() # send to outbox
    
# # stranica sa Testom, funkcija za Test-----------------------------------------------------------------

class Question:
    
    def __init__(self, section,question, options, answer):
        
        self.section = section
        self.question = question
        
        self.options = options
        
        self.answer = answer
       
    def get_section(self):
            return self.section

    def get_question(self):
            return self.question
    def get_options(self):
            return self.options
    def get_answer(self):
            return self.answer
   

with open("Osnove.json", "r") as jf:
            json_file = json.load(jf)
            df1 = pd.json_normalize(json_file, meta=[
        'Sekcija',
        'Pitanja',
        ['Ponudeni'],
        ['Tacan']])

with open("Zakonska.json", "r") as jf:
            json_file = json.load(jf)
            df2 = pd.json_normalize(json_file, meta=[
        'Sekcija',
        'Pitanja',
        ['Ponudeni'],
        ['Tacan']])

with open("Mehanicke.json", "r") as jf:
            json_file = json.load(jf)
            df3 = pd.json_normalize(json_file, meta=[
        'Sekcija',
        'Pitanja',
        ['Ponudeni'],
        ['Tacan']])

with open("Eruptivna.json", "r") as jf:
            json_file = json.load(jf)
            df4 = pd.json_normalize(json_file, meta=[
        'Sekcija',
        'Pitanja',
        ['Ponudeni'],
        ['Tacan']])

with open("Struktura.json", "r") as jf:
            json_file = json.load(jf)
            df5 = pd.json_normalize(json_file, meta=[
        'Sekcija',
        'Pitanja',
        ['Ponudeni'],
        ['Tacan']])

with open("Hemizacija.json", "r") as jf:
            json_file = json.load(jf)
            df6 = pd.json_normalize(json_file, meta=[
        'Sekcija',
        'Pitanja',
        ['Ponudeni'],
        ['Tacan']])

with open("Tehnologija.json", "r") as jf:
            json_file = json.load(jf)
            df7 = pd.json_normalize(json_file, meta=[
        'Sekcija',
        'Pitanja',
        ['Ponudeni'],
        ['Tacan']])

@st.cache
def get_osnove():
  
  L1=[]   
  for i in df1.index:
    section=df1.Sekcija[i]
    question=df1.Pitanje[i]
    options=df1.Ponudeni[i]
    answer=df1.Tacan[i]
    L1.append(Question(section,question,options,answer))

  L2=random.sample(L1,20)
  return L2

@st.cache
def get_Zakonska():
  
  L1=[]   
  for i in df2.index:
    section=df2.Sekcija[i]
    question=df2.Pitanje[i]
    options=df2.Ponudeni[i]
    answer=df2.Tacan[i]
    L1.append(Question(section,question,options,answer))

  L2=random.sample(L1,10)
  return L2

@st.cache
def get_mehanicke():
  
  L1=[]   
  for i in df3.index:
    section=df3.Sekcija[i]
    question=df3.Pitanje[i]
    options=df3.Ponudeni[i]
    answer=df3.Tacan[i]
    L1.append(Question(section,question,options,answer))

  L2=random.sample(L1,20)
  return L2

@st.cache
def get_eruptivna():
  
  L1=[]   
  for i in df4.index:
    section=df4.Sekcija[i]
    question=df4.Pitanje[i]
    options=df4.Ponudeni[i]
    answer=df4.Tacan[i]
    L1.append(Question(section,question,options,answer))

  L2=random.sample(L1,20)
  return L2

@st.cache
def get_struktura():
  
  L1=[]   
  for i in df5.index:
    section=df5.Sekcija[i]
    question=df5.Pitanje[i]
    options=df5.Ponudeni[i]
    answer=df5.Tacan[i]
    L1.append(Question(section,question,options,answer))

  L2=random.sample(L1,10)
  return L2

@st.cache
def get_hemizacija():
  
  L1=[]   
  for i in df6.index:
    section=df6.Sekcija[i]
    question=df6.Pitanje[i]
    options=df6.Ponudeni[i]
    answer=df6.Tacan[i]
    L1.append(Question(section,question,options,answer))

  L2=random.sample(L1,10)
  return L2

@st.cache
def get_tehnologija():
  
  L1=[]   
  for i in df7.index:
    section=df7.Sekcija[i]
    question=df7.Pitanje[i]
    options=df7.Ponudeni[i]
    answer=df7.Tacan[i]
    L1.append(Question(section,question,options,answer))

  L2=random.sample(L1,10)
  return L2

Ls=["Osnove nafte i gasa","Zakonska regulatva i HSE","Mehanicke metode eksploatacije","Eruptivna metoda eksploatacije","Struktura fonda busotina","Hemizacija","Tehnologija pripreme"]
def display_app_header(main_txt,sub_txt):
   

    html_temp = f"""
    <h1 style = "color:black; text_align:center; font-weight: bold;"> {main_txt} </h1>
    <p style = "color:indianred; text_align:center;"> {sub_txt} </p>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
def admin():
  
  display_app_header("ADMIN ZONA","Ovde mozete pregledati sve rezultate ukupno i detaljno po svakom clanu tima ponaosob")
  set_png_as_page_bg('nova.jpg') 
  st.markdown('-----------')
  results=view_all_results()
  clean_db=pd.DataFrame(results, columns=['Name','Datum','tacni','netacni','Osnove','Osnovenetacni','Zakonska',"Zakonskanetacni",'Mehanicke',"Mehanickenetacni",'Eruptivna',"Eruptivnanetacni",'Struktura',"Strukturanetacni",'Hemizacija',"Hemizacijanetacni",'Priprema',"Pripremanetacni"])
  
  c=clean_db[['Osnove','Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']]
  m1=pd.to_numeric(c['Osnove'], errors='coerce')
  m2=pd.to_numeric(c['Zakonska'], errors='coerce')
  m3=pd.to_numeric(c['Mehanicke'], errors='coerce')
  m4=pd.to_numeric(c['Eruptivna'], errors='coerce')
  m5=pd.to_numeric(c['Struktura'], errors='coerce')
  m6=pd.to_numeric(c['Hemizacija'], errors='coerce')
  m7=pd.to_numeric(c['Priprema'], errors='coerce')

  s1 = round(m1.mean(),1)
  s2 = round(m2.mean(),1)
  s3 = round(m3.mean(),1)
  s4 = round(m4.mean(),1)
  s5 = round(m5.mean(),1)
  s6 = round(m6.mean(),1)
  s7 = round(m7.mean(),1)

  srednja_vrednost=[s1,s2,s3,s4,s5,s6,s7]
  c=['Osnove','Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']
  df = pd.DataFrame(list(zip(c,srednja_vrednost)),
        columns =['Sekcija', 'Bodovi'])
  st.write("")

  najveca =df[df["Bodovi"]==df["Bodovi"].max()]
  naj=najveca["Sekcija"]
  naj1=naj.to_string(index=False)
  najmanja=df[df["Bodovi"]==df["Bodovi"].min()]
  najm=najmanja["Sekcija"]
  najm1=najm.to_string(index=False)

  prosecna_uspesnost=round(clean_db["tacni"].mean(),1)
  zvezda=prosecna_uspesnost/10
  star_prosecna_uspesnost=":star:"*int(round(zvezda,0))
  total=clean_db.shape[0]
  total_result = clean_db
  total_result.sort_values(by=['tacni'], inplace=True, ascending=False)
  rang = total_result.drop_duplicates(subset ="Name")
  rang.reset_index(inplace = True, drop = True)
  najbolji=rang.iloc[0]
  najbolji1=najbolji["Name"]
  najlosiji=rang.iloc[-1]
  najlosiji=najlosiji["Name"]

  col1,col2,col3,col4,col5=st.columns(5)
  with col1:
      st.write(":memo: Najbolje razvijena kompetencija je:")
      st.write(naj1)
  with col2:
      st.write(":chart_with_upwards_trend: Kompetencija na kojoj treba raditi je:")
      st.write(najm1)
  with col3:
      st.write(":date: Prosecna uspesnost tima je:")
      st.write(f"{prosecna_uspesnost} {star_prosecna_uspesnost}")
  with col4:
      st.write(":date: Trenutno najbolji rezultat ima:")
      st.write(najbolji1)
  with col5:
      st.write(":date: Svoje rezultate mora da popravi:")
      st.write(najlosiji)
    
  st.markdown('-----------')
  

  fig17 = go.Figure()
                # fig1.add_trace(go.Scatter(x = date.index,
                #        y = date[sekcija]))
  fig17.add_trace(go.Bar(x = df["Sekcija"],
          y = df["Bodovi"],
           text=df["Bodovi"],
                          textposition='auto',
          marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=0.2, opacity=0.6,
          
          orientation = "v")) 
  fig17.update_layout(plot_bgcolor = "white",
        font = dict(color = "#909497"),
        title = dict(text = "Prosecni rezultati tima po kompetencijama"),
        xaxis = dict(title = "Redni broj testa", linecolor = "#909497"), #tick prefix is the html code for Rupee
        yaxis = dict(range=[0,100],title = "Procenti,%", tickformat = ",", linecolor = "#909497"),)
  st.write(" 🔎 Uvid po clanu tima posebno")
  my_expander = st.expander("Prosiri polje", expanded=False)
  with my_expander: 
        col1,col2,col3=st.columns(3)
        with col1:
            st.empty()
        with col2:
            name_search = clean_db.drop_duplicates(subset ="Name")
            name = st.selectbox("Odaberite korisnika: ",name_search)
              #   st.write(name)
            name_list = []
            name_list.append(name)
            name_result = clean_db[clean_db['Name'].isin(name_list)]
          #   st.table(name_result)
            date_search = name_result.Datum
            date = st.selectbox("Odaberite datum testa: ",date_search)
            date_list=[]
            date_list.append(date)
            result_final = name_result[name_result['Datum'].isin(date_list)]
          # st.table(result_final)
        with col3: 
            st.empty()   

        col1,col2,col3=st.columns([4,1,4])
        with col1:

          
       
          
          table = result_final

          sales=table[["Osnove",'Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']]
          sales.reset_index(drop=True, inplace=True)
          m=sales.T
          n=m.rename(columns={0:"Procenat"},index={0:"Sekcije"})
          fig1 = go.Figure()
          fig1.add_trace(go.Bar(name="Rezultati testa",x = n.index,
                          y = n["Procenat"],
                          text=n["Procenat"],
                          textposition='auto',
                          marker_color='#F1AB86',
                          orientation = "v")) 
          fig1.add_trace(go.Bar(name="Prosek tima",x = df["Sekcija"],
          y = df["Bodovi"],
          text=df["Bodovi"],
                          textposition='auto',
          marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=0.2, opacity=0.6,
          orientation = "v")) 
          fig1.update_layout(plot_bgcolor = "white",
                          font = dict(color = "#909497"),
                          title = dict(text = "Istorijat po kompetenciji "),
                          xaxis = dict(title = "Kompetencije", linecolor = "#909497"), #tick prefix is the html code for Rupee
                          yaxis = dict(range=[0,100],title = "Procenti,%", tickformat = ",", linecolor = "black"),)
                  
                                
          st.plotly_chart(fig1,use_container_width=True)
          
 
        with col2:

              
          st.empty()

         
        with col3:
              date=name_result[["Datum","tacni"]]
              date.reset_index(drop=True, inplace=True)
              fig1 = go.Figure()
              fig1.add_trace(go.Scatter(x = date.index,
                      y = date["tacni"]))
              # fig1.add_trace(go.Bar(x = date.index,
              #        y = date["tacni"],
              #        marker_color='#F1AB86',
              #        orientation = "v")) 
              fig1.update_layout(plot_bgcolor = "white",
                    font = dict(color = "#909497"),
                    title = dict(text = "Pracenje uspesnosti"),
                    xaxis = dict(title = "Redni broj testa", linecolor = "#909497"), #tick prefix is the html code for Rupee
                    yaxis = dict(range=[0,100],title = "Procenti,%", tickformat = ",", linecolor = "#909497"),)
              st.plotly_chart(fig1,use_container_width=True)
        st.write("----------------------")
    
        c=name_result[['Osnove','Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']]
        m1=pd.to_numeric(c['Osnove'], errors='coerce')
        m2=pd.to_numeric(c['Zakonska'], errors='coerce')
        m3=pd.to_numeric(c['Mehanicke'], errors='coerce')
        m4=pd.to_numeric(c['Eruptivna'], errors='coerce')
        m5=pd.to_numeric(c['Struktura'], errors='coerce')
        m6=pd.to_numeric(c['Hemizacija'], errors='coerce')
        m7=pd.to_numeric(c['Priprema'], errors='coerce')

        s1 = round(m1.mean(),1)
        s2 = round(m2.mean(),1)
        s3 = round(m3.mean(),1)
        s4 = round(m4.mean(),1)
        s5 = round(m5.mean(),1)
        s6 = round(m6.mean(),1)
        s7 = round(m7.mean(),1)

        srednja_vrednost=[s1,s2,s3,s4,s5,s6,s7]
        c=['Osnove','Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']
        df = pd.DataFrame(list(zip(c,srednja_vrednost)),
            columns =['Sekcija', 'Bodovi'])
          
        fig10 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
        fig10.add_trace(go.Pie(labels=df["Sekcija"], values=df["Bodovi"], name=name1),
          1, 1)
        fig10.update_traces(textposition='outside',textinfo='percent+label',hole=.4, hoverinfo="label+percent+name")
        fig10.update_layout(
          title_text="Prosecna raspodela kompetencija",
          annotations=[dict(text='Kompetencije', x=0.50, y=0.5, font_size=10, showarrow=False)])

        
        st.plotly_chart(fig10,use_container_width=True)          
    
  st.write("----------------------")
  st.write(" 🔎 Uvid po kompletnom timu")
  my_expander = st.expander("Prosiri polje", expanded=False)
  with my_expander: 

    
    
    st.plotly_chart(fig17,use_container_width=True)
    

def testy():
    set_png_as_page_bg('nova.jpg') 
    st.markdown(html_temp11, unsafe_allow_html = True)
   
    st.markdown('-----------')
    now=datetime.datetime.now() 
    date=now.strftime("%d %b %Y %I:%M%p")
    
    results=view_all_results()
    clean_db=pd.DataFrame(results, columns=['Name','Datum','tacni','netacni','Osnove','Osnovenetacni','Zakonska',"Zakonskanetacni",'Mehanicke',"Mehanickenetacni",'Eruptivna',"Eruptivnanetacni",'Struktura',"Strukturanetacni",'Hemizacija',"Hemizacijanetacni",'Priprema',"Pripremanetacni"])
    clean_db1=clean_db[clean_db['Name']==name1]
    total=clean_db1.shape[0]
    if total != 0:
      prosecna_uspesnost=round(clean_db1["tacni"].mean(),1)
      zvezda=prosecna_uspesnost/10
      star_prosecna_uspesnost=":star:"*int(round(zvezda,0))
      b=clean_db1[-1:]
      datum=b["Datum"]
      datum1=datum.to_string(index=False)
    else:
      star_prosecna_uspesnost=""
      prosecna_uspesnost="Podaci ce se obnoviti nakon  prvog uradjenog testa!"
      datum1="Podaci ce se obnoviti nakon  prvog uradjenog testa!"
    
    

    col1,col2,col3=st.columns(3)
    with col1:
      st.write(":memo: Ukupan broj urađenih testova:")
      st.subheader(total)
    with col2:
      
      st.write(":chart_with_upwards_trend: Prosecna uspesnost na testovima:")
      
      st.write(f"{prosecna_uspesnost} {star_prosecna_uspesnost}")
      
    with col3:
      st.write(":date: Poslednji test je radjen:")
      
      st.write(datum1)
    st.write("----------------------")
 
    Ls1=[0,0,0,0,0,0,0]
    Ls2=[0,0,0,0,0,0,0]
  
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:

      st.empty()
      
    with col2: 
      box= st.checkbox('Pokrenite test')
    with col3:
             
        st.empty()
    with col4:
        st.empty()
    with col5:
      box1= st.checkbox('Rezultati') 
    with col6:
      st.empty()
    st.markdown('-----------')
    score=0
      
    if box and box1:
        st.warning('Mozete obeleziti samo jedno polje')

    elif box:
      
        col1,col2=st.columns([2,1]) 
        with col1:
          with st.form("2",clear_on_submit=True):
           
           
              L2=get_osnove()
              L3=get_Zakonska()
              L4=get_mehanicke()
              L5=get_eruptivna()
              L6=get_struktura()
              L7=get_hemizacija()
              L8=get_tehnologija()

              Listapitanja=L2+L3+L4+L5+L6+L7+L8
            
              for obj in Listapitanja:
                empty = st.empty()
                options = obj.get_options()
                choice = empty.radio(label = obj.get_question(),options = options)
                for i in range (0,7):
                    if Ls[i]==obj.get_section():
                      Ls2[i]+=1
                st.markdown('---------')
                
                if choice== obj.get_answer():
                  score+=1
                  for i in range (0,7):
                    if Ls[i]==obj.get_section():
                      Ls1[i]+=1
                      
                  # st.success('Tacno')
                

                if not (choice == 'Odaberite odgovor:') : 
                    # st.info('Tacan odgovor je '+ obj.get_answer())
                    empty.empty()             
                    
              if st.form_submit_button('Kraj'):

                   
#                   slanje_maila()
                  st.info("Test je zavrsen, idite na vrh stranice i kliknite na Rezultati")
                    
                  create_r()
                  add_userr(name1,date,math.trunc(score/100*100),math.trunc(100-score),(Ls1[0]/20*100),100-(Ls1[0]/20*100),(Ls1[1]/10*100),100-(Ls1[1]/10*100),(Ls1[2]/20*100),100-(Ls1[2]/20*100),(Ls1[3]/20*100),100-(Ls1[3]/20*100),(Ls1[4]/10*100),100-(Ls1[4]/10*100),(Ls1[5]/10*100),100-(Ls1[5]/10*100),(Ls1[6]/10*100),100-(Ls1[6]/10*100))
                  
                   
                  st.legacy_caching.clear_cache()
                  
                   
                  
                  st.markdown('---------')
        with col2:
          st.empty()          
                      
                  
    elif box1:
      
      results=view_all_results()
      clean_db=pd.DataFrame(results, columns=['Name','Datum','tacni','netacni','Osnove','Osnovenetacni','Zakonska',"Zakonskanetacni",'Mehanicke',"Mehanickenetacni",'Eruptivna',"Eruptivnanetacni",'Struktura',"Strukturanetacni",'Hemizacija',"Hemizacijanetacni",'Priprema',"Pripremanetacni"])
      clean_db1=clean_db[clean_db['Name']==name1]
      b=clean_db1[-1:]
      
      
      
      j=b["tacni"].to_string(index=False)
      
     

      sales=b[["Osnove",'Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']]
      netacni=b[["Osnovenetacni","Zakonskanetacni","Mehanickenetacni","Eruptivnanetacni","Strukturanetacni", "Hemizacijanetacni","Pripremanetacni"]]

      sales.reset_index(drop=True, inplace=True)
      m=sales.T
      netacni.reset_index(drop=True, inplace=True)
      net=netacni.T
      
      n=m.rename(columns={0:"Procenat"},index={0:"Sekcije"})
      n2=net.rename(columns={0:"Procenat"},index={0:"Sekcije"})
          
      sales1=b[['tacni']]
      sales1.reset_index(drop=True, inplace=True)
      m1=sales1.T
      n1=m1.rename(columns={0:"Procenat"},index={0:"Sekcije"})

      sales11=b[['netacni']]
      sales11.reset_index(drop=True, inplace=True)
      m11=sales11.T
      n11=m11.rename(columns={0:"Procenat"},index={0:"Sekcije"})

      fig1111 = go.Figure()
      fig1111.add_trace(go.Bar(name="Tacni odgovori",x = n1.index,
                     y = n1["Procenat"],
                     text=n1["Procenat"],
                     textposition='auto',
                     marker_color="#F1AB86",
                     orientation = "v")) 
      fig1111.add_trace(go.Bar(name="Netacni odgovori",x = n11.index,
                     y = n11["Procenat"],
                     text=n11["Procenat"],
                     textposition='auto',
                     marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=0.2, opacity=0.6
                     ,
                     orientation = "v")) 
      fig1111.update_layout(plot_bgcolor = "white",
                    font = dict(color = "#909497"),
                    title = dict(text = "Rezultati poslednjeg testa"),
                    xaxis = dict(title = "Odgovori", linecolor = "#909497"), #tick prefix is the html code for Rupee
                    yaxis = dict(range=[0,100],title = "Procenti,%", tickformat = ",", linecolor = "#909497"),)

      
      st.write(":pencil: Rezultati testa")

      fig111 = go.Figure()
      fig111.add_trace(go.Bar(name="Tacni odgovori",x = n.index,
                     y = n["Procenat"],
                     text=n["Procenat"],
                     textposition='auto',
                     marker_color='#F1AB86',
                     orientation = "v")) 
      fig111.add_trace(go.Bar(name="Netacni odgovori",x = n.index,
                     y = n2["Procenat"],
                     text=n2["Procenat"],
                     textposition='auto',
                     marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=0.2, opacity=0.6
                     ,
                     orientation = "v"))               
      fig111.update_layout(plot_bgcolor = "white",
                    font = dict(color = "#909497"),
                    title = dict(text = "Rezultati poslednjeg testa po kompetencijama"),
                    xaxis = dict(title = "Kompetencije", linecolor = "#909497"), #tick prefix is the html code for Rupee
                    yaxis = dict(range=[0,100],title = "Procenti,%", tickformat = ",", linecolor = "#909497"),)
      
          
      my_expander = st.expander("Prosiri polje", expanded=False)
      with my_expander: 
        a1,a2=st.columns(2)
        
        with a1:
          # st.metric("Ostvareni rezultati je: ",   j +" %",delta=razlika)
          st.metric("Ostvareni rezultati je: ",   j +" %")
        with a2: 
          st.empty()
          
       
        st.markdown('---------')
        col1,col2,col3=st.columns([4,1,4])
        with col1:
         
          
          st.plotly_chart(fig1111,use_container_width=True)
        with col2:
          st.empty()
        with col3:
         
          st.plotly_chart(fig111, use_container_width=True)
        st.markdown('---------')
     
      st.write(":notebook_with_decorative_cover: Istorijat rezultata")
      my_expander = st.expander("Prosiri polje", expanded=False)
      with my_expander:  

            c=clean_db1[['Osnove','Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']]
            m1=pd.to_numeric(c['Osnove'], errors='coerce')
            m2=pd.to_numeric(c['Zakonska'], errors='coerce')
            m3=pd.to_numeric(c['Mehanicke'], errors='coerce')
            m4=pd.to_numeric(c['Eruptivna'], errors='coerce')
            m5=pd.to_numeric(c['Struktura'], errors='coerce')
            m6=pd.to_numeric(c['Hemizacija'], errors='coerce')
            m7=pd.to_numeric(c['Priprema'], errors='coerce')

            s1 = round(m1.mean(),1)
            s2 = round(m2.mean(),1)
            s3 = round(m3.mean(),1)
            s4 = round(m4.mean(),1)
            s5 = round(m5.mean(),1)
            s6 = round(m6.mean(),1)
            s7 = round(m7.mean(),1)

            srednja_vrednost=[s1,s2,s3,s4,s5,s6,s7]
            c=['Osnove','Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']
            df = pd.DataFrame(list(zip(c,srednja_vrednost)),
                 columns =['Sekcija', 'Bodovi'])
              
            fig10 = make_subplots(rows=1, cols=1, specs=[[{'type':'domain'}]])
            fig10.add_trace(go.Pie(labels=df["Sekcija"], values=df["Bodovi"], name=name1),
              1, 1)
            fig10.update_traces(textposition='outside',textinfo='percent+label',hole=.4, hoverinfo="label+percent+name")
            fig10.update_layout(
              title_text="Prosecna raspodela kompetencija",
              annotations=[dict(text='Kompetencije', x=0.50, y=0.5, font_size=10, showarrow=False)])

            
            st.plotly_chart(fig10,use_container_width=True)

            col1,col2,col3=st.columns([4,1,4])

            with col1:
              menu=['Osnove','Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']
              sekcija=st.selectbox("Prikaz rezultata po sekciji",menu)

              date=clean_db1[["Datum",sekcija]]
              fig1 = go.Figure()
              # fig1.add_trace(go.Scatter(x = date.index,
              #        y = date[sekcija]))
              fig1.add_trace(go.Bar(x = date.index,
                     y = date[sekcija],
                     marker_color='#F1AB86',
                     orientation = "v")) 
              fig1.update_layout(plot_bgcolor = "white",
                    font = dict(color = "#909497"),
                    title = dict(text = "Istorijat po kompetenciji"),
                    xaxis = dict(title = "Redni broj testa", linecolor = "#909497"), #tick prefix is the html code for Rupee
                    yaxis = dict(range=[0,100],title = "Procenti,%", tickformat = ",", linecolor = "#909497"),)
              st.plotly_chart(fig1,use_container_width=True)
              
              
             
            with col2:
              st.empty()
            with col3:
             
              date_search = clean_db1.Datum
              date = st.selectbox("Odaberite datum testa: ",date_search)
              date_list=[]
              date_list.append(date)
              result_final = clean_db1[clean_db1['Datum'].isin(date_list)]
            
              
              table = result_final

              sales=table[["Osnove",'Zakonska','Mehanicke','Eruptivna','Struktura','Hemizacija','Priprema']]
              sales1=table[["Osnovenetacni","Zakonskanetacni","Mehanickenetacni","Eruptivnanetacni","Strukturanetacni", "Hemizacijanetacni","Pripremanetacni"]]

     
              sales.reset_index(drop=True, inplace=True)
              m=sales.T
              n=m.rename(columns={0:"Procenat"},index={0:"Sekcije"})

              sales1.reset_index(drop=True, inplace=True)
              m1=sales1.T
              n1=m1.rename(columns={0:"Procenat"},index={0:"Sekcije"})
              

              fig1 = go.Figure()
              fig1.add_trace(go.Bar(name="Tacni odgovori",x = n.index,
                     y = n["Procenat"],
                     text=n["Procenat"],
                     textposition='auto',
                     marker_color='#F1AB86',
                     orientation = "v")) 
              fig1.add_trace(go.Bar(name="Netacni odgovori",x = n.index,
                     y = n1["Procenat"],
                     text=n["Procenat"],
                     textposition='auto',
                    marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=0.2, opacity=0.6,
                     orientation = "v")) 
              fig1.update_layout(plot_bgcolor = "white",
                    font = dict(color = "#909497"),
                    title = dict(text = "Istorijat po testovima"),
                    xaxis = dict(title = "Kompetencije", linecolor = "#909497"), #tick prefix is the html code for Rupee
                    yaxis = dict(range=[0,100],title = "Procenti,%", tickformat = ",", linecolor = "#909497"),)
            
                            
              st.plotly_chart(fig1,use_container_width=True)

def animacija():
  file_ = open("C:/Bojan Martinovic/22.gif", "rb")
  contents = file_.read()
  data_url = base64.b64encode(contents).decode("utf-8")
  file_.close()
  st.markdown(
  f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
  unsafe_allow_html=True,)

#funkcija sa sign in-------------------------------------------------

def signup():
  st.markdown(html_temp1, unsafe_allow_html = True)
  st.markdown("--------------")
  with st.form("1"):
    col1,col2,col3,col4=st.columns([1,1,1,1])

    with col1:
          
      new_ime=st.text_input("Ime")
      new_username = st.text_input("Korisnicko ime")
      
    with col2:
    
      new_prezime=st.text_input("Prezime")
      new_password= st.text_input("Sifra",type='password')
      
    with col3:
      naziv_pozicije=st.text_input("Naziv pozicije")
      new_email=st.text_input("Vasa email adresa")

    with col4:
      sap_broj=st.text_input("SAP broj")
      broj_telefona=st.text_input("Broj telefona")

    if st.form_submit_button("Sign up"):
            create_usertable()
            add_userdata(new_username,new_password,new_ime,new_prezime,new_email,broj_telefona,sap_broj,naziv_pozicije)
            with col1:
              st.success("Uspesno ste se registrovali")
            with col2: 
              st.info("Ulogujte se kroz Login meni")
  st.markdown("--------------")
    
  
#naslovi stranica----------------------------------------------
html_temp = f"""
    <h2 style = "color:indianred; text_align:center; font-weight: bold;"> DOBRODOSLI U NAFTNU FISKULTURU </h2>
    <p style = "color:indianred; text_align:center;"> </p>
    </div>
    """
html_temp1 = f"""
    <h2 style = "color:indianred; text_align:center; font-weight: bold;"> KREIRAJTE KORISNICKI NALOG </h2>
    <p style = "color:indianred; text_align:center;">Sekcija za kreiranje korisničkog profila </p>
    </div>
    """
html_temp50 = f"""
    <h2 style = "color:indianred; text_align:center; font-weight: bold;"> DOBRODOSLI U ADMIN SEKCIJU </h2>
    <p style = "color:indianred; text_align:center;">ovde mozete da pregledate sve rezultate vaseg tima i da ispratite napredak </p>
    </div>
    """
html_temp11 = f"""
    <h1 style = "color:black; text_align:center; font-weight: bold;"> FISKULTURNI TEST ZNANJA </h1>
    <p style = "color:black; text_align:center;">U ovoj sekciji mozete daradite test, da pratite rezultate prethodnih testiranja i da uocite u kojim oblastima imate  visoke kompetencije a u kojim je potrebno da povecaate nivo kompetencija </p>
    </div>
    """
html_temp111 = f"""
    <h1 style = "color:indianred; text_align:center; font-weight: bold;"> NAFTNA FISKULTURA </h1>
    <p style = "color:indianred; text_align:center;">navigacija </p>
    </div>
    """
#funkcija za lottti animaciju---------------------------------------------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

#funkcija za pocetnu stranicu--------------------------------------------
def header(url):
     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

image = Image.open("1233.png")   

def main(): 
    
    menu=['Pocetna','Login','SignUp',"Admin"]
    with st.sidebar:
      st.image(image)
      st.markdown(html_temp111, unsafe_allow_html = True)
      st.markdown("---")
    choice=st.sidebar.selectbox('Menu',menu)
    with st.sidebar:
      st.markdown("---")
    if choice=='Pocetna':
       
        st.markdown(html_temp, unsafe_allow_html = True)
        st.write('_Naftna fiskultura predstavlja portal koji ce omogućiti svakom korisniku da prosiri postojece i stekne novo znjanje iz oblasti proizvodnje nafte i gasa, zakona o rudarstvu, programskih jezika itd. Ideja ovog projekta nije provera trenutnog nivoa kompetencija vec konstantno ucenje i i razvijanje kompetencija. Shodno tome prilikom odgovaranja na pitanja apsolutno se podrzava i podstrekuje koriscenje razlicitih izvora informacija kao sto su knjige, interner i pomoc starijih kolega. Sa vrlo jasnom namerom odredjeni broj pitanja su na engleskom i ruskom jeziku kako bi podstakli korisnike  da nauče terminologiju koja se koristi u literaturi i u praksi. Svaki put kada se uradi test rezultati ce moci odmah da se provere i pitanja ce se takodje ponavlajti kroz razlicite testove. Zelim Vam puno uspeha i verujem da će vam ovaj portal pomoci u nameri da dalje razvijete vase vestine._')
        st.write(':books:**_Repetitio est mater studiorum_**')
       
     
        st.sidebar.markdown(
        '<h6>Kreirano u &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="10">&nbsp od Bojana M,Miodraga S i Milice J</a></h6>',
        unsafe_allow_html=True
    )
    elif choice=='Login':
          
          st.sidebar.subheader('Ulogujte se')
          
          username=st.sidebar.text_input('Korisnicko ime')
          global name1
          name1=username
          password=st.sidebar.text_input('Sifra',type='password')
          u="Bojan"
          n="123"
          
         
          if st.sidebar.checkbox('Login'):
              
              create_usertable()
              result = login_user(username,password)
              result1=admin_user(u,n)
             
              if result:
                  st.sidebar.info('Ulogovani ste kao {}'.format(username))
                  
                  task=testy()
              
              else:
                  st.sidebar.warning('Incorrect Username/password')

              if result1:
                   task=admin()

          st.sidebar.markdown(
        '<h6>Kreirano u &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="10">&nbsp od Bojana M, Miodrag S i Milice J</a></h6>',
        unsafe_allow_html=True
    )

    elif choice=='Admin':
          
          st.sidebar.subheader('Ulogujte se')
          u=st.sidebar.text_input('Korisnicko ime')
          n=st.sidebar.text_input('Sifra',type='password')
         
          if st.sidebar.checkbox('Login'):
              result1=admin_user(u,n)
              
              if result1:
                  st.sidebar.info('Ulogovani ste kao {}'.format(u))
                  
                  task=admin()
              
              else:
                  st.sidebar.warning('Incorrect Username/password')
            

            
    elif choice=='SignUp':
            
            signup()
            st.sidebar.markdown(
        '<h6>Kreirano u &nbsp<img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit logo" height="10">&nbsp od Bojana M, Miodraga S i Milice J</a></h6>',
        unsafe_allow_html=True
    )
      
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file) 
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: scroll; # doesn't work
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('132.jpg')    
  
st.markdown(
    """
    <style>
    .reportview-container {
        background: 'nova.jpg')
    }
   .sidebar .sidebar-content {
        background: url("https://images.app.goo.gl/LFCobouKtT7oZ7Qv7")
    }
    </style>
    """,
    unsafe_allow_html=True
)

hide_streamlit_style = """
  <style>
  /* This is to hide hamburger menu completely */
  #MainMenu {visibility: hidden;}
  /* This is to hide Streamlit footer */
  footer {visibility: hidden;}
  /*
  If you did not hide the hamburger menu completely,
  you can use the following styles to control which items on the menu to hide.
  */
  ul[data-testid=main-menu-list] > li:nth-of-type(4), /* Documentation */
  ul[data-testid=main-menu-list] > li:nth-of-type(5), /* Ask a question */
  ul[data-testid=main-menu-list] > li:nth-of-type(6), /* Report a bug */
  ul[data-testid=main-menu-list] > li:nth-of-type(7), /* Streamlit for Teams */
  ul[data-testid=main-menu-list] > div:nth-of-type(2) /* 2nd divider */
    {display: none;}
  </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__=='__main__':
    main()


