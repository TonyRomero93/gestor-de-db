from winreg import QueryInfoKey
import mysql.connector as sql
import time

con = sql.connect(host="localhost", user="root", passwd="", database="mibase")
cur = con.cursor()

def Get(user, pas):
    query = "Select * FROM users where user_name = '" + user + "' and user_pass = '" + pas + "'"

    cur.execute(str(query))
    data = cur.fetchall()

    return(data)

def income(user):
    year = time.localtime().tm_year - 1
    query = f"SELECT * FROM ingresos WHERE user = '{user}' and year = {year}"
    cur.execute(str(query))
    data = cur.fetchall()
    return data

def expenses(user):
    year = time.localtime().tm_year - 1
    query = f"SELECT * FROM gastos WHERE user = '{user}' and year = {year}"
    cur.execute(str(query))
    data = cur.fetchall()
    return data
