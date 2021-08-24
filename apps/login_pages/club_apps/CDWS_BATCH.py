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
    col1,col2 = st.columns(2)
    with col1:

        st.info(" For restart data you must delete data and start over !!!")
        if st.checkbox("Process data "):
            create_CDWS_BATCH_temp()
            create_CDWS_LEAGUE_flag_option()
            df = pd.read_sql('SELECT * FROM Clubs_datas', conn)
            df_new = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]]
            to_append,rememmberr,flag_option = CDWS_MENI(df_new)
            #columns = ["Order_of_Expend","Club","State","Competition","Expenditures","Income","Arrivals","Departures","Balance","inflation_Expenditure","inflation_Income","inflation_Balance"]    
            my_form = st.form(key = "form123")
            submit = my_form.form_submit_button(label = "Submit")
            if submit:                    
                return_user_idd = return_user_id(res)
                i = (return_user_idd[0])
                id = str(''.join(map(str, i)))
                return_id_CDWS__LEAGUE_flag_option(temp_save)
                flag2 = return_id_CDWS__LEAGUE_flag_option(id)
                if flag2 == []:
                    insert_CDWS_LEAGUE_flag_option(flag_option,rememmberr,id)
                    df = to_append
                    size = NumberOfRows(df)
                    size = len(df)
                    list1 = [0] * size
                    for i in range(0,size):
                        list1[i] = id
                    df['user_id'] = list1
                    to_append.to_sql('CDWS_BATCH_temp',con=conn,if_exists='append')
                    a = view_all_CDWS__LEAGUE_flag_record(id)
                    st.success("Processed data you selected: : ")
                    for i in a:
                        st.write(''.join(map(str, i)))
                elif flag2 != []:
                    i = (flag2[0])
                    result = str(''.join(map(str, i)))
                    if flag_option == result:
                        insert_CDWS_LEAGUE_flag_option(flag_option,rememmberr,id)
                        df = to_append
                        size = NumberOfRows(df)
                        size = len(df)
                        list1 = [0] * size
                        for i in range(0,size):
                            list1[i] = id
                        df['user_id'] = list1
                        to_append.to_sql('CDWS_BATCH_temp',con=conn,if_exists='append')
                        a = view_all_CDWS__LEAGUE_flag_record(id)
                        st.success("Processed data you selected: : ")
                        for i in a:
                            st.write(''.join(map(str, i)))


                        st.success("Datas processes  successfully !!")
                        st.dataframe(to_append)

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

        try:
            if st.checkbox("Viusalise data !!!"):
                flag = return_id_CDWS_BATCH(temp_save)
                if flag != []:
                    if int(temp_save) > 0:
                        flag_option = return_id_CDWS__LEAGUE_flag_option(temp_save)
                        temp_filter = ''.join(flag_option[0])
                        if flag_option !=[]:
                            if temp_filter == 'Club':
                                df = pd.read_sql_query('SELECT * FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
                                df_save = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"]]
                            
                                st.error("Visualization the club expenses from 2000 to now")
                                st.error("Without inflation rate")
                                brush = alt.selection(type='interval')
                            
                                points = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    y='Expenditures',
                                    color=alt.condition(brush, 'Club', alt.value('lightgray'))
                                ).add_selection(
                                    brush
                                )
                            
                                bars = alt.Chart(df_save).mark_bar().encode(
                                    y='Club',
                                    color='Club',
                                    x='sum(Expenditures)'
                                ).transform_filter(
                                    brush
                                )
                            
                                st.write(points & bars)
                                ###########################################################################

                                nearest = alt.selection(type='single', nearest=True, on='mouseover',fields=['Expenditures'], empty='none')

                                # The basic line
                                line = alt.Chart(df_save).mark_line(interpolate='basis').encode(
                                    x='Arrivals',
                                    y='Expenditures',
                                    color='Club'
                                )

                                # Transparent selectors across the chart. This is what tells us
                                # the x-value of the cursor
                                selectors = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    opacity=alt.value(0),
                                ).add_selection(
                                    nearest
                                )

                                # Draw points on the line, and highlight based on selection
                                points = line.mark_point().encode(
                                    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
                                )

                                # Draw text labels near the points, and highlight based on selection
                                text = line.mark_text(align='left', dx=5, dy=-5).encode(
                                    text=alt.condition(nearest, 'Expenditures', alt.value(' '))
                                )

                                # Draw a rule at the location of the selection
                                rules = alt.Chart(df_save).mark_rule(color='gray').encode(
                                    x='Arrivals',
                                ).transform_filter(
                                    nearest
                                )

                                # Put the five layers into a chart and bind the data
                                a = alt.layer(
                                    line, selectors, points, rules, text
                                ).properties(
                                    width=600, height=300
                                )
                                st.write(a)
                                ##############
                                ##############
                                ##############
                                # Graph 2. 

                                st.error("Visualization the club expenses from 2000 to now")
                                st.error("With inflation rate")
                                brush1 = alt.selection(type='interval')
                            
                                points1 = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    y='Inflacion_Expenditures',
                                    color=alt.condition(brush1, 'Club', alt.value('lightgray'))
                                ).add_selection(
                                    brush1
                                )
                            
                                bars1 = alt.Chart(df_save).mark_bar().encode(
                                    y='Club',
                                    color='Club',
                                    x='sum(Inflacion_Expenditures)'
                                ).transform_filter(
                                    brush1
                                )
                            
                                st.write(points1 & bars1)
                                ###########################################################################

                                nearest1 = alt.selection(type='single', nearest=True, on='mouseover',fields=['Inflacion_Expenditures'], empty='none')

                                # The basic line
                                line1 = alt.Chart(df_save).mark_line(interpolate='basis').encode(
                                    x='Arrivals',
                                    y='Inflacion_Expenditures',
                                    color='Club'
                                )

                                # Transparent selectors across the chart. This is what tells us
                                # the x-value of the cursor
                                selectors1 = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    opacity=alt.value(0),
                                ).add_selection(
                                    nearest1
                                )

                                # Draw points on the line, and highlight based on selection
                                points1 = line.mark_point().encode(
                                    opacity=alt.condition(nearest1, alt.value(1), alt.value(0))
                                )

                                # Draw text labels near the points, and highlight based on selection
                                text1 = line.mark_text(align='left', dx=5, dy=-5).encode(
                                    text=alt.condition(nearest1, 'Inflacion_Expenditures', alt.value(' '))
                                )

                                # Draw a rule at the location of the selection
                                rules1 = alt.Chart(df_save).mark_rule(color='gray').encode(
                                    x='Arrivals',
                                ).transform_filter(
                                    nearest1
                                )

                                # Put the five layers into a chart and bind the data
                                a1 = alt.layer(
                                    line1, selectors1, points1, rules1, text1
                                ).properties(
                                    width=600, height=300
                                )
                                st.write(a1)
################################    Income / Revenue
#   ["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"]
                                st.error("Visualization the club expenses from 2000 to now")
                                st.error("Without inflation rate")
                                brushR = alt.selection(type='interval')
                            
                                pointsR = alt.Chart(df_save).mark_point().encode(
                                    x='Departures',
                                    y='Income',
                                    color=alt.condition(brushR, 'Club', alt.value('lightgray'))
                                ).add_selection(
                                    brushR
                                )
                            
                                barsR = alt.Chart(df_save).mark_bar().encode(
                                    y='Club',
                                    color='Club',
                                    x='sum(Income)'
                                ).transform_filter(
                                    brushR
                                )
                            
                                st.write(pointsR & barsR)
                                ###########################################################################

                                nearest = alt.selection(type='single', nearest=True, on='mouseover',fields=['Income'], empty='none')

                                # The basic line
                                line = alt.Chart(df_save).mark_line(interpolate='basis').encode(
                                    x='Departures',
                                    y='Income',
                                    color='Club'
                                )

                                # Transparent selectors across the chart. This is what tells us
                                # the x-value of the cursor
                                selectors = alt.Chart(df_save).mark_point().encode(
                                    x='Departures',
                                    opacity=alt.value(0),
                                ).add_selection(
                                    nearest
                                )

                                # Draw points on the line, and highlight based on selection
                                points = line.mark_point().encode(
                                    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
                                )

                                # Draw text labels near the points, and highlight based on selection
                                text = line.mark_text(align='left', dx=5, dy=-5).encode(
                                    text=alt.condition(nearest, 'Income', alt.value(' '))
                                )

                                # Draw a rule at the location of the selection
                                rules = alt.Chart(df_save).mark_rule(color='gray').encode(
                                    x='Departures',
                                ).transform_filter(
                                    nearest
                                )

                                # Put the five layers into a chart and bind the data
                                a = alt.layer(
                                    line, selectors, points, rules, text
                                ).properties(
                                    width=600, height=300
                                )
                                st.write(a)
                                ##############
                                ##############
                                ##############
                                # Graph 2. 

                                st.error("Visualization the club expenses from 2000 to now")
                                st.error("With inflation rate")
                                brush1 = alt.selection(type='interval')
                            
                                points1 = alt.Chart(df_save).mark_point().encode(
                                    x='Departures',
                                    y='Inflacion_Income',
                                    color=alt.condition(brush1, 'Club', alt.value('lightgray'))
                                ).add_selection(
                                    brush1
                                )
                            
                                bars1 = alt.Chart(df_save).mark_bar().encode(
                                    y='Club',
                                    color='Club',
                                    x='sum(Inflacion_Income)'
                                ).transform_filter(
                                    brush1
                                )
                            
                                st.write(points1 & bars1)
                                ###########################################################################

                                nearest1 = alt.selection(type='single', nearest=True, on='mouseover',fields=['Inflacion_Income'], empty='none')

                                # The basic line
                                line1 = alt.Chart(df_save).mark_line(interpolate='basis').encode(
                                    x='Departures',
                                    y='Inflacion_Income',
                                    color='Club'
                                )

                                # Transparent selectors across the chart. This is what tells us
                                # the x-value of the cursor
                                selectors1 = alt.Chart(df_save).mark_point().encode(
                                    x='Departures',
                                    opacity=alt.value(0),
                                ).add_selection(
                                    nearest1
                                )

                                # Draw points on the line, and highlight based on selection
                                points1 = line.mark_point().encode(
                                    opacity=alt.condition(nearest1, alt.value(1), alt.value(0))
                                )

                                # Draw text labels near the points, and highlight based on selection
                                text1 = line.mark_text(align='left', dx=5, dy=-5).encode(
                                    text=alt.condition(nearest1, 'Inflacion_Expenditures', alt.value(' '))
                                )

                                # Draw a rule at the location of the selection
                                rules1 = alt.Chart(df_save).mark_rule(color='gray').encode(
                                    x='Departures',
                                ).transform_filter(
                                    nearest1
                                )

                                # Put the five layers into a chart and bind the data
                                a1 = alt.layer(
                                    line1, selectors1, points1, rules1, text1
                                ).properties(
                                    width=600, height=300
                                )
                                st.write(a1)

                                st.success("Viusalise  Datas")
                            elif temp_filter == 'State':
                                st.write(temp_filter)
                                df = pd.read_sql_query('SELECT * FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
                                df_save = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"]]
                            
                                st.dataframe(df_save)
                                brush = alt.selection(type='interval')
                            
                                points = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    y='Expenditures',
                                    color=alt.condition(brush, 'State', alt.value('lightgray'))
                                ).add_selection(
                                    brush
                                )
                            
                                bars = alt.Chart(df_save).mark_bar().encode(
                                    y='State',
                                    color='State',
                                    x='sum(Expenditures)'
                                ).transform_filter(
                                    brush
                                )
                            
                                st.write(points & bars)
                                ###########################################################################
                            
                                nearest = alt.selection(type='single', nearest=True, on='mouseover',fields=['Expenditures'], empty='none')
                            
                                # The basic line
                                line = alt.Chart(df_save).mark_line(interpolate='basis').encode(
                                    x='Arrivals',
                                    y='Expenditures',
                                    color='State'
                                )
                            
                                # Transparent selectors across the chart. This is what tells us
                                # the x-value of the cursor
                                selectors = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    opacity=alt.value(0),
                                ).add_selection(
                                    nearest
                                )
                            
                                # Draw points on the line, and highlight based on selection
                                points = line.mark_point().encode(
                                    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
                                )
                            
                                # Draw text labels near the points, and highlight based on selection
                                text = line.mark_text(align='left', dx=5, dy=-5).encode(
                                    text=alt.condition(nearest, 'Expenditures', alt.value(' '))
                                )
                            
                                # Draw a rule at the location of the selection
                                rules = alt.Chart(df_save).mark_rule(color='gray').encode(
                                    x='Arrivals',
                                ).transform_filter(
                                    nearest
                                )
                            
                                # Put the five layers into a chart and bind the data
                                a = alt.layer(
                                    line, selectors, points, rules, text
                                ).properties(
                                    width=600, height=300
                                )
                                st.write(a)

                                st.success("Viusalise  Datas")
                            elif temp_filter == 'Competition':
                                st.write(temp_filter)
                                df = pd.read_sql_query('SELECT * FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
                                df_save = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"]]
                            
                                st.dataframe(df_save)
                                brush = alt.selection(type='interval')
                            
                                points = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    y='Expenditures',
                                    color=alt.condition(brush, 'Competition', alt.value('lightgray'))
                                ).add_selection(
                                    brush
                                )
                            
                                bars = alt.Chart(df_save).mark_bar().encode(
                                    y='Competition',
                                    color='Competition',
                                    x='sum(Expenditures)'
                                ).transform_filter(
                                    brush
                                )
                            
                                st.write(points & bars)
                                ###########################################################################
                            
                                nearest = alt.selection(type='single', nearest=True, on='mouseover',fields=['Expenditures'], empty='none')
                            
                                # The basic line
                                line = alt.Chart(df_save).mark_line(interpolate='basis').encode(
                                    x='Arrivals',
                                    y='Expenditures',
                                    color='Competition'
                                )
                            
                                # Transparent selectors across the chart. This is what tells us
                                # the x-value of the cursor
                                selectors = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    opacity=alt.value(0),
                                ).add_selection(
                                    nearest
                                )
                            
                                # Draw points on the line, and highlight based on selection
                                points = line.mark_point().encode(
                                    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
                                )
                            
                                # Draw text labels near the points, and highlight based on selection
                                text = line.mark_text(align='left', dx=5, dy=-5).encode(
                                    text=alt.condition(nearest, 'Expenditures', alt.value(' '))
                                )
                            
                                # Draw a rule at the location of the selection
                                rules = alt.Chart(df_save).mark_rule(color='gray').encode(
                                    x='Arrivals',
                                ).transform_filter(
                                    nearest
                                )
                            
                                # Put the five layers into a chart and bind the data
                                a = alt.layer(
                                    line, selectors, points, rules, text
                                ).properties(
                                    width=600, height=300
                                )
                                st.write(a)

                                st.success("Viusalise  Datas")
                            elif temp_filter == 'Season':
                                st.write(temp_filter)
                                df = pd.read_sql_query('SELECT * FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
                                df_save = df[["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"]]
                            
                                st.dataframe(df_save)
                                brush = alt.selection(type='interval')
                            
                                points = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    y='Expenditures',
                                    color=alt.condition(brush, 'Season', alt.value('lightgray'))
                                ).add_selection(
                                    brush
                                )
                            
                                bars = alt.Chart(df_save).mark_bar().encode(
                                    y='Season',
                                    color='Season',
                                    x='sum(Expenditures)'
                                ).transform_filter(
                                    brush
                                )
                            
                                st.write(points & bars)
                                ###########################################################################
                            
                                nearest = alt.selection(type='single', nearest=True, on='mouseover',fields=['Expenditures'], empty='none')
                            
                                # The basic line
                                line = alt.Chart(df_save).mark_line(interpolate='basis').encode(
                                    x='Arrivals',
                                    y='Expenditures',
                                    color='Season'
                                )
                            
                                # Transparent selectors across the chart. This is what tells us
                                # the x-value of the cursor
                                selectors = alt.Chart(df_save).mark_point().encode(
                                    x='Arrivals',
                                    opacity=alt.value(0),
                                ).add_selection(
                                    nearest
                                )
                            
                                # Draw points on the line, and highlight based on selection
                                points = line.mark_point().encode(
                                    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
                                )
                            
                                # Draw text labels near the points, and highlight based on selection
                                text = line.mark_text(align='left', dx=5, dy=-5).encode(
                                    text=alt.condition(nearest, 'Expenditures', alt.value(' '))
                                )
                            
                                # Draw a rule at the location of the selection
                                rules = alt.Chart(df_save).mark_rule(color='gray').encode(
                                    x='Arrivals',
                                ).transform_filter(
                                    nearest
                                )
                            
                                # Put the five layers into a chart and bind the data
                                a = alt.layer(
                                    line, selectors, points, rules, text
                                ).properties(
                                    width=600, height=300
                                )
                                st.write(a)

                                st.success("Viusalise  Datas")
                else:
                    st.warning("file not found")
                    st.info("Please procces data again !!")
        except Exception as e:
          st.write("Error, please resart Visaulsation checkboc !! ") 

