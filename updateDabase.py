import mysql.connector
import datetime

def updateDabase1(roll):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="smalik123",
        database="attendencesystemusingfacerecogniztion"
    )

    mycursor = mydb.cursor()
    now = datetime.datetime.now()
    dt=now.strftime("%Y-%m-%d %H:%M")

    mycursor.execute("UPDATE attendencesheet SET Statuss = 'P', Datee = '"+dt+"' WHERE stid = '"+roll+"'")

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")
    mydb.close()
