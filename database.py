# SQLite database 
import sqlite3

from pandas.core.frame import DataFrame
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()


### DATABASE FUNCTIONS !!
#----------------------------------
# BATCHED 
#----------------------------------

# EFPA_BATCH

def return_id_EFPA_BATCH(id):
    c.execute('SELECT  user_id FROM EFPA_BATCH_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def return_id_EFPA_BATCH_temp(id):
    c.execute('SELECT  user_id FROM EFPA_BATCH_temp WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_EFPA_BATCH(id):
    c.execute('DELETE  FROM EFPA_BATCH_table WHERE user_id=?',(id,))
    conn.commit()

def create_EFPA_BATCH():
    c.execute('CREATE TABLE IF NOT EXISTS EFPA_BATCH_table(EFPA_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Expend_by_player REAL,Expend_INFLACION REAL,user_id TEXT,FOREIGN KEY(EFPA_BATCH_id) REFERENCES usertable(id))')

# TEMP TABLES

def create_EFPA_BATCH_temp(): 
    c.execute('CREATE TABLE IF NOT EXISTS EFPA_BATCH_temp(EFPA_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Expend_by_player REAL,Expend_INFLACION REAL,user_id TEXT,FOREIGN KEY(EFPA_BATCH_id) REFERENCES usertable(id))')

def delite_EFPA_BATCH_temp(id):
    c.execute('DELETE  FROM EFPA_BATCH_temp WHERE user_id=?',(id,))
    conn.commit()

# LEAGUE,Year_of_Season temp,NAtionality table
def create_EFPA_LEAGUE_flag_option():
    c.execute('CREATE TABLE IF NOT EXISTS EFPA_LEAGUE_flag_option(flag_option TEXT,user_id TEXT)')

def insert_EFPA_LEAGUE_flag_option(flag_option,user_id):
    c.execute('INSERT INTO EFPA_LEAGUE_flag_option(flag_option,user_id) VALUES(?,?) ',(flag_option,user_id))
    conn.commit()
#   return_id_EFPA__LEAGUE_table
def return_id_EFPA__LEAGUE_flag_option(id):
    c.execute('SELECT DISTINCT flag_option FROM EFPA_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_EFPA_LEAGUE_flag_option(id):
    c.execute('DELETE  FROM EFPA_LEAGUE_flag_option WHERE user_id=?',(id,))
    conn.commit()
#-----------------------------------------------------

#-----------------------------------------------------
#----------------------------------
# Processed 
#----------------------------------

# DCTAS
def return_id_DCTAS_table(id):
    c.execute('SELECT  user_id FROM DCTAS_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_DCTAS(id):
    c.execute('DELETE FROM DCTAS_table WHERE user_id="{}"'.format(id))
    conn.commit()

def create_DCTAS():
    c.execute('CREATE TABLE IF NOT EXISTS DCTAS_table(DCTAS_id INTEGER PRIMARY KEY,"index" INTEGER,Order_of_Expend INTEGER,Club TEXT,State TEXT,Competition TEXT,Expenditures INTEGER,Income INTEGER,Arrivals INTEGER,Departures INTEGER,Balance INTEGER,Season INTEGER,inflation_Expenditure REAL,inflation_Income REAL,inflation_Balance REAL,user_id TEXT,FOREIGN KEY(DCTAS_id) REFERENCES usertable(id))')

##################################################################################

# CDWS
def return_id_CDWS_table(id):
    c.execute('SELECT  user_id FROM CDWS_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_CDWS(id):
    c.execute('DELETE FROM CDWS_table WHERE user_id="{}"'.format(id))
    conn.commit()

def create_CDWS():
    c.execute('CREATE TABLE IF NOT EXISTS CDWS_table(CDWS_id INTEGER PRIMARY KEY,"index" INTEGER,Order_of_Expend INTEGER,Club TEXT,State TEXT,Competition TEXT,Expenditures INTEGER,Income INTEGER,Arrivals INTEGER,Departures INTEGER,Balance INTEGER,Season INTEGER,Inflacion_Income REAL,Inflacion_Expenditures REAL,inflacion_Balance REAL,user_id TEXT,FOREIGN KEY(CDWS_id) REFERENCES usertable(id))')

##################################################################################

# DCWS
def return_id_DCWS_table(id):
    c.execute('SELECT  user_id FROM DCWS_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_DCWS(id):
    c.execute('DELETE FROM DCWS_table WHERE user_id="{}"'.format(id))
    conn.commit()

def create_DCWS():
    c.execute('CREATE TABLE IF NOT EXISTS DCWS_table(DCWS_id INTEGER PRIMARY KEY,"index" INTEGER,Year_of_Season INTEGER,Expend INTEGER,Income INTEGER,Balance INTEGER,number_of_Season INTEGER,sum_of_Arrivlas INTEGER,sum_of_Depatrues INTEGER,avg_Expend_of_Arrivlas REAL,avg_Income_of_Depatrues REAL,avg_Balance_of_Depatrues REAL,avg_Expend_Season REAL,avg_Income_Season REAL,avg_Balance_Season REAL,user_id TEXT,FOREIGN KEY(DCWS_id) REFERENCES usertable(id))')

##################################################################################

# DFLS
def return_id_DFLS_table(id):
    c.execute('SELECT  user_id FROM DFLS_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_DFLS(id):
    c.execute('DELETE FROM DFLS_table WHERE user_id="{}"'.format(id))
    conn.commit()

def create_DFLS():
    c.execute('CREATE TABLE IF NOT EXISTS DFLS_table(DFLS_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Expend INTEGER,Income INTEGER,Balance INTEGER,number_of_Season INTEGER,sum_of_Arrivlas INTEGER,sum_of_Depatrues INTEGER,avg_Expend_of_Arrivlas REAL,avg_Income_of_Depatrues REAL,avg_Balance_of_Depatrues REAL,avg_Expend_Season REAL,avg_Income_Season REAL,avg_Balance_Season REAL,user_id TEXT,FOREIGN KEY(DFLS_id) REFERENCES usertable(id))')

##################################################################################

# BFPD
def return_id_BFPD_table(id):
    c.execute('SELECT  user_id FROM BFPD_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_BFPD(id):
    c.execute('DELETE FROM BFPD_table WHERE user_id="{}"'.format(id))
    conn.commit()

def create_BFPD():
    c.execute('CREATE TABLE IF NOT EXISTS BFPD_table(BFPD_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Balance_by_player REAL,Balance_INFLACION REAL,user_id TEXT,FOREIGN KEY(BFPD_id) REFERENCES usertable(id))')

##################################################################################

# BFPD
def return_id_BFPD_table(id):
    c.execute('SELECT  user_id FROM BFPD_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_BFPD(id):
    c.execute('DELETE FROM BFPD_table WHERE user_id="{}"'.format(id))
    conn.commit()

def create_BFPD():
    c.execute('CREATE TABLE IF NOT EXISTS BFPD_table(BFPD_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Balance_by_player REAL,Balance_INFLACION REAL,user_id TEXT,FOREIGN KEY(BFPD_id) REFERENCES usertable(id))')

##################################################################################

# IFPD
def return_id_IFPD_table(id):
    c.execute('SELECT  user_id FROM IFPD_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_IFPD(id):
    c.execute('DELETE FROM IFPD_table WHERE user_id="{}"'.format(id))
    conn.commit()

def create_IFPD():
    c.execute('CREATE TABLE IF NOT EXISTS IFPD_table(IFPD_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Income_by_player REAL,Income_INFLACION REAL,user_id TEXT,FOREIGN KEY(IFPD_id) REFERENCES usertable(id))')


##################################################################################
#    EFPA
def return_id_EFPA_table(id):
    c.execute('SELECT  user_id FROM EFPA_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_EFPA(id):
    c.execute('DELETE FROM EFPA_table WHERE user_id="{}"'.format(id))
    conn.commit()

def create_EFPA():
    c.execute('CREATE TABLE IF NOT EXISTS EFPA_table(EFPA_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Expend_by_player REAL,Expend_INFLACION REAL,user_id TEXT,FOREIGN KEY(EFPA_id) REFERENCES usertable(id))')

##################################################################################
#-----------------------------------------
# Processed  END OF PROCESSED FUNCTION
#-----------------------------------------
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS usertable(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT,email TEXT,postdate DATE)')

def add_user_data(username,password,email,postdate):
    c.execute('INSERT INTO usertable(username,password,email,postdate) VALUES(?,?,?,?) ',(username,password,email,postdate))
    conn.commit()

def check_double_email(email):
    c.execute('SELECT  username FROM usertable WHERE email = "{}"'.format(email))
    data = c.fetchall()
    return data

def check_double_username(username):
    c.execute('SELECT  username FROM usertable WHERE username = "{}"'.format(username))
    data = c.fetchall()
    return data

def login_user(username,password):
    c.execute('SELECT * FROM usertable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def return_user_id(username):
    c.execute('SELECT  id FROM usertable WHERE username = "{}"'.format(username))
    data = c.fetchall()
    return data

def check_userdatatable():
    c.execute('SELECT name FROM sqlite_master')
    data = c.fetchall()
    return data

#   id_user_temp INTEGER PRIMARY KEY,
#   FOREIGN KEY(id_user_temp) REFERENCES usertable(id))
# temp user
def temp_user():
     c.execute('CREATE TABLE IF NOT EXISTS temp_user(username TEXT)')

def temp_add_user_data(username):
    c.execute('INSERT INTO temp_user(username) VALUES(?) ',(username,))
    conn.commit()

def return_username():
    c.execute('SELECT  username FROM temp_user')
    data = c.fetchall()
    return data

def delite_temp_user(username):
    c.execute('DELETE  FROM temp_user WHERE username=?',(username,))
    conn.commit()