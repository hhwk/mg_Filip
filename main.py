import streamlit as st
from deta import Deta
from PIL import Image
from datetime import date, timedelta
import time
import json
import os
import pandas as pd
import numpy as np

deta = Deta(st.secrets["deta_key"])
Global = deta.Base("Global")
db = deta.Base('Kitay')
Attak_Kitay=deta.Base('Attak_Kitay')
Graph=deta.Base('Photo_Url')

city=Global.get('Kitay')
money=city['money']-((city['sunks_of_you']*50)+(city['sunks_for_you']*100))
st.set_page_config(


page_title="Мировое господство",
page_icon="🥭",
layout="wide",
initial_sidebar_state="collapsed", #expanded/collapsed
menu_items={
         'Get Help': 'https://www.google.com/',
         'Report a bug': "https://www.google.com/",
         'About': "# Автор MangoVirus"
     })

menu = st.sidebar.selectbox(
     'Меню',
     ('Стартовая страница','Улучшения','Ракета'))


masiv_up=[0,0,0,0]
masiv_shit=[' ',' ',' ',' ']
attak=[]
attak1=[]
attak2=[]
attak3=[]
attak4=[]


if menu=='Ракета':
    st.write('Количество ваших ракет:',city['roket'])
    country = st.multiselect('Какие страны атакуем?',['Япония', 'Северная-Коррея', 'Пакистан', 'Афганистан','Сирия'])
    for l in range(0,len(country)):
        if country[l]=='Япония':
            attak=st.multiselect('Какие города атакуем в Японии?',['Йокогама','Токио','Киото','Осака',])
        if country[l]=='Северная-Коррея':
            attak1=st.multiselect('Какие города атакуем в Северной-Коррее?',['Пхеньян','Расон','Хусан','Вонсан',])
        if country[l]=='Пакистан':
            attak2=st.multiselect('Какие города атакуем в Пакистане?',['Карачи','Лахор','Мултан','Кветта',])
        if country[l]=='Афганистан':
            attak3=st.multiselect('Какие города атакуем в Афганистане?',['Кабул','Герат','Кандагар','Кундуз',])
        if country[l]=='Сирия':
            attak4=st.multiselect('Какие города атакуем в Сирии?',['Аллепо','Дамаск','Хама','Африн',])
        final_roket=city['roket']-(len(attak)+len(attak1)+len(attak2)+len(attak3)+len(attak4))
        st.write('У вас останеться ракет:',final_roket)

    if st.button('Отправить данные'):
        if final_roket>=0:
            for ll in range(0,5):
                if len(country)<5:
                    count=5-len(country)
                    for lll in range(0,count):
                        country.append(' ')
            Attak_Kitay.put({'Country':str(country[0])+str(attak),'Country1':str(country[1])+str(attak1),'Country2':str(country[2])+str(attak2),'Country3':str(country[3])+str(attak3),'Country4':str(country[4])+str(attak4)})
            db_content = Attak_Kitay.fetch().items
            st.write(db_content)
            with st.spinner('Wait for it...'):
                time.sleep(1)
            st.success('Данные обновлены!')
        else:
            st.error('Вы выпустили больше ракет чем у вас есть...')

if menu=='Улучшения':
    time1=0
    st.write('Деньги:',money)

    st.write('Какие города вы хотите улучшить?')
    up = st.checkbox('Пекин')
    if up:
        masiv_up[0]+=1
        money-=200
    up1 = st.checkbox('Шанхай')
    if up1:
        masiv_up[1] += 1
        money -= 200
    up2 = st.checkbox('Гуанчжоу')
    if up2:
        masiv_up[2] += 1
        money -= 200
    up3 = st.checkbox('Гонконг')
    if up3:
        masiv_up[3] += 1
        money -= 200

    st.write('На какие города установим щиты?')
    shit = st.checkbox('Пекин ')
    if shit:
        masiv_shit[0]+='🛡️'
        money-=400
    shit1 = st.checkbox('Шанхай ')
    if shit1:
        masiv_shit[1]+='🛡️'
        money -= 400
    shit2 = st.checkbox('Гуанчжоу ')
    if shit2:
        masiv_shit[2]+='🛡️'
        money -= 400
    shit3 = st.checkbox('Гонконг ')
    if shit3:
        masiv_shit[3]+='🛡️'
        money -= 400

    number = st.number_input('Сколько ракет делаем?')
    st.write('Вы получите в следующие количество ракет', number)
    money -= 500 * number

    sunks_for_who = st.multiselect('На какие страны вы хотите наложить санкции?', ['Япония', 'Северная-Коррея', 'Пакистан', 'Афганистан', 'Сирия'])
    money-= 50*len(sunks_for_who)

    st.write('Ваш баланс после операции:', money)

    col1, col2, col3,col4= st.columns(4)
    col1.metric('🏠'+city['shit1']+masiv_shit[0]+'Пекин','⚙️'+str(60+10*city['up1']+10*masiv_up[0])+'%'+' 🌳 '+str(72+ (10*city['up1']+10*masiv_up[0])- (city['debaf1']*20))+'%',masiv_up[0]*10)
    col2.metric('🏠'+city['shit2']+masiv_shit[1]+'Шанхай','⚙️'+str(50+10*city['up2']+10*masiv_up[1])+'%'+' 🌳 '+str(54+ (10*city['up2']+10*masiv_up[1])- - (city['debaf2']*20))+'%',masiv_up[1]*10)
    col3.metric('🏠'+city['shit3']+masiv_shit[2]+'Гуанчжоу','⚙️'+str(50+10*city['up3']+10*masiv_up[2])+'%'+' 🌳 '+str(54+ (10*city['up3']+10*masiv_up[2])- (city['debaf3']*20))+'%',masiv_up[2]*10)
    col4.metric('🏠'+city['shit4']+masiv_shit[3]+'Гонконг','⚙️'+str(40+10*city['up4']+10*masiv_up[3])+'%'+' 🌳 '+str(36+ (10*city['up4']+10*masiv_up[3])- (city['debaf4']*20))+'%',masiv_up[3]*10)

    if st.button('Отправить данные'):
        if money>=0:
            #os.system('python MG/123.py')
            db.put({"money":money, "roket": number,"shit":str(masiv_shit),"up": str(masiv_up),'sunks_for_who':str(sunks_for_who)})
            db_content = db.fetch().items
            st.write(db_content)
            with st.spinner('Wait for it...'):
                time.sleep(1)
            st.success('Данные обновлены!')
        else:
            st.error('Вы потратили больше денег чем у вас есть...')

if menu=='Стартовая страница':
    '''# Привет!
    Вы играете за Китай'''

    st.write('Деньги:', money)
    st.write('Ракеты:', city['roket'])
    st.write('Санкции наложеные вами:',city['sunks_of_you'])
    st.write('Санкции наложеные на вас:',city['sunks_for_you'])
    col1, col2, col3, col4 = st.columns(4)
    col1.metric('🏠' + city['shit1'] + 'Пекин','⚙️' + str(60 + 10 * city['up1']) + '%' + ' 🌳 ' + str(72 + 10 * city['up1']- (city['debaf1']*20)) + '%')
    col2.metric('🏠' + city['shit2'] + 'Шанхай','⚙️' + str(50 + 10 * city['up2']) + '%' + ' 🌳 ' + str(54 + 10 * city['up2']- (city['debaf2']*20)) + '%')
    col3.metric('🏠' + city['shit3'] + 'Гуанчжоу','⚙️' + str(50 + 10 * city['up3']) + '%' + ' 🌳 ' + str(54 + 10 * city['up3']- (city['debaf3']*20)) + '%')
    col4.metric('🏠' + city['shit4'] + 'Гонконг','⚙️' + str(40 + 10 * city['up4']) + '%' + ' 🌳 ' + str(36 + 10 * city['up4']- (city['debaf4']*20)) + '%')
    st.image('https://cdn.discordapp.com/attachments/1070077630197534780/1070367870632071238/Graph1.png')
    st.image('https://cdn.discordapp.com/attachments/1070077630197534780/1070367870845988934/Graph2.png')
    st.image('https://cdn.discordapp.com/attachments/1070077630197534780/1070367870380425226/Graph4.png')
    st.image('https://cdn.discordapp.com/attachments/1070077630197534780/1070367870158123078/Graph3.png')