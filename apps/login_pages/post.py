import streamlit as st
import os
import pandas as pd
import io
from io import BytesIO
import glob
import numpy as np
import sqlite3
import cv2
from database import *
from PIL import Image
from subprocess import Popen, PIPE
import numpy as np 
from streamlit import caching
from datetime import datetime

def app():
    
    
    username = return_username()
    # create_counter()
    
    i = (username[0])
    res = str(''.join(map(str, i)))
    return_user_idd = return_user_id(res)
    i = (return_user_idd[0])
    temp_save = int(''.join(map(str, i)))
    #st.write("temp_save",temp_save)
    create_post_table_temp_MAIN()
    # add_counter(1,temp_save)
    #delite_post_temp(temp_save)
    post_check_exisit = return_post_id(temp_save)
    #st.write("post_check_exisit",post_check_exisit)

    post_idd = return_post_id(temp_save)
    # if post_idd == []:
    #     postt_id = 1

    if post_check_exisit != []:
        #post_idd = return_post_id(temp_save)
        st.write(post_check_exisit)
        listt = []
        for i in post_check_exisit:
            a = int(''.join(map(str, i))) 
            listt.append(a)
        post__id = max(listt)
        i = int(post__id)
        st.write("post__id test !!",post__id)
        conn = sqlite3.connect('data.db', check_same_thread=False)
        create_post_id_temp()
        add_post_temp(i,temp_save)
        c = conn.cursor()
        caching.clear_cache()

        st.write("prije if granajnja : ",post__id)
    if post_check_exisit == []:
        df = pd.DataFrame(columns=['id_post','autohor','blog_title','blog_aricle','image','post_date','user_id']) 
        st.title('Create New Post')
        if st.checkbox("Add title "):
            blog_title = st.text_input("Enther Post title: ")
            if blog_title  == "":
                st.warning("Please first Insert Blog Title !!")
            elif blog_title != "":
                if st.checkbox("add articles and images"):
                    blog_option = st.selectbox("Chose a option ",["Add article","Add Image","Leave"], key='dsa' )
                    if blog_option == "Add article":
                        blog_articles = st.text_area("Post Articles here",height=250,key='dasdsa')
                        if blog_articles is not None:
                            if st.button("Add"):
                                df = pd.DataFrame()
                                df.insert(0,'id_post',['1'])
                                df.insert(0,'author',[res])
                                df.insert(0,'user_id',[temp_save])
                                df.insert(0,'title',[blog_title])
                                df.insert(0,'article',[blog_articles])
                                df.insert(0,'img',[None])
                                conn = sqlite3.connect('data.db', check_same_thread=False)
                                create_post_table()
                                df.to_sql('blog_table',con=conn,if_exists='append')
                                c = conn.cursor()
                                st.success("Articles added")
                                caching.clear_cache()
                    elif blog_option == "Add Image":
                        image_file = st.file_uploader("Upload a image ",type=['png','jpeg','jpg'],key='dsadsa1')
                        if image_file is not None:
                            file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
                            bytes = file_bytes.tobytes()
                            if st.button("Add"):
                                df = pd.DataFrame()
                                df.insert(0,'id_post',['1'])
                                df.insert(0,'author',[res])
                                df.insert(0,'user_id',[temp_save])
                                df.insert(0,'title',[blog_title])
                                df.insert(0,'article',[None])
                                df.insert(0,'img',[bytes])
                                conn = sqlite3.connect('data.db', check_same_thread=False)
                                create_post_table()
                                df.to_sql('blog_table',con=conn,if_exists='append')
                                c = conn.cursor()
                                st.success("Image added")
                                caching.clear_cache()
        if st.button("Save post"):
            conn = sqlite3.connect('data.db', check_same_thread=False)
            username = return_username()
            i = (username[0])
            res = str(''.join(map(str, i)))
            return_user_idd = return_user_id(res)
            i = (return_user_idd[0])
            temp_save = int(''.join(map(str, i)))
            create_post_table()      
            df = pd.read_sql_query('SELECT * FROM blog_table WHERE user_id = "{}"'.format(temp_save),conn)
            df_new = df[['id_post','author','user_id','title','article','img','postdate']]
            blog_post_date = st.date_input("Date",key='dsadsa2')
            size = len(df_new)
            list1 = [0] * size
            for i in range(0,size):
                list1[i] = str(blog_post_date)
            df_new['postdate'] = list1
            st.dataframe(df_new)
            df_new.to_sql('blog_table_temp_MAIN',con=conn,if_exists='append')
            delite_post(1)
            c = conn.cursor()
            caching.clear_cache()
            st.success("Post saved!")
        # if st.button("delite Post"):
        #     conn = sqlite3.connect('data.db', check_same_thread=False)
        #     delite_post(temp_save)
        #     delite_post_MAIN(temp_save)
            c = conn.cursor()

    elif post_check_exisit != []:
        # post_idd = return_post_id(temp_save)
        # st.write(post_idd)
        # listt = []
        # # for i in post_idd:
        # #     a = int(''.join(map(str, i))) 
        # #     listt.append(a)
        # post__id = 2
        # # post__id = max(listt) +1
        st.write("post__id",post__id)
        if st.checkbox("Add title "):
            blog_title = st.text_input("Enther Post title: ")
            if blog_title  == "":
                st.warning("Please first Insert Blog Title !!")
            elif blog_title != "":
                # post_idd = return_post_id(1)
                # listt = []
                # for i in post_idd:
                #     a = int(''.join(map(str, i))) 
                #     listt.append(a)
                # post__id = max(listt) +1
                # st.write("post__id",post__id)
                if st.checkbox("add articles and images"):
                    blog_option = st.radio("Chose a option ",["Add article","Add Image","Leave"], key='dsa' )
                    if blog_option == "Add article":
                        blog_articles = st.text_area("Post Articles here",height=250,key='dasdsa')
                        if st.button("Add"):
                            conn = sqlite3.connect('data.db', check_same_thread=False)
                            a = return_post_id_temp(temp_save)
                            listt = []
                            for i in a:
                                temp = int(''.join(map(str, i))) 
                                listt.append(temp)
                            temp2 = max(listt)
                            te = int(temp2) 
                            st.write("te test : ",te)
                            te = te +1
                            post__id = str(te)
                            #st.write("post_id second ",post__id)
                            df = pd.DataFrame()
                            df.insert(0,'id_post',[post__id])
                            df.insert(0,'author',[res])
                            df.insert(0,'user_id',[temp_save])
                            df.insert(0,'title',[blog_title])
                            df.insert(0,'article',[blog_articles])
                            df.insert(0,'img',[None])
                            create_post_table()
                            df.to_sql('blog_table',con=conn,if_exists='append')
                            c = conn.cursor()
                            st.success("Articles added")
                            caching.clear_cache()
                    elif blog_option == "Add Image":
                        image_file = st.file_uploader("Upload a image ",type=['png','jpeg','jpg'],key='dsadsa3')
                        if image_file is not None:
                            file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
                            bytes = file_bytes.tobytes()
                            if st.button("Add"):
                                conn = sqlite3.connect('data.db', check_same_thread=False)
                                a = return_post_id_temp(temp_save)
                                listt = []
                                for i in a:
                                    temp = int(''.join(map(str, i))) 
                                    listt.append(temp)
                                temp2 = max(listt)
                                te = int(temp2) 
                                te = te +1
                                st.write("te test : ",te)
                                post__id = str(te)
                                #st.write("post_id second ",post__id)
                                df = pd.DataFrame()
                                df.insert(0,'id_post',[post__id])
                                df.insert(0,'author',[res])
                                df.insert(0,'user_id',[temp_save])
                                df.insert(0,'title',[blog_title])
                                df.insert(0,'article',[None])
                                df.insert(0,'img',[bytes])
                                #conn = sqlite3.connect('data.db', check_same_thread=False)
                                create_post_table()
                                df.to_sql('blog_table',con=conn,if_exists='append')
                                c = conn.cursor()
                                st.success("Image added")
                                caching.clear_cache()
        if st.button("Save post"):
            conn = sqlite3.connect('data.db', check_same_thread=False)
            username = return_username()
            i = (username[0])
            res = str(''.join(map(str, i)))
            return_user_idd = return_user_id(res)
            i = (return_user_idd[0])
            temp_save = int(''.join(map(str, i)))
            create_post_table()      
            df = pd.read_sql_query('SELECT * FROM blog_table WHERE user_id = "{}"'.format(temp_save),conn)
            df_new = df[['id_post','author','user_id','title','article','img','postdate']]
            blog_post_date = st.date_input("Date",key='dsadsa4')
            size = len(df_new)
            list1 = [0] * size
            for i in range(0,size):
                list1[i] = str(blog_post_date)
            df_new['postdate'] = list1
            st.dataframe(df_new)
            df_new.to_sql('blog_table_temp_MAIN',con=conn,if_exists='append')
            delite_post_id_temp(temp_save)
            delite_post(1)
            c = conn.cursor()
            caching.clear_cache()
            st.success("Post saved!")


            # username = return_username()
            # i = (username[0])
            # res = str(''.join(map(str, i)))
            # return_user_idd = return_user_id(res)
            # i = (return_user_idd[0])
            # temp_save = int(''.join(map(str, i)))
            # create_post_table()
            # df = pd.read_sql_query('SELECT * FROM blog_table WHERE user_id = "{}"'.format(temp_save),conn)
            # df_new = df[['id_post','author','user_id','title','article','img','postdate']]
            # st.dataframe(df_new)
            # df_new.to_sql('blog_table_temp_MAIN',con=conn,if_exists='append')
            # delite_post(temp_save)
            # st.success("Post saved!")