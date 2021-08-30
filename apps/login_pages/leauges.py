import streamlit as st
from apps.login_pages.league_apps import EFPA,EFPA_BATCH,IFPD,IFPD_BATCH,BFPD,BFPD_BATCH,DFLS,DFLS_BATCH,DCWS,DCWS_BATCH
def app():
    st.title('Metrics for  LEAGUES')
    st.write('Welcome to app1')
    PAGES = {
        "Processed Data by average league EXPEND for player ARRIVALS": EFPA,
        "Custom options for previous function ": EFPA_BATCH,
        "Processed Data by average league INCOME for player DEPARTURES":IFPD,
        "Custom options for previous function":IFPD_BATCH,
        "Processed Data by average league BALANCE for player DEPARTURES":BFPD, 
        "Custom options for previous function":BFPD_BATCH,
        "Processed Data by average LEAGUE by AVG SESONS statistic":DFLS,
        "Custom options for previous function":DFLS_BATCH,
        "Processed Data by average -> LEAGUE by YEAR statistic":DCWS,
        "Custom options for previous function":DCWS_BATCH    
        }
    st.title('Meni')
    selection = st.selectbox("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

    # Custom options for previous function
    # Data by average league EXPEND for player ARRIVALS

    # Data by average league INCOME for player DEPARTURES

    # BATCH Data by average league BALANCE for player DEPARTURES

    # BATCH Data by average LEAGUE by AVG SESONS statistic

    # BATCH Data by average -> LEAGUE by YEAR statistic