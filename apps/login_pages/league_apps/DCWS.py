import streamlit as st
import pandas as pd
import numpy as np
from functions import *
from League_functions.DCWS_func import DCWS_base
from database import *
import altair as alt
from html_temp import *
import os
import time

def app():
    st.title('1. function DCWS  process function')
    st.write('Welcome to metrics')
    username = return_username()

    i = (username[0])
    res = str(''.join(map(str, i)))

    delite_temp_user(res)
    create_DCWS()
    col1,col2 = st.columns(2)
    with col1:
                            
        st.info(" For restart data you must delete data and start over !!!")
        # Processd data
        if st.checkbox("Process data"):
            df = pd.read_sql('SELECT * FROM League_datas', conn)
            df_new = df[["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]]
            st.dataframe(df_new)
            a_leuge_DF = DCWS_base(df_new)
            my_form = st.form(key = "form123")
            submit = my_form.form_submit_button(label = "Submit")
            if submit:
                st.success("Datas processes  :")
            my_form_save = st.form(key = "form1")
            st.info("For process data you must save data to database")
            submit = my_form_save.form_submit_button(label = "Save data")
            if submit:
                return_user_idd = return_user_id(res)
                i = (return_user_idd[0])
                res = int(''.join(map(str, i)))
                te = int(res)
                flag = return_id_DCWS_table(te)
                if flag == []:
                    df = a_leuge_DF
                    size = NumberOfRows(df)
                    size = len(df)
                    list1 = [0] * size
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
                return_user_idd = return_user_id(res)
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
                    st.info("Please procces data again !")
        # Delite datas 
        my_form_delite = st.form(key = "form12")
        submit = my_form_delite.form_submit_button(label = "Delite datas")
        if submit:
            return_user_idd = return_user_id(res)
            i = (return_user_idd[0])
            res = int(''.join(map(str, i)))
            te = int(res)
            flag = (return_id_DCWS_table(te))                               
            if flag != []:
                if int(te) > 0 :
                    delite_DCWS(te)
                    st.success("Delite Datas")
                    st.info("Please procces data")
            else:
                st.warning("file not found")
                st.info("Please procces data again !")
        # try:
        #     if st.checkbox("Viusalise data !!!"):
        #         # Viusalise datas
        #         #st.write("Viusalise datas",res)
        #         return_user_idd = return_user_id(res)
        #         st.write("")
        #         i = (return_user_idd[0])
        #         res = int(''.join(map(str, i)))
        #         te = int(res)
        #         flag = return_id_DCWS_table(te)
        #         if flag != []:
        #             if int(te) > 0:
        #                 df = pd.read_sql_query('SELECT * FROM DCWS_table WHERE user_id = "{}"'.format(te),conn)
        #                 df_new = df[["Year_of_Season","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season"]]
        #                 df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
        #                 chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(
        #                      x=alt.X('Year', axis=alt.Axis(title='date')),
        #                      y=alt.Y('Income_by_player',axis=alt.Axis(title='Income_by_player')),
        #                      ).properties(
        #                          width=800, 
        #                          height=600
        #                      )
        #                 chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
        #                     # 
        #                      x=alt.X('Year', axis=alt.Axis(title='date')),
        #                      y=alt.Y('Income_INFLACION',axis=alt.Axis(title='Income_INFLACION')),
        #                      ).properties(
        #                          width=800, 
        #                          height=600
        #                      )
        #                 # 
        #                 st.altair_chart(chartline1 + chartline2)                                
        #                 lines = alt.Chart(df_new).mark_bar(size=25).encode(
        #                   x=alt.X('Year',axis=alt.Axis(title='date')),
        #                   y=alt.Y('Income_by_player',axis=alt.Axis(title='value'))
        #                   ).properties(
        #                       width=600,
        #                       height=300
        #                   )
        #                 def plot_animation(df_new):
        #                     lines = alt.Chart(df_new).mark_bar(size=25).encode(
        #                     x=alt.X('Year', axis=alt.Axis(title='date')),
        #                     y=alt.Y('Income_by_player',axis=alt.Axis(title='value')),
        #                     ).properties(
        #                         width=600, 
        #                         height=300
        #                     )
        #                     return lines
        #                 N = df_new.shape[0] # number of elements in the dataframe
        #                 burst = 6       # number of elements (months) to add to the plot
        #                 size = burst    # size of the current dataset
        #                 line_plot = st.altair_chart(lines)
        #                 line_plot
        #                 start_btn = st.button('Start')
        #                 if start_btn:
        #                     for i in range(1,N):
        #                         step_df = df_new.iloc[0:size]       
        #                         lines = plot_animation(step_df)
        #                         line_plot = line_plot.altair_chart(lines)
        #                         size = i + burst
        #                         if size >= N:
        #                             size = N - 1  
        #                         time.sleep(0.1)
        #                 st.success("Viusalise  Datas")
        #         else:
        #             st.warning("file not found")
        #             st.info("Please procces data again !!")

        # except Exception as e:
        #   st.write("Error, please resart Visaulsation checkboc !! ") 