import streamlit as st

import streamlit as st
from apps.login_pages.club_apps import CDWS,CDWS_BATCH,DCTAS,DCTAS_BATCH
def app():
    st.title('Metrics for  LEAGUES')
    st.write('Welcome to app1')
    PAGES = {
        "IN Progress -> Processed Data by Data CLUBS statistic without   SESONS": CDWS,
        "BATCH Data by Data CLUBS statistic without   SESONS": CDWS_BATCH,
        "Processed Data by Data CLUBS statistic through all   SESONS":DCTAS,
        "NE RADI JOŠ -> BATCH Data by Data CLUBS statistic through all   SESONS":DCTAS_BATCH 
        }
    st.title('Meni')
    selection = st.selectbox("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()