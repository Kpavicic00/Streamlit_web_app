
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
import os
import altair as alt
import duckdb
import streamlit.components.v1 as components
rem_niz_CLUB_SEASON = []
rem_niz_CLUB_TROUGHT_SEASON = []
coef = 'file.txt'
fp_league = 'Ligaska_KONACAN_STAS.csv'
fp_clubs = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
save_csv_Expend = "sportska_kubska_statsitika_OBRDENO.csv"
save_csv_Expend_BATCH = 'datas/BATCH_sportska_kubska_statsitika_OBRDENO.csv'
def app():
    
    col1,col2 = st.beta_columns(2)
    with col1:
        
        if st.checkbox("Process data "):
            # Submit data 
            save_csv_Expend_BATCH = 'datas/BATCH_CLUBS_TROUGHT_SEASON_file_name_clubs.csv'                          
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
            save_csv_Expend_BATCH = 'datas/BATCH_CLUBS_TROUGHT_SEASON_file_name_clubs.csv'                               
            if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                    st.markdown(get_table_download_link_csv(DataFrameFunc_CLUB_THROUGHT_Seasons(save_csv_Expend_BATCH)), unsafe_allow_html=True)
                    st.success("Export Datas")
            else:
                st.warning("file not found")
        # Delite datas 
        my_form_delite = st.form(key = "form12")
        submit = my_form_delite.form_submit_button(label = "Delite datas")
        if submit:
            save_csv_Expend_BATCH = 'datas/BATCH_CLUBS_TROUGHT_SEASON_file_name_clubs.csv'
            if(os.path.exists(save_csv_Expend_BATCH) and os.path.isfile(save_csv_Expend_BATCH)):
                os.remove(save_csv_Expend_BATCH)
                rem_niz_CLUB_TROUGHT_SEASON.clear()
                st.success("Delite Datas")
            else:
                st.warning("file not found")