import streamlit as st
from html_temp import *

@st.cache
def app():
    # search nastaviti za sutra
    # kopirati pretrazivanje za post koje sam napravio 
    # anzurirati UI te podatke posrediti
    # stavio sam kod podataka 3 podatka za 
    # grcku super ligu i svicarsku
    # portugal /diynamo kyev probel
    # anzurirati 2019 komplet te ubaciti 2019,2020 i 2021 !!
    # deploaytri apliakciju
    st.markdown("Search")
    st.subheader("Search Articles")
	# search_term = st.text_input('Enter Search Term')
	# search_choice = st.radio("Field to Search By",("title","author"))
	
	# if st.button("Search"):
	# 	if search_choice == "title":
	# 		article_result = get_blog_by_title(search_term)
	# 	elif search_choice == "author":
	# 		article_result = get_blog_by_author(search_term)
	# 	for i in article_result:
	# 		b_author = i[0]
	# 		b_title = i[1]
	# 		b_article = i[2]
	# 		b_post_date = i[3]
	# 		st.text("Reading Time:{}".format(readingTime(b_article)))
	# 		st.markdown(head_message_temp.format(b_title,b_author,b_post_date),unsafe_allow_html=True)
	# 		st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)