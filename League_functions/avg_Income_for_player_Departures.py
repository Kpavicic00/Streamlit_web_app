from collections import Counter
from operator import itemgetter
from sort_functions import*
import numpy as np
import pandas as pd
import csv
import sys
from functions import *
from functions import DataFrameFunc

coef = 'file.txt'

# def GetAVGIncomeFORplayerDepartures(DFrame):

#     #count number of rows in date frame
#     count = NumberOfRows(DFrame)

#     #reserving the number of elements in a row
#     Nationality = [0] * count
#     Income = [0] * count
#     Departures = [0] * count
#     leauge = [0] * count
#     Season = [0] * count
#     koef = [0] * count
#     CUT =  [0] * count
#     interception = [0] * count
#     int_koef = [0] * count
#     ###############################################################################

#     # cast DataFrame rows to folat and int
#     DFrame["Income"].astype(np.int64)
#     DFrame["Departures"].astype(np.int64)
#     DFrame["Nationality"].astype(np.str)
#     DFrame["Competition"].astype(np.str)
#     DFrame["Year"].astype(np.int64)
#     ###############################################################################

#     #save values from the dateframe to a string
#     i = 0
#     for i in range(0,count):
#         Income[i] = DFrame["Income"][i]
#         Departures[i] = DFrame["Departures"][i]
#         leauge[i] = DFrame["Competition"][i]
#         Season[i] = DFrame["Year"][i]
#         Nationality[i] = DFrame["Nationality"][i]
#         ###############################################################################

#     for i in range(0,count):
#         temp = Season[i]
#         a = GETCoefficients(coef,temp)
#         koef[i] = a
#         ###############################################################################

#     for i in range(0,len(int_koef)):
#         temp = float(koef[i])
#         int_koef[i] = temp
#         ###############################################################################

#     for i in range(0,count):
#         a = float(Income[i])*int_koef[i]
#         interception[i] = round(a,2)
#         ###############################################################################


#     # conversion to numpy
#     np_Income = np.asarray(Income, dtype='float64')
#     np_Departures = np.asarray(Departures, dtype='int64')
#     npNationality = np.asarray(Nationality, dtype='str')
#     np_Season = np.asarray(Season, dtype='int64')
#     npLeauge = np.asarray(leauge, dtype='str')
#     np_CUT = np.asarray(CUT, dtype='float64')
#     np_Interception = np.asarray(interception, dtype='float64')
#     ###############################################################################

#     np_CUT = np_Income/np_Departures
#     np_CUT_inflation = np_Interception/np_Departures

#     niz = np.stack((npLeauge,np_Season,npNationality,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)

#     ###############################################################################
#     data = np.array(niz)
#     # set to DataFrame
#     df = pd.DataFrame(data)
#     # name of labels for head or names of collums
#     df.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Income by player|  ', '  Income + Inflation by player|  ']
#     ###############################################################################
#     # return DataFrame with head an names of collums
#     #print(df)
#     return df


def GetAVGExpendFORplayerArrivals(DFrame):

    # count number of rows in date frame
    #count = NumberOfRows(DFrame)
    count = 488 

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
    ###############################################################################

    #save values from the dateframe to a string
    i = 0
    for i in range(0,count):
        Name_of_leauge[i] = DFrame["Competition"][i] # ind 0
        Year_of_Season[i] = DFrame["Year"][i] # ind 1
        arrivals_players[i] = DFrame["Arrivals"][i] # ind 2
        Nationality_leuge[i] = DFrame["Nationality"][i] # ind 3
        expenditures[i] = DFrame["Expenditures"][i] # ind 4

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

    #a = Input_chose_of_GetAVGExpendFORplayerArrivals(niz)
    # convert from stack with values to data for dataFrame
    data = np.array(niz)
    # set to DataFrame
    df = pd.DataFrame(data)
    # name of labels for head or names of collums
    df.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Expend by player|  ', '  Expend + Inflation by player|  ']
    ###############################################################################
    # return DataFrame with head an names of collums
    #print(df)
    return df

# BATCH for  specific filtring data from estraction data from function GetAVGIncomeFORplayerDepartures
#  --> for League datas
def BATCH_for_GetAVGExpendFORplayerArrivals(DFrame,value):

    DFrame = 0
    #value =0
    
    # DataFrame to ecstract data
    nDFRAME = GetAVGExpendFORplayerArrivals(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)


    #reserving the number of elements in a row
    Name_of_leauge  = [0] * count # indx 0
    Year_of_Season = [0] * count # indx 1
    Nationality = [0] * count # indx 2
    Expend_by_player = [0] * count # indx 3
    Expend_Inflation_by_player = [0] * count # indx 4

    # cast from DataFrame to str int an float
    nDFRAME["    Name of League |  "].astype(str)# ind 0
    nDFRAME["   Year of Season |  "].astype(int)# ind 1
    nDFRAME["    Nationality |  "].astype(str)# ind 2
    nDFRAME["    Expend by player|  "].astype(float)# ind 3
    nDFRAME["  Expend + Inflation by player|  "].astype(float)# ind 4

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):
        Name_of_leauge[i] =  nDFRAME["    Name of League |  "][i] # indx 0
        Year_of_Season[i] = nDFRAME["   Year of Season |  "][i] # indx 1
        Nationality[i] = nDFRAME["    Nationality |  "][i] # indx 2
        Expend_by_player[i] = nDFRAME["    Expend by player|  "][i] # indx 3
        Expend_Inflation_by_player[i] = nDFRAME["  Expend + Inflation by player|  "][i] # indx 4

    # conversion to numpy
    np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
    np_Year_of_Season = np.asarray(Year_of_Season,dtype='int64')# indx 1
    np_Nationality = np.asarray(Nationality,dtype='str')# indx 2
    np_Expend_by_player= np.asarray(Expend_by_player, dtype = 'float64') # indx 3
    np_Expend_Inflation_by_player = np.asarray(Expend_Inflation_by_player,dtype='float64') # indx 4

    # set the numpy arrays values into stack
    a = np.stack((np_Name_of_leauge,np_Year_of_Season,np_Nationality,np_Expend_by_player,np_Expend_Inflation_by_player),axis= -1)

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Expend by player|  ', '  Expend + Inflation by player|  ']
    
    # convert data from numpay ndarray to list and remove   duplicates elemtes of list for LEAUGE
    listLEAUGE = np_Name_of_leauge.tolist()
    listLEAUGE = remove_duplicates(listLEAUGE)
    listLEAUGE.sort()

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Year_of_Season
    listYear_of_Season = np_Year_of_Season.tolist()
    listYear_of_Season = remove_duplicates(listYear_of_Season)
    listYear_of_Season.sort()

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Nationality
    listNationality = np_Nationality.tolist()
    listNationality = remove_duplicates(listNationality)
    listNationality.sort()

    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'
            

    if value == 1:

        flag = 1
        cont_LEAUGE = 0
        for i in range(0,len(listLEAUGE)):          
            cont_LEAUGE += 1

        value = int(value)
        value =value -1
        if 0 <= value < cont_LEAUGE:
            flagTemp =  str(listLEAUGE[value])


    elif value == 2:
        flag = 2
        cont_Year_of_Season = 0

        for i in range(0,len(listYear_of_Season)):
            cont_Year_of_Season += 1

        value = int(value)
        value =value -1
        if 0 <= value < cont_Year_of_Season:
            flagTemp =  int(listYear_of_Season[value])

    elif value == 3:

        flag = 3
        cont_Nationality = 0

        for i in range(0,len(listNationality)):
            cont_Nationality += 1


        value = int(value)
        value =value -1
        if 0 <= value < cont_Nationality:
            lagTemp =  str(listNationality[value])
    
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

    # count number of rows in date frame
    # number of Season
    if flag == 2:
        for i in range(0,len(a)):
            if int(a[i][1]) == flagTemp :
                bro +=1
    

    # count number of rows in date frame
    # Nationality
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                bro +=1

    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro

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

    # reserving the number of elements in a row
    niz_N1 = [0]*bro

    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz1,np_niz2,np_niz1,np_niz3,np_niz3),axis= -1)

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        y+=1


    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Expend by player|  ', '  Expend + Inflation by player|  ']


    
    return df_new
