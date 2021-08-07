
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
    
    #create_EFPA()

    # f_datas = 'datas/exported/GetAVGExpendFORplayerArrivals.csv'
    # df = DataFrameFuncExpend(f_datas)
    # df['Year']= pd.to_datetime(df['Year'],format='%Y')
    # #st.dataframe(df)
    # conn = sqlite3.connect('data.db', check_same_thread=False)
    # #create_EFPA()
    # #df.to_sql(name='Users', con=conn)
    # #   EFPA_table
    # df.to_sql('EFPA_table',con=conn,if_exists='append')
    # conn.close()
    #c = conn.cursor()
    # df.to_sql(name='Users', con=conn)
    # conn.close()

    # conn.execute('SELECT plot_id FROM plots WHERE plot_type="Control"')
    # cur = conn.cursor()

    # The result of a "cursor.execute" can be iterated over by row
    # df_read = pd.read_sql('SELECT * FROM Users', conn)
    # #c.fetchall()
    # st.dataframe(df_read)
    # Be sure to close the connection
    #c.close()
    # if st.checkbox("Viusalize data "):
    #     # Build an empty graph
    #     lines = alt.Chart(df_read).mark_bar(size=25).encode(
    #       x=alt.X('Year',axis=alt.Axis(title='date')),
    #       y=alt.Y('Expend_by_player',axis=alt.Axis(title='value'))
    #       ).properties(
    #           width=600,
    #           height=300
    #       )
    #     def plot_animation(df_read):
    #         lines = alt.Chart(df_read).mark_bar(size=25).encode(
    #         x=alt.X('Year', axis=alt.Axis(title='date')),
    #         y=alt.Y('Expend_by_player',axis=alt.Axis(title='value')),
    #         ).properties(
    #             width=600, 
    #             height=300
    #         )
    #         return lines

    #     N = df_read.shape[0] # number of elements in the dataframe
    #     burst = 6       # number of elements (months) to add to the plot
    #     size = burst    # size of the current dataset

    #     line_plot = st.altair_chart(lines)
    #     start_btn = st.button('Start')

    #     if start_btn:
    #         for i in range(1,N):
    #             step_df = df_read.iloc[0:size]       
    #             lines = plot_animation(step_df)
    #             line_plot = line_plot.altair_chart(lines)
    #             size = i + burst
    #             if size >= N:
    #                 size = N - 1  
    #             time.sleep(0.2)


    # chartline1 = alt.Chart(df).mark_bar(size=22,color='blue').encode(

    #     # x=df['Year'],
    #     # y=df['Nationality'],
    #     x=alt.X('Year', axis=alt.Axis(title='date')),
    #     y=alt.Y('Expend_by_player',axis=alt.Axis(title='Expend by player')),
    #     # color='Expend_by_player',
    #     # size='Expend_by_player'
    #     ).properties(

    #         width=800, 
    #         height=600
    #     )

    # chartline2 = alt.Chart(df).mark_bar(size=12,color='red').encode(

    #     # x=df['Year'],
    #     # y=df['Nationality'],
    #     x=alt.X('Year', axis=alt.Axis(title='date')),
    #     y=alt.Y('Expend_INFLACION',axis=alt.Axis(title='Expend_INFLACION')),
    #     # color='Expend_INFLACION',
    #     # size='Expend_INFLACION'
    #     ).properties(

    #         width=800, 
    #         height=600
    #     )
    # st.altair_chart(chartline1 + chartline2)

