# SQLite database 
import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()


### DATABASE FUNCTIONS !!
### DATABASE FUNCTIONS !!

# DFLS
def return_id_DFLS_table(id):
    c.execute('SELECT  user_id FROM DFLS_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_DFLS(id):
    c.execute('DELETE FROM DFLS_table WHERE user_id="{}"'.format(id))
    conn.commit()
#   "Name_of_Legue","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season"
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


