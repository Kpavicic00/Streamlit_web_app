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
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()


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
                task_options = st.selectbox("Chose ",["<default>","Leauges","Clubs"])
                if task_options == "Leauges":
                    st.write(" Leauges ")
                    task = st.selectbox("task op",["Processed Data by average league EXPEND for player ARRIVALS","BATCH Data by average league EXPEND for player ARRIVALS","Processed Data by average league INCOME for player DEPARTURES","BATCH Data by average league INCOME for player DEPARTURES","Processed Data by average league BALANCE for player DEPARTURES","BATCH Data by average league BALANCE for player DEPARTURES","Processed Data by average LEAGUE by AVG SESONS statistic","BATCH Data by average LEAGUE by AVG SESONS statistic","Processed Data by average -> LEAGUE by YEAR statistic","BATCH Data by average -> LEAGUE by YEAR statistic"],key='key123dsa')                        
                    
                    if task == "Processed Data by average league EXPEND for player ARRIVALS":

                        col1,col2 = st.beta_columns(2)
                        with col1:
                                                
                            st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            if st.checkbox("Process data "):
                        
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF = EFPA_base(leuge_DF)
                                f_file = 'datas/exported/GetAVGExpendFORplayerArrivals.csv'
                                st.dataframe(a_leuge_DF)

                                my_form = st.form(key = "form123")
                                submit = my_form.form_submit_button(label = "Submit")
                                if submit:

                                    Write_multiple_DF(f_file,a_leuge_DF)
                                    st.success("Datas processes  :  ")
                                my_form_save = st.form(key = "form1")
                                st.info("For process data you must save data to database")
                                submit = my_form_save.form_submit_button(label = "Save data")
                                if submit:
                                    #return_user_idd = return_user_id(username)
                                    return_user_idd = return_user_id(username)
                                    i = (return_user_idd[0])
                                    res = int(''.join(map(str, i)))
                                    te = int(res)

                                    flag = return_id_EFPA_table(te)
                                    if flag == []:
                                        
                                        df = a_leuge_DF
                                        size = NumberOfRows(df)
                                        #st.dataframe()
                                        size = len(df)
                                        list1 = [0] *size

                                        #st.write(ar_niz)
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
                                flag = return_id_EFPA_table(te)
                                if flag != []:
                                    if int(te) > 0:
                                        #os.remove(f_file)

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
                                        #wine_four = wine_df[['fixed_acidity', 'volatile_acidity','citric_acid', 'residual_sugar']]
                                        # data visualisation !!!
                                        df = pd.read_sql_query('SELECT * FROM EFPA_table WHERE user_id = "{}"'.format(te),conn)
                                        df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
                                        df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
                                        #st.dataframe(df_new)
                                        chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(

                                             # x=df['Year'],
                                             # y=df['Nationality'],
                                             x=alt.X('Year', axis=alt.Axis(title='date')),
                                             y=alt.Y('Expend_by_player',axis=alt.Axis(title='Expend by player')),
                                             # color='Expend_by_player',
                                             # size='Expend_by_player'
                                             ).properties(

                                                 width=800, 
                                                 height=600
                                             )

                                        chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
                                            
                                             # x=df['Year'],
                                             # y=df['Nationality'],
                                             x=alt.X('Year', axis=alt.Axis(title='date')),
                                             y=alt.Y('Expend_INFLACION',axis=alt.Axis(title='Expend_INFLACION')),
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
                                        start_btn = st.button('Start')
                                        if start_btn:
                                            for i in range(1,N):
                                                step_df = df_new.iloc[0:size]       
                                                lines = plot_animation(step_df)
                                                line_plot = line_plot.altair_chart(lines)
                                                size = i + burst
                                                if size >= N:
                                                    size = N - 1  
                                                time.sleep(0.2)
 
                                        st.success("Viusalise  Datas")
                                else:
                                    st.warning("file not found")
                                    st.info("Please procces data again !!")

                    elif task == "BATCH Data by average league EXPEND for player ARRIVALS":
                        
                        col1,col2 = st.beta_columns(2)
                        with col1:                        
                            if st.checkbox("Process data "):
                                st.info(" For restart data you must delete data and start over !!!")
                                # Submit data 
                                #save_csv_Expend_BATCH = 'datas/exported/BATCH_GetAVGExpendFORplayerArrivals.csv' 
                                                          
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF_B,rememmber = EFPA_MAIN(leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")                                                       
                                if submit:                            
                                    
                                    rem_niz_nizz.append(rememmber)
                                   #Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)
                                    df_empt = a_leuge_DF_B
                                    st.dataframe(df_empt)
                                    st.write("Youe Choose : ")
                                    for i in range(0,len(rem_niz_nizz)):
                                        st.write(i+1," ::: ",rem_niz_nizz[i])

                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/ATCH_GetAVGExpendFORplayerArrivals.csv'
                                    
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                        st.markdown(get_table_download_link_csv(DataFrameFuncExpend(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")

                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                save_csv_Expend_BATCH = 'datas/exported/ATCH_GetAVGExpendFORplayerArrivals.csv'
                                if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                    os.remove(save_csv_Expend_BATCH)
                                    
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")
                            
                    elif task == "Processed Data by average league INCOME for player DEPARTURES":
                        col1,col2 = st.beta_columns(2)
                        with col1:
                                
                            

                            st.info(" For restart data you must delete data and start over !!!")
                            # Processd data
                            if st.checkbox("Process data "):
                        
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF = IFPD_base(leuge_DF)
                                st.dataframe(a_leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")
                                f_file = 'datas/GetAVGIncomeFORplayerDepartures.csv'
                                if submit:
                                    Write_multiple_DF(f_file,a_leuge_DF)
                                    st.success("Datas processes  :  ")
                                    st.dataframe(a_leuge_DF)
                                

                            
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:                               
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                        st.markdown(get_table_download_link_csv(DataFrameFuncIncome(f_file)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")


                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                    os.remove(f_file)
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")           
                        
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
                        
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF = BFPD_base(leuge_DF)
                                st.dataframe(a_leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")
                                f_file = 'datas/exported/GetAVGBalanceFORplayerDepartures.csv'
                                st.dataframe(a_leuge_DF)
                                if submit:
                                    Write_multiple_DF(f_file,a_leuge_DF)
                                    st.success("Datas processes  :  ")
                                                            
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                    
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                        st.markdown(get_table_download_link_csv(DataFrameFuncBalance(f_file)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")

                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                    os.remove(f_file)
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found") 

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
                        
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF = DFLS_base(leuge_DF)
                                st.dataframe(a_leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")
                                f_file = 'datas/exported/GetDataForLeauge_AVG_Seasons.csv'
                                if submit:
                                    Write_multiple_DF(f_file,a_leuge_DF)
                                    st.success("Datas processes  :  ")
                                                        
                            # Export datas  
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                    
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                        st.markdown(get_table_download_link_csv(DataFrameFuncSeasons(f_file)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")

                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                    os.remove(f_file)
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")

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
                        
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF = DCWS_base(leuge_DF)
                                st.dataframe(a_leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")
                                f_file = 'datas/exported/GetBYyear.csv'
                                if submit:
                                    Write_multiple_DF(f_file,a_leuge_DF)
                                    st.success("Datas processes  :  ")
                                                        
                            # Export datas  
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                    
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                        st.markdown(get_table_download_link_csv(DataFrameFunc_THROUGHT_Seasons(f_file)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")

                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                    os.remove(f_file)
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")  

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
                            if st.checkbox("Process CLUB data "):
                                leuge_DF = DataFrameFuncClubs(fp_clubs)
                                a_leuge_DF = CDWS_base(leuge_DF)
                                st.dataframe(a_leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")
                                f_file = 'datas/exported/GETDataClubs_with_seasons.csv'
                                if submit:
                                    Write_multiple_DF(f_file,a_leuge_DF)
                                    st.success("Datas processes  :  ")
                            # Export datas  
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                    
                                if(os.path.exists(f_file) and os.path.isfile(fp_clubs)):
                                        st.markdown(get_table_download_link_csv(DataFrameFunc_THROUGHT_Seasons(f_file)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")
                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                    os.remove(f_file)
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")

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
                            if st.checkbox("Process CLUB data "):
                                leuge_DF = DataFrameFuncClubs(fp_clubs)
                                a_leuge_DF = DCTAS_base(leuge_DF)
                                st.dataframe(a_leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")
                                f_file = 'datas/exported/GetDate_for_Clubs_throught_all_seasons.csv'
                                if submit:
                                    Write_multiple_DF(f_file,a_leuge_DF)
                                    st.success("Datas processes  :  ")
                            # Export datas  
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:
                                    
                                if(os.path.exists(f_file) and os.path.isfile(fp_clubs)):
                                        st.markdown(get_table_download_link_csv(DataFrameFunc_CLUB_THROUGHT_Seasons(f_file)), unsafe_allow_html=True)
                                        st.success("Export Datas")
                                else:
                                    st.warning("file not found")
                            # Delite datas 
                            my_form_delite = st.form(key = "form12")
                            submit = my_form_delite.form_submit_button(label = "Delite datas")
                            if submit:
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                    os.remove(f_file)
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")

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





