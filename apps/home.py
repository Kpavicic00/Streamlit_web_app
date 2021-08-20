
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



def app():


    
    
    #st.subheader("This application is a free open source platform and provides a different amount of tools for process and visualise different datasets with football finance datas like transfers and income fees for clubs and leauges ")
    
    ############################################################
    ## 1. EFPA.py -> Viusalisation TEST !!! Dashboard development 
    ##  --------------------------------------------------------

    ##      1. Graph 
    df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(1),conn)
    df.columns.name = None
    #st.dataframe(df)
    df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    #df_new.rename_axis('x')
    #df_new.rename_axis('x').rename_axis('attributes', axis='columns')
    df_new.index.name = 'x'
    
    st.dataframe(df_new)
    st.write(df_new.index.names)

    #st.subheader("Visualization of player consumption with and without inflation rate")
    # <p>This application is a free open source platform and provides a different amount of tools for process and visualise different datasets with football finance datas like transfers and income fees for clubs and leauges</p>
    color_a='#3E00FF'
    a = 'Expend by player'

    st.markdown(html_vizaulazacija1,unsafe_allow_html=True)
    
    chartline1 = alt.Chart(df_new).mark_line(size=5,color='#297F87').encode(
         x=alt.X('Year', axis=alt.Axis(title='date')),
         y=alt.Y('sum(Expend_by_player)',axis=alt.Axis( title='Inflation rate'), stack=None),
         ).properties(
             width=800, 
             height=500
         ).interactive()
    chartline2 = alt.Chart(df_new).mark_line(size=5,color='#DF2E2E').encode(
         x=alt.X('Year', axis=alt.Axis(title='date')),
         y=alt.Y('sum(Expend_INFLACION)', axis=alt.Axis( title='Inflation rate'),stack=None)
         ).properties(
             width=800, 
             height=500
         ).interactive()
    st.altair_chart(chartline1 + chartline2)
    ##########################################################################################################

    
    ##      2. Graph 
    st.markdown(html_vizaulazacija2,unsafe_allow_html=True)
    st.subheader("Expend by year    :::::::::::::::::::::::::::::::::::::::::::::     Expend by year + INFLACION")

    col1,col2 = st.columns(2)
    with col1:
        df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(1),conn)
        df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]

        df_new["date2"] = pd.to_datetime(df["Year"]).dt.strftime("%Y-%m-%d")
        data_start = df_new["Year"].min()
        data_end = df_new["Year"].max()
        def timestamp(t):
          return pd.to_datetime(t).timestamp() * 1000


        slider2 = alt.binding_range(name='cutoff:', min=timestamp(data_start), max=timestamp(data_end))
        selector2 = alt.selection_single(name="SelectorName",fields=['cutoff'],bind=slider2,init={"cutoff": timestamp("2011-01-01")})

        abssa = alt.Chart(df_new).mark_bar(size=17).encode(
            x='Year',
            y=alt.Y('Expend_by_player',title =None),
            color=alt.condition(
                'toDate(datum.Year) < SelectorName.cutoff[0]',
              alt.value('red'), alt.value('blue')
            )
        ).properties(
            width=380,
        ).add_selection(
            selector2
        )
        st.write(abssa)
    with col2:
        df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(1),conn)
        df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]

        df_new["date2"] = pd.to_datetime(df["Year"]).dt.strftime("%Y-%m-%d")
        data_start = df_new["Year"].min()
        data_end = df_new["Year"].max()
        #st.write("data_start",data_start,"data_end",data_end)

        def timestamp(t):
          return pd.to_datetime(t).timestamp() * 1000


        slider2 = alt.binding_range(name='cutoff:', min=timestamp(data_start), max=timestamp(data_end))
        selector2 = alt.selection_single(name="SelectorName",fields=['cutoff'],bind=slider2,init={"cutoff": timestamp("2011-01-01")})

        abssa = alt.Chart(df_new).mark_bar(size=17).encode(
            x='Year',
            y=alt.Y('Expend_INFLACION',title =None),
            color=alt.condition(
                'toDate(datum.Year) < SelectorName.cutoff[0]',
              alt.value('red'), alt.value('blue')
            )
        ).properties(
            width=380,
        ).add_selection(
            selector2
        )
        st.write(abssa)
    ##########################################################################################################


    
    ##  --------------------------------------------------------
    
    # df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    #df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    #df["Year"] = pd.to_datetime(df["Year"]).dt.strftime("%Y-%m-%d")

    datelist = pd.date_range(datetime.today(), periods=100).tolist()

    rand = np.random.RandomState(42)

    df = pd.DataFrame({
        'xval': datelist,
        'yval': rand.randn(100).cumsum(),
    })
    st.dataframe(df)

    def timestamp(t):
      return pd.to_datetime(t).timestamp() * 1000

    slider = alt.binding_range(name='cutoff:', min=timestamp(min(datelist)), max=timestamp(max(datelist)))
    selector = alt.selection_single(name="SelectorName", fields=['cutoff'],
                                bind=slider,init={"cutoff": timestamp("2020-05-05")})

    a = alt.Chart(df).mark_point().encode(
        x='xval',
        y='yval',
        color=alt.condition(
            'toDate(datum.xval) < SelectorName.cutoff[0]',
            alt.value('red'), alt.value('blue')
        )
    ).add_selection(
        selector
    )
    st.write(a)

    #   ---------------------------------------------------------------
    df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    #df_new["Year"] = pd.to_datetime(df_new["Year"]).dt.strftime("%Y-%m-%d")

    st.dataframe(df_new)
    #df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    #df_new["Year"] = pd.to_datetime(df_new["Year"]).dt.strftime("%Y-%m-%d")

    # df_new["date2"] = pd.to_datetime(df["Year"]).dt.strftime("%Y-%m-%d")
    # data_start = df_new["Year"].min()
    # data_end = df_new["Year"].max()
    # st.write("data_start",data_start,"data_end",data_end)

    # def timestamp(t):
    #   return pd.to_datetime(t).timestamp() * 1000

    
    # slider2 = alt.binding_range(name='cutoff:', min=timestamp(data_start), max=timestamp(data_end))
    # selector2 = alt.selection_single(name="SelectorName",fields=['cutoff'],bind=slider2,init={"cutoff": timestamp("2011-01-01")})

    # abssa = alt.Chart(df_new).mark_bar(size=17).encode(
    #     x='Year',
    #     y='sum(Expend_by_player)',
    #     color=alt.condition(
    #         'toDate(datum.Year) < SelectorName.cutoff[0]',
    #       alt.value('red'), alt.value('blue')
    #     )
    # ).add_selection(
    #     selector2
    # )
    # st.write(abssa)


    #   ---------------------------------------------------------------



    # new_week= pd.to_datetime(df_new['Year'],format='%Y')
    # yearss = ('2000','2018')


    # lines = alt.Chart(df_new).mark_bar().encode(
    #      y=alt.X('Year',axis=alt.Axis(title='date')),
    #      x=alt.Y('Expend_by_player',axis=alt.Axis(title='value')),
    #      color = 'Year'
    # ).properties(
    #     width=600,
    #     height=300
    # )
    # def plot_animation(df_new):
    #     i = 2000
    #     lines = alt.Chart(df_new ).mark_bar().encode(
    #         y=alt.X('Year', axis=alt.Axis(title='date')),
    #         x=alt.Y('Expend_by_player',axis=alt.Axis(title='value')),
    #         color = 'Year'
    #     ).properties(

    #         width=600,
    #         height=300
    #     ) 
    #     return lines
    # N = df_new.shape[0] # number of elements in the dataframe
    # burst = 10      # number of elements (months) to add to the plot
    # size = burst     # size of the current dataset
    # line_plot = st.altair_chart(lines)
    # start_btn = st.button('Start')
    # if start_btn:
    #    for i in range(1,N):
    #       step_df = df_new.iloc[0:size]
    #       lines = plot_animation(step_df)
    #       line_plot = line_plot.altair_chart(lines)
    #       size = i + burst
    #       if size >= N: 
    #          size = N - 1
    #       time.sleep(0.1)

    # week = (2000,2018)

    # bars = alt.Chart(df_new).mark_bar().encode(
    #     x=alt.X('Expend_by_player'),
    #     y=alt.Y('Name_of_Legue')
    #     ).properties(
    #              width=650, 
    #              height=400
    #     )
    # bar_plot = st.altair_chart(bars)
    # def plot_bar_animated_altair(df_new,week):
    #     bars = alt.Chart(df_new).encode(
    #         x=X('Expend_by_player'), 
    #         y=Y('Name_of_Legue'),

    #         color=alt.Color('Name_of_Legue')).properties(
    #             width=650, 
    #             height=400
    #             )
        

    # if st.button('Cue Chart'):
    #     for week in df_new:
    #         # weekly_df -> this dataframe (sample shown above) contains
    #         # data for a particular week which is passed to
    #         # the 'plot_bar_animated_altair' function.
    #         # week -> Current week title, eg:-  2016-06-10

    #         bars = plot_bar_animated_altair(df_new,week)
    #         time.sleep(0.01) 

    #         bar_plot.altair_chart(bars)
    
    
    # This global variable 'bar_plot' will be used later on
    



        # a = interact(demo, i = widgets.Play(
        #     value=0,
        #     min=0,
        #     max=10,
        #     step=1,
        #     description=st.button("Press play"),
        #     disabled=False))



        # fig = plt.figure(figsize=(7,5))
        # axes = fig.add_subplot(1,1,1)
        # axes.set_ylim(0, 310)
        # plt.style.use("seaborn")

        # x, y1, y2, y3, y4 = [], [], [], [], []


        # lst1=[i if i<175 else 175 for i in range(300)]
        # lst2=[i if i<255 else 255 for i in range(300)]
        # lst3=[i if i<30 else 30 for i in range(300)]
    # lst4=[i if i<65 else 65 for i in range(300)

    # #palette = list(reversed(sns.color_palette("afmhot", 4).as_hex()))

    # def animate(i):
    #     y1=lst1[i]
    #     y2=lst2[i]
    #     y3=lst3[i]
    #     y4=lst4[i]

    #     plt.bar(range(4), sorted([y1,y2, y3, y4]))
    #     tick_lst=["one", "two", "three", "fourfive"]
    #     plt.xticks(np.arange(4), tick_lst)

    # plt.title("Some Title, Year: {} ".format(5000), color=("blue"))
    # ani = FuncAnimation(fig, animate, interval=10)
    # st.pyplot()



    # st.title("Dashboard")
    # df_new.set_index(['Year'])
    # load_da = bcr.load_dataset(df_new)
    # a = load_da.head(5)
    # st.dataframe(a2)


    # # a =  alt.Chart(df_new).mark_area(
    # #     line={'color':'darkgreen'},
    # #     color=alt.Gradient(
    # #         gradient='linear',
    # #         stops=[alt.GradientStop(color='white', offset=0),
    # #                alt.GradientStop(color='darkgreen', offset=1)],
    # #         x1=1,
    # #         x2=1,
    # #         y1=1,
    # #         y2=0
    # #     )
    # # ).encode(
    # #     alt.X('Year'),
    # #     alt.Y('sum(Expend_by_player)')
    # # ).properties(
    # #          width=800, 
    # #          height=600
    # #      )
    # # st.altair_chart(a)

    # # b =  alt.Chart(df_new).mark_line().encode(
    # #     alt.X('Year'),
    # #     alt.Y('sum(Expend_INFLACION)')
    # # ).properties(
    # #          width=800, 
    # #          height=600
    # #      )
    # # st.altair_chart(a+b)

    # # new graph animation 
    # # -------------------------------------------------------
    # # chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(

    # #     x=alt.X('Year', axis=alt.Axis(title='date')),
    # #     y=alt.Y('sum(Expend_by_player)',axis=alt.Axis(title='Expend by player')),
    # #     ).properties(
    # #          width=800, 
    # #          height=600
    # #     )

    # st.write("new graph animation ")
    # lines =  alt.Chart(df_new).mark_area(
    #     line={'color':'darkgreen'},
    #     color=alt.Gradient(
    #         gradient='linear',
    #         stops=[alt.GradientStop(color='white', offset=0),
    #                alt.GradientStop(color='darkgreen', offset=1)],
    #         x1=1,
    #         x2=1,
    #         y1=1,
    #         y2=0
    #     )
    # ).encode(
    #     alt.X('Year'),
    #     alt.Y('sum(Expend_by_player)')
    # ).properties(
    #          width=700, 
    #          height=500
    #      )

    
                                  
    # def plot_animation(df_new):
    #     lines =  alt.Chart(df_new).mark_area(

    #         line={'color':'darkgreen'},
    #         color=alt.Gradient(
    #             gradient='linear',
    #             stops=[alt.GradientStop(color='white', offset=0),
    #                    alt.GradientStop(color='darkgreen', offset=1)],
    #             x1=1,
    #             x2=1,
    #             y1=1,
    #             y2=0
    #         )
    #     ).encode(
    #         alt.X('Year'),
    #         alt.Y('sum(Expend_by_player)')
    #     ).properties(
    #              width=700, 
    #              height=500
    #         )
    #     return lines
    # N = df_new.shape[0] # number of elements in the dataframe
    # burst = 2       # number of elements (months) to add to the plot
    # size = burst    # size of the current dataset
    # line_plot = st.altair_chart(lines)
    # line_plot
    # start_btn = st.button('Start',key='123')
    # if start_btn:
    #     for i in range(1,N):
    #         step_df = df_new.iloc[0:size]       
    #         lines = plot_animation(step_df)
    #         line_plot = line_plot.altair_chart(lines)
    #         size = i + burst
    #         if size >= N:
    #             size = N - 1  
    #         time.sleep(0.1)
    # # -------------------------------------------------------

    # # a = alt.Chart(df_new).mark_line(size=12,color='blue').encode(

    # #     #y='sum(Expend_by_player)',
    # #     y=alt.Y("sum(Expend_by_player)"),
    # #     x='Year',
    # #     color='sum(Expend_by_player)'
    # #     # row='Nationality'
    # # ).properties(
    # #          width=800, 
    # #          height=600
    # #      )
    # # b = alt.Chart(df_new).mark_line(size=12,color='red').encode(

    # #     #y='sum(Expend_by_player)',
    # #     y=alt.Y("sum(Expend_INFLACION)"),
    # #     x='Year',
    # #     color='sum(Expend_INFLACION)'
    # #     # row='Nationality'
    # # ).properties(
    # #          width=800, 
    # #          height=600
    # #      )
    # # st.altair_chart(a+b)




    # # plt.rcdefaults()
    # # fig, ax = plt.subplots()

    # # # Example data
    # # people = ('Spain', 'France', 'Germany', 'England', 'Italy')
    # # y_pos = df_new["Expend_by_player"]
    # # performance = df_new['Year']
    # # #3 + 10 * np.random.rand(len(people))
    # # #error = np.random.rand(len(people))

    # # ax.barh(y_pos, performance, align='center')
    # # ax.set_yticks(y_pos)
    # # ax.set_yticklabels(people)
    # # ax.invert_yaxis()  # labels read top-to-bottom
    # # ax.set_xlabel('Performance')
    # # ax.set_title('How fast do you want to go today?')
    # # st.pyplot()





    # # plt.plot('Year', 'Expend_by_player', data=df_new)
    # #st.pyplot()
    df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(1),conn)
    df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
    df_new["Year"] = pd.to_datetime(df_new["Year"]).dt.strftime("%Y-%m-%d")

    # chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(
    #      x=alt.X('Year', axis=alt.Axis(title='date')),
    #      y=alt.Y('sum(Expend_by_player)',axis=alt.Axis(title='Expend by player')),
    #      ).properties(
    #          width=800, 
    #          height=600
    #      )
    # chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
    #     # 
    #      x=alt.X('Year', axis=alt.Axis(title='date')),
    #      y=alt.Y('sum(Expend_INFLACION)',axis=alt.Axis(title='Expend_INFLACION')),
    #      ).properties(
    #          width=800, 
    #          height=600
    #      )
    # # 
    # st.altair_chart(chartline1 + chartline2)                                
    lines = alt.Chart(df_new).mark_bar(size=25).encode(
      y=alt.X('Name_of_Legue',axis=alt.Axis(title='date')),
      x=alt.Y('Expend_by_player',axis=alt.Axis(title='value'))
      ).properties(
          width=600,
          height=300
      )
    def plot_animation(df_new):
        lines = alt.Chart(df_new).mark_bar(size=25).encode(
        y=alt.X('Name_of_Legue', axis=alt.Axis(title='date')),
        x=alt.Y('sum(Expend_by_player)',axis=alt.Axis(title='value')),
        #color = "Year",
        #column = "Nationality" ,
        ).properties(
            width=600, 
            height=300
        )
        return lines
    N = df_new.shape[0] # number of elements in the dataframe
    burst = 1       # number of elements (months) to add to the plot
    size = burst    # size of the current dataset
    line_plot = st.altair_chart(lines)
    line_plot
    start_btn = st.button('Start')
    if start_btn:
        for i in range(1,N):
            step_df = df_new.iloc[0:size]       
            lines = plot_animation(step_df)
            line_plot = line_plot.altair_chart(lines)
            size = i + burst
            if size >= N:
                size = N - 1  
            time.sleep(0.8)


















            