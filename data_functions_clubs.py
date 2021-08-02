from collections import Counter
from operator import itemgetter
from sort_functions import*
import numpy as np
import pandas as pd
import csv
import sys
from functions import*

# takes data with pandas function DataFrame for Clubs datas
def DataFrameFuncClubs(filePath):

    colls = ["Order","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season"]
    dat = pd.read_csv(filePath,header = None , names = colls)
    return dat

    
# get data for clubs calculate inflacion for profit ,Income and Expend
#  --> for Clubs datas
def GETDataClubs_with_seasons(DFrame):

    #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Order = [0] * count # 0
    Name_of_club = [0] * count # 1
    State = [0] * count # 2
    Competition =  [0] * count # 3
    Expenditures = [0] * count # 4
    Arrivals = [0] * count # 5
    Income = [0] * count # 6
    Departures = [0] * count # 7
    Balance =  [0] * count # 8
    Season = [0] * count # 9

    koef =  [0] * count
    interception_Expenditures = [0] * count
    interception_Income =  [0] * count
    interception_Balance = [0] * count
    int_koef = [0]* count
    ###############################################################################

    # cast DataFrame rows to folat and int
    DFrame["Order"].astype(np.int64) # 0
    DFrame["Club"].astype(np.str) # 1
    DFrame["State"].astype(np.str) # 2
    DFrame["Competition"].astype(np.str) # 3
    DFrame["Expenditures"].astype(np.float64) # 4
    DFrame["Arrivals"].astype(np.int64) # 5
    DFrame["Income"].astype(np.float64) # 6
    DFrame["Departures"].astype(np.int64) # 7
    DFrame["Balance"].astype(np.float64) # 8
    DFrame["Season"].astype(np.int64) # 9
    ###############################################################################


    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Order[i] = DFrame["Order"][i] # 0
        Name_of_club[i] = DFrame["Club"][i] # 1
        State[i] = DFrame["State"][i] # 2
        Competition[i] = DFrame["Competition"][i] # 3
        Expenditures[i] = DFrame["Expenditures"][i]# 4
        Arrivals[i] = DFrame["Arrivals"][i]# 5
        Income[i] = DFrame["Income"][i]# 6
        Departures[i] = DFrame["Departures"][i]# 7
        Balance[i] =  DFrame["Balance"][i]# 8
        Season[i] =  DFrame["Season"][i]# 9
        ############################################################################


    # calcualtion of coeficent for clubs seasons
    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a
        ###############################################################################

    # calculation of coeficent of inflacion
    for i in range (0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp
        ###############################################################################

    # calculation  Inflation for Potential, Earned and Profit
    for i in range(0,count):
        a = float(Income[i])*int_koef[i]
        b = float(Balance[i])*int_koef[i]
        c = float(Expenditures[i])*int_koef[i]
        interception_Income[i] = round(a,2)
        interception_Balance[i] = round(b,2)
        interception_Expenditures[i] = round(c,2)
        ###############################################################################


    # conversion to numpy
    np_Order = np.asarray(Order,dtype='int64') # 0
    np_Club = np.asarray(Name_of_club,dtype='str') # 1
    np_State = np.asarray(State,dtype='str') # 2
    np_Competition = np.asarray(Competition,dtype='str') # 3
    np_Expenditures = np.asarray(Expenditures,dtype='float64') # 4
    np_Arrivals = np.asarray(Arrivals,dtype='int64') # 5
    np_Income = np.asarray(Income,dtype='float64') # 6
    np_Departures = np.asarray(Departures,dtype='int64') # 7
    np_Balance = np.asarray(Balance,dtype='float64') # 8
    np_Seasons =  np.asarray(Season,dtype='int64') # 9

    np_INF_Income = np.asarray(interception_Income,dtype='float64') # 10
    np_INF_Balance = np.asarray(interception_Balance,dtype='float64') # 11
    np_INF_Expenditures = np.asarray(interception_Expenditures,dtype='float64') # 12
    ###############################################################################

    # set the numpy arrays values into stack
    niz = np.stack((np_Order,np_Club,np_State,np_Competition,np_Expenditures,np_Arrivals,np_Income,np_Departures,
    np_Balance,np_Seasons,np_INF_Income,np_INF_Expenditures,np_INF_Balance),axis= -1)

    # convert from stack with values to data for dataFrame
    a = Input_chose_of_sort_CLUBS_GETDataClubs_with_seasons(niz)
    # set to DataFrame
    data = np.array(a)
    # set to DataFrame
    df = pd.DataFrame(data)

    df.columns = ['    Order |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Arrivals |  ','    Income  |  ', '    Departures |  ','    Balance |  ','    Season |  ',
     ' Inflacion + Income |  ',' Inflacion + Expenditures |  ',' Inflacion + Balance |  ']
    ###############################################################################

    # return DataFrame with head an names of collums
    print(df)
    return df

    # BATCH for  specific filtring data from estraction data from function GETDataClubs_with_seasons
#  --> for Clubs data
def BATCH_for_GETDataClubs_with_seasons(DFrame):

    # DataFrame to ecstract data
    nDFRAME = GETDataClubs_with_seasons(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    #reserving the number of elements in a row
    Order  = [0] * count # indx 0
    Club = [0] * count # indx 1
    State = [0] * count # indx 2
    Competition =  [0] * count # indx 3
    Expenditures = [0] * count # indx 4
    Arrivals = [0] * count # indx 5
    Income = [0] * count # indx 6
    Departures = [0] * count # indx 7
    Balance =  [0] * count # indx 8
    Season = [0] * count # indx 9
    inflation_Income = [0] * count # indx 10
    inflation_Expenditures = [0] * count # indx 11
    inflation_Balance =  [0] * count # indx 12

    # cast DataFrame rows to folat and int
    nDFRAME["    Order |  "].astype(np.int64)# ind 0
    nDFRAME["    Club |  "].astype(np.str)# ind 1
    nDFRAME["    State |  "].astype(np.str)# ind 2
    nDFRAME["    Competition |  "].astype(np.str)# ind 3
    nDFRAME["    Expenditures |  "].astype(np.float64)# ind 4
    nDFRAME["    Arrivals |  "].astype(np.int64)# ind 5
    nDFRAME["    Income  |  "].astype(np.float64)# ind 6
    nDFRAME["    Departures |  "].astype(np.int64)# ind 7
    nDFRAME["    Balance |  "].astype(np.float64)# ind 8
    nDFRAME["    Season |  "].astype(np.int64)# ind 9
    nDFRAME[" Inflacion + Income |  "].astype(np.float64)# ind 10
    nDFRAME[" Inflacion + Expenditures |  "].astype(np.float64)# ind 11
    nDFRAME[" Inflacion + Balance |  "].astype(np.float64)# ind 12
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Order[i] =  nDFRAME["    Order |  "][i] # indx 0
        Club[i] = nDFRAME["    Club |  "][i] # indx 1
        State[i] = nDFRAME["    State |  "][i] # indx 2
        Competition[i] = nDFRAME["    Competition |  "][i] # indx 3
        Expenditures[i] = nDFRAME["    Expenditures |  "][i] # indx 4
        Arrivals[i] = nDFRAME["    Arrivals |  "][i] # indx 5
        Income[i] = nDFRAME["    Income  |  "][i] # indx 6
        Departures[i] = nDFRAME["    Departures |  "][i] # indx 7
        Balance[i] = nDFRAME["    Balance |  "][i] # indx 8
        Season[i] = nDFRAME["    Season |  "][i] # indx 9
        inflation_Income[i] = nDFRAME[" Inflacion + Income |  "][i] # indx 10
        inflation_Expenditures[i] = nDFRAME[" Inflacion + Expenditures |  "][i] # indx 11
        inflation_Balance[i] = nDFRAME[" Inflacion + Balance |  "][i] # indx 12
        ###############################################################################

    # conversion to numpy
    np_Order = np.asarray(Order, dtype = 'int64') # indx 0
    np_Club = np.asarray(Club,dtype='str')# indx 1
    np_State = np.asarray(State,dtype='str')# indx 2
    np_Competition = np.asarray(Competition, dtype = 'str') # indx 3
    np_Expenditures = np.asarray(Expenditures,dtype='float64') # indx 4
    np_Arrivals = np.asarray(Arrivals, dtype ='int64') # indx 5
    np_Income = np.asarray(Income,dtype='float64') # indx 6
    np_Departures = np.asarray(Departures, dtype = 'int64' ) # indx 7
    np_Balance = np.asarray(Balance,dtype='float64') # indx 8
    np_Season = np.asarray(Season,dtype='int64') # indx 9
    np_inflation_Income = np.asarray(inflation_Income, dtype = 'float64' ) # indx 10
    np_inflation_Expenditures = np.asarray(inflation_Expenditures, dtype = 'float64' ) # indx 11
    np_inflation_Balance = np.asarray(inflation_Balance, dtype = 'float64' ) # indx 12
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Order,np_Club,np_State,np_Competition,np_Expenditures,np_Arrivals,np_Income,np_Departures,np_Balance,
    np_Season,np_inflation_Income,np_inflation_Expenditures,np_inflation_Balance),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Order |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Arrivals |  ','    Income  |  ', '    Departures |  ','    Balance |  ','    Season |  ',
     ' Inflacion + Income |  ',' Inflacion + Expenditures |  ',' Inflacion + Balance |  ']
    ###############################################################################

    print("################################################################################################################")
    print(df_a)
    print("################################################################################################################")

    # CLUB
    # convert data from numpay ndarray to list and remove duplicates elemtes of list for CLUB
    listClub = np_Club.tolist()
    listClub = remove_duplicates(listClub)
    listClub.sort()

    #STATE
    # convert data from numpay ndarray to list and remove duplicates elemtes of list for STATE
    listState = np_State.tolist()
    listState = remove_duplicates(listState)
    listState.sort()
    ###############################################################################

    # COMPETITION
    # convert data from numpay ndarray to list and remove duplicates elemtes of list for CLUB
    listCOMPETITION = np_Competition.tolist()
    listCOMPETITION = remove_duplicates(listCOMPETITION)
    listCOMPETITION.sort()

    # SESAON
    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Competition
    listSESAON = np_Season.tolist()
    listSESAON = remove_duplicates(listSESAON)
    listSESAON.sort()
    ###############################################################################
    #######################################################################################################################################

    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'

    while True:

        print("\n")
        print("\n\t Chose a option of proces data by State or Competition  : ")
        print("\t 1 -> Club statistic ! ")
        print("\t 2 -> State statistic ! ")
        print("\t 3 -> Competition statistic ! ")
        print("\t 4 -> Season statistic ! ")
        value = raw_input("\n\tValue between 1 and 4    : ")
        if value.isdigit() == True:

            value = int(value)
            if value == 1:

                flag = 1
                ###############################################################################
                # CLUBS
                cont_CLUB = 0
                print("###############################################################################")
                print("\t Meni  Club statistic  !!!")
                #cont_state = 0
                for i in range(0,len(listClub)):
                    print(i+1,". : ",listClub[i])
                    cont_CLUB += 1
                print("###############################################################################")
                while True:

                    print("\n\t Enter Club   between 0 and ",cont_CLUB," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_CLUB:
                            print("You Chose : ",listClub[value])
                            flagTemp =  str(listClub[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                           print("\n\t Enter Club   between 0 and ",cont_CLUB," : ")
                           continue

                break
                ###############################################################################
            elif value == 2:

                flag = 2
                ###############################################################################
                cont_State = 0
                print("###############################################################################")
                print("\t Meni  State statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listState)):
                    print(i+1,". : ",listState[i])
                    cont_State += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter State   between 1 and ",cont_State," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_State:
                            print("You Chose : ",listState[value])
                            flagTemp =  str(listState[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                           print("\n\t Enter State   between 1 and ",cont_State," : ")
                           continue
                break
                ###############################################################################
            elif value == 3:

                flag = 3
                ###############################################################################
                cont_COMPETITION = 0
                print("###############################################################################")
                print("\t Meni  Competition statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listCOMPETITION)):
                    print(i+1,". : ",listCOMPETITION[i])
                    cont_COMPETITION += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter Competition   between 1 and ",cont_COMPETITION," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_COMPETITION:
                            print("You Chose : ",listCOMPETITION[value])
                            flagTemp =  str(listCOMPETITION[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                           print("\n\t Enter Competition   between 1 and ",cont_COMPETITION," : ")
                           continue
                break
                ###############################################################################
            elif value == 4:

                flag = 4
                ###############################################################################
                cont_Seson = 0
                print("###############################################################################")
                print("\t Meni  Season statistic!!!")
                #cont_Compe = 0
                for i in range(0,len(listSESAON)):
                    print(i+1,". : ",listSESAON[i])
                    cont_Seson += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter Season   between 1 and ",cont_Seson," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_Seson:
                            print("You Chose : ",listSESAON[value])
                            flagTemp =  int(listSESAON[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                           print("\n\t Enter Season   between 1 and ",cont_Seson," : ")
                           continue
                break
                ###############################################################################

            else:
                print("\n\tValue between 1 or  4  !!!")
        elif value.isdigit() != True:

             print("\n\tValue between 1 and 4  !!!")
             continue

    #######################################################################################################################################

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    # CLUB
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][1]) == flagTemp :
                bro +=1
    ###############################################################################
    # count number of rows in date frame
    # STATE
    if flag == 2:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                bro +=1
    ###############################################################################
    # count number of rows in date frame
    # COMPETITION
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][3]) == flagTemp :
                bro +=1
    ###############################################################################
    # count number of rows in date frame
    # SESAON
    if flag == 4:
        for i in range(0,len(a)):
            if int(a[i][9]) == flagTemp :
                bro +=1
    ###############################################################################
    #######################################################################################################################################
    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    array6 = [0] * bro
    array7 = [0] * bro
    array8 = [0] * bro
    array9 = [0] * bro
    array10 = [0] * bro
    array11 = [0] * bro
    array12 = [0] * bro
    array13 = [0] * bro
    ###############################################################################

    y = 0
    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from CLUB user chose options
    # CLUB
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][1]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from STATE user chose options
    # STATE
    if flag == 2:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from Competition user chose options
    # COMPETITION
    if flag == 3:
        for i in range(0,len(a)):
            if str(a[i][3]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from Competition user chose options
    # SESAON
    if flag == 4:
        for i in range(0,len(a)):
            if int(a[i][9]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                array13[y] = a[i][12]
                y+=1
    ###############################################################################

    # reserving the number of elements in a row
    niz_N1 = [0]*bro
    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz2,np_niz1,np_niz1,np_niz1,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        new_niz[i][5] = array6[y]
        new_niz[i][6] = array7[y]
        new_niz[i][7] = array8[y]
        new_niz[i][8] = array9[y]
        new_niz[i][9] = array10[y]
        new_niz[i][10] = array11[y]
        new_niz[i][11] = array12[y]
        new_niz[i][12] = array13[y]
        y+=1
    ###############################################################################

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Order |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Arrivals |  ','    Income  |  ', '    Departures |  ','    Balance |  ','    Season |  ',
     ' Inflacion + Income |  ',' Inflacion + Expenditures |  ',' Inflacion + Balance |  ']
    print("###################################################################################################################################################")
    print(df_new)
    print("###################################################################################################################################################")

    return df_new

    # get data for clubs calculate inflacion for profit ,Income and Expend but for clubs for all seasons
#  --> for Clubs data
def GetDate_for_Clubs_throught_all_seasons(DFrame):

        #count number of rows in date frame
    count = NumberOfRows(DFrame)

    #reserving the number of elements in a row
    Order  = [0] * count # indx 0
    Name_of_club = [0] * count # indx 1
    State_of_club = [0] * count # indx 2
    Competition =  [0] * count # indx 3
    Expenditures = [0] * count # indx 4
    Arrivals = [0] * count # indx 5
    Income = [0] * count # indx 6
    Departures = [0] * count # indx 7
    Balance =  [0] * count # indx 8
    Season = [0] * count # ind 9
    ###############################################################################

    # optimized array for operation for counting of  inflation
    koef =  [0] * count
    interception_Expenditures = [0] * count # ind 10
    interception_Income =  [0] * count# ind 11
    interception_Balance = [0] * count# ind 12
    int_koef = [0]* count
    niz1 = [0]* count
    ###############################################################################

    # cast DataFrame rows to folat and int
    DFrame["Order"].astype(np.int64)# ind 0
    DFrame["Club"].astype(np.str)# ind 1
    DFrame["State"].astype(np.str)# ind 2
    DFrame["Competition"].astype(np.str)# ind 3
    DFrame["Expenditures"].astype(np.float64)# ind 4
    DFrame["Arrivals"].astype(np.int64)# ind 5
    DFrame["Income"].astype(np.float64)# ind 6
    DFrame["Departures"].astype(np.int64)# ind 7
    DFrame["Balance"].astype(np.float64)# ind 8
    DFrame["Season"].astype(np.int64)# ind 9
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Order[i] = DFrame["Order"][i] # indx 0
        Name_of_club[i] = DFrame["Club"][i] # indx 1
        State_of_club[i] =  DFrame["State"][i]# indx 2
        Competition[i] = DFrame["Competition"][i] # indx 3
        Expenditures[i] =  DFrame["Expenditures"][i]# indx 4
        Arrivals[i] =  DFrame["Arrivals"][i]# indx 5
        Income[i] =  DFrame["Income"][i]# indx 6
        Departures[i] =  DFrame["Departures"][i]# indx 7
        Balance[i] =  DFrame["Balance"][i]# indx 8
        Season[i] =  DFrame["Season"][i]# ind 9
        ###############################################################################

    # calcualtion of coeficent for clubs seasons
    for i in range(0,count):
        temp = Season[i]
        a = GETCoefficients(coef,temp)
        koef[i] = a

    # calculation of coeficent of inflacion
    for i in range (0,len(int_koef)):
        temp = float(koef[i])
        int_koef[i] = temp

    # calculation  Inflation for Potential, Earned and Profit
    for i in range(0,count):

        a = float(Income[i])*int_koef[i]
        b = float(Balance[i])*int_koef[i]
        c = float(Expenditures[i])*int_koef[i]
        interception_Income[i] = round(a,2)
        interception_Balance[i] = round(b,2)
        interception_Expenditures[i] = round(c,2)
        ###############################################################################

        # conversion to numpy
    np_Order = np.asarray(Order, dtype = 'int64') # indx 0
    np_Name_of_club = np.asarray(Name_of_club,dtype='str')# indx 1
    np_State_of_club = np.asarray(State_of_club,dtype='str')# indx 2
    npLeauge = np.asarray(Competition, dtype = 'str') # indx 3
    np_Expenditures = np.asarray(Expenditures,dtype='float64') # indx 4
    np_Arrival = np.asarray(Arrivals, dtype ='int64') # indx 5
    np_Income = np.asarray(Income,dtype='float64') # indx 6
    np_Departures = np.asarray(Departures, dtype = 'int64' ) # indx 7
    np_Balance = np.asarray(Balance,dtype='float64') # indx 8
    np_Season = np.asarray(Season, dtype = 'int64' ) # indx 9
    np_in_Expenditure = np.asarray(interception_Expenditures, dtype = 'float64' ) # indx 10
    np_in_Income = np.asarray(interception_Income, dtype = 'float64' ) # indx 11
    np_in_Balance = np.asarray(interception_Balance, dtype = 'float64' ) # indx 12
    ###############################################################################


    # set the numpy arrays values into stack
    a = np.stack((np_Order,np_Name_of_club,np_State_of_club,npLeauge,np_Expenditures,np_Arrival,np_Income,
    np_Departures,np_Balance,np_Season,np_in_Expenditure,np_in_Income,np_in_Balance),axis= -1)


    np_niz1 = np.asarray(niz1, dtype = 'str')
    np_niz2 = np.asarray(niz1, dtype = 'int64')
    np_niz3 = np.asarray(niz1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    niz = np.stack((np_niz2,np_niz1,np_niz1,np_niz1,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz3,np_niz3),axis= -1)
    ###############################################################################

    # Function for sorting
    # variables in function for sorting
    n = count
    t = 0
    flag =  0

    visited = [False for i in range(n)]
    # Traverse through array elements
    # and count frequencies
    for i in range(n):
        # Skip this element if already
        # processed
        if (visited[i] == True):
            continue
        count = 1
        club = a[i][1]

        if club != 0:
            flag +=1

        suma_Arrival = int(a[i][5])
        sum_INF_Expenditures = float(a[i][10])
        sum_INF_Income = float(a[i][11])
        sum_INF_Balance = float(a[i][12])
        sum_Expenditures = float(a[i][4])
        sum_Income = float(a[i][6])
        sum_Balance = float(a[i][8])
        sum_Departures = int(a[i][7])
        ###############################################################################

        for j in range(i + 1, n, 1):
            if (a[i][1] == a[j][1]):

                suma_Arrival += int(a[j][5])
                sum_Expenditures += float(a[j][4])
                sum_Income += float(a[j][6])
                sum_Balance += float(a[j][8])
                sum_Departures += int(a[j][7])
                sum_INF_Expenditures += float(a[j][10])
                sum_INF_Income += float(a[j][11])
                sum_INF_Balance += float(a[j][12])
                visited[j] = True
                count += 1
                ###############################################################################
        if a[i][1] != 0 :
            niz[t][0] = a[i][0]
            niz[t][1] = a[i][1]
            niz[t][2] = a[i][2]
            niz[t][3] = a[i][3]
            niz[t][4] = sum_Expenditures
            niz[t][5] = suma_Arrival
            niz[t][6] = sum_Income
            niz[t][7] = sum_Departures
            niz[t][8] = sum_Balance
            niz[t][9] = a[i][9]
            niz[t][10] = sum_INF_Expenditures
            niz[t][11] = sum_INF_Income
            niz[t][12] = sum_INF_Balance
            ###############################################################################

            t +=1
            suma = 0

    # count array size with N
    # variables for flag
    N = flag
    niz_N1 = [0] * flag


    #Initialize a new array

    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz2,np_niz1,np_niz1,np_niz1,np_niz3,np_niz2,np_niz3,np_niz2,np_niz3,np_niz3,np_niz3,np_niz3),axis= -1)

    # avg Balance number the seasons
    for i in range(0,N):
        new_niz[i][0] = niz[i][0]
        new_niz[i][1] = niz[i][1]
        new_niz[i][2] = niz[i][2]
        new_niz[i][3] = niz[i][3]
        new_niz[i][4] = niz[i][4]
        new_niz[i][6] = niz[i][5]
        new_niz[i][5] = niz[i][6]
        new_niz[i][7] = niz[i][7]
        new_niz[i][8] = niz[i][8]
        #new_niz[i][9] = niz[i][9]
        new_niz[i][9] = niz[i][10]
        new_niz[i][10] = niz[i][11]
        new_niz[i][11] = niz[i][12]
        ###############################################################################

    # sort by appropriate elements and by columns
    a = Input_chose_of_sort_CLUBS(new_niz)

    # convert from stack with values to data for dataFrame
    data = np.array(a)
    # set to DataFrame
    df = pd.DataFrame(data)
    # name of labels for head or names of collums
    df.columns = ['    Order of Expend |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Income |  ','    Arrivals |  ', '    Departures |  ','    Balance |  ',
     '    inflation Expenditure |  ',' inflation Income |  ',' inflation Balance |  ']
    ###############################################################################(
    # return DataFrame with head an names of collums
    print(df)
    return df

    # BATCH for  specific filtring data from estraction data from function GetDate_for_Clubs_throught_all_seasons
#  --> for Clubs data
def BATCH_for_GetDate_for_Clubs_throught_all_seasons(DFrame):

    # DataFrame to ecstract data
    nDFRAME = GetDate_for_Clubs_throught_all_seasons(DFrame)

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)


    #reserving the number of elements in a row
    Order_of_Expend  = [0] * count # indx 0
    Club = [0] * count # indx 1
    State = [0] * count # indx 2
    Competition =  [0] * count # indx 3
    Expenditures = [0] * count # indx 4
    Income = [0] * count # indx 5
    Arrivals = [0] * count # indx 6
    Departures = [0] * count # indx 7
    Balance =  [0] * count # indx 8
    inflation_Expenditure = [0] * count # indx 9
    inflation_Income = [0] * count # indx 10
    inflation_Balance =  [0] * count # indx 11


    # cast DataFrame rows to folat and int
    nDFRAME["    Order of Expend |  "].astype(np.int64)# ind 0
    nDFRAME["    Club |  "].astype(np.str)# ind 1
    nDFRAME["    State |  "].astype(np.str)# ind 2
    nDFRAME["    Competition |  "].astype(np.str)# ind 3
    nDFRAME["    Expenditures |  "].astype(np.float64)# ind 4
    nDFRAME["    Income |  "].astype(np.float64)# ind 5
    nDFRAME["    Arrivals |  "].astype(np.int64)# ind 6
    nDFRAME["    Departures |  "].astype(np.int64)# ind 7
    nDFRAME["    Balance |  "].astype(np.float64)# ind 8
    nDFRAME["    inflation Expenditure |  "].astype(np.float64)# ind 9
    nDFRAME[" inflation Income |  "].astype(np.float64)# ind 10
    nDFRAME[" inflation Balance |  "].astype(np.float64)# ind 11
    ###############################################################################

    #save values from the dateframe to a arrays
    i = 0
    for i in range(0,count):

        Order_of_Expend[i] =  nDFRAME["    Order of Expend |  "][i] # indx 0
        Club[i] = nDFRAME["    Club |  "][i] # indx 1
        State[i] = nDFRAME["    State |  "][i] # indx 2
        Competition[i] = nDFRAME["    Competition |  "][i] # indx 3
        Expenditures[i] = nDFRAME["    Expenditures |  "][i] # indx 4
        Income[i] = nDFRAME["    Income |  "][i] # indx 5
        Arrivals[i] = nDFRAME["    Arrivals |  "][i] # indx 6
        Departures[i] = nDFRAME["    Departures |  "][i] # indx 7
        Balance[i] = nDFRAME["    Balance |  "][i] # indx 8
        inflation_Expenditure[i] = nDFRAME["    inflation Expenditure |  "][i] # indx 9
        inflation_Income[i] = nDFRAME[" inflation Income |  "][i] # indx 10
        inflation_Balance[i] = nDFRAME[" inflation Balance |  "][i] # indx 11
        ###############################################################################

    # conversion to numpy
    np_Order_of_Expend = np.asarray(Order_of_Expend, dtype = 'int64') # indx 0
    np_Club = np.asarray(Club,dtype='str')# indx 1
    np_State = np.asarray(State,dtype='str')# indx 2
    np_Competition = np.asarray(Competition, dtype = 'str') # indx 3
    np_Expenditures = np.asarray(Expenditures,dtype='float64') # indx 4
    np_Income = np.asarray(Income, dtype ='float64') # indx 5
    np_Arrivals = np.asarray(Arrivals,dtype='int64') # indx 6
    np_Departures = np.asarray(Departures, dtype = 'int64' ) # indx 7
    np_Balance = np.asarray(Balance,dtype='float64') # indx 8
    np_inflation_Expenditure = np.asarray(inflation_Expenditure, dtype = 'float64' ) # indx 9
    np_inflation_Income = np.asarray(inflation_Income, dtype = 'float64' ) # indx 10
    np_inflation_Balance = np.asarray(inflation_Balance, dtype = 'float64' ) # indx 11
    ###############################################################################

    # set the numpy arrays values into stack
    a = np.stack((np_Order_of_Expend,np_Club,np_State,np_Competition,np_Expenditures,np_Income,np_Arrivals,np_Departures,
    np_Balance,np_inflation_Expenditure,np_inflation_Income,np_inflation_Balance),axis= -1)
    ###############################################################################

    # convert from stack with values to data for dataFrame
    a_data = np.array(a)
    # set to DataFrame
    df_a = pd.DataFrame(a_data)
    # name of labels for head or names of collums
    df_a.columns = ['    Order of Expend |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Income |  ','    Arrivals |  ', '    Departures |  ','    Balance |  ',
     '    inflation Expenditure |  ',' inflation Income |  ',' inflation Balance |  ']
    ###############################################################################

    print("################################################################################################################")
    print(df_a)
    print("################################################################################################################")

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for states
    listSTATE = np_State.tolist()
    listSTATE = remove_duplicates(listSTATE)

    # convert data from numpay ndarray to list and remove duplicates elemtes of list for Competition
    listCompetition = np_Competition.tolist()
    listCompetition = remove_duplicates(listCompetition)
    ###############################################################################

    # a function in which a user selects a choice of country or championship,
    # and chooses the name of the state or championship after which the data is printed

    # temporary variables that note the value the ticker chooses
    flag = 0
    flagTemp = '0'

    while True:

        print("\n")
        print("\n\t Chose a option of proces data by State or Competition  : ")
        print("\t 1 -> State ! ")
        print("\t 2 -> Competition ! ")
        value = raw_input("\n\tValue between 1 or  2  : ")
        if value.isdigit() == True:

            value = int(value)
            if value == 1:
                flag = 1
                ###############################################################################
                # drzave
                cont_state = 0
                print("###############################################################################")
                print("\t Meni  State!!!")
                #cont_state = 0
                for i in range(0,len(listSTATE)):
                    print(i+1,". : ",listSTATE[i])
                    cont_state += 1
                print("###############################################################################")
                while True:

                    print("\n\t Enter State   between 1 and ",cont_state," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_state:
                            print("You Chose : ",listSTATE[value])
                            flagTemp =  str(listSTATE[value])
                            break
                        else:
                           print("\n\tValue between bounds :")
                    elif value.isdigit() != True:

                         print("\n\t Enter State   between 1 and ",cont_state," : ")
                         continue

                break
                ###############################################################################
            elif value == 2:

                flag = 2
                ###############################################################################
                cont_Compe = 0
                print("###############################################################################")
                print("\t Meni  Competition!!!")
                #cont_Compe = 0
                for i in range(0,len(listCompetition)):
                    print(i+1,". : ",listCompetition[i])
                    cont_Compe += 1
                print("###############################################################################")

                while True:

                    print("\n\t Enter Competition   between 1 and ",cont_Compe," : ")
                    value = raw_input("\n\tValue : " )
                    if value.isdigit() == True:

                        value = int(value)
                        value =value -1
                        if 0 <= value < cont_Compe:
                            print("You Chose : ",listCompetition[value])
                            flagTemp =  str(listCompetition[value])
                            break
                        else:
                           print("\n\tValue between 1 and ",cont_Compe," :")
                    elif value.isdigit() != True:

                         print("\n\tValue between 1 and ",cont_Compe," :")
                         continue
                break
                ###############################################################################
            else:
                print("\n\tValue between 1 or  2  !!!")
        elif value.isdigit() != True:

             print("\n\tValue between 1 and 2 !!!")
             continue
    #######################################################################################################################################

    #count number of rows in date frame
    count = NumberOfRows(nDFRAME)

    # temp var for count number of roew for dynamic reserving
    bro = 0

    # count number of rows in date frame
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                bro +=1
    ###############################################################################
    # count number of rows in date frame
    if flag == 2:
        for i in range(0,len(a)):
            if str(a[i][3]) == flagTemp :
                bro +=1
    ###############################################################################
    # reserving the number of elements in a row
    array1 = [0] * bro
    array2 = [0] * bro
    array3 = [0] * bro
    array4 = [0] * bro
    array5 = [0] * bro
    array6 = [0] * bro
    array7 = [0] * bro
    array8 = [0] * bro
    array9 = [0] * bro
    array10 = [0] * bro
    array11 = [0] * bro
    array12 = [0] * bro
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from State user chose options
    y = 0
    if flag == 1:
        for i in range(0,len(a)):
            if str(a[i][2]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                y+=1
    ###############################################################################

    # temporarily storing data from a numpy array into a
    # common array to allocate as many places as you need to avoid empty places in the DataFrame
    # storing data from Competition user chose options
    if flag == 2:
        for i in range(0,len(a)):
            if str(a[i][3]) == flagTemp :
                array1[y] = a[i][0]
                array2[y] = a[i][1]
                array3[y] = a[i][2]
                array4[y] = a[i][3]
                array5[y] = a[i][4]
                array6[y] = a[i][5]
                array7[y] = a[i][6]
                array8[y] = a[i][7]
                array9[y] = a[i][8]
                array10[y] = a[i][9]
                array11[y] = a[i][10]
                array12[y] = a[i][11]
                y+=1
    ###############################################################################

    # reserving the number of elements in a row
    niz_N1 = [0]*bro
    #Initialize a new array
    np_niz1 = np.asarray(niz_N1, dtype = 'str')
    np_niz2 = np.asarray(niz_N1, dtype = 'int64')
    np_niz3 = np.asarray(niz_N1, dtype = 'float64')

    #set arr to stack for operations with data lik sort and convert
    new_niz = np.stack((np_niz2,np_niz1,np_niz1,np_niz1,np_niz3,np_niz3,np_niz2,np_niz2,np_niz3,np_niz3,np_niz3,np_niz3),axis= -1)
    #######################################################################################################################################

    # relocating data from temporary arrays to numpy arrays
    y = 0
    for i in range(0,bro):
        new_niz[i][0] = array1[y]
        new_niz[i][1] = array2[y]
        new_niz[i][2] = array3[y]
        new_niz[i][3] = array4[y]
        new_niz[i][4] = array5[y]
        new_niz[i][5] = array6[y]
        new_niz[i][6] = array7[y]
        new_niz[i][7] = array8[y]
        new_niz[i][8] = array9[y]
        new_niz[i][9] = array10[y]
        new_niz[i][10] = array11[y]
        new_niz[i][11] = array12[y]
        y+=1
    ###############################################################################

    # convert from stack with values to data for dataFrame
    new_data = np.array(new_niz)
    # set to DataFrame
    df_new = pd.DataFrame(new_data)
    # name of labels for head or names of collums
    df_new.columns = ['    Order of Expend |  ', '    Club |  ','    State |  ', '    Competition |  ','    Expenditures |  ',
     '    Income |  ','    Arrivals |  ', '    Departures |  ','    Balance |  ',
     '    inflation Expenditure |  ',' inflation Income |  ',' inflation Balance |  ']
    print("###################################################################################################################################################")
    print(df_new)
    print("###################################################################################################################################################")

    return df_new