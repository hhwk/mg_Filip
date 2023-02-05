import streamlit as st
from deta import Deta
from PIL import Image
from datetime import date, timedelta
import time
import json
import os
import pandas as pd
import numpy as np

Country_Name='Filip'
city_1='Лусон'
city_2='Боракай'
city_3='Себу'
city_4='Панай'

deta = Deta(st.secrets["deta_key"])
sms=deta.Base('sms')
Global = deta.Base("Global")
db = deta.Base(f'{Country_Name}')
Attak=deta.Base(f'Attak_{Country_Name}')
Graph=deta.Base('Photo_Url')
request=deta.Base('request')
request_money=deta.Base('request_money')
photo=deta.Base('Photo_Url')
pp=photo.get('bb6a5172diyj')


city=Global.get(f'{Country_Name}')
money=city['money']-((city['sunks_of_you']*50)+(city['sunks_for_you']*100))
st.set_page_config(


page_title="Мировое господство",
page_icon="🚙",
layout="wide",
initial_sidebar_state="collapsed", #expanded/collapsed
menu_items={
         'Get Help': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
         'Report a bug': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
         'About': "# Автор MangoVirus"
     })
st.sidebar.image('https://cdn.discordapp.com/attachments/890188503047077928/1070451124869533758/066443762463369c.png',width=64)
menu = st.sidebar.selectbox('Меню',('Стартовая страница','Улучшения','Запуск ракет','Посещения','Гуманитарная помощь','Авторы'))
if pp['Atention'] !='':
    st.sidebar.warning(pp['Atention'])
if city['sms']!='':
    st.sidebar.warning(city['sms'])
st.sidebar.caption('Автор MangoVirus')

masiv_up=[0,0,0,0]
masiv_shit=[' ',' ',' ',' ']
attak=[]
attak1=[]
attak2=[]
attak3=[]
attak4=[]


if menu=='Авторы':
    '''# Над данным проектом работали'''
    st.subheader('MangoVirus')
    '''Разработчик сайта, создатель DataBase.'''
    st.subheader('Турба')
    '''Проектный руководитель, дизайнер.'''
    st.subheader('Если вы хотите поддержать нас и в будущем видеть более маштабные нововедения вы можете скинуть нам пару тугриков по номеру телефона 8 (977) 382-41-17')
    '''Если вам нужна помощь по сайту или вы нашли баг, можете нажать на 3 полосочки справа и Get Help или Report Bug'''


if menu=='Гуманитарная помощь':
    st.write('Деньги:',money)
    visit_money = st.selectbox('Кому вы хотите перевести деньги?',('Мексике', 'Канаде', 'Австралия', 'Швеции', 'Аргентине'))
    how_money = st.number_input('Сумма перевода?', 200)
    for ii in range(0, 20):
        if request_money.get(f'{ii}') == None:
            break
    if st.button('Перевести'):
        for ii in range(0, 20):
            if request_money.get(f'{ii}') == None:
                break
        request_money.put({'key':f'{ii}','who':f'{Country_Name}','come':visit_money,'price':how_money})
        st.success('Запрос на перевод отправлен.(Деньги придут в течение 5 минут)')


if menu=='Посещения':
    visit = st.selectbox('Какую старану вы хотите посетить?', ('Мексика', 'Канада', 'Австралия', 'Швеция', 'Аргентина'))
    if st.button('Отправить запрос'):
        for ii in range(0, 20):
            if request.get(f'{ii}') == None:
                break
        request.put({'key':f'{ii}','who':f'{Country_Name}','come':visit})
        st.success('Запрос на посещение отправлен')


if menu=='Запуск ракет':
    final_roket = -1999
    if city['reserch']=='0':
        st.error('Дружок ты еще не изучил ракеты')
    else:
        st.write('Количество ваших ракет:',city['roket'])
        country = st.multiselect('Какие страны атакуем?',['Мексика', 'Канада', 'Австралия', 'Швеция', 'Аргентина'])
        for l in range(0,len(country)):
            if country[l]=='Мексика':
                attak=st.multiselect('Какие города атакуем в Максика?',['Мехико','Канкун','Мерида','Таско'])
            if country[l]=='Канада':
                attak1=st.multiselect('Какие города атакуем в Канада?',['Оттава','Торонто','Ванкувер','Квебек'])
            if country[l]=='Австралия':
                attak2=st.multiselect('Какие города атакуем в Австралия?',['Кенберра','Сидней','Мельбрун','Перт'])
            if country[l]=='Швеция':
                attak3=st.multiselect('Какие города атакуем в Швеция?',['Стокгольм','Вестерсон','Висбю','Евле'])
            if country[l]=='Аргентина':
                attak4=st.multiselect('Какие города атакуем в Аргентина?',['Буэнос-Сальта','Сальта','Кордова','Мендоса'])
            final_roket=city['roket']-(len(attak)+len(attak1)+len(attak2)+len(attak3)+len(attak4))
            st.write('У вас останеться ракет:',final_roket)
         
        if st.button('Отправить данные'):
            if final_roket>=0:
                for ll in range(0,5):
                    if len(country)<5:
                        count=5-len(country)
                        for lll in range(0,count):
                            country.append(' ')
                for ii in range(0, 20):
                  if Attak.get(f'{ii}') == None:
                      break
                for iii in range(0,30):
                  if sms.get(f'{iii}')== None:
                      break
                sms.put({'key':f'{iii}','Country':f'{Country_Name}','sms':'Attak'})
                Attak.put({'key':f'{ii}','Country':'Мексика'+str(attak),'Country1':'Канада'+str(attak1),'Country2':'Австралия'+str(attak2),'Country3':'Швеция'+str(attak3),'Country4':'Аргентина'+str(attak4)})
                db_content = Attak.fetch().items
                st.write(db_content)
                with st.spinner('Wait for it...'):
                    time.sleep(1)
                st.success('Данные обновлены!')
            elif final_roket==-1999:
                st.error('Дружок не надо мне засарять базу данных...')
            else:
                st.error('Вы выпустили больше ракет чем у вас есть...')


if menu=='Улучшения':
    time1=0
    number=0
    reserch1=0
    st.write('Деньги:',money)
    st.write('Какие города вы хотите улучшить?')
    up = st.checkbox(f'{city_1}')
    if up:
        masiv_up[0]+=1
        money-=200
        x=st.checkbox(f'Улучшить {city_1} 2 раза?')
        if x:
            masiv_up[0]+=1
            money-=200
    up1 = st.checkbox(f'{city_2}')
    if up1:
        masiv_up[1] += 1
        money -= 200
        x1 = st.checkbox(f'Улучшить {city_2} 2 раза?')
        if x1:
            masiv_up[1] += 1
            money -= 200
    up2 = st.checkbox(f'{city_3}')
    if up2:
        masiv_up[2] += 1
        money -= 200
        x2 = st.checkbox(f'Улучшить {city_3} 2 раза?')
        if x2:
            masiv_up[2] += 1
            money -= 200
    up3 = st.checkbox(f'{city_4}')
    if up3:
        masiv_up[3] += 1
        money -= 200
        x3 = st.checkbox(f'Улучшить {city_4} 2 раза?')
        if x3:
            masiv_up[3] += 1
            money -= 200

    st.write('На какие города установим щиты?')
    shit = st.checkbox(f'{city_1} ')
    if shit:
        if city['shit1']=='🛡️':
            st.error('Дружок, у нас так не принято. По 1 щиту на город...')
        else:
            masiv_shit[0]+='🛡️'
            money-=350
    shit1 = st.checkbox(f'{city_2} ')
    if shit1:
        if city['shit2']=='🛡️':
            st.error('Дружок, у нас так не принято. По 1 щиту на город...')
        else:
            masiv_shit[1]+='🛡️'
            money-=350
    shit2 = st.checkbox(f'{city_3} ')
    if shit2:
        if city['shit3'] == '🛡️':
            st.error('Дружок, у нас так не принято. По 1 щиту на город...')
        else:
            masiv_shit[2] += '🛡️'
            money -= 350
    shit3 = st.checkbox(f'{city_4} ')
    if shit3:
        if city['shit4']=='🛡️':
            st.error('Дружок, у нас так не принято. По 1 щиту на город...')
        else:
            masiv_shit[3]+='🛡️'
            money-=350
    if city['reserch']=='1':
        number = st.number_input('Сколько ракет делаем?',0)
        st.write('Вы получите в следующие количество ракет', number)
        money -= 500 * number
    else:
        st.write(' ')
        reserch=st.checkbox('Изучить ядерные ракеты')
        st.write(' ')
        if reserch:
            money-=500
            reserch1=1

    sunks_for_who = st.multiselect('На какие страны вы хотите наложить санкции?', ['Мексика', 'Канада', 'Австралия', 'Швеция', 'Аргентина'])
    money-= 50*len(sunks_for_who)

    st.write('Ваш баланс после операции:', money)

    eco1=72+(10*city['up1']+10*masiv_up[0])-city['debaf1']
    if eco1>100:
        eco1=100
    eco2=54+(10*city['up2']+10*masiv_up[1])-city['debaf2']
    if eco2>100:
        eco2=100
    eco3=54+(10*city['up3']+10*masiv_up[2])-city['debaf3']
    if eco3>100:
        eco3=100
    eco4=36+(10*city['up4']+10*masiv_up[3])-city['debaf4']
    if eco4>100:
        eco4=100

    col1, col2, col3,col4= st.columns(4)
    col1.metric('🏠'+city['shit1']+masiv_shit[0]+f'{city_1}','⚙️'+str(60+10*city['up1']+10*masiv_up[0])+'%'+' 🌳 '+str(eco1)+'%',masiv_up[0]*10)
    col2.metric('🏠'+city['shit2']+masiv_shit[1]+f'{city_2}','⚙️'+str(50+10*city['up2']+10*masiv_up[1])+'%'+' 🌳 '+str(eco2)+'%',masiv_up[1]*10)
    col3.metric('🏠'+city['shit3']+masiv_shit[2]+f'{city_3}','⚙️'+str(50+10*city['up3']+10*masiv_up[2])+'%'+' 🌳 '+str(eco3)+'%',masiv_up[2]*10)
    col4.metric('🏠'+city['shit4']+masiv_shit[3]+f'{city_4}','⚙️'+str(40+10*city['up4']+10*masiv_up[3])+'%'+' 🌳 '+str(eco4)+'%',masiv_up[3]*10)

    mail=st.text_input('Тут вы можете отправить сообщение Представителю ООН')
    if st.button('Отправить данные'):
        if money>=0:
            for ii in range(0,20):
                if db.get(f'{ii}')==None:
                    break
            for iii in range(0,30):
                if sms.get(f'{iii}')==None:
                    break
            sms.put({'key':f'{iii}','Country': f'{Country_Name}', 'sms': mail})
            db.put({'key':f'{ii}',"money":money, "roket": number,"shit":str(masiv_shit),"up": str(masiv_up),'sunks_for_who':str(sunks_for_who),'reserch':reserch1})
            with st.spinner('Wait for it...'):
                time.sleep(1)
                st.success('Данные обновлены!')
                db_content = db.fetch().items
                st.write(db_content)
        else:
            st.error('Вы потратили больше денег чем у вас есть...')

if menu=='Стартовая страница':
    st.title(f'Вы играете за Филипинские острова')
    st.write('Деньги:', money)
    st.write('Ракеты:', city['roket'])
    st.write('Санкции наложеные вами:',city['sunks_of_you'])
    st.write('Санкции наложеные на вас:',city['sunks_for_you'])
    eco1 = 72 + (10 * city['up1'] + 10 * masiv_up[0]) - city['debaf1']
    if eco1 > 100:
        eco1 = 100
    eco2 = 54 + (10 * city['up2'] + 10 * masiv_up[1]) - city['debaf2']
    if eco2 > 100:
        eco2 = 100
    eco3 = 54 + (10 * city['up3'] + 10 * masiv_up[2]) - city['debaf3']
    if eco3 > 100:
        eco3 = 100
    eco4 = 36 + (10 * city['up4'] + 10 * masiv_up[3]) - city['debaf4']
    if eco4 > 100:
        eco4 = 100
    col1, col2, col3, col4 = st.columns(4)
    col1.metric('🏠' + city['shit1'] + f'{city_1}','⚙️' + str(60 + 10 * city['up1']) + '%' + ' 🌳 ' + str(eco1) + '%')
    col2.metric('🏠' + city['shit2'] + f'{city_2}','⚙️' + str(50 + 10 * city['up2']) + '%' + ' 🌳 ' + str(eco2) + '%')
    col3.metric('🏠' + city['shit3'] + f'{city_3}','⚙️' + str(50 + 10 * city['up3']) + '%' + ' 🌳 ' + str(eco3) + '%')
    col4.metric('🏚️' + city['shit4'] + f'{city_4}','⚙️' + str(0) + '%' + ' 🌳 ' + str(0) + '%')
    st.image(pp['Graph1'])
    st.image(pp['Graph2'])
    st.image(pp['Graph3'])
    st.image(pp['Graph4'])
