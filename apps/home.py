
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
from PIL import Image


def app():

    # Function to Read and Manupilate Images
    def load_image(img):
        im = Image.open(img)
        image = np.array(im)
        return image

    # Uploading the File to the Page
    uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png'])

    # Checking the Format of the page
    if uploadFile is not None:
        # Perform your Manupilations (In my Case applying Filters)
        img = load_image(uploadFile)
        st.image(img)
        st.write("Image Uploaded Successfully")
    else:
        st.write("Make sure you image is in JPG/PNG Format.")

    st.write("home")
    result = view_all_post()
    st.write(result)

    #username = return_username()
    i = (result[4])
    #res = str(''.join(map(str, i)))

    st.image(res)
    #df = pd.read_sql('SELECT * FROM CDWS_BATCH_table', conn)
    df = pd.read_sql_query('SELECT * FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    df_save = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"]]

    st.dataframe(df_save)
    brush = alt.selection(type='interval')

    points = alt.Chart(df_save).mark_point().encode(
        x='Arrivals',
        y='Expenditures',
        color=alt.condition(brush, 'Club', alt.value('lightgray'))
    ).add_selection(
        brush
    )

    bars = alt.Chart(df_save).mark_bar().encode(
        y='Club',
        color='Club',
        x='sum(Expenditures)'
    ).transform_filter(
        brush
    )

    st.write(points & bars)

    ###########################################################################
    ###########################################################################
    ###########################################################################

    nearest = alt.selection(type='single', nearest=True, on='mouseover',fields=['Expenditures'], empty='none')

    # The basic line
    line = alt.Chart(df_save).mark_line(interpolate='basis').encode(
        x='Arrivals',
        y='Expenditures',
        color='Club'
    )

    # Transparent selectors across the chart. This is what tells us
    # the x-value of the cursor
    selectors = alt.Chart(df_save).mark_point().encode(
        x='Arrivals',
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )

    # Draw points on the line, and highlight based on selection
    points = line.mark_point().encode(
        opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    )

    # Draw text labels near the points, and highlight based on selection
    text = line.mark_text(align='left', dx=5, dy=-5).encode(
        text=alt.condition(nearest, 'Expenditures', alt.value(' '))
    )

    # Draw a rule at the location of the selection
    rules = alt.Chart(df_save).mark_rule(color='gray').encode(
        x='Arrivals',
    ).transform_filter(
        nearest
    )

    # Put the five layers into a chart and bind the data
    a = alt.layer(
        line, selectors, points, rules, text
    ).properties(
        width=600, height=300
    )
    st.write(a)


   