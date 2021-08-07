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
    delite_temp_user(res)
    col1,col2 = st.beta_columns(2)
    with col1:

        #   df_save = pd.DataFrame()
        st.info(" For restart data you must delete data and start over !!!")
        # Processd data
        # to_append = [5, 6]
        # a_series = pd.Series(to_append, index = df.columns)
         # f = df.append(a_series, ignore_index=True)
        if st.checkbox("Process data "):
            create_EFPA_BATCH_temp()
            #create_EFPA__LEAGUE_table()
            df = pd.read_sql('SELECT * FROM League_datas', conn)
            df_new = df[["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]]
            to_append,rememmberr,flag_option = EFPA_MAIN(df_new)
            columns = ["Order_of_Expend","Club","State","Competition","Expenditures","Income","Arrivals","Departures","Balance","inflation_Expenditure","inflation_Income","inflation_Balance"]    
                         
        #st.dataframe(df_new)
        #a_leuge_DF = EFPA_MAIN(df_new)
        my_form = st.form(key = "form123")
        submit = my_form.form_submit_button(label = "Submit")
        if submit:
                                
            columns = ["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]
            st.dataframe(to_append)                                
            # to_append.to_sql('EFPA_BATCH_temp',con=conn,if_exists='append')

            ################
            return_user_idd = return_user_id(res)
            i = (return_user_idd[0])
            id = str(''.join(map(str, i)))
            #id = int(res)
            ###############
            

            create_EFPA_LEAGUE_flag_option()
            # return_user_idd = return_user_id(res)
            # i = (return_user_idd[0])
            # res = int(''.join(map(str, i)))
            # te = int(res)
            # flag = return_id_EFPA_table(te)
            # if flag == []:
            #     insert_EFPA_LEAGUE_flag_option(flag_option,id)
            #df = pd.DataFrame()
            #df = df.append({'flag_option': flag_option,'user_id': id}, ignore_index=True)
            #df.to_sql('EFPA_LEAGUE_flag_option',con=conn,if_exists='append')
            flag2 = return_id_EFPA__LEAGUE_table(id)
            if flag2 == []:
                insert_EFPA_LEAGUE_flag_option(flag_option,id)
            elif flag2 != []:
                st.write(flag2,"flag2")
                i = (flag2[0])
                result = str(''.join(map(str, i)))
                
                #flag_table = int(result)
            
                st.write("flag_option :::: ",flag_option,"result :::: ",result)
                rem_columns = ["Name_of_Legue","user_id"]
                if flag_option == result:
                    insert_EFPA_LEAGUE_flag_option(flag_option,id)
                    to_append.to_sql('EFPA_BATCH_temp',con=conn,if_exists='append')
                    #st.write("user_id",te,"LEAUGE",rememmberr)
                    #para = str(te)
                    #df = pd.DataFrame(columns=["Name_of_Legue","user_id"])
                    #df.columns = ["Name_of_Legue","user_id"]

                    #df = df.append({'user_id': para}, ignore_index=True)
                    st.write("Data frame test ")
                    #st.dataframe(df)
                    #if rememmberr
                    st.success("Datas processes  successfully !!")

                else:
                    st.warning("Please reppet your choose in search filter")
                    st.info("Leagues, Years and Nationality are different datas !!!")
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