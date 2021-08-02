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
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from League_functions.avg_Income_for_player_Departures import  BATCH_for_GetAVGExpendFORplayerArrivals
from functions import DataFrameFunc,NumberOfRows
from League_functions.EFPA_func import*
import matplotlib.pyplot as plt
import altair as alt
from bokeh.plotting import figure
import duckdb
import subprocess
coef = 'file.txt'

def app():
    st.subheader("LogIn")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password",type='password')
    if st.sidebar.checkbox("Login"):

        create_usertable()
        hashed_pswd = make_password(password)
        st.write("username",username)
        st.write("password",password)
        st.write("hashed_pswd",hashed_pswd)
        result = login_user(username,check_hashes(password,hashed_pswd))
        st.write("result",result)
        if result:
            st.success("Logged in as :: {}".format(username))
                
            task = st.selectbox("Task",["Add Posts","Metricss"],key='key123')

            if task == "Add Posts":
                st.subheader("Add Articles")
                

            elif task == "Metricss":
                st.subheader("Metricss")

                if st.checkbox("Metrics"):
                    st.title("Let's create a table!")
                    DFrame = DataFrameFunc('Ligaska_KONACAN_STAS.csv')
                    df = EFPA_MAIN(DFrame)
                    st.write(df)

                    # chart_data = pd.DataFrame(df,
                    #       columns=[c, '  Expend + Inflation by player|  '])
                    # st.bar_chart(chart_data)
                    #################################

                     
                    #df.plot(x="   Year of Season |  ", y=["  Expend + Inflation by player|  ","    Expend by player|  "])
                    #plt.show()
                    #st.pyplot()

                    # x = df['   Year of Season |  ']
                    # y = df['    Expend by player|  ']

                    # p = figure(

                    #     title='simple line example',
                    #     x_axis_label='x',
                    #     y_axis_label='y')

                    # p.line(x, y, legend_label='Trend', line_width=2)

                    # st.bokeh_chart(p, use_container_width=True)

                    # lines = alt.Chart(df).mark_line().encode(

                    #     x=alt.X('Season ',axis=alt.Axis(title='   Year of Season |  '))
                    #     #y=alt.Y('Expend',axis=alt.Axis(title='    Expend by player|  '))
                    # ).properties(
                    #     width=600,
                    #     height=300
                    # )
                    # st.altair_chart(lines)
                    # DFrame = DataFrameFunc('Ligaska_KONACAN_STAS.csv')
                    # df = EFPA_MAIN(DFrame)
                    # st.write(df)

                    #st.write(" : ",duckdb.query("SELECT * FROM df WHERE '' ").to_df())
                    # df.reset_index().plot(
                    # x="   Year of Season |  ", y=["    Expend by player|  ", "  Expend + Inflation by player|  "], kind="bar"
                    # )
                    # plt.title("Mince Pie Consumption 18/19")
                    # plt.xlabel("   Year of Season |  ")
                    # plt.ylabel("Expend")
                    # chart = alt.Chart(df).mark_line().encode(
                    #   x=alt.X('   Year of Season |  '),
                    #   y=alt.Y('value:Q'),
                    #   color=alt.Color("name:N")
                    # ).properties(title="Hello World")
                    # st.altair_chart(chart, use_container_width=True)
                #st.pyplot()
                    # y = df['    Expend by player|  ']
                    # x = df['   Year of Season |  ']
                    # plt.pie(x,y)
                    # plt.title("title")
                    # plt.ylabel("Expend by player")
                    # plt.xlabel("Year of Season")
                    # plt.show()


