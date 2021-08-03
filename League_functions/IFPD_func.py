import streamlit as st 
import pandas as pd
import numpy as np
from functions import*
import base64



def IFPD_base(DFrame):
    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Nationality = [0] * count
    Income = [0] * count
    Departures = [0] * count
    leauge = [0] * count
    Season = [0] * count
    koef = [0] * count
    CUT =  [0] * count
    interception = [0] * count
    int_koef = [0] * count
    ###############################################################################

    # cast DataFrame rows to folat and int
    DFrame["Income"].astype(np.int)
    DFrame["Departures"].astype(np.int)
    DFrame["Nationality"].astype(np.str)
    DFrame["Competition"].astype(np.str)
    DFrame["Year"].astype(np.int)
    ###############################################################################

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Income[i] = DFrame["Income"][i]
        Departures[i] = DFrame["Departures"][i]
        leauge[i] = DFrame["Competition"][i]
        Season[i] = DFrame["Year"][i]
        Nationality[i] = DFrame["Nationality"][i]
        ###############################################################################

    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a
        ###############################################################################

    for i in range(0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp
        ###############################################################################

    for i in range(0,count):
        a = float(Income[i])*int_koef[i]
        interception[i] = round(a,2)
        ###############################################################################


    # conversion to numpy
    np_Income = np.asarray(Income, dtype='float')
    np_Departures = np.asarray(Departures, dtype='int')
    npNationality = np.asarray(Nationality, dtype='str')
    np_Season = np.asarray(Season, dtype='int')
    npLeauge = np.asarray(leauge, dtype='str')
    np_CUT = np.asarray(CUT, dtype='float')
    np_Interception = np.asarray(interception, dtype='float')
    ###############################################################################

    np_CUT = np_Income/np_Departures
    np_CUT_inflation = np_Interception/np_Departures

    niz = np.stack((npLeauge,np_Season,npNationality,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)

    ###############################################################################
    a = input_Menisort(niz)
    # convert from stack with values to data for dataFrame
    data = np.array(a)
    # set to DataFrame
    df = pd.DataFrame(data)
    # name of labels for head or names of collums
    df.columns = ["Name_of_Legue","Year","Nationality","Income_by_player","Income_INFLACION"]
    ###############################################################################
    # return DataFrame with head an names of collums
    print(df)
    return df

def input_Menisort(DFN):
    st.subheader("Meni options :: ")
    #   ,"Sort data by Expend + Inflation by player"
        
    options = st.selectbox("Chose sort option by ::: ",["Sort data by Name of League","Sort data by Nationality","Sort data by Year of Season","Sort data by Income by player"])
    if options =="Sort data by Name of League":
        st.subheader("Sort data by Name of League")
        b = Chose_sort()
        a =  sorted(DFN, key=lambda DFN: str(DFN[0]),reverse = b) 
        return a
        

    elif options == "Sort data by Year of Season":
        st.subheader("Sort data by Year of Season")
        b = Chose_sort()
        a = sorted(DFN, key=lambda DFN: int(DFN[1]),reverse = b) 
        return a
            
        
    elif options == "Sort data by Nationality":
        st.subheader("Sort data by Nationality")
        b = Chose_sort()
        a = sorted(DFN, key=lambda DFN: str(DFN[2]),reverse = b) 
        return a
            

    elif options == "Sort data by Income by player":
        st.subheader("Sort data by Income by player")
        b = Chose_sort()
        a = sorted(DFN, key=lambda DFN: float(DFN[3]),reverse = b) 
        return a