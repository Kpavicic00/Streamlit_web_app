from collections import Counter
from operator import itemgetter
import numpy as np
import pandas as pd
import csv
import sys
from functions import *
from data_functions_clubs import*
from data_functions_league import*


# meni of options for sort for function Input_chose_of_sort
def Meni_of_options_for_sorting_CLUBS_GETDataClubs_with_seasons():
    print("\n")
    print("\t======> Sort for Clubs with year of seasons   <======")
    print("\t 1 =>  Sort data BY Order") # 0
    print("\t 2 =>  Sort data BY Club") # 1
    print("\t 3 =>  Sort data BY State") # 2
    print("\t 4 =>  Sort data BY Competition") # 3
    print("\t 5 =>  Sort data BY Expenditures") # 4
    print("\t 6 =>  Sort data BY Arrivals") # 5
    print("\t 7 =>  Sort data BY Income") # 6
    print("\t 8 =>  Sort data BY Departures") # 7
    print("\t 9 =>  Sort data BY Balance") # 8
    print("\t 10 =>  Sort data BY Season") # 9
    print("\t 11 =>  Sort data BY Inflacion + Income") # 11
    print("\t 12 =>  Sort data BY Inflacion + Expenditures") # 12
    print("\t 13 =>  Sort data BY Inflacion + Balance") # 13 ,
    print("\t======> Sort for Clubs with year of seasons   <======")
    print("\n")# function ~ 1.
###################################################################################################################################################

# meni of options for sort for function Input_chose_of_sort
def Meni_of_options_for_sorting():
    print("\t======> Sort  for Clubs throught all seasons   <======")
    print("\t 1 =>  Sort data BY Order of Expend") # 0
    print("\t 2 =>  Sort data BY Club") # 1
    print("\t 3 =>  Sort data BY State") # 2
    print("\t 4 =>  Sort data BY Competition") # 3
    print("\t 5 =>  Sort data BY Expenditures") # 4
    print("\t 6 =>  Sort data BY Income") # 5
    print("\t 7 =>  Sort data BY Arrivals") # 6
    print("\t 8 =>  Sort data BY Departures") # 7
    print("\t 9 =>  Sort data BY Balance") # 8
    print("\t 10 =>  Sort data BY inflation calculate on Expenditure") # 9
    print("\t 11 =>  Sort data BY inflation calculate on Income") # 10
    print("\t 12 =>  Sort data BY inflation calculate on Balance") # 11
    print("\t======> Sort  for Clubs throught all seasons   <======")
    print("\n")# function ~ 2.
###################################################################################################################################################

# meni for Chose_reverse_or functions
def Meni_of_Chose_reverse_or():
    print("\n")
    print("\t======> Options for sorting   <======")
    print("\t 1 =>  Sort data BY Clasic sort  ")
    print("\t 2 =>  Sort data BY Reverse sort ")
    print("\t======> Options for sorting   <======")
    print("\n")# function ~ 3.
###################################################################################################################################################

# meni for GetBYyea
def Meni_of_GetBYyear():
    print("\n")
    print("\t======> Sort  for LAUGES by year   <======")
    print("\t 1 =>  Sort data BY Year") # 0
    print("\t 2 =>  Sort data BY Expend") # 1
    print("\t 3 =>  Sort data BY Income") # 2
    print("\t 4 =>  Sort data BY Balance") # 3
    print("\t 5 =>  Sort data BY number of Season") # 4
    print("\t 6 =>  Sort data BY sum of Arrivlas") # 5
    print("\t 7 =>  Sort data BY sum of Depatrues") # 6
    print("\t 8 =>  Sort data BY avg Expend of Arrivlas") # 7
    print("\t 9 =>  Sort data BY avg Income of Depatrues ") # 8
    print("\t 10 =>  Sort data BY  avg Balance of Depatrues ") # 9
    print("\t 11 =>  Sort data BY avg Expend/Season ") # 10
    print("\t 12 =>  Sort data BY avg Income/Season") # 11
    print("\t 13 =>  Sort data BY avg Balance/Season") # 12
    print("\t======>Sort  for LAUGES by year   <======")
    print("\n") # function ~ 4.
###################################################################################################################################################

# meni for GetDataForLeauge_AVG_Seasons
def Meni_of_GetDataForLeauge_AVG_Seasons():
    print("\n")
    print("\t 1 =>  Sort data BY Name of leauge") # 1
    print("\t 2 =>  Sort data BY Expend") # 1
    print("\t 3 =>  Sort data BY Income") # 2
    print("\t 4 =>  Sort data BY Balance") # 3
    print("\t 5 =>  Sort data BY number of Season") # 4
    print("\t 6 =>  Sort data BY sum of Arrivlas") # 5
    print("\t 7 =>  Sort data BY sum of Depatrues") # 6
    print("\t 8 =>  Sort data BY avg Expend of Arrivlas") # 7
    print("\t 9 =>  Sort data BY avg Income of Depatrues ") # 8
    print("\t 10 =>  Sort data BY  avg Balance of Depatrues ") # 9
    print("\t 11 =>  Sort data BY avg Expend/Season ") # 10
    print("\t 12=>  Sort data BY avg Income/Season") # 11
    print("\t 13 =>  Sort data BY avg Balance/Season") # 12
    print("\t======>Sort  for LAUGES by year   <======")
    print("\n")# function ~ 5.
###################################################################################################################################################

# meni for GetAVGBalanceFORplayerDepartures
def Meni_of_GetAVGBalanceFORplayerDepartures():
    print("\n")
    print("\t======> Sort  for GetAVGBalanceFORplayerDepartures   <======")
    print("\t 1 =>  Sort data BY Name of League") # 0
    print("\t 2 =>  Sort data BY Year of Season") # 1
    print("\t 3 =>  Sort data BY Nationality") # 2
    print("\t 4 =>  Sort data BY Balance by player") # 3
    print("\t 5 =>  Sort data BY Balance + Inflation by player") # 4
    print("\t======>Sort  for LAUGES by year   <======")
    print("\n")# function ~ 6.
###################################################################################################################################################

# meni for GetAVGIncomeFORplayerDepartures
def Meni_of_GetAVGIncomeFORplayerDepartures():
    print("\n")
    print("\t======> Sort  for GetAVGIncomeFORplayerDepartures   <======")
    print("\t 1 =>  Sort data BY Name of League") # 0
    print("\t 2 =>  Sort data BY Year of Season") # 1
    print("\t 3 =>  Sort data BY Nationality") # 2
    print("\t 4 =>  Sort data BY Income by player") # 3
    print("\t 5 =>  Sort data BY Income + Inflation by player") # 4
    print("\t======>Sort  for LAUGES by year   <======")
    print("\n")# function ~ 7.
###################################################################################################################################################

# meni for GetAVGExpendFORplayerArrivals
def Meni_of_GetAVGExpendFORplayerArrivals():
    print("\t======> Sort  for GetAVGExpendFORplayerArrival   <======")
    print("\t 1 =>  Sort data BY Name of League") # 0
    print("\t 2 =>  Sort data BY Year of Season") # 1
    print("\t 3 =>  Sort data BY Nationality") # 2
    print("\t 4 =>  Sort data BY Expend by player") # 3
    print("\t 5 =>  Sort data BY Expend + Inflation by player") # 4
    print("\t======>Sort  for LAUGES by year   <======")
    print("\n")# function ~ 8.
###################################################################################################################################################

def Meni_for_MAIN_program():
    print("\t====================================================================================================")
    print("\t=======================================>    MENI  <=================================================")
    print("\t=  1->  Processed Data by average league EXPEND for player ARRIVALS  <->  LEAGUE datas  !!         =") # 1
    print("\t=  2->  (0) BATCH Data by average league EXPEND for player ARRIVALS  <->  LEAGUE datas  !!         =") # 2
    print("\t=  3->  Processed Data by average league INCOME for player DEPARTURES  <->  LEAGUE datas  !!       =") # 3
    print("\t=  4->  (0) BATCH Data by average league INCOME for player DEPARTURES  <->  LEAGUE datas  !!       =") # 4
    print("\t=  5->  Processed Data by average league BALANCE for player DEPARTURES  <->  LEAGUE datas  !!      =") # 5
    print("\t=  6->  (0) BATCH Data by average league BALANCE for player DEPARTURES  <->  LEAGUE datas  !!      =") # 6
    print("\t=  7->  Processed Data by average LEAGUE by AVG SESONS statistic   <->  LEAGUE datas  !!           =") # 7
    print("\t=  8->  (0) BATCH Data by average LEAGUE by AVG SESONS statistic   <->  LEAGUE datas  !!           =") # 8
    print("\t=  9->  Processed Data by average -> LEAGUE by YEAR statistic   <->  LEAGUE datas  !!              =") # 9
    print("\t=  10->  (0) BATCH Data by average -> LEAGUE by YEAR statistic   <->  LEAGUE datas  !!             =") # 10
    print("\t=  11->  Processed Data by Data CLUBS statistic without   SESONS      <0>  CLUB datas  !!          =") # 11
    print("\t=  12->  (0) BATCH Data by Data CLUBS statistic without   SESONS      <0>  CLUB datas  !!          =") # 12
    print("\t=  13->  Processed Data by Data CLUBS statistic through all   SESONS      <0>  CLUB datas  !!      =") # 13
    print("\t=  14->  (0) BATCH Data by Data CLUBS statistic through all   SESONS      <0>  CLUB datas  !!      =") # 14
    print("\t=  15->  END OF PROGRAM ====>>>>>  press 15 for EXIT <<<<<====== !!!!!                             =") # 15
    print("\t=======================================>    MENI  <=================================================")
    print("\t====================================================================================================")
    print("\n")