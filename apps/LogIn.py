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
                
            task = st.radio("task op",["Add Posts","Metricss"],key='key123')

            if task == "Add Posts":
                st.subheader("Add Articles")
                

            elif task == "Metricss":

                st.subheader("Metricss")
                task_options = st.selectbox("Chose ",[" choose ","Leauges","Clubs"])
                if task_options == "Leauges":
                    st.write(" Leauges ")
                    task = st.selectbox("task op",["Processed Data by average league EXPEND for player ARRIVALS","BATCH Data by average league EXPEND for player ARRIVALS","Processed Data by average league INCOME for player DEPARTURES","BATCH Data by average league INCOME for player DEPARTURES","Processed Data by average league BALANCE for player DEPARTURES","BATCH Data by average league BALANCE for player DEPARTURES","Processed Data by average LEAGUE by AVG SESONS statistic","BATCH Data by average LEAGUE by AVG SESONS statistic","Processed Data by average -> LEAGUE by YEAR statistic","BATCH Data by average -> LEAGUE by YEAR statistic"],key='key123dsa')                        
                    if task == "Processed Data by average league EXPEND for player ARRIVALS":

                        col1,col2 = st.beta_columns(2)
                        with col1:
                                                
                            st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            if st.checkbox("Process data "):

                                df = pd.read_sql('SELECT * FROM League_datas', conn)
                                df_new = df[["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]]
                                st.dataframe(df_new)
                                a_leuge_DF = EFPA_base(df_new)
                                my_form = st.form(key = "form123")
                                submit = my_form.form_submit_button(label = "Submit")
                                if submit:

                                    st.success("Datas processes  :  ")

                                my_form_save = st.form(key = "form1")
                                st.info("For process data you must save data to database")
                                submit = my_form_save.form_submit_button(label = "Save data")
                                if submit:
                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)

                                    flag = return_id_EFPA_table(te)
                                    if flag == []:
                                        
                                        df = a_leuge_DF
                                        size = NumberOfRows(df)
                                        size = len(df)
                                        list1 = [0] *size


                                        for i in range(0,size):
                                            list1[i] = te
                                        df['user_id'] = list1
                                        create_EFPA()
                                        df.to_sql('EFPA_table',con=conn,if_exists='append')
                                        st.success("Data successfuly saved !")
                                    else:
                                        st.warning("Please first delite your records from database !!")
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:                                
                                if submit:

                                    return_user_idd = return_user_id(username)
                                    (return_user_idd)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)
                                    flag = return_id_EFPA_table(te)
                                    if flag != []:
                                        if int(te) > 0:
                                            df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(te),conn)
                                            df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
                                            st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                                            st.success("Export Datas")
                                    else:
                                        st.warning("file not found")
                                        st.info("Please procces data again !!")



                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:

                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = (return_id_EFPA_table(te))                               
                                if flag != []:
                                    if int(te) > 0:

                                        delite_EFPA(te)
                                        st.success("Delite Datas")
                                        st.info("Please procces data")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")

                            if st.checkbox("Viusalise data !!!"):
                                # Viusalise datas
                                        
                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = return_id_EFPA_table(te)
                                if flag != []:
                                    if int(te) > 0:
                                        df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(te),conn)
                                        df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
                                        df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
                                        chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(

                                             x=alt.X('Year', axis=alt.Axis(title='date')),
                                             y=alt.Y('Expend_by_player',axis=alt.Axis(title='Expend by player')),
                                             ).properties(

                                                 width=800, 
                                                 height=600
                                             )

                                        chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
                                            
                                             x=alt.X('Year', axis=alt.Axis(title='date')),
                                             y=alt.Y('Expend_INFLACION',axis=alt.Axis(title='Expend_INFLACION')),

                                             ).properties(

                                                 width=800, 
                                                 height=600
                                             )
                                        st.altair_chart(chartline1 + chartline2)                                    

                                        lines = alt.Chart(df_new).mark_bar(size=25).encode(
                                          x=alt.X('Year',axis=alt.Axis(title='date')),
                                          y=alt.Y('Expend_by_player',axis=alt.Axis(title='value'))
                                          ).properties(
                                              width=600,
                                              height=300
                                          )
                                        def plot_animation(df_new):
                                            lines = alt.Chart(df_new).mark_bar(size=25).encode(
                                            x=alt.X('Year', axis=alt.Axis(title='date')),
                                            y=alt.Y('Expend_by_player',axis=alt.Axis(title='value')),
                                            ).properties(
                                                width=600, 
                                                height=300
                                            )
                                            return lines
                                        N = df_new.shape[0] # number of elements in the dataframe
                                        burst = 6       # number of elements (months) to add to the plot
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
                                                time.sleep(0.1)
                                        st.success("Viusalise  Datas")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")

                    elif task == "BATCH Data by average league EXPEND for player ARRIVALS":

                        
                        col1,col2 = st.beta_columns(2)
                        with col1:                        
                            if st.checkbox("Test"):
                                #   df_save = pd.DataFrame()
                                st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            # to_append = [5, 6]
                            # a_series = pd.Series(to_append, index = df.columns)
                            # df = df.append(a_series, ignore_index=True)
                                if st.checkbox("Process data "):
                                    create_EFPA_BATCH_temp()

                                    df = pd.read_sql('SELECT * FROM League_datas', conn)
                                    df_new = df[["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]]
                                    to_append,rememmberr = EFPA_MAIN(df_new)
                                    columns = ["Order_of_Expend","Club","State","Competition","Expenditures","Income","Arrivals","Departures","Balance","inflation_Expenditure","inflation_Income","inflation_Balance"]    
                                    #st.dataframe(df_new)
                                    #a_leuge_DF = EFPA_MAIN(df_new)
                                    my_form = st.form(key = "form123")
                                    submit = my_form.form_submit_button(label = "Submit")
                                    if submit:
                                        
                                        columns = ["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]
                                        st.dataframe(to_append)
                                        #a_series = pd.Series(to_append)
                                        #to_append = df_save.append(to_append)
                                        to_append.to_sql('EFPA_BATCH_temp',con=conn,if_exists='append')

                                        #st.dataframe(df_save)
                                        st.success("Datas processes  :  ")
                                        #a_series = pd.Series(df_test,index = df.columns)
                                        # df = df.append(df_test, ignore_index=True)
                                        # st.dataframe(df)
                                        

                                # my_form_save = st.form(key = "form1")
                                # st.info("For process data you must save data to database")
                                # submit = my_form_save.form_submit_button(label = "Save data")
                                # if submit:
                                #     return_user_idd = return_user_id(username)
                                #     i = (return_user_idd[0])
                                #     res = int(''.join(map(str, i)))
                                #     te = int(res)

                                #     flag = return_id_EFPA_BATCH(te)
                                #     if flag == []:

                                #         df = a_leuge_DF
                                #         size = NumberOfRows(df)
                                #         size = len(df)
                                #         list1 = [0] *size


                                #         for i in range(0,size):
                                #             list1[i] = te
                                #         df['user_id'] = list1
                                #         create_EFPA_BATCH()
                                #         df.to_sql('EFPA_BATCH_table',con=conn,if_exists='append')
                                #         st.success("Data successfuly saved !")
                                #     else:
                                #         st.warning("Please first delite your records from database !!")

                            # # Export datas
                            # form_export_csv = st.form(key = "export_form")
                            # submit = form_export_csv.form_submit_button(label = "Export datas")
                            # if submit:                                
                            #     if submit:

                            #         return_user_idd = return_user_id(username)
                            #         (return_user_idd)
                            #         i = (return_user_idd[0])
                            #         res = int(''.join(map(str, i)))
                            #         te = int(res)
                            #         flag = return_id_EFPA_table(te)
                            #         if flag != []:
                            #             if int(te) > 0:
                            #                 df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(te),conn)
                            #                 df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
                            #                 st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                            #                 st.success("Export Datas")
                            #         else:
                            #             st.warning("file not found")
                            #             st.info("Please procces data again !!")



                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:

                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = (return_id_EFPA_table(te))                               
                                if flag != []:
                                    if int(te) > 0:

                                        delite_EFPA(te)
                                        st.success("Delite Datas")
                                        st.info("Please procces data")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")
                            
                    elif task == "Processed Data by average league INCOME for player DEPARTURES":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                                                
                            st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            if st.checkbox("Process data "):

                                df = pd.read_sql('SELECT * FROM League_datas', conn)
                                df_new = df[["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]]
                                st.dataframe(df_new)
                                a_leuge_DF = IFPD_base(df_new)
                                create_IFPD()
                                my_form = st.form(key = "form123")
                                submit = my_form.form_submit_button(label = "Submit")
                                if submit:
                                   
                                    st.success("Datas processes  :  ")

                                my_form_save = st.form(key = "form1")
                                st.info("For process data you must save data to database")
                                submit = my_form_save.form_submit_button(label = "Save data")
                                if submit:
                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)

                                    flag = return_id_IFPD_table(te)
                                    if flag == []:
                                        
                                        df = a_leuge_DF
                                        size = NumberOfRows(df)
                                        #st.dataframe()
                                        size = len(df)
                                        list1 = [0] *size

                                        for i in range(0,size):
                                            list1[i] = te
                                        df['user_id'] = list1
                                        
                                        df.to_sql('IFPD_table',con=conn,if_exists='append')
                                        st.success("Data successfuly saved !")
                                    else:
                                        st.warning("Please first delite your records from database !!")
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:                                
                                if submit:

                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)
                                    flag = return_id_IFPD_table(te)
                                    if flag != []:
                                        if int(te) > 0:
                                            df = pd.read_sql_query('SELECT * FROM IFPD_table WHERE user_id = "{}"'.format(te),conn)
                                            df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
                                            st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                                            st.success("Export Datas")
                                    else:
                                        st.warning("file not found")
                                        st.info("Please procces data again !!")



                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:

                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = return_id_IFPD_table(te)
                                if flag != []:
                                    if int(te) > 0:
                                        delite_IFPD(te)
                                        st.success("Delite Datas")
                                        st.info("Please procces data")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")

                            if st.checkbox("Viusalise data !!!"):
                                # Viusalise datas
                                        
                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = return_id_IFPD_table(te)
                                if flag != []:
                                    if int(te) > 0:
                                        # data visualisation !!!
                                        df = pd.read_sql_query('SELECT * FROM IFPD_table WHERE user_id = "{}"'.format(te),conn)
                                        df_new = df[["Name_of_Legue","Year","Nationality","Income_by_player","Income_INFLACION"]]
                                        df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
                                        #st.dataframe(df_new)
                                        chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(


                                             x=alt.X('Year', axis=alt.Axis(title='date')),
                                             y=alt.Y('Income_by_player',axis=alt.Axis(title='Income by player')),

                                             ).properties(

                                                 width=800, 
                                                 height=600
                                             )

                                        chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
                                            
                                             # x=df['Year'],
                                             # y=df['Nationality'],
                                             x=alt.X('Year', axis=alt.Axis(title='date')),
                                             y=alt.Y('Income_INFLACION',axis=alt.Axis(title='Income_INFLACION')),
                                             # color='Expend_INFLACION',
                                             # size='Expend_INFLACION'
                                             ).properties(

                                                 width=800, 
                                                 height=600
                                             )
                                        st.altair_chart(chartline1 + chartline2)                                    

                                        # Build an empty graph
                                        lines = alt.Chart(df_new).mark_bar(size=25).encode(
                                          x=alt.X('Year',axis=alt.Axis(title='date')),
                                          y=alt.Y('Income_by_player',axis=alt.Axis(title='value'))
                                          ).properties(
                                              width=600,
                                              height=300
                                          )
                                        def plot_animation(df_new):
                                            lines = alt.Chart(df_new).mark_bar(size=25).encode(
                                            x=alt.X('Year', axis=alt.Axis(title='date')),
                                            y=alt.Y('Income_by_player',axis=alt.Axis(title='value')),
                                            ).properties(
                                                width=600, 
                                                height=300
                                            )
                                            return lines
                                        N = df_new.shape[0] # number of elements in the dataframe
                                        burst = 6       # number of elements (months) to add to the plot
                                        size = burst    # size of the current dataset
                                        line_plot = st.altair_chart(lines)
                                        start_btn = st.button('Start')
                                        if start_btn:
                                            for i in range(1,N):
                                                step_df = df_new.iloc[0:size]       
                                                lines = plot_animation(step_df)
                                                line_plot = line_plot.altair_chart(lines)
                                                size = i + burst
                                                if size >= N:
                                                    size = N - 1  
                                                time.sleep(0.1)
                                        st.success("Viusalise  Datas")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")           
                        
                    elif task == "BATCH Data by average league INCOME for player DEPARTURES":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                            
                            rem_niz_BALANCE = []
                            if st.checkbox("Process data "):
                                
                                st.info(" For restart data you must delete data and start over !!!")
                                # Submit data 
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetAVGIncomeFORplayerDepartures.csv'                           
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF_B,rememmber = IFPD_MAIN(leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")                               
                                if submit:                            
                                    rem_niz_BALANCE.append(rememmber)
                                    Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)

                                    st.dataframe(DataFrameFuncIncome(save_csv_Expend_BATCH))
                                    st.write("Youe Choose : ")
                                    for i in range(0,len(rem_niz_BALANCE)):
                                        st.write(i+1," ::: ",rem_niz_BALANCE[i])

                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetAVGIncomeFORplayerDepartures'
                                    
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                        st.markdown(get_table_download_link_csv(DataFrameFuncIncome(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")

                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetAVGIncomeFORplayerDepartures'
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                    os.remove(save_csv_Expend_BATCH)
                                    del rem_niz_BALANCE
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")
                        
                    elif task == "Processed Data by average league BALANCE for player DEPARTURES":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                                                
                            st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            if st.checkbox("Process data "):

                                df = pd.read_sql('SELECT * FROM League_datas', conn)
                                df_new = df[["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]]
                                st.dataframe(df_new)
                                a_leuge_DF = BFPD_base(df_new)
                                create_BFPD()
                                my_form = st.form(key = "form123")
                                submit = my_form.form_submit_button(label = "Submit")
                                if submit:
                                   
                                    st.success("Datas processes  :  ")

                                my_form_save = st.form(key = "form1")
                                st.info("For process data you must save data to database")
                                submit = my_form_save.form_submit_button(label = "Save data")
                                if submit:
                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)

                                    flag = return_id_BFPD_table(te)
                                    if flag == []:
                                        
                                        df = a_leuge_DF
                                        size = NumberOfRows(df)
                                        #st.dataframe()
                                        size = len(df)
                                        list1 = [0] *size

                                        for i in range(0,size):
                                            list1[i] = te
                                        df['user_id'] = list1
                                        
                                        df.to_sql('BFPD_table',con=conn,if_exists='append')
                                        st.success("Data successfuly saved !")
                                    else:
                                        st.warning("Please first delite your records from database !!")
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:                                
                                if submit:

                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)
                                    flag = return_id_BFPD_table(te)
                                    if flag != []:
                                        if int(te) > 0:
                                            df = pd.read_sql_query('SELECT * FROM BFPD_table WHERE user_id = "{}"'.format(te),conn)
                                            df_new = df[["Name_of_Legue","Year","Nationality","Balance_by_player","Balance_INFLACION"]]
                                            st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                                            st.success("Export Datas")
                                    else:
                                        st.warning("file not found")
                                        st.info("Please procces data again !!")



                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:

                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = return_id_BFPD_table(te)
                                if flag != []:
                                    if int(te) > 0:
                                        delite_BFPD(te)
                                        st.success("Delite Datas")
                                        st.info("Please procces data")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")

                            if st.checkbox("Viusalise data !!!"):
                                # Viusalise datas
                                        
                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = return_id_BFPD_table(te)
                                if flag != []:
                                    if int(te) > 0:
                                        # data visualisation !!!
                                        df = pd.read_sql_query('SELECT * FROM BFPD_table WHERE user_id = "{}"'.format(te),conn)
                                        df_new = df[["Name_of_Legue","Year","Nationality","Balance_by_player","Balance_INFLACION"]]
                                        df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
                                        #st.dataframe(df_new)
                                        chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(


                                             x=alt.X('Year', axis=alt.Axis(title='date')),
                                             y=alt.Y('Balance_by_player',axis=alt.Axis(title='Balance by player')),

                                             ).properties(

                                                 width=800, 
                                                 height=600
                                             )

                                        chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
                                            
                                             # x=df['Year'],
                                             # y=df['Nationality'],
                                             x=alt.X('Year', axis=alt.Axis(title='date')),
                                             y=alt.Y('Balance_INFLACION',axis=alt.Axis(title='Balance_INFLACION')),
                                             # color='Expend_INFLACION',
                                             # size='Expend_INFLACION'
                                             ).properties(

                                                 width=800, 
                                                 height=600
                                             )
                                        st.altair_chart(chartline1 + chartline2)                                    

                                        # Build an empty graph
                                        lines = alt.Chart(df_new).mark_bar(size=25).encode(
                                          x=alt.X('Year',axis=alt.Axis(title='date')),
                                          y=alt.Y('Balance_by_player',axis=alt.Axis(title='value'))
                                          ).properties(
                                              width=600,
                                              height=300
                                          )
                                        def plot_animation(df_new):
                                            lines = alt.Chart(df_new).mark_bar(size=25).encode(
                                            x=alt.X('Year', axis=alt.Axis(title='date')),
                                            y=alt.Y('Balance_by_player',axis=alt.Axis(title='value')),
                                            ).properties(
                                                width=600, 
                                                height=300
                                            )
                                            return lines
                                        N = df_new.shape[0] # number of elements in the dataframe
                                        burst = 6       # number of elements (months) to add to the plot
                                        size = burst    # size of the current dataset
                                        line_plot = st.altair_chart(lines)
                                        start_btn = st.button('Start')
                                        if start_btn:
                                            for i in range(1,N):
                                                step_df = df_new.iloc[0:size]       
                                                lines = plot_animation(step_df)
                                                line_plot = line_plot.altair_chart(lines)
                                                size = i + burst
                                                if size >= N:
                                                    size = N - 1  
                                                time.sleep(0.1)
                                        st.success("Viusalise  Datas")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!") 

                    elif task == "BATCH Data by average league BALANCE for player DEPARTURES":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                            
                            rem_niz_BALANCE = []
                            if st.checkbox("Process data "):
                                st.info(" For restart data you must delete data and start over !!!") 

                                # Submit data 
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetAVGBalanceFORplayerDepartures.csv'
                                
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF_B,rememmber = BFPD_MAIN(leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")  
                                                        
                                if submit:                            
                                    rem_niz_BALANCE.append(rememmber)
                                    Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)
                                    st.dataframe(DataFrameFuncBalance(save_csv_Expend_BATCH))
                                    st.write("Youe Choose : ")
                                    for i in range(0,len(rem_niz_BALANCE)):
                                        st.write(i+1," ::: ",rem_niz_BALANCE[i])

                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetAVGBalanceFORplayerDepartures.csv'
                                    
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                        st.markdown(get_table_download_link_csv(DataFrameFuncBalance(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")

                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetAVGBalanceFORplayerDepartures.csv'
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                    os.remove(save_csv_Expend_BATCH)
                                    del rem_niz_BALANCE
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")

                    elif task == "Processed Data by average LEAGUE by AVG SESONS statistic":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                                                
                            st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            if st.checkbox("Process data "):

                                df = pd.read_sql('SELECT * FROM League_datas', conn)
                                df_new = df[["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]]
                                
                                st.dataframe(df_new)
                                a_leuge_DF = DFLS_base(df_new)
                                my_form = st.form(key = "form123")
                                create_DFLS()
                                submit = my_form.form_submit_button(label = "Submit")
                                if submit:

                                    st.success("Datas processes  :  ")

                                my_form_save = st.form(key = "form1")
                                st.info("For process data you must save data to database")
                                submit = my_form_save.form_submit_button(label = "Save data")
                                if submit:
                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)

                                    flag = return_id_DFLS_table(te)
                                    if flag == []:

                                        df = a_leuge_DF
                                        size = NumberOfRows(df)
                                        size = len(df)
                                        list1 = [0] *size


                                        for i in range(0,size):
                                            list1[i] = te
                                        df['user_id'] = list1
                                        # st.write("create_DFLS")
                                        create_DFLS()
                                        df.to_sql('DFLS_table',con=conn,if_exists='append')
                                        st.success("Data successfuly saved !")
                                    else:
                                        st.warning("Please first delite your records from database !!")
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:                                
                                if submit:

                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)
                                    flag = return_id_DFLS_table(te)
                                    if flag != []:
                                        if int(te) > 0:
                                            df = pd.read_sql_query('SELECT * FROM DFLS_table WHERE user_id = "{}"'.format(te),conn)
                                            df_new = df[["Name_of_Legue","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season"]]
                                            st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                                            st.success("Export Datas")
                                    else:
                                        st.warning("file not found")
                                        st.info("Please procces data again !!")



                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:

                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = return_id_DFLS_table(te)
                                if flag != []:
                                    if int(te) > 0:

                                        delite_DFLS(te)
                                        st.success("Delite Datas")
                                        st.info("Please procces data")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")

                            # if st.checkbox("Viusalise data !!!"):
                            #     # Viusalise datas
                                        
                            #     return_user_idd = return_user_id(username)
                            #     i = (return_user_idd[0])
                            #     res = int(''.join(map(str, i)))
                            #     te = int(res)
                            #     flag = return_id_EFPA_table(te)
                            #     if flag != []:
                            #         if int(te) > 0:
                            #             df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(te),conn)
                            #             df_new = df[["Name_of_Legue","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season"]]
                            #             df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
                            #             chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(

                            #                  x=alt.X('Year', axis=alt.Axis(title='date')),
                            #                  y=alt.Y('Expend_by_player',axis=alt.Axis(title='Expend by player')),
                            #                  ).properties(

                            #                      width=800, 
                            #                      height=600
                            #                  )

                            #             chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
                                            
                            #                  x=alt.X('Year', axis=alt.Axis(title='date')),
                            #                  y=alt.Y('Expend_INFLACION',axis=alt.Axis(title='Expend_INFLACION')),

                            #                  ).properties(

                            #                      width=800, 
                            #                      height=600
                            #                  )
                            #             st.altair_chart(chartline1 + chartline2)                                    

                            #             lines = alt.Chart(df_new).mark_bar(size=25).encode(
                            #               x=alt.X('Year',axis=alt.Axis(title='date')),
                            #               y=alt.Y('Expend_by_player',axis=alt.Axis(title='value'))
                            #               ).properties(
                            #                   width=600,
                            #                   height=300
                            #               )
                            #             def plot_animation(df_new):
                            #                 lines = alt.Chart(df_new).mark_bar(size=25).encode(
                            #                 x=alt.X('Year', axis=alt.Axis(title='date')),
                            #                 y=alt.Y('Expend_by_player',axis=alt.Axis(title='value')),
                            #                 ).properties(
                            #                     width=600, 
                            #                     height=300
                            #                 )
                            #                 return lines
                            #             N = df_new.shape[0] # number of elements in the dataframe
                            #             burst = 6       # number of elements (months) to add to the plot
                            #             size = burst    # size of the current dataset
                            #             line_plot = st.altair_chart(lines)
                            #             start_btn = st.button('Start')
                            #             if start_btn:
                            #                 for i in range(1,N):
                            #                     step_df = df_new.iloc[0:size]       
                            #                     lines = plot_animation(step_df)
                            #                     line_plot = line_plot.altair_chart(lines)
                            #                     size = i + burst
                            #                     if size >= N:
                            #                         size = N - 1  
                            #                     time.sleep(0.1)
                            #             st.success("Viusalise  Datas")
                            #     else:
                            #         st.warning("file not found")
                            #         st.info("Please procces data again !!")

                    elif task == "BATCH Data by average LEAGUE by AVG SESONS statistic":

                        col1,col2 = st.beta_columns(2)
                        with col1:

                            rem_niz_SEASON = []
                            st.info(" For restart data you must delete data and start over !!!")
                            if st.checkbox("Process data "):
                                # Submit data 
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetDataForLeauge_AVG_Seasons.csv'                          
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF_B,rememmber = DFLS_MAIN(leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")                                                       
                                if submit:                            
                                    rem_niz_SEASON.append(rememmber)
                                    Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)
                                    st.dataframe(DataFrameFuncSeasons(save_csv_Expend_BATCH))
                                    st.write("Youe Choose : ")
                                    for i in range(0,len(rem_niz_SEASON)):
                                        st.write(i+1," ::: ",rem_niz_SEASON[i])

                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetDataForLeauge_AVG_Seasons.csv'                               
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                        st.markdown(get_table_download_link_csv(DataFrameFuncSeasons(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")

                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetDataForLeauge_AVG_Seasons.csv'
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                    os.remove(save_csv_Expend_BATCH)
                                    del rem_niz_SEASON
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")

                    elif task == "Processed Data by average -> LEAGUE by YEAR statistic":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                                                
                            st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            if st.checkbox("Process data "):

                                df = pd.read_sql('SELECT * FROM League_datas', conn)
                                df_new = df[["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]]
                                
                                st.dataframe(df_new)
                                a_leuge_DF = DCWS_base(df_new)
                                my_form = st.form(key = "form123")
                                create_DCWS()
                                submit = my_form.form_submit_button(label = "Submit")
                                if submit:

                                    st.success("Datas processes  :  ")

                                my_form_save = st.form(key = "form1")
                                st.info("For process data you must save data to database")
                                submit = my_form_save.form_submit_button(label = "Save data")
                                if submit:
                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)

                                    flag = return_id_DCWS_table(te)
                                    if flag == []:

                                        df = a_leuge_DF
                                        size = NumberOfRows(df)
                                        size = len(df)
                                        list1 = [0] *size


                                        for i in range(0,size):
                                            list1[i] = te
                                        df['user_id'] = list1
                                        create_DCWS()
                                        df.to_sql('DCWS_table',con=conn,if_exists='append')
                                        st.success("Data successfuly saved !")
                                    else:
                                        st.warning("Please first delite your records from database !!")
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:                                
                                if submit:

                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)
                                    flag = return_id_DCWS_table(te)
                                    if flag != []:
                                        if int(te) > 0:
                                            df = pd.read_sql_query('SELECT * FROM DCWS_table WHERE user_id = "{}"'.format(te),conn)
                                            df_new = df[["Year_of_Season","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season"]]
                                            st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                                            st.success("Export Datas")
                                    else:
                                        st.warning("file not found")
                                        st.info("Please procces data again !!")



                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:

                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = return_id_DFLS_table(te)
                                if flag != []:
                                    if int(te) > 0:

                                        delite_DFLS(te)
                                        st.success("Delite Datas")
                                        st.info("Please procces data")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")  

                    elif task == "BATCH Data by average -> LEAGUE by YEAR statistic":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                            
                            rem_niz_SEASON = []
                            st.info(" For restart data you must delete data and start over !!!")
                            if st.checkbox("Process data "):
                                # Submit data 
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetBYyear.csv'                          
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF_B,rememmber = DCWS_MAIN(leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")                                                       
                                if submit:                            
                                    rem_niz_SEASON.append(rememmber)
                                    Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)
                                    st.dataframe(DataFrameFunc_THROUGHT_Seasons(save_csv_Expend_BATCH))
                                    st.write("Youe Choose : ")
                                    for i in range(0,len(rem_niz_SEASON)):
                                        st.write(i+1," ::: ",rem_niz_SEASON[i])

                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetBYyear.csv'                               
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                        st.markdown(get_table_download_link_csv(DataFrameFunc_THROUGHT_Seasons(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")

                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetBYyear.csv'
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                    os.remove(save_csv_Expend_BATCH)
                                    del rem_niz_SEASON
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")

                elif task_options == "Clubs": 
                    
                    task_clubs = st.selectbox("Chose ",["Processed Data by Data CLUBS statistic without   SESONS","BATCH Data by Data CLUBS statistic without   SESONS","Processed Data by Data CLUBS statistic through all   SESONS","BATCH Data by Data CLUBS statistic through all   SESONS"])
                    if task_clubs == "Processed Data by Data CLUBS statistic without   SESONS":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                                                
                            st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            if st.checkbox("Process data "):

                                df = pd.read_sql('SELECT * FROM Clubs_datas', conn)
                                df_new = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]]
                                
                                st.dataframe(df_new)
                                a_leuge_DF = CDWS_base(df_new)
                                my_form = st.form(key = "form123")
                                create_CDWS()
                                submit = my_form.form_submit_button(label = "Submit")
                                if submit:

                                    st.success("Datas processes  :  ")

                                my_form_save = st.form(key = "form1")
                                st.info("For process data you must save data to database")
                                submit = my_form_save.form_submit_button(label = "Save data")
                                if submit:
                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)

                                    flag = return_id_CDWS_table(te)
                                    if flag == []:

                                        df = a_leuge_DF
                                        size = NumberOfRows(df)
                                        size = len(df)
                                        list1 = [0] *size


                                        for i in range(0,size):
                                            list1[i] = te
                                        df['user_id'] = list1
                                        create_CDWS()
                                        df.to_sql('CDWS_table',con=conn,if_exists='append')
                                        st.success("Data successfuly saved !")
                                    else:
                                        st.warning("Please first delite your records from database !!")
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:                                
                                if submit:

                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)
                                    flag = return_id_CDWS_table(te)
                                    if flag != []:
                                        if int(te) > 0:
                                            df = pd.read_sql_query('SELECT * FROM CDWS_table WHERE user_id = "{}"'.format(te),conn)
                                            df_new = df[["Order_of_Expend","Club","State","Competition","Expenditures","Income","Arrivals","Departures","Balance","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"]]
                                            st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                                            st.success("Export Datas")
                                    else:
                                        st.warning("file not found")
                                        st.info("Please procces data again !!")



                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:

                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = return_id_CDWS_table(te)
                                if flag != []:
                                    if int(te) > 0:

                                        delite_CDWS(te)
                                        st.success("Delite Datas")
                                        st.info("Please procces data")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")

                    elif task_clubs == "BATCH Data by Data CLUBS statistic without   SESONS":
                        col1,col2 = st.beta_columns(2)
                        with col1:

                            rem_niz_CLUB_SEASON = []
                            st.info(" For restart data you must delete data and start over !!!")
                            if st.checkbox("Process data "):
                                # Submit data 
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GETDataClubs_with_seasons.csv'                          
                                leuge_DF = DataFrameFuncClubs(fp_clubs)
                                a_leuge_DF_B,rememmber = CDWS_MENI(leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")                                                       
                                if submit:                            
                                    rem_niz_CLUB_SEASON.append(rememmber)
                                    Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)
                                    st.dataframe(DataFrameFunc_CLUBS_Seasons(save_csv_Expend_BATCH))
                                    st.write("Youe Choose : ")
                                    for i in range(0,len(rem_niz_CLUB_SEASON)):
                                        st.write(i+1," ::: ",rem_niz_CLUB_SEASON[i])
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GETDataClubs_with_seasons.csv'                               
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                        st.markdown(get_table_download_link_csv(DataFrameFunc_CLUBS_Seasons(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")
                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GETDataClubs_with_seasons.csv'
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                    os.remove(save_csv_Expend_BATCH)
                                    del rem_niz_CLUB_SEASON
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")

                    elif task_clubs == "Processed Data by Data CLUBS statistic through all   SESONS":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                                                
                            st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            if st.checkbox("Process data "):

                                df = pd.read_sql('SELECT * FROM Clubs_datas', conn)
                                df_new = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]]
                                
                                st.dataframe(df_new)
                                a_leuge_DF = DCTAS_base(df_new)
                                my_form = st.form(key = "form123")
                                create_DCTAS()
                                submit = my_form.form_submit_button(label = "Submit")
                                if submit:

                                    st.success("Datas processes  :  ")

                                my_form_save = st.form(key = "form1")
                                st.info("For process data you must save data to database")
                                submit = my_form_save.form_submit_button(label = "Save data")
                                if submit:
                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)

                                    flag = return_id_DCTAS_table(te)
                                    if flag == []:

                                        df = a_leuge_DF
                                        size = NumberOfRows(df)
                                        size = len(df)
                                        list1 = [0] *size


                                        for i in range(0,size):
                                            list1[i] = te
                                        df['user_id'] = list1
                                        create_DCTAS()
                                        df.to_sql('DCTAS_table',con=conn,if_exists='append')
                                        st.success("Data successfuly saved !")
                                    else:
                                        st.warning("Please first delite your records from database !!")
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:                                
                                if submit:

                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)
                                    flag = return_id_CDWS_table(te)
                                    if flag != []:
                                        if int(te) > 0:
                                            df = pd.read_sql_query('SELECT * FROM DCTAS_table WHERE user_id = "{}"'.format(te),conn)
                                            df_new = df[["Order_of_Expend","Club","State","Competition","Expenditures","Income","Arrivals","Departures","Balance","inflation_Expenditure","inflation_Income","inflation_Balance"]]
                                            st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                                            st.success("Export Datas")
                                    else:
                                        st.warning("file not found")
                                        st.info("Please procces data again !!")



                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:

                                return_user_idd = return_user_id(username)
                                i = (return_user_idd[0])
                                res = int(''.join(map(str, i)))
                                te = int(res)
                                flag = return_id_DCTAS_table(te)
                                if flag != []:
                                    if int(te) > 0:

                                        delite_DCTAS(te)
                                        st.success("Delite Datas")
                                        st.info("Please procces data")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")

                    elif task_clubs == "BATCH Data by Data CLUBS statistic through all   SESONS":
                        col1,col2 = st.beta_columns(2)
                        with col1:

                            rem_niz_CLUB_TROUGHT_SEASON = []
                            st.info(" For restart data you must delete data and start over !!!")
                            if st.checkbox("Process data "):
                                # Submit data 
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetDate_for_Clubs_throught_all_seasons.csv'                          
                                leuge_DF = DataFrameFuncClubs(fp_clubs)
                                a_leuge_DF_B,rememmber = DCTAS_MAIN(leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")                                                       
                                if submit:                            
                                    rem_niz_CLUB_TROUGHT_SEASON.append(rememmber)
                                    Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)
                                    st.dataframe(DataFrameFunc_CLUB_THROUGHT_Seasons(save_csv_Expend_BATCH))
                                    st.write("Youe Choose : ")
                                    for i in range(0,len(rem_niz_CLUB_TROUGHT_SEASON)):
                                        st.write(i+1," ::: ",rem_niz_CLUB_TROUGHT_SEASON[i])
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetDate_for_Clubs_throught_all_seasons.csv'                               
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                        st.markdown(get_table_download_link_csv(DataFrameFunc_CLUB_THROUGHT_Seasons(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")
                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_for_GetDate_for_Clubs_throught_all_seasons.csv'
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                    os.remove(save_csv_Expend_BATCH)
                                    del rem_niz_CLUB_TROUGHT_SEASON
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")





