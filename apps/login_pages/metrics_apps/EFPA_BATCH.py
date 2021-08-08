from numpy.core.numeric import identity
import streamlit as st
import pandas as pd
import numpy as np
from functions import *
from League_functions.EFPA_func import*
from database import *
import altair as alt

def app():
    st.title('2. function EFPA_BATCH  process function')
    st.write('Welcome to metrics')
    username = return_username()
    i = (username[0])
    res = str(''.join(map(str, i)))
    return_user_idd = return_user_id(res)
    st.write("")
    i = (return_user_idd[0])
    temp_save = int(''.join(map(str, i)))
    delite_temp_user(res)
    col1,col2 = st.beta_columns(2)
    with col1:

        st.info(" For restart data you must delete data and start over !!!")
        if st.checkbox("Process data "):
            create_EFPA_BATCH_temp()
            #create_EFPA__LEAGUE_table()
            df = pd.read_sql('SELECT * FROM League_datas', conn)
            df_new = df[["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]]
            to_append,rememmberr,flag_option = EFPA_MAIN(df_new)
            columns = ["Order_of_Expend","Club","State","Competition","Expenditures","Income","Arrivals","Departures","Balance","inflation_Expenditure","inflation_Income","inflation_Balance"]    
            my_form = st.form(key = "form123")
            submit = my_form.form_submit_button(label = "Submit")
            if submit:
                                
                columns = ["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]
                st.dataframe(to_append)                                
                return_user_idd = return_user_id(res)
                i = (return_user_idd[0])
                id = str(''.join(map(str, i)))
                create_EFPA_LEAGUE_flag_option()
                flag2 = return_id_EFPA__LEAGUE_flag_option(id)
                if flag2 == []:
                    insert_EFPA_LEAGUE_flag_option(flag_option,id)
                elif flag2 != []:
                    st.write(flag2,"flag2")
                    i = (flag2[0])
                    result = str(''.join(map(str, i)))
          
                    st.write("flag_option :::: ",flag_option,"result :::: ",result)
                    rem_columns = ["Name_of_Legue","user_id"]
                    if flag_option == result:
                        insert_EFPA_LEAGUE_flag_option(flag_option,id)
                        df = to_append
                        size = NumberOfRows(df)
                        size = len(df)
                        list1 = [0] * size
                        for i in range(0,size):
                            list1[i] = id
                        df['user_id'] = list1
                        to_append.to_sql('EFPA_BATCH_temp',con=conn,if_exists='append')
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
           
            flag_id = return_id_EFPA_BATCH(temp_save)
            if flag_id == []:
                flag2 = return_id_EFPA_BATCH_temp(temp_save)
                if flag2 != []:
                    if int(temp_save) > 0:
                        df = pd.read_sql('SELECT * FROM EFPA_BATCH_temp', conn)
                        df_save = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION","user_id"]]
                        st.write("save")
                        st.dataframe(df_save)
                        df_save.to_sql('EFPA_BATCH_table',con=conn,if_exists='append')
                        delite_EFPA_BATCH_temp(temp_save)
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
                flag = return_id_EFPA_BATCH(temp_save)
                if flag != []:
                    if int(temp_save) > 0:
                        df = pd.read_sql_query('SELECT * FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(temp_save),conn)
                        df_new = df[["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]]
                        st.markdown(get_table_download_link_csv(df_new), unsafe_allow_html=True)
                        st.success("Export Datas")
                else:
                    st.warning("file not found")
                    st.info("Please procces data again !")

       # Delite datas 
        my_form_delite = st.form(key = "form_Delite")
        submit = my_form_delite.form_submit_button(label = "Delite datas")
        if submit:
            flag = return_id_EFPA_BATCH(temp_save)                             
            if flag != []:
                if int(temp_save) > 0 :
                    delite_EFPA_BATCH(temp_save)
                    delite_EFPA_LEAGUE_flag_option(temp_save)
                    #delite_EFPA_BATCH_temp(temp_save)
                    st.success("Delite Datas")
                    st.info("Please procces data")
            else:
                st.warning("file not found")
                st.info("Please procces data again !") 