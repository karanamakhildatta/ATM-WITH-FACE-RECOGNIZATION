import sqlite3
import pandas as pd
k = pd.read_csv('Data.csv')
# print(k)
name = list(k['Name'])
MobileNo = list(k['Mobile No'])
Adhar_Number = list(k['Aadhar Number'])
Balance = list(k['Balance'])
PIN = list(k['PIN'])
path = list(k['Path'])
db = sqlite3.connect("main.db")

cursor = db.cursor()
# cursor.execute("create table Users(s_no integer primary key AUTOINCREMENT,name varchar,mobile varchar,aadhaar varchar, balance varchar,pin varchar,path varchar)")
# db.commit()

# for i in range(len(name)):
#     p = (name[i],MobileNo[i],Adhar_Number[i],Balance[i],PIN[i],path[i])
#     cursor.execute(f"insert into Users (name,mobile,aadhaar,balance,pin,path) values {p}")
#     db.commit()
db.commit()
db.close()

