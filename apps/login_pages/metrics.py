import streamlit as st
from apps.login_pages.metrics_apps import EFPA,EFPA_BATCH
def app():
    st.title('Metrics')
    st.write('Welcome to app1')
    PAGES = {
        "Processed Data by average league EXPEND for player ARRIVALS": EFPA,
        "BATCH Data by average league EXPEND for player ARRIVALS": EFPA_BATCH      
        }
    st.title('Meni')
    selection = st.selectbox("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()