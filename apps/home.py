
from numpy.core.numerictypes import _typedict
import streamlit as st 
import pandas as pd
import numpy as np
from sqlite3.dbapi2 import paramstyle
#import bcrypt
from functions import check_email,make_password,check_hashes,GETCoefficients,remove_duplicates
from database import create_usertable,add_user_data,check_double_email,check_double_username,login_user,check_userdatatable
#import datetime
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
#import sqlite3
#import time
from database import*

import os
import altair as alt
import duckdb
import streamlit.components.v1 as components
import sqlite3
import os
#import bar_chart_race as bcr
#import base64
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
import pandas as pd



def app():
    create_post_table_temp_MAIN()
    # conn = sqlite3.connect('data_new.db', check_same_thread=False)
    # c = conn.cursor()
    # path_file = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
    # def DataFrameFuncClubs(filePath):

    #     colls = ["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]
    #     dat = pd.read_csv(filePath,header = None , names = colls)
    #     return dat
    # # def DataFrameFunc(filePath):

    # # #     colls = ["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]
    # # #     dat = pd.read_csv(filePath,header = None , names = colls)
    # # #     return dat
    # save_df = DataFrameFuncClubs(path_file)
    # sqlite_table = "Clubs_datas"
    # save_df.to_sql(sqlite_table, con=conn, if_exists='fail')


    #st.title('View all posts !!!')
    a = " Welcome to the Football data revolution !!"
    b = " Here you are chance to investigate and explore football financial data about leagues and clubs across Europe and the World"
    c = " Data are collected by Transfmarket.com and data records by the Expenditures of top 100 clubs every season and top 25/26 Leagues by Expenditures"
    d = " With expending by club or league are recorded how many players come or leave club and league, also recorded Profit and revenue or income"
    e = " We take the coefficient of inflation and calculate for every cash transfer and thus have the opportunity to see the role we call the ‘inflation rate’ and see the monetary amount and the real value of a monetary transaction that took place 15 or more years ago."
    p = " We hope you enjoy and indulge your research imagination, also here you can explore, prove and argue your theses. We’ve provided you with interactive graos, data processing tools that handle a bunch and a bunch of different data, and allowed you to create your own post and share your thoughts with us. To use our software you need to register and log in, and the fun begins"
    
    powerd_by_datavision = "Powerd by Data.Vision"
    st.markdown(home_message.format(a,b,c,d,e,p,powerd_by_datavision),unsafe_allow_html=True)

    if st.checkbox(" Read some post !! "):
        a  = return_post_id_temp_MAIN()
        dfsve = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN',conn)
        df_user = pd.read_sql_query('SELECT DISTINCT user_id FROM blog_table_temp_MAIN',conn)
        temp_user = df_user['user_id'].unique() 
        df_post = pd.read_sql_query('SELECT DISTINCT id_post FROM blog_table_temp_MAIN',conn)
        temp_post = df_post['id_post'].unique() 
        post_lista =[]
        for i in temp_post:
            post_lista.append(i)


        user_lista =[]
        for i in temp_user:
            user_lista.append(i)
        d = {}
        for i in user_lista:
            for j in post_lista:
                df = pd.read_sql_query('SELECT author,read_time FROM blog_table_temp_MAIN WHERE id_post = "{}"'.format(int(j)),conn)
                Total = df['read_time'].sum()
                add_if_key_not_exist(d,j,Total)


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
                    st.markdown(head_message_temp.format(df_a_d_t['title'][0],df_a_d_t['author'][0],df_a_d_t['postdate'][0],temp_reading_time),unsafe_allow_html=True)
                    for i in range(0,len(df_print)):
                        if type(df_print['img'][i]) != str and df_print['img'][i] != None:
                            test = np.frombuffer(df_print['img'][i], dtype=np.uint8)
                            opencv_image = cv2.imdecode(test, 1)
                            st.image(opencv_image, channels="BGR")
                        elif type(df_print['article'][i]) == str and df_print['article'][i] != None:
                            st.markdown(full_message_temp.format(df_print['article'][i]),unsafe_allow_html=True)


        caching.clear_cache()

    if st.checkbox(" Take look and see some awesome interactive dashboard !! "):
        st.info("Still update !!!")












   