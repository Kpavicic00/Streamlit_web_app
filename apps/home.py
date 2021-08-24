
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
import altair as alt
from altair import Chart, X, Y, Axis, SortField, OpacityValue
from altair.expr import datum, if_
from vega_datasets import data
import altair as alt
from vega_datasets import data
from datetime import datetime
from html_temp import *
from plotnine import ggplot, aes, geom_line


def app():


    
    
    #st.subheader("This application is a free open source platform and provides a different amount of tools for process and visualise different datasets with football finance datas like transfers and income fees for clubs and leauges ")
    
    ############################################################
    ## 1. EFPA_BATCH.py -> Viusalisation TEST !!! Dashboard development 
    ##  --------------------------------------------------------

    
    # df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    

    #       Expend by player 

    #   ---------------------------------------------------------------
    ##      1. Graph 

    # nastaviti za sutra  !!!
    # df = pd.read_sql_query('SELECT * FROM CDWS_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"]]
    # df_new['Season']= pd.to_datetime(df_new['Season'],format='%Y')
    # df = df_new.nlargest(22,'Expenditures')
    # st.dataframe(df)

    # brush = alt.selection(type='interval')

    # points = alt.Chart(df).mark_point(size=200,filled=True).encode(
    #     x='Season',
    #     y='Inflacion_Expenditures',
    #     color=alt.condition(brush, 'Club', alt.value('lightgray'))
    # ).add_selection(
    #     brush
    # )

    # bars = alt.Chart(df).mark_bar().encode(
    #     y='Club',
    #     color='Club',
    #     x='sum(Inflacion_Expenditures)'
    # ).transform_filter(
    #     brush
    # )

    # st.write(points & bars)

    df1 = pd.read_sql_query('SELECT * FROM DCTAS_table WHERE user_id = "{}"'.format(1),conn)
    df_new1 = df1[["Order_of_Expend","Club","State","Competition","Expenditures","Income","Arrivals","Departures","Balance","inflation_Expenditure","inflation_Income","inflation_Balance"]]
    #df_new1['Season']= pd.to_datetime(df_new1['Season'],format='%Y')
    dff = df_new1.nlargest(10,'Expenditures')
    st.dataframe(dff)
    brush = alt.selection(type='interval')

    points = alt.Chart(dff).mark_point(size=200,filled=True).encode(
        x='Arrivals',
        y='Expenditures',
        color=alt.condition(brush, 'Club', alt.value('lightgray'))
    ).add_selection(
        brush
    )

    bars = alt.Chart(dff).mark_bar().encode(
        y='Club',
        color='Club',
        x='sum(Expenditures)'
    ).transform_filter(
        brush
    )

    st.write(points & bars)


















            