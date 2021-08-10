from numpy.core.numeric import True_
import streamlit as st 
import pandas as pd
import numpy as np
from sqlite3.dbapi2 import paramstyle
import bcrypt
from functions import *
from database import *
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from League_functions.avg_Income_for_player_Departures import  BATCH_for_GetAVGExpendFORplayerArrivals
from functions import DataFrameFunc,NumberOfRows
from League_functions.EFPA_func import*
from League_functions.IFPD_func import*
from League_functions.BFPD_func import*
from League_functions.DFLS_func import*
from League_functions.DCWS_func import*
from Club_functions.CDWS_func import*
from Club_functions.CDTAS_func import*
import matplotlib.pyplot as plt
import altair as alt
from bokeh.plotting import figure
import duckdb
import subprocess
from html_temp import *
import os
import time

#################
from apps.login_pages import metrics, post
######################
import sqlite3
save_df = DataFrameFunc('datas/Ligaska_KONACAN_STAS.csv')
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()
# sqlite_table = "League_datas"
# save_df.to_sql(sqlite_table, con=conn, if_exists='fail')

fp_clubs = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
coef = 'file.txt'
fp_league = 'datas/Ligaska_KONACAN_STAS.csv'
save_csv_Expend = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
save_csv_Expend_BATCH = 'datas/BATCH_sportska_kubska_statsitika_OBRDENO.csv'

rem_niz_INCOME = []
rem_niz_BALANCE = []
rem_niz_SEASON = []
rem_niz_CLUB_SEASON = []
rem_niz_CLUB_TROUGHT_SEASON = []
df_empt = pd.DataFrame()
flag = 0
rem_niz_nizz = []



def app():

    

    st.subheader("LogIn")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password",type='password')
    if st.sidebar.checkbox("Login"):

        st.write("Log in as ::: ",username)
        create_usertable()
        st.write("username",username,"type(username)",type(username))
        temp_user()
        temp_add_user_data(username)
        hashed_pswd = make_password(password)
        result = login_user(username,check_hashes(password,hashed_pswd))

        #st.write("return_user_id :: ",return_user_idd)


        # return_user_idd = return_user_id(username)
        # i = (return_user_idd[0])
        # res = int(''.join(map(str, i)))
        # te = int(res)
        # delite_EFPA(te)
        # st.write(te,"te")
        # # printing result
        
        # st.write("Tuple to integer conversion : " + str(res))
        # st.write("type()",type(i),i,"type(te)",type(te))
        #create_EFPA()

        
        
        # f_datas = 'datas/exported/GetAVGExpendFORplayerArrivals.csv'
        # df = DataFrameFuncExpend(f_datas)
        # len_df = NumberOfRows(df)
        # # st.write("len(len_df)",(len_df))
        # size = len(df)
        # list1 = [0] *size
        
        # #st.write(ar_niz)
        # for i in range(0,size):
        #     list1[i] = te

        # my_array = np.array(list1)
        # st.write("type",type(my_array))
        # st.write(my_array)
        # for i in range(size):
        #     df = df.append({'A': i}, ignore_index=True)
        # df = pd.concat([pd.DataFrame([i], columns=['A']) for i in range(size)],
        #   ignore_index=True)
           
       
        #df["id_user"] = my_array
        # test= 'datas/exported/TEST_DATA_23432432432.csv' 
        # Write_multiple_DF(test,df)
        # address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
  

        # df['user_id'] = list1
        # st.dataframe(df)

        
        #conn = sqlite3.connect('data.db')
        #df.to_sql('EFPA_table',con=conn,if_exists='append')
        
        # df['Year']= pd.to_datetime(df['Year'],format='%Y')
        # #st.dataframe(df)
        # c = conn.cursor()
        # if c.fetchone()[0]==1 : 
	    #     st.write('Table exists.')
        # else :
	    #     st.write('Table does not exist.')
        #c = conn.cursor()
			
        #get the count of tables with the name
        c.execute('SELECT count(name) FROM sqlite_master WHERE type="table" AND name="EFPA_table"')

        #if the count is 1, then table exists
        if c.fetchone()[0]==1 : 
        	st.write('Table exists.')
        else :
        	st.write('Table does not exist.')
        
        
        # add_forien_key(return_user_idd)
        # #create_EFPA()
        # #df.to_sql(name='Users', con=conn)
        # #   EFPA_table
        # df.to_sql('EFPA_table',con=conn,if_exists='append')
        # conn.close()

        if result:
            # st.success("Logged in as :: {}".format(username))
                
            

            PAGES = {
                "Metrics": metrics,
                "Post": post
            }
            st.title('Meni')
            selection = st.radio("Go to", list(PAGES.keys()))
            page = PAGES[selection]
            page.app()
