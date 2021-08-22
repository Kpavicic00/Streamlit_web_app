from numpy.core.numeric import identity
import streamlit as st
import pandas as pd
import numpy as np
from functions import *
from Club_functions.CDWS_func import*
from database import *
import altair as alt
from html_temp import *
import os
import time

def app():
    st.title('2. function CDWS_BATCH  process function')
    st.write('Welcome to metrics')
    username = return_username()
    i = (username[0])
    res = str(''.join(map(str, i)))
    return_user_idd = return_user_id(res)
    i = (return_user_idd[0])
    temp_save = int(''.join(map(str, i)))
    delite_temp_user(res)
    create_CDWS_BATCH()
    col1,col2 = st.beta_columns(2)
    with col1:

        st.info(" For restart data you must delete data and start over !!!")
        if st.checkbox("Process data "):
            create_CDWS_BATCH_temp()
            create_CDWS_LEAGUE_flag_option()
            df = pd.read_sql('SELECT * FROM Clubs_datas', conn)
            df_new = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]]
            to_append,rememmberr,flag_option = CDWS_MENI(df_new)
            columns = ["Order_of_Expend","Club","State","Competition","Expenditures","Income","Arrivals","Departures","Balance","inflation_Expenditure","inflation_Income","inflation_Balance"]    
            my_form = st.form(key = "form123")
            submit = my_form.form_submit_button(label = "Submit")
            if submit:
                                
                columns = ["Name_of_Legue","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season"]
                st.dataframe(to_append)                                
                return_user_idd = return_user_id(res)
                i = (return_user_idd[0])
                id = str(''.join(map(str, i)))
                return_id_CDWS__LEAGUE_flag_option(temp_save)
                flag2 = return_id_CDWS__LEAGUE_flag_option(id)
                if flag2 == []:
                    insert_CDWS_LEAGUE_flag_option(flag_option,id)
                elif flag2 != []:
                    i = (flag2[0])
                    result = str(''.join(map(str, i)))
                    if flag_option == result:
                        insert_CDWS_LEAGUE_flag_option(flag_option,id)
                        df = to_append
                        size = NumberOfRows(df)
                        size = len(df)
                        list1 = [0] * size
                        for i in range(0,size):
                            list1[i] = id
                        df['user_id'] = list1
                        to_append.to_sql('CDWS_BATCH_temp',con=conn,if_exists='append')
                        st.success("Datas processes  successfully !!")

                    else:
                        st.warning("Please reppet your choose in search filter")
                        st.info("Leagues, Years and Nationality are different datas!!!")
                        st.info("Or Delite perviuos data !")

        # Save datas
        my_form_save = st.form(key = "form1")
        st.info("For process data you must save data to database")
        submit = my_form_save.form_submit_button(label = "Save data")
        if submit:
           
            flag_id = return_id_CDWS_BATCH(temp_save)
            if flag_id == []:
                flag2 = return_id_CDWS_BATCH_temp(temp_save)
                if flag2 != []:
                    if int(temp_save) > 0:
                        df = pd.read_sql('SELECT * FROM CDWS_BATCH_temp', conn)
                        df_save = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance","user_id"]]
                        st.dataframe(df_save)
                        df_save.to_sql('CDWS_BATCH_table',con=conn,if_exists='append')
                        delite_CDWS_BATCH_temp(temp_save)
                        st.success("Data successfuly saved !")
                else:
                    st.warning("Please first proces jour data")
                    
            
            else:
                st.warning("Record already exisit please first delite datas !!")

        # Export datas
        form_export_csv = st.form(key = "export_form")
        submit = form_export_csv.form_submit_button(label = "Export datas")
        if submit:                                
            if submit:
                flag = return_id_CDWS_BATCH(temp_save)
                if flag != []:
                    if int(temp_save) > 0:
                        df = pd.read_sql_query('SELECT * FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
                        df_new = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"]]
                        st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                        st.success("Export Datas")
                else:
                    st.warning("file not found")
                    st.info("Please procces data again !")

       # Delite datas 
        my_form_delite = st.form(key = "form_Delite")
        submit = my_form_delite.form_submit_button(label = "Delite datas")
        if submit:
            flag = return_id_CDWS_BATCH(temp_save)                             
            if flag != []:
                if int(temp_save) > 0 :
                    delite_CDWS_BATCH(temp_save)
                    delite_CDWS_LEAGUE_flag_option(temp_save)
                    #delite_CDWS_BATCH_temp(temp_save)
                    st.success("Delite Datas")
                    st.info("Please procces data")
            else:
                st.warning("file not found")
                st.info("Please procces data again !") 

    #     try:
    #         if st.checkbox("Viusalise data !!!"):
    #             # Viusalise datas
    #             #st.write("Viusalise datas",res)
    #             # return_user_idd = return_user_id(temp_save)
    #             # st.write("")
    #             # i = (return_user_idd[0])
    #             # res = int(''.join(map(str, i)))
    #             # te = int(res)
    #             flag = return_id_CDWS_BATCH(temp_save)
    #             if flag != []:
    # # 
    #                 if int(temp_save) > 0:
    #                     flag_option = return_id_CDWS__LEAGUE_flag_option(temp_save)
    #                     st.write("i(flag_option[0])",flag_option[0])
    #                     temp_filter = ''.join(flag_option[0])
    #                     st.write("temp_filter",temp_filter,"type(temp_filter)",type(temp_filter))
    #                     if flag_option !=[]:
    #                         if temp_filter == 'LEAUGE':
    #                             temp_option = "Name_of_Legue"
    # # 
    #                             st.write("temp_option",temp_option)
    # # 
    #                             df = pd.read_sql_query('SELECT * FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
    #                             df_new = df[["Name_of_Legue","Year","Nationality","Balance_by_player","Balance_INFLACION"]]
    #                             df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    # # 
    # # 
    #                             #   matplot 
    #                             # df_new["Nationality"].value_counts().plot.pie(autopct="%1.1f%%")
    #                             # st.pyplot()
    # # 
    #                             chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(
    #                                  x=alt.X('Year', axis=alt.Axis(title='date')),
    #                                  y=alt.Y('Balance_by_player',axis=alt.Axis(title='Balance by player')),
    #                                  ).properties(
    #                                      width=800, 
    #                                      height=600
    #                                  )
    #                             chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
    #         # 
    #                                  x=alt.X('Year', axis=alt.Axis(title='date')),
    #                                  y=alt.Y('Balance_INFLACION',axis=alt.Axis(title='Balance_INFLACION')),
    #                                  ).properties(
    #                                      width=800, 
    #                                      height=600
    #                                  )
    # # 
    #                             st.altair_chart(chartline1 + chartline2)                                
    #                             lines = alt.Chart(df_new).mark_bar(size=25).encode(
    #                               x=alt.X('Year',axis=alt.Axis(title='date')),
    #                               y=alt.Y('Balance_by_player',axis=alt.Axis(title='value'))
    #                               ).properties(
    #                                   width=600,
    #                                   height=300
    #                               )
    #                             def plot_animation(df_new):
    #                                 lines = alt.Chart(df_new).mark_bar(size=25).encode(
    #                                 x=alt.X('Year', axis=alt.Axis(title='date')),
    #                                 y=alt.Y('Balance_by_player',axis=alt.Axis(title='value')),
    #                                 ).properties(
    #                                     width=600, 
    #                                     height=300
    #                                 )
    #                                 return lines
    #                             N = df_new.shape[0] # number of elements in the dataframe
    #                             burst = 6       # number of elements (months) to add to the plot
    #                             size = burst    # size of the current dataset
    #                             line_plot = st.altair_chart(lines)
    #                             line_plot
    #                             start_btn = st.button('Start')
    #                             if start_btn:
    #                                 for i in range(1,N):
    #                                     step_df = df_new.iloc[0:size]       
    #                                     lines = plot_animation(step_df)
    #                                     line_plot = line_plot.altair_chart(lines)
    #                                     size = i + burst
    #                                     if size >= N:
    #                                         size = N - 1  
    #                                     time.sleep(0.1)
    #                             st.success("Viusalise  Datas")
    # # 
    #                         elif temp_filter == 'Year':
    #                             temp_option = "Nationality"
    #                             st.write("temp_option",temp_option)
    # # 
    #                             df = pd.read_sql_query('SELECT * FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
    #                             df_new = df[["Name_of_Legue","Year","Nationality","Balance_by_player","Balance_INFLACION"]]
    #                             df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    # # 
    # # 
    #                             #   matplot 
    #                             # df_new["Nationality"].value_counts().plot.pie(autopct="%1.1f%%")
    #                             # st.pyplot()
    # # 
    #                             chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(
    #                                  x=alt.X('Year', axis=alt.Axis(title='date')),
    #                                  y=alt.Y('Balance_by_player',axis=alt.Axis(title='Balance by player')),
    #                                  ).properties(
    #                                      width=800, 
    #                                      height=600
    #                                  )
    #                             chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
    #         # 
    #                                  x=alt.X('Year', axis=alt.Axis(title='date')),
    #                                  y=alt.Y('Balance_INFLACION',axis=alt.Axis(title='Balance_INFLACION')),
    #                                  ).properties(
    #                                      width=800, 
    #                                      height=600
    #                                  )
    # # 
    #                             st.altair_chart(chartline1 + chartline2)                                
    #                             lines = alt.Chart(df_new).mark_bar(size=25).encode(
    #                               x=alt.X('Year',axis=alt.Axis(title='date')),
    #                               y=alt.Y('Balance_by_player',axis=alt.Axis(title='value'))
    #                               ).properties(
    #                                   width=600,
    #                                   height=300
    #                               )
    #                             def plot_animation(df_new):
    #                                 lines = alt.Chart(df_new).mark_bar(size=25).encode(
    #                                 x=alt.X('Year', axis=alt.Axis(title='date')),
    #                                 y=alt.Y('Balance_by_player',axis=alt.Axis(title='value')),
    #                                 ).properties(
    #                                     width=600, 
    #                                     height=300
    #                                 )
    #                                 return lines
    #                             N = df_new.shape[0] # number of elements in the dataframe
    #                             burst = 6       # number of elements (months) to add to the plot
    #                             size = burst    # size of the current dataset
    #                             line_plot = st.altair_chart(lines)
    #                             line_plot
    #                             start_btn = st.button('Start')
    #                             if start_btn:
    #                                 for i in range(1,N):
    #                                     step_df = df_new.iloc[0:size]       
    #                                     lines = plot_animation(step_df)
    #                                     line_plot = line_plot.altair_chart(lines)
    #                                     size = i + burst
    #                                     if size >= N:
    #                                         size = N - 1  
    #                                     time.sleep(0.1)
    #                             st.success("Viusalise  Datas")
    #                             st.write("temp_option",temp_option,type(temp_option))
    #                         elif temp_filter == 'Nationality':
    #                             temp_option = "Nationality"
    #                             st.write("temp_option",temp_option)
    # # 
    #                             df = pd.read_sql_query('SELECT * FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
    #                             df_new = df[["Name_of_Legue","Year","Nationality","Balance_by_player","Balance_INFLACION"]]
    #                             df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    # # 
    # # 
    #                             #   matplot 
    #                             # df_new["Nationality"].value_counts().plot.pie(autopct="%1.1f%%")
    #                             # st.pyplot()
    # # 
    #                             chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(
    #                                  x=alt.X('Year', axis=alt.Axis(title='date')),
    #                                  y=alt.Y('Balance_by_player',axis=alt.Axis(title='Balance by player')),
    #                                  ).properties(
    #                                      width=800, 
    #                                      height=600
    #                                  )
    #                             chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
    #         # 
    #                                  x=alt.X('Year', axis=alt.Axis(title='date')),
    #                                  y=alt.Y('Balance_INFLACION',axis=alt.Axis(title='Balance_INFLACION')),
    #                                  ).properties(
    #                                      width=800, 
    #                                      height=600
    #                                  )
    # # 
    #                             st.altair_chart(chartline1 + chartline2)                                
    #                             lines = alt.Chart(df_new).mark_bar(size=25).encode(
    #                               x=alt.X('Year',axis=alt.Axis(title='date')),
    #                               y=alt.Y('Balance_by_player',axis=alt.Axis(title='value'))
    #                               ).properties(
    #                                   width=600,
    #                                   height=300
    #                               )
    #                             def plot_animation(df_new):
    #                                 lines = alt.Chart(df_new).mark_bar(size=25).encode(
    #                                 x=alt.X('Year', axis=alt.Axis(title='date')),
    #                                 y=alt.Y('Balance_by_player',axis=alt.Axis(title='value')),
    #                                 ).properties(
    #                                     width=600, 
    #                                     height=300
    #                                 )
    #                                 return lines
    #                             N = df_new.shape[0] # number of elements in the dataframe
    #                             burst = 6       # number of elements (months) to add to the plot
    #                             size = burst    # size of the current dataset
    #                             line_plot = st.altair_chart(lines)
    #                             line_plot
    #                             start_btn = st.button('Start')
    #                             if start_btn:
    #                                 for i in range(1,N):
    #                                     step_df = df_new.iloc[0:size]       
    #                                     lines = plot_animation(step_df)
    #                                     line_plot = line_plot.altair_chart(lines)
    #                                     size = i + burst
    #                                     if size >= N:
    #                                         size = N - 1  
    #                                     time.sleep(0.1)
    #                             st.success("Viusalise  Datas")
    #                             st.write("temp_option",temp_option,type(temp_option))
    # # 
    #                             # st.write("temp_option",temp_option)
    # # 
    #                             # df = pd.read_sql_query('SELECT * FROM CDWS_table WHERE user_id = "{}"'.format(te),conn)
    #                             # df_new = df[["Year_of_Season","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season"]]
    #                             # df_new['Year']= pd.to_datetime(df_new['Year'],format='%Y')
    #                             # chartline1 = alt.Chart(df_new).mark_bar(size=22,color='blue').encode(
    #                             #      x=alt.X('Year', axis=alt.Axis(title='date')),
    #                             #      y=alt.Y('Balance_by_player',axis=alt.Axis(title='Balance by player')),
    #                             #      ).properties(
    #                             #          width=800, 
    #                             #          height=600
    #                             #      )
    #                             # chartline2 = alt.Chart(df_new).mark_bar(size=12,color='red').encode(
    #         # 
    #                             #      x=alt.X('Year', axis=alt.Axis(title='date')),
    #                             #      y=alt.Y('Balance_INFLACION',axis=alt.Axis(title='Balance_INFLACION')),
    #                             #      ).properties(
    #                             #          width=800, 
    #                             #          height=600
    #                             #      )
    # # 
    #                             # st.altair_chart(chartline1 + chartline2)                                
    #                             # lines = alt.Chart(df_new).mark_bar(size=25).encode(
    #                             #   x=alt.X('Year',axis=alt.Axis(title='date')),
    #                             #   y=alt.Y('Balance_by_player',axis=alt.Axis(title='value'))
    #                             #   ).properties(
    #                             #       width=600,
    #                             #       height=300
    #                             #   )
    #                             # def plot_animation(df_new):
    #                             #     lines = alt.Chart(df_new).mark_bar(size=25).encode(
    #                             #     x=alt.X('Year', axis=alt.Axis(title='date')),
    #                             #     y=alt.Y('Balance_by_player',axis=alt.Axis(title='value')),
    #                             #     ).properties(
    #                             #         width=600, 
    #                             #         height=300
    #                             #     )
    #                             #     return lines
    #                             # N = df_new.shape[0] # number of elements in the dataframe
    #                             # burst = 6       # number of elements (months) to add to the plot
    #                             # size = burst    # size of the current dataset
    #                             # line_plot = st.altair_chart(lines)
    #                             # line_plot
    #                             # start_btn = st.button('Start')
    #                             # if start_btn:
    #                             #     for i in range(1,N):
    #                             #         step_df = df_new.iloc[0:size]       
    #                             #         lines = plot_animation(step_df)
    #                             #         line_plot = line_plot.altair_chart(lines)
    #                             #         size = i + burst
    #                             #         if size >= N:
    #                             #             size = N - 1  
    #                             #         time.sleep(0.1)
    #                             # st.success("Viusalise  Datas")
    #             # 
    #             else:
    #                 st.warning("file not found")
    #                 st.info("Please procces data again !!")
    #     except Exception as e:
    #       st.write("Error, please resart Visaulsation checkboc !! ") 
