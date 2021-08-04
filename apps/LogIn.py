from numpy.core.numeric import True_
import streamlit as st 
import pandas as pd
import numpy as np
from sqlite3.dbapi2 import paramstyle
import bcrypt
from functions import *
from database import create_usertable,add_user_data,check_double_email,check_double_username,login_user,check_userdatatable
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
fp_clubs = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
coef = 'file.txt'
fp_league = 'datas/Ligaska_KONACAN_STAS.csv'
save_csv_Expend = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
save_csv_Expend_BATCH = 'datas/BATCH_sportska_kubska_statsitika_OBRDENO.csv'
rem_niz = []
rem_niz_INCOME = []
rem_niz_BALANCE = []
rem_niz_SEASON = []
rem_niz_CLUB_SEASON = []
rem_niz_CLUB_TROUGHT_SEASON = []
flag = 0
def app():
    st.subheader("LogIn")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password",type='password')
    if st.sidebar.checkbox("Login"):

        st.write("Log in as ::: ",username)
        create_usertable()
        hashed_pswd = make_password(password)
        result = login_user(username,check_hashes(password,hashed_pswd))

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
                                f_file = 'datas/exportedGetAVGExpendFORplayerArrivals.csv'
                                st.dataframe(a_leuge_DF)

                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")
                                if submit:
                                    Write_multiple_DF(f_file,a_leuge_DF)
                                    st.success("Datas processes  :  ")
                                
                            # Export datas
                            form_export_csv = st.form(key = "export_form")
                            submit = form_export_csv.form_submit_button(label = "Export datas")
                            if submit:                                
                                if(os.path.exists(f_file) and os.path.isfile(f_file)):
                                        st.markdown(get_table_download_link_csv(DataFrameFuncExpend(f_file)), unsafe_allow_html=True)
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
                                
                    elif task == "BATCH Data by average league EXPEND for player ARRIVALS":

                        col1,col2 = st.beta_columns(2)
                        with col1:                        
                            if st.checkbox("Process data "):
                                st.info(" For restart data you must delete data and start over !!!")
                                # Submit data 
                                save_csv_Expend_BATCH = 'datas/exported/BATCH_GetAVGExpendFORplayerArrivals.csv'                           
                                leuge_DF = DataFrameFunc(fp_league)
                                a_leuge_DF_B,rememmber = EFPA_MAIN(leuge_DF)
                                my_form = st.form(key = "form1")
                                submit = my_form.form_submit_button(label = "Submit")                                                       
                                if submit:                            
     
                                    rem_niz.append(rememmber)
                                    Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)

                                    st.dataframe(DataFrameFuncExpend(save_csv_Expend_BATCH))
                                    st.write("Youe Choose : ")
                                    for i in range(0,len(rem_niz)):
                                        st.write(i+1," ::: ",rem_niz[i])

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
                                    rem_niz.clear()
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
                                    rem_niz_BALANCE.clear()
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
                                    rem_niz_BALANCE.clear()
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
                                    rem_niz_SEASON.clear()
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
                                    rem_niz_SEASON.clear()
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
                                    rem_niz_CLUB_SEASON.clear()
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
                                    rem_niz_CLUB_TROUGHT_SEASON.clear()
                                    st.success("Delite Datas")
                                else:
                                    st.warning("file not found")





