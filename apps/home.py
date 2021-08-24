
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
    df = pd.read_sql_query('SELECT * FROM DCWS_table WHERE user_id = "{}"'.format(1),conn)
    df_new = df[["Year_of_Season","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season"]]
    df_new['Year_of_Season']= pd.to_datetime(df_new['Year_of_Season'],format='%Y')
    st.dataframe(df_new)


    base = alt.Chart(df_new).encode(
        alt.X('Year_of_Season', axis=alt.Axis(title=None))
    )

    area = base.mark_point(size=200,filled=True, color='#57A44C').encode(
        alt.Y('Expend',
              axis=alt.Axis(title='profit', titleColor='#57A44C')),
        #alt.Y2('Income')
        #size=alt.Size('count', scale=alt.Scale(range=[100, 500]))
    )

    line = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
        alt.Y('sum_of_Arrivlas',
              axis=alt.Axis(title='number of arrivals', titleColor='#5276A7'))
    )

    b = alt.layer(area, line).resolve_scale(
        y = 'independent'
    ).properties(
        width=700,
        height=400
    ).configure_point(
        size=500
    ).interactive()   
    st.write(b)
    
    #################################################
    #################################################
    #################################################

    source = data.seattle_weather()
    st.dataframe(source)

    base = alt.Chart(source).encode(
        alt.X('month(date):T', axis=alt.Axis(title=None))
    )


    area = base.mark_area(opacity=0.3, color='#57A44C').encode(
        alt.Y('average(temp_max)',
              axis=alt.Axis(title='Avg. Temperature (°C)', titleColor='#57A44C')),
        alt.Y2('average(temp_min)')
    )

    line = base.mark_line(stroke='#5276A7', interpolate='monotone').encode(
        alt.Y('average(precipitation)',
              axis=alt.Axis(title='Precipitation (inches)', titleColor='#5276A7'))
    )

    a = alt.layer(area, line).resolve_scale(
        y = 'independent'
    )
    st.write(a)
    
    # selector = alt.selection_single(empty='all', fields=['Name_of_Legue'])

    # #color_scale = alt.Scale(domain=['M', 'F'],range=['#1FC3AA', '#8624F5'])

    # base = alt.Chart(df_new).properties(
    #     width=250,
    #     height=250
    # ).add_selection(selector)

    # points = base.mark_point(filled=True, size=200).encode(
    #     x=alt.X('Expend',scale=alt.Scale(domain=[0,84])),
    #     y=alt.Y('sum_of_Arrivlas',scale=alt.Scale(domain=[0,250])),
    #     color=alt.condition(selector,'Name_of_Legue',alt.value('lightgray')))

    # hists = base.mark_bar(opacity=0.5, thickness=100).encode(
    #     x=alt.X('avg_Expend_Season',bin=alt.Bin(step=5),scale=alt.Scale(domain=[0,100])),
    #     y=alt.Y('avg_Expend_of_Arrivlas',stack=None,scale=alt.Scale(domain=[0,350])),
    #     color=alt.Color('Name_of_Legue')
    # ).transform_filter(
    #     selector
    # )

    # st.write(points | hists) # zakljucak ne radi testirati ensot drugo sto ne zahtjeva histogram !!!

    # test = alt.Chart(df_new).mark_circle().encode(
    #     alt.X('sum_of_Arrivlas', scale=alt.Scale(zero=False)),
    #     y='Expend',
    #     color='Name_of_Legue',
    #     facet=alt.Facet('Name_of_Legue', columns=1 ),
    # ).properties(
    #     width=200,
    #     height=100,
    # )
    # st.write(test)




    # selection1 = alt.selection_multi(fields=['Name_of_Legue'], bind='legend')
    # c = alt.Chart(df).mark_circle().encode(
    # alt.X('sum_of_Arrivlas', scale=alt.Scale(zero=True)),
    # alt.Y('Expend', scale=alt.Scale(zero=True, padding=5)),
    # alt.Color('Name_of_Legue', scale=alt.Scale(scheme='category20b')),
    # opacity=alt.condition(selection1, alt.value(1), alt.value(0.2)),
    # size='number_of_Season'
    # ).add_selection(
    #     selection1
    # ).properties(
    #     width = 700,
    #     height = 600
    # ).interactive()
    # st.altair_chart(c)


    # df = pd.read_sql_query('SELECT * FROM DCWS_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Year_of_Season","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season"]]
    # df_new['Year_of_Season']= pd.to_datetime(df_new['Year_of_Season'],format='%Y')
    # st.dataframe(df_new)
    # base = alt.Chart(df_new).mark_area(
    #     color='goldenrod',
    #     opacity=0.3
    # ).encode(
    #     x='Year_of_Season',
    #     y='Expend',
    # ).properties(
    #     width = 600,
    #     height = 400
    # )

    # brush = alt.selection_interval(encodings=['x'],empty='all')
    # background = base.add_selection(brush)
    # selected = base.transform_filter(brush).mark_area(color='goldenrod')
    # st.write(background + selected)
    # b = alt.Chart(df_new).mark_circle().encode(
    # alt.X('Year_of_Season'),
    # alt.Y('Expend',),
    # size='sum_of_Arrivlas'
    # )
    # st.write(b)
    ############################################

    #df = df_new.nlargest('Expend')
    #selection = alt.selection_multi(fields=['sum_of_Arrivlas'], bind='legend')
    
    # c = alt.Chart(df_new).mark_circle().encode(
    # alt.X('Year_of_Season', scale=alt.Scale(zero=True)),
    # alt.Y('Expend', scale=alt.Scale(zero=True, padding=5)),
    # # alt.Color('sum_of_Arrivlas', scale=alt.Scale(scheme='category20b')),
    # # opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
    # size='sum_of_Arrivlas'
    # ).properties(
    #     width = 600,
    #     height = 600
    # ).interactive()
    # st.write(c)



    












    # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
    # # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]

    # st.header("Graph 1.")

    # error_bars = alt.Chart(df_new).mark_errorbar(extent='ci').encode(
    #   x=alt.X('Expend_by_player', scale=alt.Scale(zero=False)),
    #   y=alt.Y('Year'),
    #   color =  'Year'
    # ).properties(
    #     width=600,
    #     height=500
    # ).interactive()

    # points = alt.Chart(df_new).mark_point(filled=True, color='black',size=90).encode(
    #   x=alt.X('Expend_by_player', aggregate='mean'),
    #   y=alt.Y('Year'),
    #   color =  'Year'
    # ).properties(
    #     width=600,
    #     height=500
    # ).interactive()

    # error_bars + points
    # st.write(error_bars + points)


    # st.header("Graph 2.")
    # test = alt.Chart(df_new).mark_circle(size=60).encode(
    #     #x='Expend_by_player',
    #     y=alt.Y('Expend_by_player', axis=alt.Axis(title=None)),
    #     x=alt.X('Nationality', axis=alt.Axis(labels=False,title=None)),
    #     color='Year'
    # ).properties(
    #     width=600,
    #     height=500
    # ).interactive()
    # st.write(test)

    # st.header("Graph 3.")
    # brush = alt.selection(type='interval')
    # points = alt.Chart(df_new).mark_point().encode(
    #     x=alt.X('Name_of_Legue', axis=alt.Axis(labels=False,title=None)),
    #     y=alt.Y('Expend_by_player', axis=alt.Axis( title='Expend by player')),
    #     color=alt.condition(brush, 'Year', alt.value('lightgray'))
    # ).add_selection(
    #     brush
    # ).properties(
    #     width=500,
    #     height=400)
    
    # bars = alt.Chart(df_new).mark_bar().encode(
    #     y=alt.Y('Year', axis=alt.Axis( title='Year')),
    #     color='Expend_by_player',
    #     x=alt.Y('Expend_by_player', axis=alt.Axis( title='Expend by player')),
    # ).transform_filter(
    #     brush
    # ).properties(
    #     width=500,
    #     height=100)
    
    # st.write(points & bars)

        # # Create a pie chart
    # plt.pie(
    #     # using data total)arrests
    #     df_new['Year'],
    #     # with the labels being officer names
    #     labels=df_new['Expend_by_player'],
    #     # with no shadows
    #     shadow=False,
    #     # with colors
    #     # colors=colors,
    #     # with one slide exploded out
    #     # explode=(0, 0, 0, 0, 0.15),
    #     # with the start angle at 90%
    #     startangle=90,
    #     # with the percent listed as a fraction
    #     autopct='%1.1f%%',
    #     )

    # # View the plot drop above
    # plt.axis('equal')

    # # View the plot
    # plt.tight_layout()
    # st.pyplot()

    # plt.pie(df_new['Year'],labels=df_new['Year'],autopct='%1.1f%%')
    # plt.title('My Tasks')
    # plt.axis('equal')
    # st.pyplot()

    # brush = alt.selection(type='interval')
    # points = alt.Chart(df_new).mark_point().encode(
    #     x=alt.X('Nationality', axis=alt.Axis(title='Nationality')),
    #     y=alt.Y('Expend_by_player', axis=alt.Axis( title='Expend by player')),
    #     color=alt.condition(brush, 'Year', alt.value('lightgray'))
    # ).add_selection(
    #     brush
    # ).properties(
    #     width=500,
    #     height=400
    # )
    
    # bars = alt.Chart(df_new).mark_bar().encode(
    #     y=alt.Y('Nationality', axis=alt.Axis( title='Nationality')),

    #     color='Year',
    #     x=alt.Y('Expend_by_player', axis=alt.Axis( title='Expend by player')),
    # ).transform_filter(
    #     brush
    # ).properties(
    #     width=500,
    #     height=100
    # )
    
    # st.write(points & bars)
    #   ---------------------------------------------------------------
    ##      1. Graph 
    # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    # brush = alt.selection(type='interval')
    # points = alt.Chart(df_new).mark_point().encode(
    #     x=alt.X('Name_of_Legue', axis=alt.Axis(labels=False)),
    #     y=alt.Y('Expend_by_player', axis=alt.Axis( title='Expend by player')),
    #     color=alt.condition(brush, 'Year', alt.value('lightgray'))
    # ).add_selection(
    #     brush
    # ).properties(
    #     width=500,
    #     height=400)
    
    # bars = alt.Chart(df_new).mark_bar().encode(
    #     y=alt.Y('Year', axis=alt.Axis( title='Year')),
    #     color='Expend_by_player',
    #     x=alt.Y('Expend_by_player', axis=alt.Axis( title='Expend by player')),
    # ).transform_filter(
    #     brush
    # ).properties(
    #     width=500,
    #     height=100)
    
    # st.write(points & bars)



    # ##      2. Graph 
    # # Create a selection that chooses the nearest point & selects based on x-value
    # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
    # # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    # nearest = alt.selection(type='single', nearest=True, on='mouseover',
    #                         fields=['Expend_by_player'], empty='none')

    # # The basic line
    # line = alt.Chart(df_new).mark_line(interpolate='basis').encode(
    #     x=alt.X('Year', axis=alt.Axis(title='Date')),
    #     y=alt.Y('Expend_by_player', axis=alt.Axis( title='Expend by player')),
    #     color='Name_of_Legue'
    # ).properties(
    #     width=700,
    #     height=600
    # )

    # # Transparent selectors across the chart. This is what tells us
    # # the x-value of the cursor
    # selectors = alt.Chart(df_new).mark_point().encode(
    #     x=alt.X('Year', axis=alt.Axis(title='Date')),
    #     y=alt.Y('Expend_by_player', axis=alt.Axis( title='Expend by player')),
    #     opacity=alt.value(0),
    # ).add_selection(
    #     nearest
    # ).properties(
    #     width=700,
    #     height=600
    # )

    # # Draw points on the line, and highlight based on selection
    # points = line.mark_point().encode(
    #     opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    # )

    # # Draw text labels near the points, and highlight based on selection
    # text = line.mark_text(align='left', dx=5, dy=-5).encode(
    #     text=alt.condition(nearest, 'Expend_by_player', alt.value(' '))
    # )

    # # Draw a rule at the location of the selection
    # rules = alt.Chart(df_new).mark_rule(color='gray').encode(
    #     x='Year',
    # ).transform_filter(
    #     nearest
    # ).properties(
    #     width=700,
    #     height=600
    # )

    # # Put the five layers into a chart and bind the data
    # a = alt.layer(
    #     line, selectors, points, rules, text
    # ).properties(
    #     width=700, height=300
    # )
    # st.write(a)

    # #   ---------------------------------------------------------------
    
    # ##      3. Graph 
    # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
    # # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')

    # highlight = alt.selection(type='single', on='mouseover',
    #                       fields=['Name_of_Legue'], nearest=True)

    # base = alt.Chart(df_new).encode(
    #     x=alt.X('Year', axis=alt.Axis(title='Date')),
    #     y=alt.Y('Expend_by_player', axis=alt.Axis( title='Expend by player')),
    #     color='Name_of_Legue'
    # )

    # points = base.mark_circle().encode(
    #     opacity=alt.value(0)
    # ).add_selection(
    #     highlight
    # ).properties(
    #     width=700, height=400
    # )

    # lines = base.mark_line().encode(
    #     size=alt.condition(~highlight, alt.value(1), alt.value(3))
    # )

    # points + lines
    # st.write(points + lines)

    #   ---------------------------------------------------------------



    # st.header("Expend by player + INFATION ")
    # #       Expend by player + INFATION 

    # #   ---------------------------------------------------------------
    # ##      1. Graph 
    # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
    # # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')

    # brush = alt.selection(type='interval')
    # points = alt.Chart(df_new).mark_point().encode(
    #     x=alt.X('Year', axis=alt.Axis(title='Date')),
    #     y=alt.Y('Expend_INFLACION', axis=alt.Axis( title='Expend by player + INFLACION')),
    #     color=alt.condition(brush, 'Name_of_Legue', alt.value('lightgray'))
    # ).add_selection(
    #     brush
    # ).properties(
    #     width=500,
    #     height=400
    # )
    
    # bars = alt.Chart(df_new).mark_bar().encode(
    #     y=alt.Y('Name_of_Legue', axis=alt.Axis( title='Name of Legue')),

    #     color='Name_of_Legue',
    #     x=alt.Y('Expend_INFLACION', axis=alt.Axis( title='Expend by player + INFLACION')),
    # ).transform_filter(
    #     brush
    # ).properties(
    #     width=500,
    #     height=100
    # )
    
    # st.write(points & bars)
    # st.success("Viusalise  Datas")
    # #   ---------------------------------------------------------------




    # ##      2. Graph 
    # # Create a selection that chooses the nearest point & selects based on x-value
    # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
    # # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    # nearest = alt.selection(type='single', nearest=True, on='mouseover',
    #                         fields=['Expend_INFLACION'], empty='none')

    # # The basic line
    # line = alt.Chart(df_new).mark_line(interpolate='basis').encode(
    #     x=alt.X('Year', axis=alt.Axis(title='Date')),
    #     y=alt.Y('Expend_INFLACION', axis=alt.Axis( title='Expend by player + INFLACION')),
    #     color='Name_of_Legue'
    # ).properties(
    #     width=700,
    #     height=600
    # )

    # # Transparent selectors across the chart. This is what tells us
    # # the x-value of the cursor
    # selectors = alt.Chart(df_new).mark_point().encode(
    #     x=alt.X('Year', axis=alt.Axis(title='Date')),
    #     y=alt.Y('Expend_INFLACION', axis=alt.Axis( title='Expend by player + INFLACION')),
    #     opacity=alt.value(0),
    # ).add_selection(
    #     nearest
    # ).properties(
    #     width=700,
    #     height=600
    # )

    # # Draw points on the line, and highlight based on selection
    # points = line.mark_point().encode(
    #     opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    # )

    # # Draw text labels near the points, and highlight based on selection
    # text = line.mark_text(align='left', dx=5, dy=-5).encode(
    #     text=alt.condition(nearest, 'Expend_INFLACION', alt.value(' '))
    # )

    # # Draw a rule at the location of the selection
    # rules = alt.Chart(df_new).mark_rule(color='gray').encode(
    #     x='Year',
    # ).transform_filter(
    #     nearest
    # ).properties(
    #     width=700,
    #     height=600
    # )

    # # Put the five layers into a chart and bind the data
    # a = alt.layer(
    #     line, selectors, points, rules, text
    # ).properties(
    #     width=700, height=300
    # )
    # st.write(a)

    # #   ---------------------------------------------------------------
    
    # ##      3. Graph 
    # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
    # # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    # df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')

    # highlight = alt.selection(type='single', on='mouseover',
    #                       fields=['Name_of_Legue'], nearest=True)

    # base = alt.Chart(df_new).encode(
    #     x=alt.X('Year', axis=alt.Axis(title='Date')),
    #     y=alt.Y('Expend_INFLACION', axis=alt.Axis( title='Expend by player + INFLACION')),
    #     color='Name_of_Legue'
    # )

    # points = base.mark_circle().encode(
    #     opacity=alt.value(0)
    # ).add_selection(
    #     highlight
    # ).properties(
    #     width=700, height=400
    # )

    # lines = base.mark_line().encode(
    #     size=alt.condition(~highlight, alt.value(1), alt.value(3))
    # )

    # points + lines
    # st.write(points + lines)

    #   ---------------------------------------------------------------

















            