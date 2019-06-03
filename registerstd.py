import mysql.connector
import datetime

def updatestd(self,roll,name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345",
        database="attendencesystemusingfacerecogniztion"
    )

    mycursor = mydb.cursor()
    now = datetime.datetime.now()
    dt=now.strftime("%Y-%m-%d %H:%M")

    mycursor.execute("UPDATE attendencesheet SET Statuss = 'P', Datee = '"+dt+"' WHERE Rollno = '"+roll+"'")

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")
    mydb.close()
