import streamlit as st
from apps.login_pages.league_apps import EFPA,EFPA_BATCH,IFPD,IFPD_BATCH,BFPD,BFPD_BATCH,DFLS,DFLS_BATCH,DCWS,DCWS_BATCH
def app():
    st.title('Metrics for  LEAGUES')
    st.write('Welcome to app1')
    PAGES = {
        "DO -> Processed Data by average league EXPEND for player ARRIVALS": EFPA,
        "DO -> BATCH Data by average league EXPEND for player ARRIVALS": EFPA_BATCH,
        "DO -> Processed Data by average league INCOME for player DEPARTURES":IFPD,
        "DO -> BATCH Data by average league INCOME for player DEPARTURES":IFPD_BATCH,
        "DO -> Processed Data by average league BALANCE for player DEPARTURES":BFPD, 
        "DO -> BATCH Data by average league BALANCE for player DEPARTURES":BFPD_BATCH,
        "DO -> Processed Data by average LEAGUE by AVG SESONS statistic":DFLS,
        "DO -> BATCH Data by average LEAGUE by AVG SESONS statistic":DFLS_BATCH,
        "DO -> Processed Data by average -> LEAGUE by YEAR statistic":DCWS,
        "IN Progress -> BATCH Data by average -> LEAGUE by YEAR statistic":DCWS_BATCH    
        }
    st.title('Meni')
    selection = st.selectbox("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()