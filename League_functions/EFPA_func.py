from numpy.core.einsumfunc import einsum
import streamlit as st 
import pandas as pd
import numpy as np
from functions import*



def EFPA_base(DFrame):


    count = NumberOfRows(DFrame)

    # reserving arraya for cast
    Name_of_leauge = [0] * count
    Year_of_Season = [0] * count
    arrivals_players = [0] * count
    Nationality_leuge = [0] * count
    expenditures = [0] * count

    koef = [0] * count
    int_koef = [0] * count
    expend_inflation = [0] * count
    ###############################################################################

    # cast data from Data to float, int and str
    DFrame["Competition"].astype(str) # ind 0
    DFrame["Year"].astype(int) # ind 1
    DFrame["Arrivals"].astype(int) # ind 2
    DFrame["Nationality"].astype(str) # ind 3
    DFrame["Expenditures"].astype(int) # ind 4
    # st.write("DFrame Competition ")
    # st.dataframe(DFrame["Competition"])
    a = NumberOfRows(DFrame)
    st.write("a",a)
    i = 0
    for i in range(0,count):
        Name_of_leauge[i] = DFrame["Competition"][i] # ind 0
        Year_of_Season[i] = DFrame["Year"][i] # ind 1
        arrivals_players[i] = DFrame["Arrivals"][i] # ind 2
        Nationality_leuge[i] = DFrame["Nationality"][i] # ind 3
        expenditures[i] = DFrame["Expenditures"][i] # ind 4
    ###################################################
        # st.dataframe(Nationality_leuge)


    # the inflation calculation coefficient operatorion
    for i in range(0,count):
        temp = Year_of_Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a
    ###############################################################################

    # save coefficient to specific array
    for i in range(0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp
        ###############################################################################

     # operation of inflation
    for i in range(0,count):
        a = float(expenditures[i])*int_koef[i]
        expend_inflation[i] = round(a,2)
        ###############################################################################

    # conversion to numpy
    np_Expend = np.asarray(expenditures, dtype='float64') # ind 0
    np_arrivals_players = np.asarray(arrivals_players, dtype='int64') # ind 1
    np_Year_of_Season = np.asarray(Year_of_Season, dtype='int64') # ind 2
    npNationality_leuge = np.asarray(Nationality_leuge, dtype='str') # ind 3
    np_Name_of_leauge = np.asarray(Name_of_leauge, dtype='str') # ind 4
    np_expend_inflation = np.asarray(expend_inflation, dtype='float64') # ind 5
    ###############################################################################

    niz = np.stack((np_Name_of_leauge,np_Year_of_Season,npNationality_leuge,np.round((np_Expend/np_arrivals_players),2),np.round((np_expend_inflation/np_arrivals_players),2)), axis = -1)
                        ###############################################################################
    #a =  sorted(niz, key=lambda niz: str(niz[0]),reverse = False) 

    a = inputMeni_sort(niz)
    #a = Input_chose_of_GetAVGExpendFORplayerArrivals(niz)
    # convert from stack with values to data for dataFrame
    data = np.array(a)
    # set to DataFrame
    df = pd.DataFrame(data)
    # name of labels for head or names of collums
    df.columns = ["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]

    return df


def EFPA_MAIN(DFrame):
    #dframe = EFPA_base(DFrame)

    nDFRAME = EFPA_base(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)


    #reserving the number of elements in a row
    Name_of_leauge  = [0] * count # indx 0
    Year_of_Season = [0] * count # indx 1
    Nationality = [0] * count # indx 2
    Expend_by_player = [0] * count # indx 3
    Expend_Inflation_by_player = [0] * count # indx 4

    # cast from DataFrame to str int an float
    nDFRAME["Name_of_Legue"].astype(str)# ind 0
    nDFRAME["Year"].astype(int)# ind 1
    nDFRAME["Nationality"].astype(str)# ind 2
    nDFRAME["Expend_by_player"].astype(float)# ind 3
    nDFRAME["Expend_INFLACION"].astype(float)# ind 4
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):
        Name_of_leauge[i] =  nDFRAME["Name_of_Legue"][i] # indx 0
        Year_of_Season[i] = nDFRAME["Year"][i] # indx 1
        Nationality[i] = nDFRAME["Nationality"][i] # indx 2
        Expend_by_player[i] = nDFRAME["Expend_by_player"][i] # indx 3
        Expend_Inflation_by_player[i] = nDFRAME["Expend_INFLACION"][i] # indx 4
        ###############################################################################

    # conversion to numpy
    np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
    np_Year_of_Season = np.asarray(Year_of_Season,dtype='int64')# indx 1
    np_Nationality = np.asarray(Nationality,dtype='str')# indx 2
    np_Expend_by_player= np.asarray(Expend_by_player, dtype = 'float64') # indx 3
    np_Expend_Inflation_by_player = np.asarray(Expend_Inflation_by_player,dtype='float64') # indx 4
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Name_of_leauge,np_Year_of_Season,np_Nationality,np_Expend_by_player,np_Expend_Inflation_by_player),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]

    listLEAUGE = np_Name_of_leauge.tolist()
    listLEAUGE = remove_duplicates(listLEAUGE)
    listLEAUGE.sort()
    ###############################################################################

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Year_of_Season
    listYear_of_Season = np_Year_of_Season.tolist()
    listYear_of_Season = remove_duplicates(listYear_of_Season)
    listYear_of_Season.sort()
    ###############################################################################

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Nationality
    listNationality = np_Nationality.tolist()
    listNationality = remove_duplicates(listNationality)
    listNationality.sort()

    ###############################################################################
    #######################################################################################################################################


    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker 
    # ,"Year_of_Season statistic","Nationality statistic"


    colums,col2 = st.beta_columns(2)

    with colums:
        flag = 0
        flagTemp = '0'
        task = st.selectbox("Task",["LEAUGE statistic","Year_of_Season statistic","Nationality statistic"],key='key_options')
        st.write("type(task)",type(task))

        if task == "LEAUGE statistic":
            flag = 1
            cont_LEAUGE = 0
        
            st.write("Meni  LEAUGE statistic")
            for i in range(0,len(listLEAUGE)):
                cont_LEAUGE += 1
            options = ['0'] * cont_LEAUGE
        
            for i in range(0,len(listLEAUGE)):
                options[i] = listLEAUGE[i]

            remeber = st.selectbox("Select Dynamic", options= list(options))
            flagTemp = remeber
            cnt = 1
            for i in range(0,len(listLEAUGE)):
                if listLEAUGE[i] == remeber:
                    break
                cnt +=1

        elif task == "Year_of_Season statistic":

            flag = 2
            cont_LEAUGE = 0
        
            st.write("Meni  Year_of_Season statistic")
            for i in range(0,len(listYear_of_Season)):
                cont_LEAUGE += 1
            options = ['0'] * cont_LEAUGE

            for i in range(0,len(listYear_of_Season)):
                options[i] = listYear_of_Season[i]

            remeber = st.selectbox("Select Dynamic", options= list(options))
            flagTemp = remeber
            cnt = 1
            for i in range(0,len(listYear_of_Season)):
                if listYear_of_Season[i] == remeber:
                    break
                cnt +=1
        
        elif task == "Nationality statistic":

            flag = 3
            cont_LEAUGE = 0
        
            st.write("Meni  listNationality")
            for i in range(0,len(listNationality)):
                cont_LEAUGE += 1
            options = ['0'] * cont_LEAUGE
        
            for i in range(0,len(listNationality)):
                options[i] = listNationality[i]

            remeber = st.selectbox("Select Dynamic", options= list(options))
            flagTemp = remeber
            cnt = 1
            for i in range(0,len(listNationality)):
                if listNationality[i] == remeber:
                    break
                cnt +=1


    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    # name of LEAUGE
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                bro +=1
    ###############################################################################

    # count number of rows in date frame
    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][1]) == flagTemp :
                bro +=1
    ###############################################################################

    #   count number of rows in date frame
    #   Nationality
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                bro +=1
    ###############################################################################

    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from State user chose options

    # name of LEAUGE
    y = 0
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][0]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################

    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][1]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################

    # Nationality
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                y+=1
    ###############################################################################

    # reserving the number of elements in a row
    niz_N1 = [0]*bro

    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz1,np_niz2,np_niz1,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        y+=1
    ###############################################################################

    

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ["Name_of_Legue","Year","Nationality","Expend_by_player","Expend_INFLACION"]
    return df_new     
    

def inputMeni_sort(DFN):
    st.subheader("meni")
    col1,col2 = st.beta_columns(2)

    with col1:
        while True:
        
            options = st.selectbox("Task",["Sort data BY Name of League","Sort data BY Nationality","Sort data BY Year of Season","Sort data BY Expend by player","Sort data BY Expend + Inflation by player"],key='key22')
            if options == "Sort data BY Name of League":
                st.subheader("Sort data BY Name of League")
                b = Chose_sort()
                a =  sorted(DFN, key=lambda DFN: str(DFN[0]),reverse = b) 
                return a
                break

            elif options == "Sort data BY Year of Season":
                st.subheader("Sort data BY Year of Season")
                b = Chose_sort()
                a = sorted(DFN, key=lambda DFN: int(DFN[1]),reverse = b) 
                return a
                break    
        
            elif options == "Sort data BY Nationality":
                st.subheader("Sort data BY Nationality")
                b = Chose_sort()
                a = sorted(DFN, key=lambda DFN: str(DFN[2]),reverse = b) 
                return a
                break

            elif options == "Sort data BY Expend by player":
                st.subheader("Sort data BY Expend by player")
                b = Chose_sort()
                a = sorted(DFN, key=lambda DFN: float(DFN[3]),reverse = b) 
                return a
                break

            elif options == "Sort data BY Expend + Inflation by player":
                st.subheader("Sort data BY Expend + Inflation by player")
                b = Chose_sort()
                a = sorted(DFN, key=lambda DFN: float(DFN[4]),reverse = b) 
                return a
                break

def Chose_sort():
    while True:

        sort_option = st.selectbox("Option",["Clasic sort","Reverse sort"],key='key33')

        if sort_option == "Clasic sort":
            a = False
            return a
            break
        elif sort_option == "Reverse sort":
            a = True
            return a
            break



def stringToList(string):
    listRes = list(string.split(" "))
    return listRes
