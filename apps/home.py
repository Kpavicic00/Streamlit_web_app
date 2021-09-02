
from numpy.core.numeric import NaN
from numpy.core.numerictypes import _typedict
import streamlit as st 
import marshal
import pandas as pd
import numpy as np
from sqlite3.dbapi2 import paramstyle
#import bcrypt
from functions import check_email,make_password,check_hashes,GETCoefficients,remove_duplicates
from database import create_usertable,add_user_data,check_double_email,check_double_username,login_user,check_userdatatable
#import datetime
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
#import sqlite3
#import time
from database import*

import os
import altair as alt
#import duckdb
import streamlit.components.v1 as components
import sqlite3
import os
#import bar_chart_race as bcr
#import base64
#import re



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
#import bar_chart_race as bcr
from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#import seaborn as sns
import time
import io
import altair as alt
# from altair import Chart, X, Y, Axis, SortField, OpacityValue
# from altair.expr import datum, if_
# from vega_datasets import data
# import altair as alt
# from vega_datasets import data
from datetime import datetime
from html_temp import *
#from plotnine import ggplot, aes, geom_line
import PIL.Image as Image
from pathlib import Path
from PIL import UnidentifiedImageError
#import cv2
from streamlit import caching
from html_temp import*
from functions import*
import pandas as pd
import base64
from PIL import Image
import textwrap
from io import StringIO
from io import BytesIO
from PIL import Image
from database import*
from keras.preprocessing.image import array_to_img
# from keras.preprocessing.image import load_img
# from keras.preprocessing.image import img_to_array
# from keras.preprocessing.image import array_to_img



def app():
    st.write("post home !! test alpha")
    blog_articles = st.text_area("Post Articles here",height=250,key='dasdsa')
    st.write(type(blog_articles))
    if blog_articles == '':
        st.write("empty")
    df = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}"'.format(1),conn)
    df_new = df[['id_post','author','user_id','title','article','img','postdate','read_time']]
    post__id = df_new['id_post'].unique() 
    st.write(post__id)
    #if blog_articles
    #create_post_table_temp_MAIN()


    #conn = sqlite3.connect('data_new.db', check_same_thread=False)

    # a = return_post_id_for_image(1,1)
    # lsita_post_id = []
    # for i in a:
    #     temp = (str(''.join(map(str, i))))  
    #     lsita_post_id.append(int(temp))
    # #st.write(lsita_post_id)

    # df = pd.read_sql_query('SELECT * FROM table_Image',conn)
    # df = df[['Image_id','blog_table_id','id_post','user_id','width','height']]
    # check_for_nan = df['height'].isnull()
    # arraa = check_for_nan.tolist()

    # counter = 0
    # temp = 0
    # for i in arraa:
    #     if i == False:   
    #         df.loc[counter,'blog_table_id']=lsita_post_id[temp]
    #         temp +=1
    #     counter +=1
    # #create_IMAGE_FINAL()
    # df.to_sql('IMAGE_FINAL',con=conn,if_exists='append')



    # st.dataframe(df)


    # for i in range(0,2):
    #     if df.loc[i,'width'].isnull() == False:
    #         df.loc[i,'blog_table_id'] = lsita_post_id[i]
    #         counter +=1
    # st.dataframe(df)



    #.write(len(df_new))
    # for i in lsita_post_id:
    #     df.loc[df['id_post'] == 1, df['blog_table_id']] = i
    # counter = 0
    # gg = len(df_new)
    # for i in range(0,gg+1):
    #     i+1
    #     #df_new['blog_table_id'][i] = lsita_post_id[counter]
    #     df_new['0']['blog_table_id']= lsita_post_id[counter]
    #     counter +=1
    #df_new[0]['blog_table_id']= 1
    #st.dataframe(df)

    #df.set_value('C', 'x', 10)
   # a = df_new['id_post'].unique() 

    # for i in lsita_post_id:
    #     temp = int(i)
    #     dbdata = temp
    #     for j in i:

    #         update_post_id_image(dbdata,1,1)


            # c.execute('UPDATE table_Image SET blog_table_id=? WHERE user_id =? AND id_post = ? AND blog_table_id IS NULL',(temp,1,1))
            # c.fetchall()
        #conn.commit()



            #cur.execute("""INSERT INTO TESTTABLE VALUES(?, ?)""", (tmp1, tmp2))


    # post_id = int(temp)
    # update_post_id_image(post_id,1,1)
    # df = pd.read_sql_query('SELECT * FROM table_Image',conn)
    # df_new = df[['img','user_id','id_post','width','height']]
    # # st.write(df_new['user_id'][0])

    # height = df['height'][0]
    # width = df['width'][0]
    # imagee = df_new['img'][0]

    # nova_lista = marshal.loads(imagee)   

    # #st.write(nova_lista)
    # arr = np.array(nova_lista) 
    # st.write(arr)
    # oimg = convert_bytes_to_img(width,height,arr)
    # st.image(oimg)
    # st.write("h and w",height,width)
    # st.write("test",type(imagee))

    # data = np.zeros((height, width, 4), dtype=np.uint8)
    # data[0:2560, 0:2560] = imagee
    # st.write("type : ",type(imagee))
    # st.write(type(imagee.decode('utf-8')))
    
    # with open(imagee, "r") as f:
    #      header = f.readline()
    # img = convert_bytes_to_img(width,height,header)
    # pw_bytes = imagee.encode('utf-8')
    # object_image = convert_bytes_to_img(width,height,imagee)
    # st.image(object_image)


    #temp_img = return_img(1,1)
    # temp_height = return_height(1,1)
    # temp_width = return_width(1,1)

    # #st.write(temp_img[0])
    # #st.write(temp_img)
    # lista_img = 0
    # for i in temp_img:
    #     lista_img = ((''.join(map(str, i))))
    #     st.write("i::::::::::::::::         ",type(i))

    
    # #st.write(lista_img[0])
    # a = image_to_byte_array(imagee)
    # st.write("test ",type(a))
    # st.write(a)
    # oimg = convert_bytes_to_img(width,height,a)
    # st.image(oimg)
    # st.write(type(lista_img))
    # # encoded_string = lista_img.encode()
    # # byte_array = bytearray(encoded_string)
    # st.write("2. tip",type(lista_img.decode("utf-8")))


    # lista_height = 0
    # for i in temp_height:
    #     lista_height = (str(''.join(map(str, i))))   

    # lista_width = 0
    # for i in temp_width:
    #     lista_width = (str(''.join(map(str, i))))   

    # imagee = convert_bytes_to_img(int(lista_width),int(lista_height),lista_img.decode("utf-8"))
    # st.image(imagee)

    
    # i = (temp_img[0])
    # res = str(''.join(map(str, i)))
    #st.write(lista_height)
    # for i in lista_height:
    #     st.write(i)
    # df = pd.read_sql_query('SELECT * FROM table_Image',conn)
    # df_new = df[['img','user_id','id_post','width','height']]
    # st.dataframe(df_new['user_id'][0])
    
    # create_counter()
    
    # def png_bytes_to_numpy(png):
    #     return np.array(Image.open(BytesIO(png)))

    # @st.cache
    # def load_image(image_file):
    #     img = Image.open(image_file)
    #     return img
    # def image_to_byte_array(image:Image):
    #     imgByteArr = io.BytesIO()
    #     image.save(imgByteArr, format=image.format)
    #     imgByteArr = imgByteArr.getvalue()
    #     return imgByteArr

    # def convert_img_to_byte(uploaded_file):
    #     dimenzije = Image.open(uploaded_file)
    #     width, height = dimenzije.size
    #     img = load_image(uploaded_file)
    #     a = image_to_byte_array(img)
    #     bytes_temp = png_bytes_to_numpy(a)
    #     return width, height, bytes_temp

    # def convert_bytes_to_img(width,height,a):

    #     data = np.zeros((height, width, 4), dtype=np.uint8)
    #     data[0:2560, 0:2560] = a # red patch in upper left
    #     img = Image.fromarray(data, 'RGBA')
    #     return img



    # def writeimage(uploaded_file):
    #     with open(uploaded_file,"wb") as f:
    #         a = f.write(uploaded_file.getbufferd())
    #         return a

#############################




    # uploaded_file = st.file_uploader("Choose a image file",type=['png','jpeg','jpg '],key='321321')
    # if uploaded_file is not None:
    #     file_details = {"FileName": uploaded_file.name,"FileType":uploaded_file.type}

    #     width,height,a = convert_img_to_byte(uploaded_file)
    #     st.write("type 1 test",type(a))
    #     #st.write(a)
    #     # create_image_table()
    #     # add_image_to_table(a,1,1,width,height)
    #     oimg = convert_bytes_to_img(width,height,a)
    #     st.image(oimg)
    #     st.write("test to string !!!")

    #     nova_lista = a.tolist()
    #     data = marshal.dumps(nova_lista)
    #     st.write("type rjesenje ",type(data))

    #     create_image_table()
    #     add_image_to_table(data,1,1,width,height)

    #     nova_lista = marshal.loads(data)   

    #     #st.write(nova_lista)
    #     arr = np.array(nova_lista) 
    #     st.write(arr)
    #     oimg = convert_bytes_to_img(width,height,arr)
    #     st.image(oimg)


#############################
        #testa = a.tostring()
        # st.write("type 2 test",type(testa))
        # #st.write(testa)
        # novi_test = png_bytes_to_numpy(testa)
        # st.write(novi_test)

        # dimenzije = Image.open(uploaded_file)
        # width, height = dimenzije.size
        # st.write("# sirina i visinaa : ",width,height)
        # #dimenzije.close()
        
        # # st.write(file_details)
        # # st.write(type(file_details))
        # #add_counter(file_details,1)
        
        # img = load_image(uploaded_file)
        # a = image_to_byte_array(img)
        # bytes_temp = png_bytes_to_numpy(a)
        # width,height,a = convert_img_to_byte(uploaded_file)
        #st.write("width",width,"    ::::::: ",height)
        #add_counter(a,1,width,height)

        # def convert_bytes_to_img(width,height,a):
        #     data = np.zeros((height, width, 4), dtype=np.uint8)
        #     data[0:2560, 0:2560] = a # red patch in upper left
        #     img = Image.fromarray(data, 'RGBA')
        #     return img


        # w = width
        # h = height
        # #data = [np.zeros((224,224,3) ,dtype=np.uint8).astype(object), np.zeros((224,224,3), dtype=np.uint8).astype(object), np.zeros((224,224,13), dtype=np.uint8).astype(object)]
        # data = np.zeros((h, w, 4), dtype=np.uint8)
        # data[0:2560, 0:2560] = a # red patch in upper left
        # img = Image.fromarray(data, 'RGBA')
        # img = convert_bytes_to_img(width,height,a)
        # st.image(img)
        #st.write(bytes_temp)


        # arr = np.array(bytes_temp, dtype =np.uint8)
        # ts = arr.tostring()
        # st.write("# type -> string",type(ts))
  
        # gfg = arr.tobytes()
        # st.write("## Type",type(gfg))

        # b = base64.b64decode(gfg)
        # st.write(" # type 222",type(gfg))
        # slika = Image.open(io.BytesIO(b))
        # st.write("# tip slike test",type(slika))
        # img2 = load_image(gfg)
        # st.image(img2)


        # l = np.arange(1, 100, dtype=np.uint8)
        # print(l.dtype) 

        # img_test = np.asarray(bytearray(bytes_temp.read()), dtype=np.uint8)
        #img_test = np.zeros(bytes_temp, np.uint8)


        # b=array_to_img(gfg)
        # st.image(b)


        # f = open(a, 'rb')
        # image_bytes = f.read()

        # image = np.array(Image.open(io.BytesIO(image_bytes))) 
        # st.image(image)

        # image = Image.open(img).convert("RGBA")
        # st.image(image)
        # text_file = open("sample.txt", "wb")
        # n = text_file.write(a)
        # text_file.close()
        # st.write("type",type(a))
        # add_counter(a,1)

        # with open ("sample.txt", "r") as myfile:
        #     data = myfile.read().splitlines()
        # st.write("############ type",type(data))

        # by = a.decode("utf-8")
        # stream = StringIO(by)
        

        # image = Image.open(a).convert("RGBA")
        # st.image(image)
        
    # file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    # bytes = file_bytes.tobytes()
    # st.write("type",type(bytes))
#     im = Image.open(uploaded_file)
#     im_resize = im.resize((500, 500))
#     buf = io.BytesIO()
#     im_resize.save(buf, format='JPEG')
#     byte_im = buf.getvalue()
# #     file = 'deer.jpg'
#     image = open(file, 'rb')
#     image_read = image.read()
#     image_64_encode = base64.encodebytes(image_read) #encodestring also works aswell as decodestring

#    # print('This is the image in base64: ' + str(image_64_encode))

#     image_64_decode = base64.decodebytes(image_64_encode) 
#     image_result = open(uploaded_file, 'wb') # create a writable image and write the decoding result
#     image_result.write(image_64_decode)
#     st.image(image_result)
    # if uploaded_file is not None:
    #     # Convert the file to an opencv image.
    #     st.write("type(uploaded_file)",uploaded_file)
    #     file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    #     bytes = file_bytes.tobytes()
    #     #temp_string = file_bytes.decode("utf-8") 
    #     #.write(" type file_bytes",type(bytes))
    #     #insert_image(bytes,2)
    #     test = np.frombuffer(bytes, dtype=np.uint8)
    #     opencv_image = cv2.imdecode(test, 1)
    #     st.image(opencv_image, channels="BGR")

#########################################
    # uploaded_file2 = st.file_uploader("Choose a image file")
    # if uploaded_file2 is not None:
    #     data = uploaded_file2.read()
    #     img = load_img(data)
    #     img_array = img_to_array(img)
    #     img_pil = array_to_img(img_array)
    #     st.image(img_pil)

#######################################

    create_post_table_temp_MAIN()
    # conn = sqlite3.connect('data_new.db', check_same_thread=False)
    # c = conn.cursor()
    # path_file = 'datas/sportska_kubska_statsitika_OBRDENO.csv'
    # def DataFrameFuncClubs(filePath):

    #     colls = ["Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]
    #     dat = pd.read_csv(filePath,header = None , names = colls)
    #     return dat
    # # def DataFrameFunc(filePath):

    # # #     colls = ["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]
    # # #     dat = pd.read_csv(filePath,header = None , names = colls)
    # # #     return dat
    # save_df = DataFrameFuncClubs(path_file)
    # sqlite_table = "Clubs_datas"
    # save_df.to_sql(sqlite_table, con=conn, if_exists='fail')


    #st.title('View all posts !!!')
    a = " Welcome to the Football data revolution !!"
    b = " Here you are chance to investigate and explore football financial data about leagues and clubs across Europe and the World"
    c = " Data are collected by Transfmarket.com and data records by the Expenditures of top 100 clubs every season and top 25/26 Leagues by Expenditures"
    d = " With expending by club or league are recorded how many players come or leave club and league, also recorded Profit and revenue or income"
    e = " We take the coefficient of inflation and calculate for every cash transfer and thus have the opportunity to see the role we call the ‘inflation rate’ and see the monetary amount and the real value of a monetary transaction that took place 15 or more years ago."
    p = " We hope you enjoy and indulge your research imagination, also here you can explore, prove and argue your theses. We’ve provided you with interactive graos, data processing tools that handle a bunch and a bunch of different data, and allowed you to create your own post and share your thoughts with us. To use our software you need to register and log in, and the fun begins"
    
    powerd_by_datavision = "Powerd by Data.Vision"
    st.markdown(home_message.format(a,b,c,d,e,p,powerd_by_datavision),unsafe_allow_html=True)

    if st.checkbox(" Read some post !! "):
        a  = return_post_id_temp_MAIN()
        dfsve = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN',conn)
        df_user = pd.read_sql_query('SELECT DISTINCT user_id FROM blog_table_temp_MAIN',conn)
        temp_user = df_user['user_id'].unique() 
        df_post = pd.read_sql_query('SELECT DISTINCT id_post FROM blog_table_temp_MAIN',conn)
        temp_post = df_post['id_post'].unique() 
        post_lista =[]
        for i in temp_post:
            post_lista.append(i)


        user_lista =[]
        for i in temp_user:
            user_lista.append(i)
        d = {}
        for i in user_lista:
            for j in post_lista:
                df = pd.read_sql_query('SELECT author,read_time FROM blog_table_temp_MAIN WHERE id_post = "{}"'.format(int(j)),conn)
                Total = df['read_time'].sum()
                add_if_key_not_exist(d,j,Total)


        df = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN',conn)
        df_new = df[['id_post','author','user_id','title','article','img','postdate']]
        a = df_new['id_post'].unique() 
        lista =[]
        for i in a:
            lista.append(i)
        caching.clear_cache()
        for j in user_lista:
            df = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}"'.format(int(j)),conn)
            for i in lista:
                df_print = pd.read_sql_query('SELECT * FROM blog_table_temp_MAIN WHERE user_id = "{}" AND id_post = "{}"'.format(int(j),int(i)),conn)
                df_a_d_t = pd.read_sql_query('SELECT DISTINCT title,author,postdate FROM blog_table_temp_MAIN WHERE user_id = "{}" AND id_post = "{}"'.format(int(j),int(i)),conn)
                if df_a_d_t.empty != True :             
                    temp_reading_time = d.get(i)
                    st.markdown(head_message_temp.format(df_a_d_t['title'][0],df_a_d_t['author'][0],df_a_d_t['postdate'][0],temp_reading_time),unsafe_allow_html=True)
                    for i in range(0,len(df_print)):
                        if type(df_print['img'][i]) != str and df_print['img'][i] != None:
                            test = np.frombuffer(df_print['img'][i], dtype=np.uint8)
                            opencv_image = cv2.imdecode(test, 1)
                            st.image(opencv_image, channels="BGR")
                        elif type(df_print['article'][i]) == str and df_print['article'][i] != None:
                            st.markdown(full_message_temp.format(df_print['article'][i]),unsafe_allow_html=True)


        caching.clear_cache()

    if st.checkbox(" Take look and see some awesome interactive dashboard !! "):
        st.info("Still update !!!")












   