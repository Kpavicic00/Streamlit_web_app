import streamlit as st
from database import *
from PIL import Image
import numpy as np 
def app():
    st.title('Post')
    username = return_username()
    i = (username[0])
    res = str(''.join(map(str, i)))
    return_user_idd = return_user_id(res)
    i = (return_user_idd[0])
    temp_save = int(''.join(map(str, i)))
    create_post_table()
    #blog_author = st.text_input("Enther Author name : ",max_chars = 50)

    blog_title = st.text_input("Enther Post title: ")
    blog_articles = st.text_area("Post Articles here",height=250)
    blog_post_date = st.date_input("Date")
        # Function to Read and Manupilate Images
    def load_image(img):
        im = Image.open(img)
        image = np.array(im)
        return image

    # Uploading the File to the Page
    uploadFile = st.file_uploader(label="Upload image", type=['jpg', 'png'])

    # Checking the Format of the page
    if uploadFile is not None:
        # Perform your Manupilations (In my Case applying Filters)
        img = load_image(uploadFile)
        st.image(img)
        st.write("Image Uploaded Successfully")
    else:
        st.write("Make sure you image is in JPG/PNG Format.")
    if st.button("Add"):
        add_data_to_post(res,blog_title,blog_articles,img,blog_post_date,temp_save)
        st.success("Post {} saved".format(blog_title))

    st.image(img)