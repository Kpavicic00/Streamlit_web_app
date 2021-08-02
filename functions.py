# functions
from os import makedirs
import bcrypt
import re
import hashlib
import numpy as np
import pandas as pd
from collections import Counter
from operator import itemgetter
from sort_functions import*
import numpy as np
import pandas as pd
import csv
import sys

def DataFrameFunc(filePath):

    colls = ["0","Nationality","Competition","Expenditures","Arrivals","Income","Departures","Balance","Year"]
    dat = pd.read_csv(filePath,header = None , names = colls)
    return dat 

def make_password(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_password(password) == hashed_text:
		return hashed_text
	return False

# a function in python that erases repeating sequence members from the array
def remove_duplicates(l):

    return list(set(l))

# a function in python that release  memory for dataframes
def Delite_DataFrame_from_memory(DatFr):

    print("\n\t Release DataFrame memory !!!")
    del(DatFr)

#function count number of rows for specific DateFrame
def NumberOfRows(datFrame): # for data frame

    total_rows = len((datFrame))
    return  total_rows # function ~ 3.

# function  count the length of lines for the required size allocation of the string #TXT
def file_lengthy(fname):

    with open(fname) as f:
        for i ,j in enumerate (f):
            pass
        return i +1 #

#function get Coefients for specific year
def GETCoefficients(files,year):

    lenght = file_lengthy(files) # count the length of lines for the required size allocation of the string

    with open(files, "r") as f: # open the file
        data = f.readlines()

    count = 0 # counter for arrays

    #reserving the number of elements in a row
    y = [0] * lenght
    k = [0] * lenght

    for line in data:
        words = line.split()

        y[count] = words[0] # years
        k[count] = words[1] # coefficient
        count += 1

    # conversion to numpy
    np_years = np.asarray(y, dtype='int64')
    np_koef = np.asarray(k, dtype='float64')

    # the intake part put a try catch between the 2000 and 2009 intervals and to index them with the 2019 index

    np_specific_coefficient = np_koef[np_years == year]
    #print("\n\t You have chosen a year :  ",i)

    return np_specific_coefficient

# Security functions

def check_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)

# def make_password(password):
#     hashed= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)) 
#     return hashed

# def check_hashes(password,hashed):
#     if bcrypt.checkpw(password.encode('utf-8'),hashed):
#         return password
#     return None


