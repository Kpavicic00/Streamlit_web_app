import streamlit as st
from apps.login_pages.league_apps import EFPA,EFPA_BATCH,IFPD,IFPD_BATCH,BFPD,BFPD_BATCH,DFLS,DFLS_BATCH,DCWS,DCWS_BATCH
def app():
    st.title('Metrics for  LEAGUES')
    st.write('Welcome to app1')
    PAGES = {
        "DONE -> Processed Data by average league EXPEND for player ARRIVALS": EFPA,
        "DONE -> BATCH Data by average league EXPEND for player ARRIVALS": EFPA_BATCH,
        "DONE -> Processed Data by average league INCOME for player DEPARTURES":IFPD,
        "DONE -> BATCH Data by average league INCOME for player DEPARTURES":IFPD_BATCH,
        "DONE -> Processed Data by average league BALANCE for player DEPARTURES":BFPD, 
        "DONE -> BATCH Data by average league BALANCE for player DEPARTURES":BFPD_BATCH,
        "DONE -> Processed Data by average LEAGUE by AVG SESONS statistic":DFLS,
        "DONE -> BATCH Data by average LEAGUE by AVG SESONS statistic":DFLS_BATCH,
        "DONE -> Processed Data by average -> LEAGUE by YEAR statistic":DCWS,
        "DONE -> BATCH Data by average -> LEAGUE by YEAR statistic":DCWS_BATCH    
        }
    st.title('Meni')
    selection = st.selectbox("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()