import streamlit as st
from apps.login_pages.metrics_apps import EFPA,EFPA_BATCH,IFPD,IFPD_BATCH,BFPD,BFPD_BATCH,DFLS,DFLS_BATCH
def app():
    st.title('Metrics for  LEAGUES')
    st.write('Welcome to app1')
    PAGES = {
        "Processed Data by average league EXPEND for player ARRIVALS": EFPA,
        "BATCH Data by average league EXPEND for player ARRIVALS": EFPA_BATCH,
        "Processed Data by average league INCOME for player DEPARTURES":IFPD,
        "BATCH Data by average league INCOME for player DEPARTURES":IFPD_BATCH,
        "Processed Data by average league BALANCE for player DEPARTURES":BFPD, 
        "BATCH Data by average league BALANCE for player DEPARTURES":BFPD_BATCH,
        "Processed Data by average LEAGUE by AVG SESONS statistic":DFLS,
        "BATCH Data by average LEAGUE by AVG SESONS statistic":DFLS_BATCH    
        }
    st.title('Meni')
    selection = st.selectbox("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()