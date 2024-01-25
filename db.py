import mysql.connector as sql

try:
    conn=sql.connect(host='localhost',user='intel',password='1234',database='customer')
    c=conn.cursor()
    print("db connected successful")
    c.execute('show databases')
    cc=c.fetchall()
    for x in cc:
        print(x)
except:
    print("connetion failed")




# query=conn.cursor()
# s1=query.execute('show databases')
# for x in s1:
#     print(x)