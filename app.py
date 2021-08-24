
import streamlit as st


from pyngrok import ngrok
from multiapp import MultiApp
from apps import home, SingUp, model, LogIn, LogIn, Search , About , TandC_FAQ# import your app modules here


app = MultiApp()


st.markdown("""
# Multi-Page App Football Data app
""")

#    menu = ["Home", "LogIn", "SingUp", "Search", "About", "Terms and Conditions: FAQ"]

# Home rjeseno Sučelje urediti  Task # 6
# LogIn rjeseno UREDITI dodatno opcije !!! Task #1
# SingUp rijeseno !!! UREDITI UI !!! Task #2
# About rijeseno !!! Task #3
# Search rijeseno !!! Task #4
# Terms and Conditions: FAQ rijeseno !!! Task #5


# Add all your application here
app.add_app("Home", home.app)
app.add_app("SingUp", SingUp.app)
app.add_app("Model", model.app)
app.add_app("LogIn",LogIn.app)
app.add_app("Search",Search.app)
app.add_app("About",About.app)
app.add_app("Terms and Conditions: FAQ",TandC_FAQ.app)
# The main app
app.run()