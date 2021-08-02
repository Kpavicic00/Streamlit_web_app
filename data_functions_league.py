# from collections import Counter
# from operator import itemgetter
# from sort_functions import*
# import numpy as np
# import pandas as pd
# import csv
# import sys
# from functions import *
# coef = 'file.txt'

# # takes data with pandas function DataFrame for League datas
# def DataFrameFunc(filePath):

#     colls = ["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]
#     dat = pd.read_csv(filePath,header = None , names = colls)
#     return dat


# #get average League spending for each player
# #  --> for League datas
# def GetAVGExpendFORplayerArrivals(DFrame):

#     # count number of rows in date frame
#     count = NumberOfRows(DFrame)

#     # reserving arraya for cast
#     Name_of_leauge = [0] * count
#     Year_of_Season = [0] * count
#     arrivals_players = [0] * count
#     Nationality_leuge = [0] * count
#     expenditures = [0] * count

#     koef = [0] * count
#     int_koef = [0] * count
#     expend_inflation = [0] * count
#     ###############################################################################

#     # cast data from Data to float, int and str
#     DFrame["Competition"].astype(np.str) # ind 0
#     DFrame["Year"].astype(np.int64) # ind 1
#     DFrame["Arrivals"].astype(np.int64) # ind 2
#     DFrame["Nationality"].astype(np.str) # ind 3
#     DFrame["Expenditures"].astype(np.int64) # ind 4
#     ###############################################################################

#     #save values from the dateframe to a string
#     i = 0
#     for i in range(0,count):
#         Name_of_leauge[i] = DFrame["Competition"][i] # ind 0
#         Year_of_Season[i] = DFrame["Year"][i] # ind 1
#         arrivals_players[i] = DFrame["Arrivals"][i] # ind 2
#         Nationality_leuge[i] = DFrame["Nationality"][i] # ind 3
#         expenditures[i] = DFrame["Expenditures"][i] # ind 4

#     # the inflation calculation coefficient operatorion
#     for i in range(0,count):
#         temp = Year_of_Season[i]
#         a = GETCoefficients(coef,temp)
#         koef[i] = a
#         ###############################################################################

#     # save coefficient to specific array
#     for i in range(0,len(int_koef)):
#         temp = float(koef[i])
#         int_koef[i] = temp
#         ###############################################################################

#     # operation of inflation
#     for i in range(0,count):
#         a = float(expenditures[i])*int_koef[i]
#         expend_inflation[i] = round(a,2)
#         ###############################################################################

#     # conversion to numpy
#     np_Expend = np.asarray(expenditures, dtype='float64') # ind 0
#     np_arrivals_players = np.asarray(arrivals_players, dtype='int64') # ind 1
#     np_Year_of_Season = np.asarray(Year_of_Season, dtype='int64') # ind 2
#     npNationality_leuge = np.asarray(Nationality_leuge, dtype='str') # ind 3
#     np_Name_of_leauge = np.asarray(Name_of_leauge, dtype='str') # ind 4
#     np_expend_inflation = np.asarray(expend_inflation, dtype='float64') # ind 5
#     ###############################################################################



#     niz = np.stack((np_Name_of_leauge,np_Year_of_Season,npNationality_leuge,np.round((np_Expend/np_arrivals_players),2)
#     ,np.round((np_expend_inflation/np_arrivals_players),2)), axis = -1)
#     ###############################################################################

#     a = Input_chose_of_GetAVGExpendFORplayerArrivals(niz)
#     # convert from stack with values to data for dataFrame
#     data = np.array(a)
#     # set to DataFrame
#     df = pd.DataFrame(data)
#     # name of labels for head or names of collums
#     df.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Expend by player|  ', '  Expend + Inflation by player|  ']
#     ###############################################################################
#     # return DataFrame with head an names of collums
#     print(df)
#     return df


# # BATCH for  specific filtring data from estraction data from function GetAVGIncomeFORplayerDepartures
# #  --> for League datas
# def BATCH_for_GetAVGExpendFORplayerArrivals(DFrame):

#     # DataFrame to ecstract data
#     nDFRAME = GetAVGExpendFORplayerArrivals(DFrame)

#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)


#     #reserving the number of elements in a row
#     Name_of_leauge  = [0] * count # indx 0
#     Year_of_Season = [0] * count # indx 1
#     Nationality = [0] * count # indx 2
#     Expend_by_player = [0] * count # indx 3
#     Expend_Inflation_by_player = [0] * count # indx 4

#     # cast from DataFrame to str int an float
#     nDFRAME["    Name of League |  "].astype(np.str)# ind 0
#     nDFRAME["   Year of Season |  "].astype(np.int64)# ind 1
#     nDFRAME["    Nationality |  "].astype(np.str)# ind 2
#     nDFRAME["    Expend by player|  "].astype(np.float64)# ind 3
#     nDFRAME["  Expend + Inflation by player|  "].astype(np.float64)# ind 4
#     ###############################################################################

#     #save values from the dateframe to a arrays
#     i = 0
#     for i in range(0,count):
#         Name_of_leauge[i] =  nDFRAME["    Name of League |  "][i] # indx 0
#         Year_of_Season[i] = nDFRAME["   Year of Season |  "][i] # indx 1
#         Nationality[i] = nDFRAME["    Nationality |  "][i] # indx 2
#         Expend_by_player[i] = nDFRAME["    Expend by player|  "][i] # indx 3
#         Expend_Inflation_by_player[i] = nDFRAME["  Expend + Inflation by player|  "][i] # indx 4
#         ###############################################################################

#     # conversion to numpy
#     np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
#     np_Year_of_Season = np.asarray(Year_of_Season,dtype='int64')# indx 1
#     np_Nationality = np.asarray(Nationality,dtype='str')# indx 2
#     np_Expend_by_player= np.asarray(Expend_by_player, dtype = 'float64') # indx 3
#     np_Expend_Inflation_by_player = np.asarray(Expend_Inflation_by_player,dtype='float64') # indx 4
#     ###############################################################################

#     # set the numpy arrays values into stack
#     a = np.stack((np_Name_of_leauge,np_Year_of_Season,np_Nationality,np_Expend_by_player,np_Expend_Inflation_by_player),axis= -1)
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     a_data = np.array(a)
#     # set to DataFrame
#     df_a = pd.DataFrame(a_data)
#     # name of labels for head or names of collums
#     df_a.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Expend by player|  ', '  Expend + Inflation by player|  ']
#     ###############################################################################

#     print("################################################################################################################")
#     print(df_a)
#     print("################################################################################################################")

#     # convert data from numpay ndarray to list and remove   duplicates elemtes of list for LEAUGE
#     listLEAUGE = np_Name_of_leauge.tolist()
#     listLEAUGE = remove_duplicates(listLEAUGE)
#     listLEAUGE.sort()
#     ###############################################################################

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for Year_of_Season
#     listYear_of_Season = np_Year_of_Season.tolist()
#     listYear_of_Season = remove_duplicates(listYear_of_Season)
#     listYear_of_Season.sort()
#     ###############################################################################

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for Nationality
#     listNationality = np_Nationality.tolist()
#     listNationality = remove_duplicates(listNationality)
#     listNationality.sort()
#     ###############################################################################
#     #######################################################################################################################################


#     # a function in which a user selects a choice of country or championship,
#     # and chooses the name of the state or championship after which the data is printed

#     # temporary variables that note the value the ticker chooses
#     flag = 0
#     flagTemp = '0'

#     while True:

#         print("\n")
#         print("\n\t Chose a option of proces data by LEAUGE,Year_of_Season or Nationality  : ")
#         print("\t 1 -> LEAUGE statistic ! ")
#         print("\t 2 -> Year_of_Season statistic ! ")
#         print("\t 3 -> Nationality statistic ! ")
#         value = raw_input("\n\tValue between 1 and 3    : ")
#         if value.isdigit() == True:

#             value = int(value)
#             if value == 1:

#                 flag = 1
#                 ###############################################################################
#                 cont_LEAUGE = 0
#                 print("###############################################################################")
#                 print("\t Meni  LEAUGE statistic  !!!")
#                 for i in range(0,len(listLEAUGE)):
#                     print(i+1,". : ",listLEAUGE[i])
#                     cont_LEAUGE += 1
#                 print("###############################################################################")
#                 while True:

#                     print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_LEAUGE:
#                             print("You Chose : ",listLEAUGE[value])
#                             flagTemp =  str(listLEAUGE[value])
#                             break

#                         else:
#                            print("\n\tValue between bounds :")

#                     elif value.isdigit() != True:
#                          print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
#                          continue
#                 break
#                 ###############################################################################
#             elif value == 2:
#                 flag = 2
#                 ###############################################################################
#                 cont_Year_of_Season = 0
#                 print("###############################################################################")
#                 print("\t Meni  Year_of_Season statistic!!!")
#                 #cont_Compe = 0
#                 for i in range(0,len(listYear_of_Season)):
#                     print(i+1,". : ",listYear_of_Season[i])
#                     cont_Year_of_Season += 1
#                 print("###############################################################################")

#                 while True:

#                     print("\n\t Enter Year_of_Season   between 1 and ",cont_Year_of_Season," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_Year_of_Season:

#                             print("You Chose : ",listYear_of_Season[value])
#                             flagTemp =  int(listYear_of_Season[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")

#                     elif value.isdigit() != True:

#                          print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
#                          continue

#                 break
#                 ###############################################################################
#             elif value == 3:

#                 flag = 3
#                 ###############################################################################
#                 cont_Nationality = 0
#                 print("###############################################################################")
#                 print("\t Meni  Competition statistic!!!")
#                 #cont_Compe = 0
#                 for i in range(0,len(listNationality)):
#                     print(i+1,". : ",listNationality[i])
#                     cont_Nationality += 1
#                 print("###############################################################################")

#                 while True:

#                     print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
#                     value = raw_input("\n\tValue : " )

#                     if value.isdigit() == True:
#                         value = int(value)
#                         value =value -1

#                         if 0 <= value < cont_Nationality:
#                             print("You Chose : ",listNationality[value])
#                             flagTemp =  str(listNationality[value])
#                             break
#                         else:

#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                          print("\n\tValue between 1 or  2  !!!")
#                          continue
#                 break
#                 ###############################################################################

#             else:
#                 print("\n\tValue between 1 and  4  !!!")

#         elif value.isdigit() != True:

#              print("\n\tValue between 1 and  4  !!!")
#              continue
#     #######################################################################################################################################


#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)

#     # temp var for count number of roew for dynamic reserving
#     bro = 0

#     # count number of rows in date frame
#     # name of LEAUGE
#     if flag == 1:
#         for i in range(0,len(a)):
#             if str(a[i][0]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # count number of rows in date frame
#     # number of Season
#     if flag == 2:
#         for i in range(0,len(a)):
#             if int(a[i][1]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # count number of rows in date frame
#     # Nationality
#     if flag == 3:
#         for i in range(0,len(a)):
#             if str(a[i][2]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # reserving the number of elements in a row
#     array1 = [0] * bro
#     array2 = [0] * bro
#     array3 = [0] * bro
#     array4 = [0] * bro
#     array5 = [0] * bro
#     ###############################################################################

#     # temporarily storing data from a numpy array into a
#     # common array to allocate as many places as you need to avoid empty places in the DataFrame
#     # storing data from State user chose options

#     # name of LEAUGE
#     y = 0
#     if flag == 1:
#         for i in range(0,len(a)):
#             if str(a[i][0]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 y+=1
#     ###############################################################################

#     # number of Season
#     if flag == 2:
#         for i in range(0,len(a)):
#             if int(a[i][1]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 y+=1
#     ###############################################################################

#     # Nationality
#     if flag == 3:
#         for i in range(0,len(a)):
#             if str(a[i][2]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 y+=1
#     ###############################################################################

#     # reserving the number of elements in a row
#     niz_N1 = [0]*bro

#     #Initialize a new array
#     np_niz1 = np.asarray(niz_N1, dtype = 'str')
#     np_niz2 = np.asarray(niz_N1, dtype = 'int64')
#     np_niz3 = np.asarray(niz_N1, dtype = 'float64')

#     #set arr to stack for operations with data lik sort and convert
#     new_niz = np.stack((np_niz1,np_niz2,np_niz1,np_niz3,np_niz3),axis= -1)
#     #######################################################################################################################################

#     # relocating data from temporary arrays to numpy arrays
#     y = 0
#     for i in range(0,bro):
#         new_niz[i][0] = array1[y]
#         new_niz[i][1] = array2[y]
#         new_niz[i][2] = array3[y]
#         new_niz[i][3] = array4[y]
#         new_niz[i][4] = array5[y]
#         y+=1
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     new_data = np.array(new_niz)
#     # set to DataFrame
#     df_new = pd.DataFrame(new_data)
#     # name of labels for head or names of collums
#     df_new.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Expend by player|  ', '  Expend + Inflation by player|  ']
#     print("###################################################################################################################################################")
#     print(df_new)
#     print("###################################################################################################################################################")

#     return df_new


# #get average League brutto earnings for each player
# #  --> for League datas
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
#     a = Input_chose_of_GetAVGIncomeFORplayerDepartures(niz)
#     # convert from stack with values to data for dataFrame
#     data = np.array(a)
#     # set to DataFrame
#     df = pd.DataFrame(data)
#     # name of labels for head or names of collums
#     df.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Income by player|  ', '  Income + Inflation by player|  ']
#     ###############################################################################
#     # return DataFrame with head an names of collums
#     print(df)
#     return df


# # BATCH for  specific filtring data from estraction data from function GetAVGIncomeFORplayerDepartures
# #  --> for League datas
# def BATCH_for_GetAVGIncomeFORplayerDepartures(DFrame):

#     # DataFrame to ecstract data
#     nDFRAME = GetAVGIncomeFORplayerDepartures(DFrame)

#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)


#     #reserving the number of elements in a row
#     Name_of_leauge  = [0] * count # indx 0
#     Year_of_Season = [0] * count # indx 1
#     Nationality = [0] * count # indx 2
#     Income_by_player = [0] * count # indx 3
#     Income_Inflation_by_player = [0] * count # indx 4

#     # '    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Income by player|  ', '  Income + Inflation by player|  '
#     # cast DataFrame rows to folat and int
#     nDFRAME["    Name of League |  "].astype(np.str)# ind 0
#     nDFRAME["   Year of Season |  "].astype(np.int64)# ind 1
#     nDFRAME["    Nationality |  "].astype(np.str)# ind 2
#     nDFRAME["    Income by player|  "].astype(np.float64)# ind 3
#     nDFRAME["  Income + Inflation by player|  "].astype(np.float64)# ind 4
#     ###############################################################################

#     #save values from the dateframe to a arrays
#     i = 0
#     for i in range(0,count):
#         Name_of_leauge[i] =  nDFRAME["    Name of League |  "][i] # indx 0
#         Year_of_Season[i] = nDFRAME["   Year of Season |  "][i] # indx 1
#         Nationality[i] = nDFRAME["    Nationality |  "][i] # indx 2
#         Income_by_player[i] = nDFRAME["    Income by player|  "][i] # indx 3
#         Income_Inflation_by_player[i] = nDFRAME["  Income + Inflation by player|  "][i] # indx 4
#         ###############################################################################

#     # conversion to numpy
#     np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
#     np_Year_of_Season = np.asarray(Year_of_Season,dtype='int64')# indx 1
#     np_Nationality = np.asarray(Nationality,dtype='str')# indx 2
#     np_Income_by_player = np.asarray(Income_by_player, dtype = 'float64') # indx 3
#     np_Income_Inflation_by_player = np.asarray(Income_Inflation_by_player,dtype='float64') # indx 4
#     ###############################################################################

#     # set the numpy arrays values into stack
#     a = np.stack((np_Name_of_leauge,np_Year_of_Season,np_Nationality,np_Income_by_player,np_Income_Inflation_by_player),axis= -1)
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     a_data = np.array(a)
#     # set to DataFrame
#     df_a = pd.DataFrame(a_data)
#     # name of labels for head or names of collums
#     df_a.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Income by player|  ', '  Income + Inflation by player|  ']
#     ###############################################################################

#     print("################################################################################################################")
#     print(df_a)
#     print("################################################################################################################")

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for LEAUGE
#     listLEAUGE = np_Name_of_leauge.tolist()
#     listLEAUGE = remove_duplicates(listLEAUGE)
#     listLEAUGE.sort()
#     ###############################################################################

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for Year_of_Season
#     listYear_of_Season = np_Year_of_Season.tolist()
#     listYear_of_Season = remove_duplicates(listYear_of_Season)
#     listYear_of_Season.sort()
#     ###############################################################################

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for Nationality
#     listNationality = np_Nationality.tolist()
#     listNationality = remove_duplicates(listNationality)
#     listNationality.sort()
#     ###############################################################################
#     #######################################################################################################################################

#     # a function in which a user selects a choice of country or championship,
#     # and chooses the name of the state or championship after which the data is printed

#     # temporary variables that note the value the ticker chooses
#     flag = 0
#     flagTemp = '0'

#     while True:

#         print("\n")
#         print("\n\t Chose a option of proces data by LEAUGE,Year_of_Season or Nationality  : ")
#         print("\t 1 -> LEAUGE statistic ! ")
#         print("\t 2 -> Year_of_Season statistic ! ")
#         print("\t 3 -> Nationality statistic ! ")
#         value = raw_input("\n\tValue between 1 and 3    : ")
#         print("\n")
#         if value.isdigit() == True:

#             value = int(value)
#             if value == 1:

#                 flag = 1
#                 ###############################################################################
#                 cont_LEAUGE = 0
#                 print("###############################################################################")
#                 print("\t Meni  LEAUGE statistic  !!!")
#                 for i in range(0,len(listLEAUGE)):
#                     print(i+1,". : ",listLEAUGE[i])
#                     cont_LEAUGE += 1
#                 print("###############################################################################")
#                 while True:

#                     print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_LEAUGE:

#                             print("You Chose : ",listLEAUGE[value])
#                             flagTemp =  str(listLEAUGE[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                          print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
#                          continue
#                 break
#                 ###############################################################################
#             elif value == 2:

#                 flag = 2
#                 ###############################################################################
#                 cont_Year_of_Season = 0
#                 print("###############################################################################")
#                 print("\t Meni  State statistic!!!")
#                 #cont_Compe = 0
#                 for i in range(0,len(listYear_of_Season)):
#                     print(i+1,". : ",listYear_of_Season[i])
#                     cont_Year_of_Season += 1
#                 print("###############################################################################")

#                 while True:

#                     print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_Year_of_Season:
#                             print("You Chose : ",listYear_of_Season[value])
#                             flagTemp =  int(listYear_of_Season[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                          print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
#                          continue
#                 break
#                 ###############################################################################
#             elif value == 3:
#                 flag = 3
#                 ###############################################################################
#                 cont_Nationality = 0
#                 print("###############################################################################")
#                 print("\t Meni  Competition statistic!!!")
#                 #cont_Compe = 0
#                 for i in range(0,len(listNationality)):
#                     print(i+1,". : ",listNationality[i])
#                     cont_Nationality += 1
#                 print("###############################################################################")

#                 while True:
#                     print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_Nationality:

#                             print("You Chose : ",listNationality[value])
#                             flagTemp =  str(listNationality[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                          print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
#                          continue
#                 break
#                 ###############################################################################
#             else:
#                 print("\n\tValue between 1 or  4  !!!")
#         elif value.isdigit() != True:

#              print("\n\tValue between 1 and 3  !!!")
#              continue
#     #######################################################################################################################################


#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)

#     # temp var for count number of roew for dynamic reserving
#     bro = 0

#     # count number of rows in date frame
#     # name of LEAUGE
#     if flag == 1:
#         for i in range(0,len(a)):
#             if str(a[i][0]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # count number of rows in date frame
#     # number of Season
#     if flag == 2:
#         for i in range(0,len(a)):
#             if int(a[i][1]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # count number of rows in date frame
#     # Nationality
#     if flag == 3:
#         for i in range(0,len(a)):
#             if str(a[i][2]) == flagTemp :
#                 bro +=1
#     ###############################################################################
#     # reserving the number of elements in a row
#     array1 = [0] * bro
#     array2 = [0] * bro
#     array3 = [0] * bro
#     array4 = [0] * bro
#     array5 = [0] * bro
#     ###############################################################################

#     # temporarily storing data from a numpy array into a
#     # common array to allocate as many places as you need to avoid empty places in the DataFrame
#     # storing data from State user chose options

#     # name of LEAUGE
#     y = 0
#     if flag == 1:
#         for i in range(0,len(a)):
#             if str(a[i][0]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 y+=1
#     ###############################################################################
#     # number of Season
#     if flag == 2:
#         for i in range(0,len(a)):
#             if int(a[i][1]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 y+=1
#     ###############################################################################
#     # Nationality
#     if flag == 3:
#         for i in range(0,len(a)):
#             if str(a[i][2]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 y+=1
#     ###############################################################################

#     # reserving the number of elements in a row
#     niz_N1 = [0]*bro
#     #Initialize a new array
#     np_niz1 = np.asarray(niz_N1, dtype = 'str')
#     np_niz2 = np.asarray(niz_N1, dtype = 'int64')
#     np_niz3 = np.asarray(niz_N1, dtype = 'float64')

#     #set arr to stack for operations with data lik sort and convert
#     new_niz = np.stack((np_niz1,np_niz2,np_niz1,np_niz3,np_niz3),axis= -1)
#     #######################################################################################################################################

#     # relocating data from temporary arrays to numpy arrays
#     y = 0
#     for i in range(0,bro):
#         new_niz[i][0] = array1[y]
#         new_niz[i][1] = array2[y]
#         new_niz[i][2] = array3[y]
#         new_niz[i][3] = array4[y]
#         new_niz[i][4] = array5[y]
#         y+=1
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     new_data = np.array(new_niz)
#     # set to DataFrame
#     df_new = pd.DataFrame(new_data)
#     # name of labels for head or names of collums
#     df_new.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Income by player|  ', '  Income + Inflation by player|  ']
#     print("###################################################################################################################################################")
#     print(df_new)
#     print("###################################################################################################################################################")

#     return df_new


# #get average League netto earnings for each player
# #  --> for League datas
# def GetAVGBalanceFORplayerDepartures(DFrame):

#         #count number of rows in date frame
#         count = NumberOfRows(DFrame)

#         #reserving the number of elements in a row
#         Nationality = [0] * count
#         Balance = [0] * count
#         Departures = [0] * count
#         leauge = [0] * count
#         Season = [0] * count
#         koef = [0] * count
#         CUT =  [0] * count
#         interception = [0] * count
#         int_koef = [0] * count
#         ###############################################################################

#         # cast DataFrame rows to folat and int
#         DFrame["Balance"].astype(np.int64)
#         DFrame["Departures"].astype(np.int64)
#         DFrame["Competition"].astype(np.str)
#         DFrame["Nationality"].astype(np.str)
#         DFrame["Year"].astype(np.int64)
#         ###############################################################################

#         #save values from the dateframe to a string
#         i = 0
#         for i in range(0,count):
#             Balance[i] = DFrame["Balance"][i]
#             Departures[i] = DFrame["Departures"][i]
#             leauge[i] = DFrame["Competition"][i]
#             Season[i] = DFrame["Year"][i]
#             Nationality[i] = DFrame["Nationality"][i]
#             ###############################################################################

#         # for i in range(0,count):
#         #     temp = Season[i]
#         #     a = GETCoefficients(coef,temp)
#         #     koef[i] = a
#         #     ###############################################################################
#         #
#         # for i in range(0,count):
#         #     interception[i] = round((Balance[i]*koef[i]),2)
#         #     ###############################################################################

#         for i in range(0,count):
#             temp = Season[i]
#             a = GETCoefficients(coef,temp)
#             koef[i] = a
#             ###############################################################################

#         for i in range(0,len(int_koef)):
#             temp = float(koef[i])
#             int_koef[i] = temp
#             ###############################################################################

#         for i in range(0,count):
#             a = float(Balance[i])*int_koef[i]
#             interception[i] = round(a,2)
#             ###############################################################################

#         # conversion to numpy
#         np_Balance = np.asarray(Balance, dtype='float64')
#         np_Departures = np.asarray(Departures, dtype='int64')
#         npNationality = np.asarray(Nationality, dtype='str')
#         np_Season = np.asarray(Season, dtype='int64')
#         npLeauge = np.asarray(leauge, dtype='str')
#         np_CUT = np.asarray(CUT, dtype='float64')
#         np_Interception = np.asarray(interception, dtype='float64')
#         ###############################################################################

#         np_CUT = np_Balance/np_Departures
#         np_CUT_inflation = np_Interception/np_Departures


#         niz = np.stack((npLeauge,np_Season,npNationality,np.round(np_CUT,2),np.round(np_CUT_inflation,2)), axis = -1)

#         ###############################################################################
#         a = Input_chose_of_GetAVGBalanceFORplayerDepartures(niz)
#         # set to DataFrame
#         data = np.array(a)
#         # set to DataFrame
#         df = pd.DataFrame(data)
#         # name of labels for head or names of collums
#         ###############################################################################
#         df.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Balance by player|  ', '  Balance + Inflation by player|  ']
#         # return DataFrame with head an names of collums
#         print("GetAVGBalanceFORpayerDepartures TEST")
#         print(df)
#         return df

# # BATCH for  specific filtring data from estraction data from function GetAVGBalanceFORplayerDepartures
# #  --> for League datas
# def BATCH_for_GetAVGBalanceFORplayerDepartures(DFrame):

#     # DataFrame to ecstract data
#     nDFRAME = GetAVGBalanceFORplayerDepartures(DFrame)

#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)


#     #reserving the number of elements in a row
#     Name_of_leauge  = [0] * count # indx 0
#     Year_of_Season = [0] * count # indx 1
#     Nationality = [0] * count # indx 2
#     Balance_by_player = [0] * count # indx 3
#     Balance_Inflation_by_player = [0] * count # indx 4

#     # '    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Balance by player|  ', '  Balance + Inflation by player|  '
#     # cast DataFrame rows to folat and int
#     nDFRAME["    Name of League |  "].astype(np.str)# ind 0
#     nDFRAME["   Year of Season |  "].astype(np.int64)# ind 1
#     nDFRAME["    Nationality |  "].astype(np.str)# ind 2
#     nDFRAME["    Balance by player|  "].astype(np.float64)# ind 3
#     nDFRAME["  Balance + Inflation by player|  "].astype(np.float64)# ind 4
#     ###############################################################################

#     #save values from the dateframe to a arrays
#     i = 0
#     for i in range(0,count):
#         Name_of_leauge[i] =  nDFRAME["    Name of League |  "][i] # indx 0
#         Year_of_Season[i] = nDFRAME["   Year of Season |  "][i] # indx 1
#         Nationality[i] = nDFRAME["    Nationality |  "][i] # indx 2
#         Balance_by_player[i] = nDFRAME["    Balance by player|  "][i] # indx 3
#         Balance_Inflation_by_player[i] = nDFRAME["  Balance + Inflation by player|  "][i] # indx 4
#         ###############################################################################

#     # conversion to numpy
#     np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
#     np_Year_of_Season = np.asarray(Year_of_Season,dtype='int64')# indx 1
#     np_Nationality = np.asarray(Nationality,dtype='str')# indx 2
#     np_Balance_by_player = np.asarray(Balance_by_player, dtype = 'float64') # indx 3
#     np_Balance_Inflation_by_player = np.asarray(Balance_Inflation_by_player,dtype='float64') # indx 4
#     ###############################################################################

#     # set the numpy arrays values into stack
#     a = np.stack((np_Name_of_leauge,np_Year_of_Season,np_Nationality,np_Balance_by_player,np_Balance_Inflation_by_player),axis= -1)
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     a_data = np.array(a)
#     # set to DataFrame
#     df_a = pd.DataFrame(a_data)
#     # name of labels for head or names of collums
#     df_a.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Balance by player|  ', '  Balance + Inflation by player|  ']
#     ###############################################################################

#     print("################################################################################################################")
#     print(df_a)
#     print("################################################################################################################")

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for LEAUGE
#     listLEAUGE = np_Name_of_leauge.tolist()
#     listLEAUGE = remove_duplicates(listLEAUGE)
#     listLEAUGE.sort()
#     ###############################################################################

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for Year_of_Season
#     listYear_of_Season = np_Year_of_Season.tolist()
#     listYear_of_Season = remove_duplicates(listYear_of_Season)
#     listYear_of_Season.sort()
#     ###############################################################################

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for Nationality
#     listNationality = np_Nationality.tolist()
#     listNationality = remove_duplicates(listNationality)
#     listNationality.sort()
#     ###############################################################################
#     #######################################################################################################################################


#     # a function in which a user selects a choice of country or championship,
#     # and chooses the name of the state or championship after which the data is printed

#     # temporary variables that note the value the ticker chooses
#     flag = 0
#     flagTemp = '0'

#     while True:

#         print("\n")
#         print("\n\t Chose a option of proces data by LEAUGE,Year_of_Season or Nationality  : ")
#         print("\t 1 -> LEAUGE statistic ! ")
#         print("\t 2 -> Year_of_Season statistic ! ")
#         print("\t 3 -> Nationality statistic ! ")
#         value = raw_input("\n\tValue between 1 and 3    : ")
#         print("\n")
#         if value.isdigit() == True:

#             value = int(value)
#             if value == 1:
#                 flag = 1
#                 ###############################################################################
#                 cont_LEAUGE = 0
#                 print("###############################################################################")
#                 print("\t Meni  LEAUGE statistic  !!!")
#                 for i in range(0,len(listLEAUGE)):
#                     print(i+1,". : ",listLEAUGE[i])
#                     cont_LEAUGE += 1
#                 print("###############################################################################")
#                 while True:

#                     print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_LEAUGE:
#                             print("You Chose : ",listLEAUGE[value])
#                             flagTemp =  str(listLEAUGE[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                          print("\n\t Enter Club   between 1 and ",cont_LEAUGE," : ")
#                          continue
#                 break
#                 ###############################################################################
#             elif value == 2:

#                 flag = 2
#                 ###############################################################################
#                 cont_Year_of_Season = 0
#                 print("###############################################################################")
#                 print("\t Meni  State statistic!!!")
#                 #cont_Compe = 0
#                 for i in range(0,len(listYear_of_Season)):
#                     print(i+1,". : ",listYear_of_Season[i])
#                     cont_Year_of_Season += 1
#                 print("###############################################################################")

#                 while True:

#                     print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_Year_of_Season:
#                             print("You Chose : ",listYear_of_Season[value])
#                             flagTemp =  int(listYear_of_Season[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                          print("\n\t Enter State   between 1 and ",cont_Year_of_Season," : ")
#                          continue

#                 break
#                 ###############################################################################
#             elif value == 3:
#                 flag = 3
#                 ###############################################################################
#                 cont_Nationality = 0
#                 print("###############################################################################")
#                 print("\t Meni  Competition statistic!!!")
#                 #cont_Compe = 0
#                 for i in range(0,len(listNationality)):
#                     print(i+1,". : ",listNationality[i])
#                     cont_Nationality += 1
#                 print("###############################################################################")

#                 while True:

#                     print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_Nationality:
#                             print("You Chose : ",listNationality[value])
#                             flagTemp =  str(listNationality[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                          print("\n\t Enter Competition   between 1 and ",cont_Nationality," : ")
#                          continue
#                 break
#                 ###############################################################################
#             else:
#                 print("\n\tValue between 1 or  4  !!!")
#         elif value.isdigit() != True:

#              print("\n\tValue between 1 or    !!!")
#              continue

#     #######################################################################################################################################


#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)

#     # temp var for count number of roew for dynamic reserving
#     bro = 0

#     # count number of rows in date frame
#     # name of LEAUGE
#     if flag == 1:
#         for i in range(0,len(a)):
#             if str(a[i][0]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # count number of rows in date frame
#     # number of Season
#     if flag == 2:
#         for i in range(0,len(a)):
#             if int(a[i][1]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # count number of rows in date frame
#     # Nationality
#     if flag == 3:
#         for i in range(0,len(a)):
#             if str(a[i][2]) == flagTemp :
#                 bro +=1
#     ###############################################################################
#     # reserving the number of elements in a row
#     array1 = [0] * bro
#     array2 = [0] * bro
#     array3 = [0] * bro
#     array4 = [0] * bro
#     array5 = [0] * bro
#     ###############################################################################

#     # temporarily storing data from a numpy array into a
#     # common array to allocate as many places as you need to avoid empty places in the DataFrame
#     # storing data from State user chose options

#     # name of LEAUGE
#     y = 0
#     if flag == 1:
#         for i in range(0,len(a)):
#             if str(a[i][0]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 y+=1
#     ###############################################################################
#     # number of Season
#     if flag == 2:
#         for i in range(0,len(a)):
#             if int(a[i][1]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 y+=1
#     ###############################################################################
#     # Nationality
#     if flag == 3:
#         for i in range(0,len(a)):
#             if str(a[i][2]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 y+=1
#     ###############################################################################

#     # reserving the number of elements in a row
#     niz_N1 = [0]*bro
#     #Initialize a new array
#     np_niz1 = np.asarray(niz_N1, dtype = 'str')
#     np_niz2 = np.asarray(niz_N1, dtype = 'int64')
#     np_niz3 = np.asarray(niz_N1, dtype = 'float64')

#     #set arr to stack for operations with data lik sort and convert
#     new_niz = np.stack((np_niz1,np_niz2,np_niz1,np_niz3,np_niz3),axis= -1)
#     #######################################################################################################################################

#     # relocating data from temporary arrays to numpy arrays
#     y = 0
#     for i in range(0,bro):
#         new_niz[i][0] = array1[y]
#         new_niz[i][1] = array2[y]
#         new_niz[i][2] = array3[y]
#         new_niz[i][3] = array4[y]
#         new_niz[i][4] = array5[y]
#         y+=1
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     new_data = np.array(new_niz)
#     # set to DataFrame
#     df_new = pd.DataFrame(new_data)
#     # name of labels for head or names of collums
#     df_new.columns = ['    Name of League |  ', '   Year of Season |  ','    Nationality |  ', '    Balance by player|  ', '  Balance + Inflation by player|  ']
#     print("###################################################################################################################################################")
#     print(df_new)
#     print("###################################################################################################################################################")

#     return df_new        


# # get sorted data by the leauge
# #  --> for League datas
# def GetDataForLeauge_AVG_Seasons(DFrame):

#     #count number of rows in date frame
#     count = NumberOfRows(DFrame)

#     #reserving the number of elements in a row
#     Nationality = [0] * count
#     Arrivals = [0] * count
#     koef = [0] * count
#     Season = [0] * count
#     leauge = [0] * count
#     niz1 = [0] *count
#     Expenditures = [0] *count
#     Income = [0] *count
#     Balance = [0] *count
#     Departures = [0] *count
#     inter_Balance = [0] *count
#     inter_Expenditures = [0] *count
#     inter_Income = [0] *count
#     int_koef = [0] * count
#     ###############################################################################

#     # cast DataFrame rows to folat and int and str
#     DFrame["Expenditures"].astype(np.int64)
#     DFrame["Income"].astype(np.int64)
#     DFrame["Balance"].astype(np.int64)
#     DFrame["Departures"].astype(np.int64)
#     DFrame["Arrivals"].astype(np.int64)
#     DFrame["Competition"].astype(np.str)
#     DFrame["Year"].astype(np.int64)
#     ###############################################################################

#     i = 0
#     for i in range(0,count):
#         Arrivals[i] = DFrame["Arrivals"][i]
#         leauge[i] = DFrame["Competition"][i]
#         Season[i] =  DFrame["Year"][i]
#         Expenditures[i] =  DFrame["Expenditures"][i]
#         Income[i] =  DFrame["Income"][i]
#         Balance[i] =  DFrame["Balance"][i]
#         Departures[i] =  DFrame["Departures"][i]
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
#         a = float(Balance[i])*int_koef[i]
#         b = float(Expenditures[i])*int_koef[i]
#         c = float(Income[i])*int_koef[i]
#         inter_Balance[i] = round(a,2)
#         inter_Expenditures[i] = round(b,2)
#         inter_Income[i] = round(c,2)
#         ###############################################################################

#     npLeauge = np.asarray(leauge, dtype = 'str')
#     np_Arrival = np.asarray(Arrivals, dtype ='int64')
#     np_Season = np.asarray(Season, dtype = 'int64' )
#     np_Expenditures = np.asarray(inter_Expenditures, dtype = 'float64' )
#     np_Income = np.asarray(inter_Income, dtype = 'float64' )
#     np_Balance = np.asarray(inter_Balance, dtype = 'float64' )
#     np_Departures = np.asarray(Departures, dtype = 'int64' )
#     ###############################################################################


#     np_niz1 = np.asarray(niz1, dtype = 'str')
#     np_niz2 = np.asarray(niz1, dtype = 'int64')
#     np_niz3 = np.asarray(niz1, dtype = 'int64')
#     np_niz4 = np.asarray(niz1, dtype = 'int64')


#     niz = np.stack((np_niz1,np_niz2,np_niz3,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4), axis = -1)
#     a = np.stack((np_Arrival,npLeauge,np_Expenditures,np_Income,np_Balance,np_Departures,np_Season), axis = -1)
#     ###############################################################################

#     # Function
#     n = count
#     t = 0
#     visited = [False for i in range(n)]
#     # Traverse through array elements
#     # and count frequencies
#     for i in range(n):
#         # Skip this element if already
#         # processed
#         if (visited[i] == True):
#             continue
#         count = 1
#         suma_Arrival = int(a[i][0])
#         sum_Expenditures = float(a[i][2])
#         sum_Income = float(a[i][3])
#         sum_Balance = float(a[i][4])
#         sum_Departures = int(a[i][5])
#         ###############################################################################
#         for j in range(i + 1, n, 1):
#             if (a[i][1] == a[j][1]):
#                 suma_Arrival += int(a[j][0])
#                 sum_Expenditures += float(a[j][2])
#                 sum_Income += float(a[j][3])
#                 sum_Balance += float(a[j][4])
#                 sum_Departures += int(a[j][5])
#                 visited[j] = True
#                 count += 1
#                 ###############################################################################

#         if a[i][1] != 0 :
#             niz[t][1] = a[i][1]
#             niz[t][0] = suma_Arrival
#             niz[t][2] = count
#             niz[t][3] = sum_Expenditures
#             niz[t][4] = sum_Income
#             niz[t][5] = sum_Departures
#             niz[t][6] = sum_Balance
#             niz[t][7] = round(sum_Expenditures/float(suma_Arrival),2)
#             niz[t][8] = round(sum_Income/float(sum_Departures),2)
#             niz[t][9] = round(sum_Balance/float(sum_Departures),2)
#             niz[t][10] = round(sum_Expenditures/float(count),2)
#             niz[t][11] = round(sum_Income/float(count),2)
#             niz[t][12] = round(sum_Balance/float(count),2)
#             niz[t][13] = a[i][6]
#             t +=1
#             suma = 0
#             ###############################################################################

#     N =0
#     for i in range(0,len(niz)):
#         if int(niz[i][0]) != 0:
#             N +=1


#     #inicijalizacija novog niza ::
#     niz_1 = [0] * N


#     np_niz_1 = np.asarray(niz_1,dtype='str')
#     np_niz_2 = np.asarray(niz_1, dtype='int64')
#     np_niz_3 = np.asarray(niz_1, dtype='int64')
#     np_niz_4 = np.asarray(niz_1, dtype='float64')


#     new_niz = np.stack((np_niz_1,np_niz_2,np_niz_3,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4), axis = -1)
#     ###############################################################################
#     for i in range(0,N):
#         #print("int(niz[i][0])",int(niz[i][0]))
#         if int(niz[i][0]) != 0:
#             #print(" drugi ispis int(niz[i][0])",int(niz[i][0]))
#             int(niz[i][0]) != 0
#             new_niz[i][0] = niz[i][1] # leauge
#             new_niz[i][1] = niz[i][3] # Expend
#             new_niz[i][2] = niz[i][4] # Income
#             new_niz[i][3] = niz[i][6] # Balance
#             new_niz[i][4] = niz[i][2] # number of seasons
#             new_niz[i][5] = niz[i][0] # sum of Arrivlas of all seasons
#             new_niz[i][6] = niz[i][5] # sum of Depatrues of all seasons
#             new_niz[i][7] = niz[i][7] # avg Expend of Arrivlas
#             new_niz[i][8] = niz[i][8] # avg Income of Arrivlas
#             new_niz[i][9] = niz[i][9] # avg Balance of Arrivlas
#             new_niz[i][10] = niz[i][10] # avg Expend number the seasons
#             new_niz[i][11] = niz[i][11] # avg Income number the seasons
#             new_niz[i][12] = niz[i][12] # avg Balance number the seasons
#             ###############################################################################

#     # call the function
#     a = Input_chose_of_GetDataForLeauge_AVG_Season(new_niz)
#     # set to DataFrame
#     data = np.array(a)

#     df = pd.DataFrame(data)
#     df.columns = ['    Name of leauge |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
#      '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
#      '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
#     print(df)
#     ###############################################################################
#     return df


# # BATCH for  specific filtring data from estraction data from function GetDataForLeauge_AVG_Seasons
# #  --> for League datas
# def BATCH_for_GetDataForLeauge_AVG_Seasons(DFrame):

#     # DataFrame to ecstract data
#     nDFRAME = GetDataForLeauge_AVG_Seasons(DFrame)

#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)


#     #reserving the number of elements in a row
#     Name_of_leauge  = [0] * count # indx 0
#     Expend = [0] * count # indx 1
#     Income = [0] * count # indx 2
#     Balance =  [0] * count # indx 3
#     number_of_Season = [0] * count # indx 4
#     sum_of_Arrivlas = [0] * count # indx 5
#     sum_of_Depatrues = [0] * count # indx 6
#     avg_Expend_of_Arrivlas = [0] * count # indx 7
#     avg_Income_of_Depatrues =  [0] * count # indx 8
#     avg_Balance_of_Depatrues = [0] * count # indx 9
#     avg_Expend_Season = [0] * count # indx 10
#     avg_Income_Season  =  [0] * count # indx 11
#     avg_Balance_Season  =  [0] * count # indx 12


#     # cast DataFrame rows to folat and int
#     nDFRAME["    Name of leauge |  "].astype(np.str)# ind 0
#     nDFRAME["    Expend |  "].astype(np.float64)# ind 1
#     nDFRAME["    Income |  "].astype(np.float64)# ind 2
#     nDFRAME["    Balance |  "].astype(np.float64)# ind 3
#     nDFRAME["    number of Season |  "].astype(np.int64)# ind 4
#     nDFRAME["    sum of Arrivlas |  "].astype(np.int64)# ind 5
#     nDFRAME["    sum of Depatrues |  "].astype(np.int64)# ind 6
#     nDFRAME["    avg Expend of Arrivlas |  "].astype(np.float64)# ind 7
#     nDFRAME["    avg Income of Depatrues |  "].astype(np.float64)# ind 8
#     nDFRAME["    avg Balance of Depatrues |  "].astype(np.float64)# ind 9
#     nDFRAME["    avg Expend/Season |  "].astype(np.float64)# ind 10
#     nDFRAME["    avg Income/Season |  "].astype(np.float64)# ind 11
#     nDFRAME["    avg Balance/Season |  "].astype(np.float64)# ind 12
#     ###############################################################################

#     #save values from the dateframe to a arrays
#     i = 0
#     for i in range(0,count):

#         Name_of_leauge[i] =  nDFRAME["    Name of leauge |  "][i] # indx 0
#         Expend[i] = nDFRAME["    Expend |  "][i] # indx 1
#         Income[i] = nDFRAME["    Income |  "][i] # indx 2
#         Balance[i] = nDFRAME["    Balance |  "][i] # indx 3
#         number_of_Season[i] = nDFRAME["    number of Season |  "][i] # indx 4
#         sum_of_Arrivlas[i] = nDFRAME["    sum of Arrivlas |  "][i] # indx 5
#         sum_of_Depatrues[i] = nDFRAME["    sum of Depatrues |  "][i] # indx 6
#         avg_Expend_of_Arrivlas[i] = nDFRAME["    avg Expend of Arrivlas |  "][i] # indx 7
#         avg_Income_of_Depatrues[i] = nDFRAME["    avg Income of Depatrues |  "][i] # indx 8
#         avg_Balance_of_Depatrues[i] = nDFRAME["    avg Balance of Depatrues |  "][i] # indx 9
#         avg_Expend_Season[i] = nDFRAME["    avg Expend/Season |  "][i] # indx 10
#         avg_Income_Season[i] = nDFRAME["    avg Income/Season |  "][i] # indx 11
#         avg_Balance_Season[i] = nDFRAME["    avg Balance/Season |  "][i] # indx 12
#         ###############################################################################

#     # conversion to numpy
#     np_Name_of_leauge = np.asarray(Name_of_leauge, dtype = 'str') # indx 0
#     np_Expend = np.asarray(Expend,dtype='float64')# indx 1
#     np_Income = np.asarray(Income,dtype='float64')# indx 2
#     np_Balance = np.asarray(Balance, dtype = 'float64') # indx 3
#     np_number_of_Season = np.asarray(number_of_Season,dtype='int64') # indx 4
#     np_sum_of_Arrivlas = np.asarray(sum_of_Arrivlas, dtype ='int64') # indx 5
#     np_sum_of_Depatrues = np.asarray(sum_of_Depatrues,dtype='int64') # indx 6
#     np_avg_Expend_of_Arrivlas = np.asarray(avg_Expend_of_Arrivlas, dtype = 'float64' ) # indx 7
#     np_avg_Income_of_Depatrues = np.asarray(avg_Income_of_Depatrues,dtype='float64') # indx 8
#     np_avg_Balance_of_Depatrues = np.asarray(avg_Balance_of_Depatrues, dtype = 'float64' ) # indx 9
#     np_avg_Expend_Season = np.asarray(avg_Expend_Season, dtype = 'float64' ) # indx 10
#     np_avg_Income_Season = np.asarray(avg_Income_Season, dtype = 'float64' ) # indx 11
#     np_avg_Balance_Season = np.asarray(avg_Balance_Season, dtype = 'float64' ) # indx 12
#     ###############################################################################

#     # set the numpy arrays values into stack
#     a = np.stack((np_Name_of_leauge,np_Expend,np_Income,np_Balance,np_number_of_Season,np_sum_of_Arrivlas,np_sum_of_Depatrues,
#     np_avg_Expend_of_Arrivlas,np_avg_Income_of_Depatrues,np_avg_Balance_of_Depatrues,np_avg_Expend_Season,np_avg_Income_Season,np_avg_Balance_Season),axis= -1)
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     a_data = np.array(a)
#     # set to DataFrame
#     df_a = pd.DataFrame(a_data)
#     # name of labels for head or names of collums
#     df_a.columns = ['    Name of leauge |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
#      '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
#      '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
#     ###############################################################################

#     print("################################################################################################################")
#     print(df_a)
#     print("################################################################################################################")

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for LEAUGE
#     listLEAUGE = np_Name_of_leauge.tolist()
#     listLEAUGE = remove_duplicates(listLEAUGE)
#     listLEAUGE.sort()
#     ###############################################################################

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for number_of_Season
#     listNUMBERofSesons = np_number_of_Season.tolist()
#     listNUMBERofSesons = remove_duplicates(listNUMBERofSesons)
#     listNUMBERofSesons.sort()
#     ###############################################################################
#     #######################################################################################################################################


#     # a function in which a user selects a choice of country or championship,
#     # and chooses the name of the state or championship after which the data is printed

#     # temporary variables that note the value the ticker chooses
#     flag = 0
#     flagTemp = '0'

#     while True:

#         print("\n")
#         print("\n\t Chose a option of proces data by State or Competition  : ")
#         print("\t 1 -> LEAUGE statistic ! ")
#         print("\t 2 -> NUMBER of Sesons statistic ! ")
#         value = raw_input("\n\tValue between 1 and 2    : ")
#         print("\n")
#         if value.isdigit() == True:

#             value = int(value)
#             if value == 1:
#                 flag = 1
#                 ###############################################################################
#                 # CLUBS
#                 cont_LEAUGE = 0
#                 print("###############################################################################")
#                 print("\t Meni  LEAUGE statistic  !!!")
#                 #cont_state = 0
#                 for i in range(0,len(listLEAUGE)):
#                     print(i+1,". : ",listLEAUGE[i])
#                     cont_LEAUGE += 1
#                 print("###############################################################################")
#                 while True:

#                     print("\n\t Enter Club   between 0 and ",cont_LEAUGE," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_LEAUGE:
#                             print("You Chose : ",listLEAUGE[value])
#                             flagTemp =  str(listLEAUGE[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                          print("\n\t Enter Club   between 0 and ",cont_LEAUGE," : ")
#                          continue
#                 break
#                 ###############################################################################


#             elif value == 2:

#                 flag = 2
#                 ###############################################################################
#                 cont_NUMBERofSesons = 0
#                 print("###############################################################################")
#                 print("\t Meni  State statistic!!!")
#                 #cont_Compe = 0
#                 for i in range(0,len(listNUMBERofSesons)):
#                     print(i+1,". : ",listNUMBERofSesons[i])
#                     cont_NUMBERofSesons += 1
#                 print("###############################################################################")

#                 while True:

#                     print("\n\t Enter State   between 1 and ",cont_NUMBERofSesons," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_NUMBERofSesons:
#                             print("You Chose : ",listNUMBERofSesons[value])
#                             flagTemp =  int(listNUMBERofSesons[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                           print("\n\tValue between 1 or  2  !!!")
#                           continue
#                 break
#                 ###############################################################################
#             else:
#                 print("\n\tValue between 1 or  4  !!!")
#         elif value.isdigit() != True:

#              print("\n\tValue between 1 or  2  !!!")
#              continue
#     #######################################################################################################################################

#     print("flagTemp",flagTemp,"flag",flag)
#     #######################################################################################################################################

#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)

#     # temp var for count number of roew for dynamic reserving
#     bro = 0

#     # count number of rows in date frame
#     # LEAUGE
#     if flag == 1:
#         for i in range(0,len(a)):
#             if str(a[i][0]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # count number of rows in date frame
#     # number of Season
#     if flag == 2:
#         for i in range(0,len(a)):
#             if int(a[i][4]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # reserving the number of elements in a row
#     array1 = [0] * bro
#     array2 = [0] * bro
#     array3 = [0] * bro
#     array4 = [0] * bro
#     array5 = [0] * bro
#     array6 = [0] * bro
#     array7 = [0] * bro
#     array8 = [0] * bro
#     array9 = [0] * bro
#     array10 = [0] * bro
#     array11 = [0] * bro
#     array12 = [0] * bro
#     array13 = [0] * bro
#     ###############################################################################

#     # temporarily storing data from a numpy array into a
#     # common array to allocate as many places as you need to avoid empty places in the DataFrame
#     # storing data from State user chose options
#     y = 0
#     if flag == 1:
#         for i in range(0,len(a)):
#             if str(a[i][0]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 array6[y] = a[i][5]
#                 array7[y] = a[i][6]
#                 array8[y] = a[i][7]
#                 array9[y] = a[i][8]
#                 array10[y] = a[i][9]
#                 array11[y] = a[i][10]
#                 array12[y] = a[i][11]
#                 array13[y] = a[i][12]
#                 y+=1
#     ###############################################################################

#     if flag == 2:
#         for i in range(0,len(a)):
#             if int(a[i][4]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 array6[y] = a[i][5]
#                 array7[y] = a[i][6]
#                 array8[y] = a[i][7]
#                 array9[y] = a[i][8]
#                 array10[y] = a[i][9]
#                 array11[y] = a[i][10]
#                 array12[y] = a[i][11]
#                 array13[y] = a[i][12]
#                 y+=1
#     ###############################################################################


#     # reserving the number of elements in a row
#     niz_N1 = [0]*bro
#     #Initialize a new array
#     np_niz1 = np.asarray(niz_N1, dtype = 'str')
#     np_niz2 = np.asarray(niz_N1, dtype = 'int64')
#     np_niz3 = np.asarray(niz_N1, dtype = 'float64')

#     #set arr to stack for operations with data lik sort and convert
#     new_niz = np.stack((np_niz1,np_niz3,np_niz3,np_niz3,np_niz2,np_niz2,np_niz2,np_niz3,np_niz3,np_niz3,np_niz3,np_niz3,np_niz3),axis= -1)
#     #######################################################################################################################################

#     # relocating data from temporary arrays to numpy arrays
#     y = 0
#     for i in range(0,bro):
#         new_niz[i][0] = array1[y]
#         new_niz[i][1] = array2[y]
#         new_niz[i][2] = array3[y]
#         new_niz[i][3] = array4[y]
#         new_niz[i][4] = array5[y]
#         new_niz[i][5] = array6[y]
#         new_niz[i][6] = array7[y]
#         new_niz[i][7] = array8[y]
#         new_niz[i][8] = array9[y]
#         new_niz[i][9] = array10[y]
#         new_niz[i][10] = array11[y]
#         new_niz[i][11] = array12[y]
#         new_niz[i][12] = array13[y]
#         y+=1
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     new_data = np.array(new_niz)
#     # set to DataFrame
#     df_new = pd.DataFrame(new_data)
#     # name of labels for head or names of collums
#     df_new.columns = ['    Name of leauge |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
#      '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
#      '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
#     print("###################################################################################################################################################")
#     print(df_new)
#     print("###################################################################################################################################################")

#     return df_new     


# # get avg Year Season of first 25 leuge money transaction for all Leuges ,regardless of the league, therefore, only years of all seasons together
# #  --> for League datas
# def GetBYyear(DFrame):

#     #count number of rows in date frame
#     count = NumberOfRows(DFrame)

#     #reserving the number of elements in a row
#     Nationality = [0] * count
#     Arrivals = [0] * count
#     Season = [0] * count
#     leauge = [0] * count
#     niz1 = [0] *count
#     Expenditures = [0] *count
#     Income = [0] *count
#     Balance = [0] *count
#     Departures = [0] *count

#     koef = [0] * count
#     inter_Balance = [0] *count
#     inter_Expenditures = [0] *count
#     inter_Income = [0] * count
#     int_koef = [0] * count
#     ###############################################################################

#     # cast DataFrame rows to folat and int and str
#     DFrame["Expenditures"].astype(np.int64)
#     DFrame["Income"].astype(np.int64)
#     DFrame["Balance"].astype(np.int64)
#     DFrame["Departures"].astype(np.int64)
#     DFrame["Arrivals"].astype(np.int64)
#     DFrame["Competition"].astype(np.str)
#     DFrame["Year"].astype(np.int64)
#     ###############################################################################

#     #save values from the dateframe to a string
#     i = 0
#     for i in range(0,count):
#         Arrivals[i] = DFrame["Arrivals"][i]
#         leauge[i] = DFrame["Competition"][i]
#         Season[i] =  DFrame["Year"][i]
#         Expenditures[i] =  DFrame["Expenditures"][i]
#         Income[i] =  DFrame["Income"][i]
#         Balance[i] =  DFrame["Balance"][i]
#         Departures[i] =  DFrame["Departures"][i]
#         ###############################################################################

#     # calculation of coeficent of inflacion
#     for i in range(0,count):
#         temp = Season[i]
#         a = GETCoefficients(coef,temp)
#         koef[i] = a
#         ###############################################################################

#     for i in range(0,len(int_koef)):
#         temp = float(koef[i])
#         int_koef[i] = temp
#         ###############################################################################
#     # calculation  Inflation for Potential, Earned and Profit
#     for i in range(0,count):
#         a = float(Balance[i])*int_koef[i]
#         b = float(Expenditures[i])*int_koef[i]
#         c = float(Income[i])*int_koef[i]
#         inter_Balance[i] = round(a,2)
#         inter_Expenditures[i] = round(b,2)
#         inter_Income[i] = round(c,2)
#         ###############################################################################


#     npLeauge = np.asarray(leauge, dtype = 'str')
#     np_Arrival = np.asarray(Arrivals, dtype ='int64')
#     np_Season = np.asarray(Season, dtype = 'int64' )
#     np_Expenditures = np.asarray(inter_Expenditures, dtype = 'float64' )
#     np_Income = np.asarray(inter_Income, dtype = 'float64' )
#     np_Balance = np.asarray(inter_Balance, dtype = 'float64' )
#     np_Departures = np.asarray(Departures, dtype = 'int64' )
#     ###############################################################################


#     np_niz1 = np.asarray(niz1, dtype = 'str')
#     np_niz2 = np.asarray(niz1, dtype = 'int64')
#     np_niz3 = np.asarray(niz1, dtype = 'int64')
#     np_niz4 = np.asarray(niz1, dtype = 'int64')

#     #set arr to stack for operations with data lik sort and convert
#     niz = np.stack((np_niz1,np_niz2,np_niz3,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4,np_niz4), axis = -1)
#     a = np.stack((np_Arrival,npLeauge,np_Expenditures,np_Income,np_Balance,np_Departures,np_Season), axis = -1)
#     ###############################################################################

#     # Function for sorting
#     # varibales for sorting
#     n = count
#     t = 0

#     visited = [False for i in range(n)]
#     # Traverse through array elements
#     # and count frequencies
#     for i in range(n):
#         # Skip this element if already
#         # processed
#         if (visited[i] == True):
#             continue
#         count = 1
#         suma_Arrival = int(a[i][0])
#         sum_Expenditures = float(a[i][2])
#         sum_Income = float(a[i][3])
#         sum_Balance = float(a[i][4])
#         sum_Departures = int(a[i][5])
#         ###############################################################################
#         for j in range(i + 1, n, 1):
#             if (a[i][6] == a[j][6]):
#                 suma_Arrival += int(a[j][0])
#                 sum_Expenditures += float(a[j][2])
#                 sum_Income += float(a[j][3])
#                 sum_Balance += float(a[j][4])
#                 sum_Departures += int(a[j][5])
#                 visited[j] = True
#                 count += 1
#                 ###############################################################################

#         if a[i][1] != 0 :
#             niz[t][1] = a[i][1]
#             niz[t][0] = suma_Arrival
#             niz[t][2] = count
#             niz[t][3] = sum_Expenditures
#             niz[t][4] = sum_Income
#             niz[t][5] = sum_Departures
#             niz[t][6] = sum_Balance
#             niz[t][7] = round(sum_Expenditures/float(suma_Arrival),2)
#             niz[t][8] = round(sum_Income/float(sum_Departures),2)
#             niz[t][9] = round(sum_Balance/float(sum_Departures),2)
#             niz[t][10] = round(sum_Expenditures/(count),2)
#             niz[t][11] = round(sum_Income/(count),2)
#             niz[t][12] = round(sum_Balance/float(count),2)
#             niz[t][13] = a[i][6]
#             ###############################################################################

#             t +=1
#             suma = 0

#     # count array size with N
#     N =0
#     for i in range(0,len(niz)):
#         if int(niz[i][0]) != 0:
#             N +=1


#     #Initialize a new array
#     niz_1 = [0] * N


#     np_niz_1 = np.asarray(niz_1,dtype='str')
#     np_niz_2 = np.asarray(niz_1, dtype='int64')
#     np_niz_3 = np.asarray(niz_1, dtype='int64')
#     np_niz_4 = np.asarray(niz_1, dtype='float64')


#     new_niz = np.stack((np_niz_1,np_niz_2,np_niz_3,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4,np_niz_4), axis = -1)

#     # avg Balance number the seasons
#     for i in range(0,N):
#         if int(niz[i][0]) != 0:
#             # int(niz[i][0]) != 0
#             new_niz[i][0] = niz[i][13] # year
#             new_niz[i][1] = niz[i][3] # Expend
#             new_niz[i][2] = niz[i][4] # Income
#             new_niz[i][3] = niz[i][6] # Balance
#             new_niz[i][4] = niz[i][2] # number of seasons
#             new_niz[i][5] = niz[i][0] # sum of Arrivlas of all seasons
#             new_niz[i][6] = niz[i][5] # sum of Depatrues of all seasons
#             new_niz[i][7] = niz[i][7] # avg Expend of Arrivlas
#             new_niz[i][8] = niz[i][8] # avg Income of Depatrues
#             new_niz[i][9] = niz[i][9] # avg Balance of Depatrues
#             new_niz[i][10] = niz[i][10] # avg Expend number the seasons
#             new_niz[i][11] = niz[i][11] # avg Income number the seasons
#             new_niz[i][12] = niz[i][12] # avg Balance number the seasons
#             ###############################################################################


#     # sort by appropriate elements and by columns
#     # cekanje na funkciju !!!!!  meni napravljen

#     # convert from stack with values to data for dataFrame
#     a = Input_chose_of_GetBYyear(new_niz)
#     data = np.array(a)
#     # set to DataFrame
#     df = pd.DataFrame(data)
#     # name of labels for head or names of collums
#     df.columns = ['    Year |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
#      '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
#      '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
#     ###############################################################################
#     # return DataFrame with head an names of collums
#     print(df)
#     return df # function FULL -> BATCH  ~ 20.
# #######################################################################################################################################

# # BATCH for  specific filtring data from estraction data from function GetBYyear
# #  --> for League datas
# def BATCH_for_GetBYyear(DFrame):

#     # DataFrame to ecstract data
#     nDFRAME = GetBYyear(DFrame)

#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)


#     #reserving the number of elements in a row
#     Year  = [0] * count # indx 0
#     Expend = [0] * count # indx 1
#     Income = [0] * count # indx 2
#     Balance =  [0] * count # indx 3
#     number_of_Season = [0] * count # indx 4
#     sum_of_Arrivlas = [0] * count # indx 5
#     sum_of_Depatrues = [0] * count # indx 6
#     avg_Expend_of_Arrivlas = [0] * count # indx 7
#     avg_Income_of_Depatrues =  [0] * count # indx 8
#     avg_Balance_of_Depatrues = [0] * count # indx 9
#     avg_Expend_Season = [0] * count # indx 10
#     avg_Income_Season  =  [0] * count # indx 11
#     avg_Balance_Season  =  [0] * count # indx 12


#     # cast DataFrame rows to folat and int
#     nDFRAME["    Year |  "].astype(np.int64)# ind 0
#     nDFRAME["    Expend |  "].astype(np.str)# ind 1
#     nDFRAME["    Income |  "].astype(np.str)# ind 2
#     nDFRAME["    Balance |  "].astype(np.str)# ind 3
#     nDFRAME["    number of Season |  "].astype(np.int64)# ind 4
#     nDFRAME["    sum of Arrivlas |  "].astype(np.int64)# ind 5
#     nDFRAME["    sum of Depatrues |  "].astype(np.int64)# ind 6
#     nDFRAME["    avg Expend of Arrivlas |  "].astype(np.float64)# ind 7
#     nDFRAME["    avg Income of Depatrues |  "].astype(np.float64)# ind 8
#     nDFRAME["    avg Balance of Depatrues |  "].astype(np.float64)# ind 9
#     nDFRAME["    avg Expend/Season |  "].astype(np.float64)# ind 10
#     nDFRAME["    avg Income/Season |  "].astype(np.float64)# ind 11
#     nDFRAME["    avg Balance/Season |  "].astype(np.float64)# ind 12
#     ###############################################################################

#     #save values from the dateframe to a arrays
#     i = 0
#     for i in range(0,count):

#         Year[i] =  nDFRAME["    Year |  "][i] # indx 0
#         Expend[i] = nDFRAME["    Expend |  "][i] # indx 1
#         Income[i] = nDFRAME["    Income |  "][i] # indx 2
#         Balance[i] = nDFRAME["    Balance |  "][i] # indx 3
#         number_of_Season[i] = nDFRAME["    number of Season |  "][i] # indx 4
#         sum_of_Arrivlas[i] = nDFRAME["    sum of Arrivlas |  "][i] # indx 5
#         sum_of_Depatrues[i] = nDFRAME["    sum of Depatrues |  "][i] # indx 6
#         avg_Expend_of_Arrivlas[i] = nDFRAME["    avg Expend of Arrivlas |  "][i] # indx 7
#         avg_Income_of_Depatrues[i] = nDFRAME["    avg Income of Depatrues |  "][i] # indx 8
#         avg_Balance_of_Depatrues[i] = nDFRAME["    avg Balance of Depatrues |  "][i] # indx 9
#         avg_Expend_Season[i] = nDFRAME["    avg Expend/Season |  "][i] # indx 10
#         avg_Income_Season[i] = nDFRAME["    avg Income/Season |  "][i] # indx 11
#         avg_Balance_Season[i] = nDFRAME["    avg Balance/Season |  "][i] # indx 12
#         ###############################################################################

#     # conversion to numpy
#     np_Year = np.asarray(Year, dtype = 'int64') # indx 0
#     np_Expend = np.asarray(Expend,dtype='float64')# indx 1
#     np_Income = np.asarray(Income,dtype='float64')# indx 2
#     np_Balance = np.asarray(Balance, dtype = 'float64') # indx 3
#     np_number_of_Season = np.asarray(number_of_Season,dtype='int64') # indx 4
#     np_sum_of_Arrivlas = np.asarray(sum_of_Arrivlas, dtype ='int64') # indx 5
#     np_sum_of_Depatrues = np.asarray(sum_of_Depatrues,dtype='int64') # indx 6
#     np_avg_Expend_of_Arrivlas = np.asarray(avg_Expend_of_Arrivlas, dtype = 'float64' ) # indx 7
#     np_avg_Income_of_Depatrues = np.asarray(avg_Income_of_Depatrues,dtype='float64') # indx 8
#     np_avg_Balance_of_Depatrues = np.asarray(avg_Balance_of_Depatrues, dtype = 'float64' ) # indx 9
#     np_avg_Expend_Season = np.asarray(avg_Expend_Season, dtype = 'float64' ) # indx 10
#     np_avg_Income_Season = np.asarray(avg_Income_Season, dtype = 'float64' ) # indx 11
#     np_avg_Balance_Season = np.asarray(avg_Balance_Season, dtype = 'float64' ) # indx 12
#     ###############################################################################

#     # set the numpy arrays values into stack
#     a = np.stack((np_Year,np_Expend,np_Income,np_Balance,np_number_of_Season,np_sum_of_Arrivlas,np_sum_of_Depatrues,
#     np_avg_Expend_of_Arrivlas,np_avg_Income_of_Depatrues,np_avg_Balance_of_Depatrues,np_avg_Expend_Season,np_avg_Income_Season,np_avg_Balance_Season),axis= -1)
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     a_data = np.array(a)
#     # set to DataFrame
#     df_a = pd.DataFrame(a_data)
#     # name of labels for head or names of collums
#     df_a.columns = ['    Year |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
#      '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
#      '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
#     ###############################################################################

#     print("################################################################################################################")
#     print(df_a)
#     print("################################################################################################################")

#     # convert data from numpay ndarray to list and remove duplicates elemtes of list for YEAR
#     listYEAR = np_Year.tolist()
#     listYEAR = remove_duplicates(listYEAR)
#     listYEAR.sort()
#     ###############################################################################


#     # a function in which a user selects a choice of country or championship,
#     # and chooses the name of the state or championship after which the data is printed

#     # temporary variables that note the value the ticker chooses
#     flag = 0
#     flagTemp = '0'

#     while True:

#         print("\n")
#         print("\n\t Chose a option of proces data by YEAR : ")
#         print("\t 1 -> YEAR ! ")
#         value = raw_input("\n\tValue ")
#         print("\n")
#         if value.isdigit() == True:

#             value = int(value)
#             if value == 1:

#                 flag = 1
#                 ###############################################################################
#                 # drzave
#                 cont_YEAR = 0
#                 print("###############################################################################")
#                 print("\t Meni  State!!!")
#                 #cont_state = 0
#                 for i in range(0,len(listYEAR)):
#                     print(i+1,". : ",listYEAR[i])
#                     cont_YEAR += 1
#                 print("###############################################################################")
#                 while True:

#                     print("\n\t Enter State   between 0 and ",cont_YEAR," : ")
#                     value = raw_input("\n\tValue : " )
#                     if value.isdigit() == True:

#                         value = int(value)
#                         value =value -1
#                         if 0 <= value < cont_YEAR:
#                             print("You Chose : ",listYEAR[value])
#                             flagTemp =  int(listYEAR[value])
#                             break
#                         else:
#                            print("\n\tValue between bounds :")
#                     elif value.isdigit() != True:

#                           print("\n\t Enter State   between 0 and ",cont_YEAR," : ")
#                           continue
#                 break
#                 ###############################################################################
#             else:
#                 print("\n\tValue :  !!!")
#         elif value.isdigit() != True:

#              print("\n\tValue 1 !!!")
#              continue
#     #######################################################################################################################################

#     #count number of rows in date frame
#     count = NumberOfRows(nDFRAME)

#     # temp var for count number of roew for dynamic reserving
#     bro = 0

#     # count number of rows in date frame
#     # YEAR
#     if flag == 1:
#         for i in range(0,len(a)):
#             if int(a[i][0]) == flagTemp :
#                 bro +=1
#     ###############################################################################

#     # reserving the number of elements in a row
#     array1 = [0] * bro
#     array2 = [0] * bro
#     array3 = [0] * bro
#     array4 = [0] * bro
#     array5 = [0] * bro
#     array6 = [0] * bro
#     array7 = [0] * bro
#     array8 = [0] * bro
#     array9 = [0] * bro
#     array10 = [0] * bro
#     array11 = [0] * bro
#     array12 = [0] * bro
#     array13 = [0] * bro
#     ###############################################################################

#     # temporarily storing data from a numpy array into a
#     # common array to allocate as many places as you need to avoid empty places in the DataFrame
#     # storing data from State user chose options
#     y = 0
#     if flag == 1:
#         for i in range(0,len(a)):
#             if int(a[i][0]) == flagTemp :
#                 array1[y] = a[i][0]
#                 array2[y] = a[i][1]
#                 array3[y] = a[i][2]
#                 array4[y] = a[i][3]
#                 array5[y] = a[i][4]
#                 array6[y] = a[i][5]
#                 array7[y] = a[i][6]
#                 array8[y] = a[i][7]
#                 array9[y] = a[i][8]
#                 array10[y] = a[i][9]
#                 array11[y] = a[i][10]
#                 array12[y] = a[i][11]
#                 array13[y] = a[i][12]
#                 y+=1
#     ###############################################################################


#     # reserving the number of elements in a row
#     niz_N1 = [0]*bro
#     #Initialize a new array
#     np_niz2 = np.asarray(niz_N1, dtype = 'int64')
#     np_niz3 = np.asarray(niz_N1, dtype = 'float64')

#     #set arr to stack for operations with data lik sort and convert
#     new_niz = np.stack((np_niz2,np_niz3,np_niz3,np_niz3,np_niz2,np_niz2,np_niz2,np_niz3,np_niz3,np_niz3,np_niz3,np_niz3,np_niz3),axis= -1)
#     #######################################################################################################################################

#     # relocating data from temporary arrays to numpy arrays
#     y = 0
#     for i in range(0,bro):
#         new_niz[i][0] = array1[y]
#         new_niz[i][1] = array2[y]
#         new_niz[i][2] = array3[y]
#         new_niz[i][3] = array4[y]
#         new_niz[i][4] = array5[y]
#         new_niz[i][5] = array6[y]
#         new_niz[i][6] = array7[y]
#         new_niz[i][7] = array8[y]
#         new_niz[i][8] = array9[y]
#         new_niz[i][9] = array10[y]
#         new_niz[i][10] = array11[y]
#         new_niz[i][11] = array12[y]
#         new_niz[i][12] = array13[y]
#         y+=1
#     ###############################################################################

#     # convert from stack with values to data for dataFrame
#     new_data = np.array(new_niz)
#     # set to DataFrame
#     df_new = pd.DataFrame(new_data)
#     # name of labels for head or names of collums
#     df_new.columns = ['    Year |  ', '    Expend |  ','    Income |  ', '    Balance |  ','    number of Season |  ',
#      '    sum of Arrivlas |  ','    sum of Depatrues |  ', '    avg Expend of Arrivlas |  ','    avg Income of Depatrues |  ',
#      '    avg Balance of Depatrues |  ','    avg Expend/Season |  ', '    avg Income/Season |  ','    avg Balance/Season |  ']
#     print("###################################################################################################################################################")
#     print(df_new)
#     print("###################################################################################################################################################")

#     return df_new

    