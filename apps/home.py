
from numpy.core.numerictypes import _typedict
import streamlit as st 
import pandas as pd
import numpy as np
from sqlite3.dbapi2 import paramstyle
import bcrypt
from functions import check_email,make_password,check_hashes,GETCoefficients,remove_duplicates
from database import create_usertable,add_user_data,check_double_email,check_double_username,login_user,check_userdatatable
import datetime
#from data_functions_clubs import*
#from data_functions_league import*
import matplotlib
matplotlib.use('Agg')
from League_functions.avg_Income_for_player_Departures import  BATCH_for_GetAVGExpendFORplayerArrivals
from functions import DataFrameFunc,NumberOfRows
from League_functions.EFPA_func import*
from Club_functions.CDWS_func import*
from Club_functions.CDTAS_func import*
#    import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import sqlite3
import time
from database import*

import os
import altair as alt
import duckdb
import streamlit.components.v1 as components
import sqlite3
import os
import bar_chart_race as bcr
import base64
import re



# save_df = DataFrameFuncClubs('datas/sportska_kubska_statsitika_OBRDENO.csv')
# conn = sqlite3.connect('data.db', check_same_thread=False)
# c = conn.cursor()
# sqlite_table = "Clubs_datas"
# save_df.to_sql(sqlite_table, con=conn, if_exists='fail')

rem_niz_CLUB_SEASON = []
rem_niz_CLUB_TROUGHT_SEASON = []
coef = 'file.txt'
fp_league = 'Ligaska_KONACAN_STAS.csv'
fp_clubs = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
save_csv_Expend = "sportska_kubska_statsitika_OBRDENO.csv"
save_csv_Expend_BATCH = 'datas/BATCH_sportska_kubska_statsitika_OBRDENO.csv'
#-----------------------------------------
f_datas = 'datas/exported/GetAVGExpendFORplayerArrivals.csv'
#------------------------------------
# from apps.login_pages import app1,app2
#import login_pages.app1
import bar_chart_race as bcr
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import time
import io
import altair as alt
from altair import Chart, X, Y, Axis, SortField, OpacityValue
from altair.expr import datum, if_
from vega_datasets import data
import altair as alt
from vega_datasets import data
from datetime import datetime
from html_temp import *
from plotnine import ggplot, aes, geom_line
import PIL.Image as Image
from pathlib import Path
from PIL import UnidentifiedImageError
import cv2
from streamlit import caching
from html_temp import*
from functions import*



def app():
    a  = return_post_id_temp_MAIN()
    st.write("a",a)
    # def add_if_key_not_exist(dict_obj, key, value):
    #     if key not in dict_obj:
    #         dict_obj.update({key: value})
    # head_message_temp ="""
	# <div style="background-color:silver;padding:10px;border-radius:5px;margin:10px;">
	# <h2 style="color:white;text-align:center;">{}</h1>
	# <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
	# <h4>Author: {} </h4> 		
	# <h4>Post Date: {} </h4>	
    # <h4>Reading time: {} </h4>	
	# </div>
    # """


    # full_message_temp ="""
	# <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
	# 	<p style="text-align:justify;color:black;padding:10px">{}</p>
	# </div>
	# """

    dfsve = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN',conn)
    st.write("dataframe ")
    st.dataframe(dfsve)
    df_user = pd.read_sql_query('SELECT DISTINCT user_id FROM blog_table_temp_MAIN',conn)
    temp_user = df_user['user_id'].unique() 
    df_post = pd.read_sql_query('SELECT DISTINCT id_post FROM blog_table_temp_MAIN',conn)
    temp_post = df_post['id_post'].unique() 
    st.success("temp_post")
    st.dataframe(temp_post)

    post_lista =[]
    for i in temp_post:
        post_lista.append(i)


    user_lista =[]
    for i in temp_user:
        user_lista.append(i)
    d = {}
    for i in user_lista:
        st.write(" i :: ",i)
        for j in post_lista:
            st.write(" j :: ",j)
            df = pd.read_sql_query('SELECT author,read_time FROM blog_table_temp_MAIN WHERE id_post = "{}"'.format(int(j)),conn)
            st.dataframe(df)
            Total = df['read_time'].sum()
            add_if_key_not_exist(d,j,Total)
            #st.write("Total time read",Total)
            #st.success("isis read time")

    st.write(d)
    
    st.warning("kraj ispisa svih postova !!")
    st.title('View all posts !!!')
    df = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN',conn)
    df_new = df[['id_post','author','user_id','title','article','img','postdate']]
    a = df_new['id_post'].unique() 
    lista =[]
    for i in a:
        lista.append(i)
    caching.clear_cache()
    for j in user_lista:
        df = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}"'.format(int(j)),conn)
        for i in lista:
            df_print = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}" AND id_post = "{}"'.format(int(j),int(i)),conn)
            df_a_d_t = pd.read_sql_query('SELECT DISTINCT title,author,postdate FROM blog_table_temp_MAIN WHERE user_id = "{}" AND id_post = "{}"'.format(int(j),int(i)),conn)
            if df_a_d_t.empty != True :
                temp_reading_time = d.get(i)
                st.write("temp_reading_time : ",temp_reading_time)
                
                st.markdown(head_message_temp.format(df_a_d_t['title'][0],df_a_d_t['author'][0],df_a_d_t['postdate'][0],temp_reading_time),unsafe_allow_html=True)
                for i in range(0,len(df_print)):
                    if type(df_print['img'][i]) != str and df_print['img'][i] != None:
                        test = np.frombuffer(df_print['img'][i], dtype=np.uint8)
                        opencv_image = cv2.imdecode(test, 1)
                        st.image(opencv_image, channels="BGR")
                    elif type(df_print['article'][i]) == str and df_print['article'][i] != None:
                        st.markdown(full_message_temp.format(df_print['article'][i]),unsafe_allow_html=True)
                st.success("end of post")
    

    caching.clear_cache()

    st.warning("kraj ispisa svih postova !!")

    st.success("ispis potova izborom naslova !!! pocetak  -> title")
    df_title = pd.read_sql_query('SELECT title FROM blog_table_temp_MAIN',conn)
    temp_title = df_title['title'].unique() 

    title_lista =[]
    for i in temp_title:
        title_lista.append(i)
    st.write(title_lista)

    st.write("Ispis naslova :: ")
    for i in title_lista:

        st.write(i)

    remeber = st.selectbox("Select title post", options= list(title_lista))
    if st.button("Submit"):
        df_title_temp = pd.read_sql_query('SELECT id_post,user_id FROM blog_table_temp_MAIN WHERE title = "{}"'.format(remeber),conn)
        st.dataframe(df_title_temp)
        j = df_title_temp['user_id'][0]
        i = df_title_temp['id_post'][0]

        df_title = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}" AND id_post = "{}"'.format(int(j),int(i)),conn)
        df_a_d_t = pd.read_sql_query('SELECT DISTINCT title,author,postdate FROM blog_table_temp_MAIN WHERE user_id = "{}" AND id_post = "{}"'.format(int(j),int(i)),conn)
        if df_a_d_t.empty != True :
            temp_reading_time = d.get(i)
            st.write("temp_reading_time : ",temp_reading_time)
            
            st.markdown(head_message_temp.format(df_a_d_t['title'][0],df_a_d_t['author'][0],df_a_d_t['postdate'][0],temp_reading_time),unsafe_allow_html=True)
            for i in range(0,len(df_title)):
                if type(df_title['img'][i]) != str and df_title['img'][i] != None:
                    test = np.frombuffer(df_title['img'][i], dtype=np.uint8)
                    opencv_image = cv2.imdecode(test, 1)
                    st.image(opencv_image, channels="BGR")
                elif type(df_title['article'][i]) == str and df_title['article'][i] != None:
                    st.markdown(full_message_temp.format(df_title['article'][i]),unsafe_allow_html=True)
            st.success("end of post")
    st.success("ispis potova izborom naslova !!! KRAJ KRAJ KRAJ !!!!!   ")



    st.warning("ISPIS POSTOVA OD AUTORA (JEDAN ILI VISE POSTOVA)  POČETAK !!! ")
    df_autor = pd.read_sql_query('SELECT author FROM blog_table_temp_MAIN',conn)
    temp_autor = df_autor['author'].unique() 

    title_autor =[]
    for i in temp_autor:
        title_autor.append(i)
    st.write(title_autor)

    st.write("Ispis naslova :: ")
    for i in title_autor:

        st.write(i)

    autor_temp = st.selectbox("Select title post", options= list(title_autor))
    if st.button("Submit author"):
        st.write("autor_temp",autor_temp)
        df_title_temp = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE author = "{}"'.format(autor_temp),conn)
        st.dataframe(df_title_temp)
        temp_user = df_title_temp['user_id'].unique() 
        user_lista =[]
        for i in temp_user:
            user_lista.append(i)
        df = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN',conn)
        df_new = df[['id_post','author','user_id','title','article','img','postdate']]
        a = df_new['id_post'].unique() 
        lista =[]
        for i in a:
            lista.append(i)
        for j in user_lista:
            df = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}"'.format(int(j)),conn)
            for i in lista:
                df_print = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}" AND id_post = "{}"'.format(int(j),int(i)),conn)
                df_a_d_t = pd.read_sql_query('SELECT DISTINCT title,author,postdate FROM blog_table_temp_MAIN WHERE user_id = "{}" AND id_post = "{}"'.format(int(j),int(i)),conn)
                if df_a_d_t.empty != True :
                    temp_reading_time = d.get(i)
                    st.write("temp_reading_time : ",temp_reading_time)

                    st.markdown(head_message_temp.format(df_a_d_t['title'][0],df_a_d_t['author'][0],df_a_d_t['postdate'][0],temp_reading_time),unsafe_allow_html=True)
                    for i in range(0,len(df_print)):
                        if type(df_print['img'][i]) != str and df_print['img'][i] != None:
                            test = np.frombuffer(df_print['img'][i], dtype=np.uint8)
                            opencv_image = cv2.imdecode(test, 1)
                            st.image(opencv_image, channels="BGR")
                        elif type(df_print['article'][i]) == str and df_print['article'][i] != None:
                            st.markdown(full_message_temp.format(df_print['article'][i]),unsafe_allow_html=True)
                    st.success("end of post")



    st.warning("ISPIS POSTOVA OD AUTORA (JEDAN ILI VISE POSTOVA)  KRAJ !!! ")













   