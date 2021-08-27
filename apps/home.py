
from numpy.core.numerictypes import _typedict
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
import sqlite3
import time
from database import*

import os
import altair as alt
import duckdb
import streamlit.components.v1 as components
import sqlite3
import os
import bar_chart_race as bcr
import base64
import re



# save_df = DataFrameFuncClubs('datas/sportska_kubska_statsitika_OBRDENO.csv')
# conn = sqlite3.connect('data.db', check_same_thread=False)
# c = conn.cursor()
# sqlite_table = "Clubs_datas"
# save_df.to_sql(sqlite_table, con=conn, if_exists='fail')

rem_niz_CLUB_SEASON = []
rem_niz_CLUB_TROUGHT_SEASON = []
coef = 'file.txt'
fp_league = 'Ligaska_KONACAN_STAS.csv'
fp_clubs = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
save_csv_Expend = "sportska_kubska_statsitika_OBRDENO.csv"
save_csv_Expend_BATCH = 'datas/BATCH_sportska_kubska_statsitika_OBRDENO.csv'
#-----------------------------------------
f_datas = 'datas/exported/GetAVGExpendFORplayerArrivals.csv'
#------------------------------------
# from apps.login_pages import app1,app2
#import login_pages.app1
import bar_chart_race as bcr
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
import time
import io
import altair as alt
from altair import Chart, X, Y, Axis, SortField, OpacityValue
from altair.expr import datum, if_
from vega_datasets import data
import altair as alt
from vega_datasets import data
from datetime import datetime
from html_temp import *
from plotnine import ggplot, aes, geom_line
import PIL.Image as Image
from pathlib import Path
from PIL import UnidentifiedImageError
import cv2




def app():
    head_message_temp ="""
	<div style="background-color:silver;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
	<h6>Author:{}</h6> 		
	<h6>Post Date: {}</h6>		
	</div>
    """


    full_message_temp ="""
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<p style="text-align:justify;color:black;padding:10px">{}</p>
	</div>
	"""

    st.title('Post')
    df = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN',conn)
    df_new = df[['id_post','author','user_id','title','article','img','postdate']]
    st.dataframe(df_new)
    a = df_new['id_post'].unique() 
    # st.write(df_new['user_id'][0])
    # st.write(a)
    # lista =[]
    # for i in a:
    #     lista.append(i)

    # st.write(lista)

    #for i in lista:
    #st.write("i ::: ",int(i))
    df = pd.read_sql_query('SELECT id_post FROM blog_table_temp_MAIN WHERE user_id = "{}"'.format(1),conn)
    a = df['id_post'].unique() 
    st.dataframe(a)
    lista =[]
    for i in a:
        lista.append(i)
        

    st.write(lista)
    for i in lista:
        df_print = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}" AND id_post = "{}"'.format(1,int(i)),conn)
        st.markdown(head_message_temp.format(df_print['title'][0],df_print['author'][0],df_print['postdate'][0]),unsafe_allow_html=True)

        for i in range(0,len(df_print)):
            if type(df_print['img'][i]) != str and df_print['img'][i] != None:
                #st.write("df_print['img'][i]",df_print['img'][i])
                test = np.frombuffer(df_print['img'][i], dtype=np.uint8)
                opencv_image = cv2.imdecode(test, 1)
                st.image(opencv_image, channels="BGR")
                #st.markdown(title_temp.format(st.image(opencv_image, channels="BGR")),unsafe_allow_html=True)
            elif type(df_print['article'][i]) == str and df_print['article'][i] != None:
                st.markdown(full_message_temp.format(df_print['article'][i]),unsafe_allow_html=True)
        st.write("______________________________-")
    


    # df_new = df_new[df_new.groupby(['id_post', 'author'])['id_post'].transform('nunique') > 3]
    # st.dataframe(df_new)

    # for i in range(0,len(df_new)):
    #     i df_new[]















    # post_idd = return_post_id(1)
    # listt = []
    # for i in post_idd:
    #     a = int(''.join(map(str, i))) 
    #     listt.append(a)
    # st.write("max",max(listt))
    #df = pd.DataFrame(columns=['id_post','author','user_id','title','article','img','postdate']) 
    #df = ['1',None,None,None,None,None,'1']
    #create_post_table_temp_MAIN()

    # df = pd.DataFrame(columns=['id_post','autohor','blog_title','blog_aricle','image','post_date','user_id']) 
    # df = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[['id_post','author','user_id','title','article','img','postdate']]
    # st.dataframe(df_new)
    # df_new.to_sql('blog_table_temp_MAIN',con=conn,if_exists='append')
    # df = pd.DataFrame()
    # post__id = 1
    # temp_save = 2
    # blog_title = 3
    # #df = [post__id,res,temp_save,blog_title,blog_articles,None,blog_post_date]
    # df = df.append({'id_post': post__id, 'author': temp_save, 'user_id': blog_title, 'title':22,}, ignore_index=True)
    # st.dataframe(df)
    # te = (post_idd[0])
    # temp_id_post = int(''.join(map(str, te)))
    # st.write("temp_id_post",temp_id_post)
    # post_check_exisit = return_post_id(1)
    # st.write("post_check_exisit",post_check_exisit)

    #df = pd.DataFrame(columns=['id_post','autohor','blog_title','blog_aricle','image','post_date','user_id']) 
    # df = pd.read_sql_query('SELECT * FROM blog_table_temp WHERE user_id = "{}"'.format(1),conn)
    # df_new = df[['id_post','author','user_id','title','article','img','postdate']]
    # st.dataframe(df_new)
    # df_new.to_sql('blog_table',con=conn,if_exists='append')
    

    # username = return_username()
    # i = (username[0])
    # res = str(''.join(map(str, i)))
    # return_user_idd = return_user_id(res)
    # i = (return_user_idd[0])
    # temp_save = int(''.join(map(str, i)))
    # create_post_table()

    # # id_post-> 1 , author_name , user_id -> temp_save
    # if st.checkbox("Add title "):
    #     blog_title = st.text_input("Enther Post title: ")
    #     if blog_title  == "":

    #         st.warning("Please first Insert Blog Title !!")

    #     elif blog_title != "":

    #         if st.checkbox("add articles and images"):
    #             blog_option = st.radio("Chose a option ",["Add article","Add Image","Leave"], key='dsa' )
    #             if blog_option == "Add article":
    #                 blog_articles = st.text_area("Post Articles here",height=250,key='dasdsa')
    #                 blog_post_date = st.date_input("Date")
    #                 if st.button("Add"):
    #                     df = pd.DataFrame(columns=['id_post','author','user_id','title','article','img','postdate']) 
    #                     df.loc[1] = ['1',res,temp_save,blog_title,blog_articles,None,blog_post_date]
    #                     df.to_sql('blog_table',con=conn,if_exists='append')
    #                     st.dataframe(df)
    #                     st.success("Articles added")
    #             elif blog_option == "Add Image":
    #                 image_file = st.file_uploader("Upload a image ",type=['png','jpeg','jpg'],key='dsadsa')
    #                 if image_file is not None:
    #                     file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    #                     bytes = file_bytes.tobytes()
    #                     blog_post_date = st.date_input("Date")
    #                     if st.button("Add"):
    #                         #add_data_to_post('1',res,temp_save,blog_title,None,bytes,'datum:213321')
    #                         #df = pd.DataFrame()
    #                         df = pd.DataFrame(columns=['id_post','author','user_id','title','article','img','postdate']) 
    #                         df.loc[1] = ['1',res,temp_save,blog_title,None,bytes,blog_post_date]
    #                         df.to_sql('blog_table',con=conn,if_exists='append')
    #                         st.success("Image added")


    # df = pd.read_sql_query('SELECT * FROM blog_table WHERE user_id = "{}"'.format(temp_save),conn)
    # df_new = df[['id_post','author','user_id','title','article','img','postdate']]

    # st.write("dataframe : df_new")
    # st.dataframe(df_new)
    # #st.write(df_new['img'][0])
    # autor = df_new['author'][0]
    # datum = df_new['postdate'][0]
    # title = df_new['title'][0]
    # df_2 = df_new[['article', 'img']]
    # st.dataframe(df_2)
    # num = []
    # #st.write(num)
    # for i in range(0,len(df_2)):
        
    #     if df_2['article'][i] != None:
    #         num.append(df_2['article'][i])
    #         #st.write(i)
    #     if df_2['article'][i] == None:
    #         if df_2['img'][i] != None:
    #             num.append(df_2['img'][i])
    #             #st.write(i)



    # head_message_temp ="""
	# <div style="background-color:silver;padding:10px;border-radius:5px;margin:10px;">
	# <h4 style="color:white;text-align:center;">{}</h1>
	# <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
	# <h6>Author:{}</h6> 		
	# <h6>Post Date: {}</h6>		
	# </div>
    # """


    # full_message_temp ="""
	# <div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
	# 	<p style="text-align:justify;color:black;padding:10px">{}</p>
	# </div>
	# """
    # # df_save = pd.DataFrame({'col':num})
    # # st.dataframe(df_save)
    # st.markdown(head_message_temp.format(title,autor,datum),unsafe_allow_html=True)
    # for i in range(0,len(num)):
    #     #st.write(type(i))

    #     if type(num[i]) != str:
    #         #st.write(i)
    #         test = np.frombuffer(num[i], dtype=np.uint8)
    #         opencv_image = cv2.imdecode(test, 1)
    #         st.image(opencv_image, channels="BGR")
            
    #         #st.markdown(title_temp.format(st.image(opencv_image, channels="BGR")),unsafe_allow_html=True)
    #     elif type(num[i]) == str:
    #         #st.write(i)
    #         st.markdown(full_message_temp.format(num[i]),unsafe_allow_html=True)

            



    # a = return_id_post(1,1)
    # st.write(a)
    # test = 1
    # # if st.checkbox("Add title new "):
    # #     blog_title = st.text_input("Enther Post title: ",key='update')
    # if st.button("Delite"):
    #     delite_post(1)
    # b = return_id_post(1,1)
    # st.write(b)
    # remove_nan = series. dropna()
    # print(remove_nan)
    # df_2["Value"] = df_2["article"] +" "+ df_2["img"]
    # st.dataframe(df_2)
        # add_paragraf(article)  and Image
        
        # st.info("Add post or image or just leave")
        # blog_option = st.radio("Chose a option ",["Add article","Add Image","Leave"], key='dsa' )
        # if blog_option == "Add article":
        #         blog_articles = st.text_area("Post Articles here",height=250,key='dasdsa')
        #         # add article
        #         if st.button("add data"):
        #                 st.success("Image added")
        # elif blog_option == "Add Image":
        #         image_file = st.file_uploader("Upload a image ",type=['png','jpeg','jpg'],key='dsadsa')
        #         if image_file is not None:
        #             file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
        #             bytes = file_bytes.tobytes()
        #             if st.button("add data"):
        #                 st.success("Image added")
        # elif blog_option == "Leave":
        #     while True:
        #         st.write("End")
        #         break

    
    # #blog_articles = st.text_area("Post Articles here",height=250)
    # blog_post_date = st.date_input("Date")
    # image_file = st.file_uploader("Upload a image ",type=['png','jpeg','jpg'])
    # if image_file is not None:
    #     file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    #     bytes = file_bytes.tobytes()

        # if st.button("Add Data"):

        #     df.loc[1] = ['1',res,blog_title,blog_articles,bytes,blog_post_date,temp_save]
            # df['id_post'] = 1
            # df['autohor'] = res
            # df['blog_title'] = blog_title
            # df['blog_aricle'] = blog_articles
            # df['image'] = bytes
            # df['post_date'] = blog_post_date
            # df['user_id'] = temp_save
            #add_data_to_post(res,blog_title,blog_articles,blog_post_date,temp_save)
    #         st.subheader("Upload Images")
            

    # st.dataframe(df)
    # temp = df.loc[1,'image']

    # test = np.frombuffer(temp, dtype=np.uint8)
    
    # opencv_image = cv2.imdecode(test, 1)
    # st.image(opencv_image, channels="BGR")








    # uploaded_file = st.file_uploader("Choose a image file")
    
    # create_images()

    # if uploaded_file is not None:
    #     # Convert the file to an opencv image.
    #     st.write("type(uploaded_file)",uploaded_file)
    #     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    #     bytes = file_bytes.tobytes()
    #     #temp_string = file_bytes.decode("utf-8") 
    #     st.write(" type file_bytes",type(bytes))
        
    #     insert_image(bytes,2)

    #     test = np.frombuffer(bytes, dtype=np.uint8)

        
    #     opencv_image = cv2.imdecode(test, 1)

    #     st.image(opencv_image, channels="BGR")
  
    
    # a = return_img(1)

    # for i in a:
    #     #st.write(i[0]," ::",i[1])
    #     img = i[1]

    # test = np.frombuffer(img, dtype=np.uint8)
    
    # opencv_image = cv2.imdecode(test, 1)
    # st.image(opencv_image, channels="BGR")
