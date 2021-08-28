# SQLite database 
import sqlite3

from pandas.core.frame import DataFrame
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# POST 
def create_counter():
    c.execute('CREATE TABLE IF NOT EXISTS Conuter(Conuter_id INTEGER PRIMARY KEY,counter INTEGER,user_id TEXT,FOREIGN KEY(Conuter_id) REFERENCES usertable(id))')

def add_counter(counter,user_id):
    c.execute('INSERT INTO Conuter(counter,user_id) VALUES(?) ',(counter,user_id))
    conn.commit()

def delite_counter(user_id):
    c.execute('DELETE  FROM Conuter WHERE user_id=?',(user_id,))
    conn.commit()


def return_counter(user_id):
    c.execute('SELECT counter FROM Conuter WHERE images_id = {}'.format(user_id))
    data = c.fetchall()
    return data

# def create_images():
#     c.execute('CREATE TABLE IF NOT EXISTS Images(images_id INTEGER PRIMARY KEY,img TEXT,user_id TEXT,FOREIGN KEY(images_id) REFERENCES usertable(id))')

# def insert_image(img,user_id):
#     c.execute("INSERT INTO Images(img,user_id) VALUES(?,?)",(img,user_id))
#     conn.commit()

# def return_img(id):
# 	c.execute('SELECT * FROM Images WHERE images_id = {}'.format(id))
# 	data = c.fetchall()
# 	return data

def create_post_table_temp_MAIN():
    c.execute('CREATE TABLE IF NOT EXISTS blog_table_temp_MAIN(blog_table_id INTEGER PRIMARY KEY,"index" INTEGER,id_post TEXT,author TEXT,user_id TEXT,title TEXT,article TEXT,img TEXT,postdate TEXT,read_time REAL,FOREIGN KEY(blog_table_id) REFERENCES usertable(id))')

def return_post_id_temp_MAIN():
	c.execute('SELECT DISTINCT id_post FROM blog_table_temp_MAIN')
	data = c.fetchall()
	return data

def create_post_table():
    c.execute('CREATE TABLE IF NOT EXISTS blog_table(blog_table_id INTEGER PRIMARY KEY,"index" INTEGER,id_post TEXT,author TEXT,user_id TEXT,title TEXT,article TEXT,img TEXT,postdate TEXT,read_time REAL,FOREIGN KEY(blog_table_id) REFERENCES usertable(id))')

def delite_post_by_title(title):
    c.execute('DELETE  FROM blog_table_temp_MAIN WHERE title=?',(title,))
    conn.commit()

# def add_data_to_post(id_post,author,user_id,title,article,img,postdate):
#     c.execute('INSERT INTO blog_table(id_post,author,user_id,title,article,img,postdate) VALUES (?,?,?,?,?,?,?)',(id_post,author,user_id,title,article,img,postdate))
#     conn.commit()

# def return_id_post(id_post,user_id):
#     c.execute('SELECT DISTINCT title FROM blog_table WHERE id_post = {} AND user_id = {}'.format(id_post,user_id))
#     data = c.fetchall()
#     return data


# def view_all_post():
# 	c.execute('SELECT * FROM blog_table')
# 	data = c.fetchall()
# 	return data

# def view_all_post_my_post_title(id):
# 	c.execute('SELECT title FROM blog_table WHERE user_id = "{}"'.format(id))
# 	data = c.fetchall()
# 	return data

def delite_post(id):
    c.execute('DELETE  FROM blog_table WHERE user_id=?',(id,))
    conn.commit()

def delite_post_MAIN(id):
    c.execute('DELETE  FROM blog_table_temp_MAIN WHERE user_id=?',(id,))
    conn.commit()

#   #   #   post_id temp  querrys

def create_post_id_temp():
    c.execute('CREATE TABLE IF NOT EXISTS post_id_temp(post_id INTEGER PRIMARY KEY,post_id_temp INTEGER,user_id,FOREIGN KEY(post_id) REFERENCES usertable(id))')

def add_post_temp(post_id,user_id):
    #c.execute('INSERT INTO post_id_temp(post_id) VALUES(?) ',(post_id))
    c.execute('INSERT INTO post_id_temp(post_id_temp,user_id) VALUES(?,?) ',(post_id,user_id))
    conn.commit()

def return_post_id_temp(user_id):
	c.execute('SELECT DISTINCT post_id_temp FROM post_id_temp WHERE user_id = {}'.format(user_id))
	data = c.fetchall()
	return data

def delite_post_id_temp(user_id):
    c.execute('DELETE  FROM post_id_temp WHERE post_id=?',(user_id,))
    conn.commit()

#   #   #   post_id temp  querrys

# def delite_post_temp(author):
#     c.execute('DELETE  FROM blog_table WHERE author=?',(author,))
#     conn.commit()

# def return_post_id(user_id):
# 	c.execute('SELECT DISTINCT post_id FROM blog_table WHERE user_id = {}'.format(user_id))
# 	data = c.fetchall()
# 	return data

def return_post_id(user_id):
	c.execute('SELECT DISTINCT id_post FROM blog_table_temp_MAIN WHERE user_id = {}'.format(user_id))
	data = c.fetchall()
	return data




#------------------------------------------------------------------
### DATABASE FUNCTIONS !!
#----------------------------------
# BATCHED 
#----------------------------------

#   DCTAS
def return_id_DCTAS_BATCH(id):
    c.execute('SELECT  user_id FROM DCTAS_BATCH_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def return_id_DCTAS_BATCH_temp(id):
    c.execute('SELECT  user_id FROM DCTAS_BATCH_temp WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_DCTAS_BATCH(id):
    c.execute('DELETE  FROM DCTAS_BATCH_table WHERE user_id=?',(id,))
    conn.commit()
#   "Order_of_Expend","Club","State","Competition","Expenditures","Income","Arrivals","Departures","Balance","inflation_Expenditure","inflation_Income","inflation_Balance"
def create_DCTAS_BATCH():
    c.execute('CREATE TABLE IF NOT EXISTS DCTAS_BATCH_table(DCTAS_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Order_of_Expend INTEGER,Club TEXT,State TEXT,Competition TEXT,Expenditures INTEGER,Income INTEGER,Arrivals INTEGER,Departures INTEGER,Balance INTEGER,Season INTEGER,inflation_Expenditure REAL,inflation_Income REAL,inflation_Balance REAL,user_id TEXT,FOREIGN KEY(DCTAS_BATCH_id) REFERENCES usertable(id))')

# TEMP TABLES

def create_DCTAS_BATCH_temp(): 
    c.execute('CREATE TABLE IF NOT EXISTS DCTAS_BATCH_temp(DCTAS_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Order_of_Expend INTEGER,Club TEXT,State TEXT,Competition TEXT,Expenditures INTEGER,Income INTEGER,Arrivals INTEGER,Departures INTEGER,Balance INTEGER,Season INTEGER,inflation_Expenditure REAL,inflation_Income REAL,inflation_Balance REAL,user_id TEXT,FOREIGN KEY(DCTAS_BATCH_id) REFERENCES usertable(id))')

def delite_DCTAS_BATCH_temp(id):
    c.execute('DELETE  FROM DCTAS_BATCH_temp WHERE user_id=?',(id,))
    conn.commit()

# LEAGUE,Year_of_Season temp,NAtionality table
def create_DCTAS_LEAGUE_flag_option():
    c.execute('CREATE TABLE IF NOT EXISTS  DCTAS_LEAGUE_flag_option(flag_option TEXT,flag_record TEXT,user_id TEXT)')

def insert_DCTAS_LEAGUE_flag_option(flag_option,flag_record,user_id):
    c.execute('INSERT INTO DCTAS_LEAGUE_flag_option(flag_option,flag_record,user_id) VALUES(?,?,?) ',(flag_option,flag_record,user_id))
    conn.commit()

def view_all_DCTAS__LEAGUE_flag_record(id):
	c.execute('SELECT DISTINCT flag_record FROM DCTAS_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
	data = c.fetchall()
	return data

#   return_id_DCTAS__LEAGUE_table
def return_id_DCTAS__LEAGUE_flag_option(id):
    c.execute('SELECT DISTINCT flag_option FROM DCTAS_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_DCTAS_LEAGUE_flag_option(id):
    c.execute('DELETE  FROM DCTAS_LEAGUE_flag_option WHERE user_id=?',(id,))
    conn.commit()
#-----------------------------------------------------

#   CDWS
def return_id_CDWS_BATCH(id):
    c.execute('SELECT  user_id FROM CDWS_BATCH_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def return_id_CDWS_BATCH_temp(id):
    c.execute('SELECT  user_id FROM CDWS_BATCH_temp WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_CDWS_BATCH(id):
    c.execute('DELETE  FROM CDWS_BATCH_table WHERE user_id=?',(id,))
    conn.commit()
#   "Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"
def create_CDWS_BATCH():
    c.execute('CREATE TABLE IF NOT EXISTS CDWS_BATCH_table(CDWS_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Order_of_Expend INTEGER,Club TEXT,State TEXT,Competition TEXT,Expenditures INTEGER,Arrivals INTEGER,Income INTEGER,Departures INTEGER,Balance INTEGER,Season INTEGER,Inflacion_Income REAL,Inflacion_Expenditures REAL,Inflacion_Balance REAL,user_id TEXT,FOREIGN KEY(CDWS_BATCH_id) REFERENCES usertable(id))')

# TEMP TABLES
#   "Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"

def create_CDWS_BATCH_temp(): 
    c.execute('CREATE TABLE IF NOT EXISTS CDWS_BATCH_temp(CDWS_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Order_of_Expend INTEGER,Club TEXT,State TEXT,Competition TEXT,Expenditures INTEGER,Arrivals INTEGER,Income INTEGER,Departures INTEGER,Balance INTEGER,Season INTEGER,Inflacion_Income REAL,Inflacion_Expenditures REAL,Inflacion_Balance REAL,user_id TEXT,FOREIGN KEY(CDWS_BATCH_id) REFERENCES usertable(id))')

def delite_CDWS_BATCH_temp(id):
    c.execute('DELETE  FROM CDWS_BATCH_temp WHERE user_id=?',(id,))
    conn.commit()

# LEAGUE,Year_of_Season temp,NAtionality table
def create_CDWS_LEAGUE_flag_option():
    c.execute('CREATE TABLE IF NOT EXISTS CDWS_LEAGUE_flag_option(flag_option TEXT,flag_record TEXT,user_id TEXT)')

def insert_CDWS_LEAGUE_flag_option(flag_option,flag_record,user_id):
    c.execute('INSERT INTO CDWS_LEAGUE_flag_option(flag_option,flag_record,user_id) VALUES(?,?,?) ',(flag_option,flag_record,user_id))
    conn.commit()
#   return_id_CDWS__LEAGUE_table
def return_id_CDWS__LEAGUE_flag_option(id):
    c.execute('SELECT DISTINCT flag_option FROM CDWS_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def view_all_CDWS__LEAGUE_flag_record(id):
	c.execute('SELECT DISTINCT flag_record FROM CDWS_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
	data = c.fetchall()
	return data

def delite_CDWS_LEAGUE_flag_option(id):
    c.execute('DELETE  FROM CDWS_LEAGUE_flag_option WHERE user_id=?',(id,))
    conn.commit()
#-----------------------------------------------------


#   DCWS
def return_id_DCWS_BATCH(id):
    c.execute('SELECT  user_id FROM DCWS_BATCH_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def return_id_DCWS_BATCH_temp(id):
    c.execute('SELECT  user_id FROM DCWS_BATCH_temp WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_DCWS_BATCH(id):
    c.execute('DELETE  FROM DCWS_BATCH_table WHERE user_id=?',(id,))
    conn.commit()
def create_DCWS_BATCH():
    c.execute('CREATE TABLE IF NOT EXISTS DCWS_BATCH_table(DCWS_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Year_of_Season INTEGER,Expend INTEGER,Income INTEGER,Balance INTEGER,number_of_Season INTEGER,sum_of_Arrivlas INTEGER,sum_of_Depatrues INTEGER,avg_Expend_of_Arrivlas REAL,avg_Income_of_Depatrues REAL,avg_Balance_of_Depatrues REAL,avg_Expend_Season REAL,avg_Income_Season REAL,avg_Balance_Season REAL,user_id TEXT,FOREIGN KEY(DCWS_BATCH_id) REFERENCES usertable(id))')

# TEMP TABLES
def create_DCWS_BATCH_temp(): 
    c.execute('CREATE TABLE IF NOT EXISTS DCWS_BATCH_temp(DCWS_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Year_of_Season INTEGER,Expend INTEGER,Income INTEGER,Balance INTEGER,number_of_Season INTEGER,sum_of_Arrivlas INTEGER,sum_of_Depatrues INTEGER,avg_Expend_of_Arrivlas REAL,avg_Income_of_Depatrues REAL,avg_Balance_of_Depatrues REAL,avg_Expend_Season REAL,avg_Income_Season REAL,avg_Balance_Season REAL,user_id TEXT,FOREIGN KEY(DCWS_BATCH_id) REFERENCES usertable(id))')

def delite_DCWS_BATCH_temp(id):
    c.execute('DELETE  FROM DCWS_BATCH_temp WHERE user_id=?',(id,))
    conn.commit()

# LEAGUE,Year_of_Season temp,NAtionality table
def create_DCWS_LEAGUE_flag_option():
    c.execute('CREATE TABLE IF NOT EXISTS DCWS_LEAGUE_flag_option(flag_option TEXT,flag_record TEXT,user_id TEXT)')

def insert_DCWS_LEAGUE_flag_option(flag_option,flag_record,user_id):
    c.execute('INSERT INTO DCWS_LEAGUE_flag_option(flag_option,flag_record,user_id) VALUES(?,?,?) ',(flag_option,flag_record,user_id))
    conn.commit()

def view_all_DCWS__LEAGUE_flag_record(id):
	c.execute('SELECT DISTINCT flag_record FROM DCWS_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
	data = c.fetchall()
	return data

#   return_id_DCWS__LEAGUE_table
def return_id_DCWS__LEAGUE_flag_option(id):
    c.execute('SELECT DISTINCT flag_option FROM DCWS_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_DCWS_LEAGUE_flag_option(id):
    c.execute('DELETE  FROM DCWS_LEAGUE_flag_option WHERE user_id=?',(id,))
    conn.commit()
#-----------------------------------------------------


#   DFLS_BATCH
def return_id_DFLS_BATCH(id):
    c.execute('SELECT  user_id FROM DFLS_BATCH_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def return_id_DFLS_BATCH_temp(id):
    c.execute('SELECT  user_id FROM DFLS_BATCH_temp WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_DFLS_BATCH(id):
    c.execute('DELETE  FROM DFLS_BATCH_table WHERE user_id=?',(id,))
    conn.commit()
#   "Name_of_Legue","Expend","Income","Balance","number_of_Season","sum_of_Arrivlas","sum_of_Depatrues","avg_Expend_of_Arrivlas","avg_Income_of_Depatrues","avg_Balance_of_Depatrues","avg_Expend_Season","avg_Income_Season","avg_Balance_Season","user_id"
def create_DFLS_BATCH():
    c.execute('CREATE TABLE IF NOT EXISTS DFLS_BATCH_table(DFLS_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Expend INTEGER,Income INTEGER,Balance INTEGER,number_of_Season INTEGER,sum_of_Arrivlas INTEGER,sum_of_Depatrues INTEGER,avg_Expend_of_Arrivlas REAL,avg_Income_of_Depatrues REAL,avg_Balance_of_Depatrues REAL,avg_Expend_Season REAL,avg_Income_Season REAL,avg_Balance_Season REAL,user_id TEXT,FOREIGN KEY(DFLS_BATCH_id) REFERENCES usertable(id))')

# TEMP TABLES

def create_DFLS_BATCH_temp(): 
    c.execute('CREATE TABLE IF NOT EXISTS DFLS_BATCH_temp(DFLS_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Expend INTEGER,Income INTEGER,Balance INTEGER,number_of_Season INTEGER,sum_of_Arrivlas INTEGER,sum_of_Depatrues INTEGER,avg_Expend_of_Arrivlas REAL,avg_Income_of_Depatrues REAL,avg_Balance_of_Depatrues REAL,avg_Expend_Season REAL,avg_Income_Season REAL,avg_Balance_Season REAL,user_id TEXT,FOREIGN KEY(DFLS_BATCH_id) REFERENCES usertable(id))')

def delite_DFLS_BATCH_temp(id):
    c.execute('DELETE  FROM DFLS_BATCH_temp WHERE user_id=?',(id,))
    conn.commit()

# LEAGUE,Year_of_Season temp,NAtionality table
def create_DFLS_LEAGUE_flag_option():
    c.execute('CREATE TABLE IF NOT EXISTS DFLS_LEAGUE_flag_option(flag_option TEXT,flag_record TEXT,user_id TEXT)')

def insert_DFLS_LEAGUE_flag_option(flag_option,flag_record,user_id):
    c.execute('INSERT INTO DFLS_LEAGUE_flag_option(flag_option,flag_record,user_id) VALUES(?,?,?) ',(flag_option,flag_record,user_id))
    conn.commit()
#   return_id_DFLS__LEAGUE_table
def return_id_DFLS__LEAGUE_flag_option(id):
    c.execute('SELECT DISTINCT flag_option FROM DFLS_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def view_all_DFLS__LEAGUE_flag_record(id):
	c.execute('SELECT DISTINCT flag_record FROM DFLS_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
	data = c.fetchall()
	return data

def delite_DFLS_LEAGUE_flag_option(id):
    c.execute('DELETE  FROM DFLS_LEAGUE_flag_option WHERE user_id=?',(id,))
    conn.commit()
#-----------------------------------------------------

#   BFPD_BATCH
def return_id_BFPD_BATCH(id):
    c.execute('SELECT  user_id FROM BFPD_BATCH_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def return_id_BFPD_BATCH_temp(id):
    c.execute('SELECT  user_id FROM BFPD_BATCH_temp WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_BFPD_BATCH(id):
    c.execute('DELETE  FROM BFPD_BATCH_table WHERE user_id=?',(id,))
    conn.commit()

def create_BFPD_BATCH():
    c.execute('CREATE TABLE IF NOT EXISTS BFPD_BATCH_table(BFPD_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Balance_by_player REAL,Balance_INFLACION REAL,user_id TEXT,FOREIGN KEY(BFPD_BATCH_id) REFERENCES usertable(id))')

# TEMP TABLES

def create_BFPD_BATCH_temp(): 
    c.execute('CREATE TABLE IF NOT EXISTS BFPD_BATCH_temp(BFPD_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Balance_by_player REAL,Balance_INFLACION REAL,user_id TEXT,FOREIGN KEY(BFPD_BATCH_id) REFERENCES usertable(id))')

def delite_BFPD_BATCH_temp(id):
    c.execute('DELETE  FROM BFPD_BATCH_temp WHERE user_id=?',(id,))
    conn.commit()

# LEAGUE,Year_of_Season temp,NAtionality table
def create_BFPD_LEAGUE_flag_option():
    c.execute('CREATE TABLE IF NOT EXISTS BFPD_LEAGUE_flag_option(flag_option TEXT,flag_record TEXT,user_id TEXT)')

def insert_BFPD_LEAGUE_flag_option(flag_option,flag_record,user_id):
    c.execute('INSERT INTO BFPD_LEAGUE_flag_option(flag_option,flag_record,user_id) VALUES(?,?,?) ',(flag_option,flag_record,user_id))
    conn.commit()

def view_all_BFPD__LEAGUE_flag_record(id):
	c.execute('SELECT DISTINCT flag_record FROM BFPD_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
	data = c.fetchall()
	return data

#   return_id_BFPD__LEAGUE_table
def return_id_BFPD__LEAGUE_flag_option(id):
    c.execute('SELECT DISTINCT flag_option FROM BFPD_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_BFPD_LEAGUE_flag_option(id):
    c.execute('DELETE  FROM BFPD_LEAGUE_flag_option WHERE user_id=?',(id,))
    conn.commit()
#-----------------------------------------------------

# IFPA_BATCH

def return_id_IFPA_BATCH(id):
    c.execute('SELECT  user_id FROM IFPA_BATCH_table WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def return_id_IFPA_BATCH_temp(id):
    c.execute('SELECT  user_id FROM IFPA_BATCH_temp WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_IFPA_BATCH(id):
    c.execute('DELETE  FROM IFPA_BATCH_table WHERE user_id=?',(id,))
    conn.commit()

def create_IFPA_BATCH():
    c.execute('CREATE TABLE IF NOT EXISTS IFPA_BATCH_table(IFPA_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Income_by_player REAL,Income_INFLACION REAL,user_id TEXT,FOREIGN KEY(IFPA_BATCH_id) REFERENCES usertable(id))')

# TEMP TABLES

def create_IFPA_BATCH_temp(): 
    c.execute('CREATE TABLE IF NOT EXISTS IFPA_BATCH_temp(IFPA_BATCH_id INTEGER PRIMARY KEY,"index" INTEGER,Name_of_Legue TEXT,Year TEXT,Nationality TEXT,Income_by_player REAL,Income_INFLACION REAL,user_id TEXT,FOREIGN KEY(IFPA_BATCH_id) REFERENCES usertable(id))')

def delite_IFPA_BATCH_temp(id):
    c.execute('DELETE  FROM IFPA_BATCH_temp WHERE user_id=?',(id,))
    conn.commit()

# LEAGUE,Year_of_Season temp,NAtionality table
def create_IFPA_LEAGUE_flag_option():
    c.execute('CREATE TABLE IF NOT EXISTS IFPA_LEAGUE_flag_option(flag_option TEXT,flag_record TEXT,user_id TEXT)')

def insert_IFPA_LEAGUE_flag_option(flag_option,flag_record,user_id):
    c.execute('INSERT INTO IFPA_LEAGUE_flag_option(flag_option,flag_record,user_id) VALUES(?,?,?) ',(flag_option,flag_record,user_id))
    conn.commit()

def view_all_IFPA__LEAGUE_flag_record(id):
	c.execute('SELECT DISTINCT flag_record FROM IFPA_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
	data = c.fetchall()
	return data

#   return_id_IFPA__LEAGUE_table
def return_id_IFPA__LEAGUE_flag_option(id):
    c.execute('SELECT DISTINCT flag_option FROM IFPA_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data

def delite_IFPA_LEAGUE_flag_option(id):
    c.execute('DELETE  FROM IFPA_LEAGUE_flag_option WHERE user_id=?',(id,))
    conn.commit()
#-----------------------------------------------------
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
    c.execute('CREATE TABLE IF NOT EXISTS EFPA_LEAGUE_flag_option(flag_option TEXT,flag_record TEXT,user_id TEXT)')

def insert_EFPA_LEAGUE_flag_option(flag_option,flag_record,user_id):
    c.execute('INSERT INTO EFPA_LEAGUE_flag_option(flag_option,flag_record,user_id) VALUES(?,?,?) ',(flag_option,flag_record,user_id))
    conn.commit()
#   return_id_EFPA__LEAGUE_table
def return_id_EFPA__LEAGUE_flag_option(id):
    c.execute('SELECT DISTINCT flag_option FROM EFPA_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
    data = c.fetchall()
    return data
def view_all_EFPA__LEAGUE_flag_record(id):
	c.execute('SELECT DISTINCT flag_record FROM EFPA_LEAGUE_flag_option WHERE user_id = "{}"'.format(id))
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

#   "Order_of_Expend","Club","State","Competition","Expenditures","Arrivals","Income","Departures","Balance","Season","Inflacion_Income","Inflacion_Expenditures","Inflacion_Balance"
def create_CDWS():
    c.execute('CREATE TABLE IF NOT EXISTS CDWS_table(CDWS_id INTEGER PRIMARY KEY,"index" INTEGER,Order_of_Expend INTEGER,Club TEXT,State TEXT,Competition TEXT,Expenditures INTEGER,Arrivals INTEGER,Income INTEGER,Departures INTEGER,Balance INTEGER,Season INTEGER,Inflacion_Income REAL,Inflacion_Expenditures REAL,Inflacion_Balance REAL,user_id TEXT,FOREIGN KEY(DCTAS_id) REFERENCES usertable(id))')

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