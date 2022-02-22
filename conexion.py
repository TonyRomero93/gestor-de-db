import mysql.connector as sql

con = sql.connect(host="localhost", user="root", passwd="", database="mibase")
cur = con.cursor()

def Connect(user_name, passord):
    conexion = False
    query = "SELECT * FROM users WHERE user_name = '" + user_name + "' and  user_pass = '" + passord +"'"
    cur.execute(str(query))
    data = cur.fetchall()

    try:
        if data[0][1] == user_name and data[0][2] == passord:
            conexion = True
    except:
        conexion = False
        
    return conexion

if __name__=='__main__':
    Connect()
