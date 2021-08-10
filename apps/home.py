
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

def app():
    st.write("home")

    df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(1),conn)
    df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')

    st.dataframe(df_new)

    subsetdf = df_new["Name_of_Legue"]
    subsetdf.set_index("Year",inplace=True)
    cum_sum_df = subsetdf.cumsum(axis=0)
    dada_Ada=cum_sum_df.cumsum(axis = 0)

    # bcr.bar_chart_race(df=dada_Ada, filename='covid19_horiz.mp4', figsize = (3.5,3),title='COVID-19 Cases by Country')
    #dada_Ada=cum_sum_df.cumsum(axis = 0)
    bcr.bar_chart_race(df=dada_Ada,figsize = (3.5,3),title='COVID-19 Cases by Country')
    #ata_deaths.set_index("date", inplace = True)
    # a = cum_sum_df.tail(10)
    # pritn(a)


    # x = alt.Chart(df_new).mark_bar().encode(

    #     x='Year',
    #     y="year:O"
    #     ).properties(height=700)
    
    

