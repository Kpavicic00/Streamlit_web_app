from numpy.core.numeric import True_
import streamlit as st 
import pandas as pd
import numpy as np
from sqlite3.dbapi2 import paramstyle
import bcrypt
from functions import *
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
from html_temp import *
import os
coef = 'file.txt'
fp_league = 'Ligaska_KONACAN_STAS.csv'
save_csv_Expend = 'sportska_kubska_statsitika_OBRDENO.csv'
save_csv_Expend_BATCH = 'BATCH_sportska_kubska_statsitika_OBRDENO.csv'
rem_niz = []
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
                
            task = st.selectbox("task op",["Add Posts","Metricss"],key='key123')

            if task == "Add Posts":
                st.subheader("Add Articles")
                

            elif task == "Metricss":
                st.subheader("Metricss")

                if st.checkbox("Metrics"):

                    # Create a menu for the data analysis process
                    col1,col2 = st.beta_columns(2)
                    with col1:
                        
                        if st.checkbox("Processed Data by average league EXPEND for player ARRIVALS"):

                            
                            leuge_DF = DataFrameFunc(fp_league)

                            a_leuge_DF = EFPA_base(leuge_DF)
                            #st.dataframe(a_leuge_DF)

                            st.success("Final result ")
                            my_form = st.form(key = "form1")
                            submit = my_form.form_submit_button(label = "Submit")
                            if submit:
                                df_file = a_leuge_DF.to_csv('file_name_clubs.csv')
                                f_file = 'file_name_clubs.csv'
                                st.write("Postoji",df_file)

                                # if os.path.isfile(df_file) or os.path.exists(df_file):
                                #     st.write("Postoji")
                                
                                # if (os.path.exists(df_file) and os.path.isfile(df_file)):
                                #Write_multiple_DF(f_file,a_leuge_DF)
                                
                                    
                                #Delite_DataFrame_from_memory(leuge_DF)
                                #Delite_DataFrame_from_memory(a_leuge_DF)
                                #st.dataframe(DataFrameFunc(df_file))

                            submit = my_form.form_submit_button(label = "Delite datas")
                            if submit:
                                st.success("Delite Datas")
                                #a_leuge_DF.drop(a_leuge_DF.index, inplace=True)
                                #Delite_DataFrame_from_memory(leuge_DF)
                                if(os.path.exists(df_file) and os.path.isfile(df_file)):
                                    os.remove(df_file)
                                    print("file deleted")
                                    #st.success("Delite Datas")
                                else:
                                    print("file not found")
                            #if(os.path.exists(df_file) and os.path.isfile(df_file)):
                                
                                st.dataframe(DataFrameFuncExpend(df_file))

                        if st.checkbox("BATCH Data by average league EXPEND for player ARRIVALS"):
                            leuge_DF = DataFrameFunc(fp_league)
                            a_leuge_DF_B,rememmber = EFPA_MAIN(leuge_DF)
                            

                            #a_leuge_DF_B.to_csv('BATCH_file_name_clubs.csv')
                            save_csv_Expend_BATCH = 'BATCH_file_name_clubs.csv'
                            Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)
                            # for i in range(0,len(rem_niz)):
                            #     st.write("test",rem_niz[i])

                            st.dataframe(a_leuge_DF_B)

                            # st.success("Final result ")
                            my_form = st.form(key = "form1")
                            submit = my_form.form_submit_button(label = "Submit")
                            #a_leuge_DF_B.to_csv('BATCH_file_name_clubs.csv')
                            #df_file_batch = 'BATCH_file_name_clubs.csv'
                            
                            if submit:
                                rem_niz.append(rememmber)
                                save_csv_Expend_BATCH = 'BATCH_file_name_clubs.csv'
                                Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF_B)

                                st.dataframe(DataFrameFuncExpend(save_csv_Expend_BATCH))
                                #Write_multiple_DF('BATCH_file_name_clubs.csv',a_leuge_DF_B)
                                
                                #st.data   frame(DataFrameFuncExpend(df_file_batch))
                            st.write("Youe Choose : ")
                            for i in range(0,len(rem_niz)):
                                st.write(i+1," ::: ",rem_niz[i])
                            #   ,"Specific Proces data by average league EXPEND for player ARRIVALS"
                            #options = st.selectbox("Select Option", ["Processed Data by average league EXPEND for player ARRIVALS","Specific Proces data by average league EXPEND for player ARRIVALS"],key='123412')

                            # if options == "Processed Data by average league EXPEND for player ARRIVALS":

                            #     if count_1 == 0:
                            #         st.write("You choose option Get AVERAGE Expend for player arrivals")
                            #         leuge_DF = DataFrameFunc(fp_league)
                                    

                                    
                            #         a_leuge_DF = EFPA_base(leuge_DF)
                            #         #st.dataframe(a_leuge_DF)
                            #         Write_multiple_DF(save_csv_Expend,a_leuge_DF)
                            #         Delite_DataFrame_from_memory(leuge_DF)
                            #         Delite_DataFrame_from_memory(a_leuge_DF)
                            #         count_1 +=1
                            #         st.success("Final result ")
                            #         my_form = st.form(key = "form1")
                            #         submit = my_form.form_submit_button(label = "Submit")
                            #         if submit:
                            #             break

                            #     if count_1 == 1:
                            #         #st.warning("You can use this function only one")
                            #         st.warning("ou can use this function only one, Pleas use something else  :-) ")
                            
                            # if options == "Specific Proces data by average league EXPEND for player ARRIVALS":
                                # st.write("You choose option Specific Proces data by average league EXPEND for player ARRIVALS")
                                # leuge_DF = DataFrameFunc(fp_league)
                                # a_leuge_DF = EFPA_MAIN(leuge_DF)
                                # #st.dataframe(a_leuge_DF)
                                # Write_multiple_DF(save_csv_Expend_BATCH,a_leuge_DF)
                                # Delite_DataFrame_from_memory(leuge_DF)
                                # Delite_DataFrame_from_memory(a_leuge_DF)
                                # my_form = st.form(key = "form1")
                                # submit = my_form.form_submit_button(label = "Submit")
                                # if submit:
                                #     break
                                


                        
                        


                        

                    
                    

                    


