import mysql.connector
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345",
        database="attendencesystemusingfacerecogniztion")
if mydb==None:
    print("connect")