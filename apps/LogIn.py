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
import matplotlib.pyplot as plt
import altair as alt
from bokeh.plotting import figure
import duckdb
import subprocess
from html_temp import *
import os
import time
coef = 'file.txt'
fp_league = 'datas/Ligaska_KONACAN_STAS.csv'
save_csv_Expend = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
save_csv_Expend_BATCH = 'datas/BATCH_sportska_kubska_statsitika_OBRDENO.csv'
rem_niz = []
flag = 0
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
                
            task = st.radio("task op",["Add Posts","Metricss"],key='key123')

            if task == "Add Posts":
                st.subheader("Add Articles")
                

            elif task == "Metricss":
                df_frame = pd.DataFrame()
                flag = 0
                st.subheader("Metricss")

                task = st.selectbox("task op",["Processed Data by average league EXPEND for player ARRIVALS","BATCH Data by average league EXPEND for player ARRIVALS","Processed Data by average league INCOME for player DEPARTURES","BATCH Data by average league INCOME for player DEPARTURES"],key='key123dsa')
                        
                if task == "Processed Data by average league EXPEND for player ARRIVALS":

                    col1,col2 = st.beta_columns(2)
                    with col1:
                            
                        

                        st.info(" For restart data you must delete data and start over !!!")
                        # Processd data
                        if st.checkbox("Process data "):
                       
                            leuge_DF = DataFrameFunc(fp_league)
                            a_leuge_DF = EFPA_base(leuge_DF)
                            my_form = st.form(key = "form1")
                            submit = my_form.form_submit_button(label = "Submit")
                            f_file = 'datas/file_name_clubs.csv'
                            st.dataframe(a_leuge_DF)
                            if submit:
                                Write_multiple_DF(f_file,a_leuge_DF)
                                st.success("Datas processd :  ")
                                st.dataframe(a_leuge_DF)
                            

                        
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
                            
                            
                    #################################################################################

                elif task == "BATCH Data by average league EXPEND for player ARRIVALS":

                    col1,col2 = st.beta_columns(2)
                    with col1:
                        
                        if st.checkbox("Process data "):
                            

                            # Submit data 
                            save_csv_Expend_BATCH = 'datas/BATCH_file_name_clubs.csv'
                            
                            leuge_DF = DataFrameFunc(fp_league)
                            a_leuge_DF_B,rememmber = EFPA_MAIN(leuge_DF)
                            my_form = st.form(key = "form1")
                            submit = my_form.form_submit_button(label = "Submit")  
                                                     
                            if submit:                            
                                Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)

                                #st.dataframe(a_leuge_DF_B)
                                rem_niz.append(rememmber)
                                #save_csv_Expend_BATCH = 'datas/BATCH_file_name_clubs.csv'
                                Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)

                                st.dataframe(DataFrameFunc(save_csv_Expend_BATCH))
                                st.write("Youe Choose : ")
                                for i in range(0,len(rem_niz)):
                                    st.write(i+1," ::: ",rem_niz[i])

                        # Export datas
                        form_export_csv = st.form(key = "export_form")
                        submit = form_export_csv.form_submit_button(label = "Export datas")
                        if submit:
                            save_csv_Expend_BATCH = 'datas/BATCH_file_name_clubs.csv'
                                
                            if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                    st.markdown(get_table_download_link_csv(DataFrameFuncExpend(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                                    st.success("Export Datas")
                            else:
                                st.warning("file not found")

                        # Delite datas 
                        my_form_delite = st.form(key = "form12")
                        submit = my_form_delite.form_submit_button(label = "Delite datas")
                        if submit:
                            save_csv_Expend_BATCH = 'datas/BATCH_file_name_clubs.csv'
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
                            my_form = st.form(key = "form1")
                            submit = my_form.form_submit_button(label = "Submit")
                            f_file = 'datas/INCOME_file_name_clubs.csv'
                            st.dataframe(a_leuge_DF)
                            if submit:
                                Write_multiple_DF(f_file,a_leuge_DF)
                                st.success("Datas processd :  ")
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
                            

                            # Submit data 
                            save_csv_Expend_BATCH = 'datas/BATCH_INCOME_file_name_clubs.csv'
                            
                            leuge_DF = DataFrameFunc(fp_league)
                            a_leuge_DF_B,rememmber = IFPD_MAIN(leuge_DF)
                            my_form = st.form(key = "form1")
                            submit = my_form.form_submit_button(label = "Submit")  
                                                     
                            if submit:                            
                                Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)

                                #st.dataframe(a_leuge_DF_B)
                                rem_niz.append(rememmber)
                                #save_csv_Expend_BATCH = 'datas/BATCH_file_name_clubs.csv'
                                Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)

                                st.dataframe(DataFrameFunc(save_csv_Expend_BATCH))
                                st.write("Youe Choose : ")
                                for i in range(0,len(rem_niz)):
                                    st.write(i+1," ::: ",rem_niz[i])

                        # Export datas
                        form_export_csv = st.form(key = "export_form")
                        submit = form_export_csv.form_submit_button(label = "Export datas")
                        if submit:
                            save_csv_Expend_BATCH = 'datas/BATCH_INCOME_file_name_clubs.csv'
                                
                            if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                    st.markdown(get_table_download_link_csv(DataFrameFuncIncome(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                                    st.success("Export Datas")
                            else:
                                st.warning("file not found")

                        # Delite datas 
                        my_form_delite = st.form(key = "form12")
                        submit = my_form_delite.form_submit_button(label = "Delite datas")
                        if submit:
                            save_csv_Expend_BATCH = 'datas/BATCH_file_name_clubs.csv'
                            if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                                os.remove(save_csv_Expend_BATCH)
                                st.success("Delite Datas")
                            else:
                                st.warning("file not found")
                    


