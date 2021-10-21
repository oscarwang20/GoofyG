#Clyde "Thluffy" Sinclair
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Dec 2020 -- The Time of the Rona

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

command = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

def getstudents(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader: 
            name = row['name']
            age = int(row['age'])
            id = int(row['id'])
            # print(name, age, id)
            command = f"INSERT INTO students VALUES ('{name}', {age}, {id});"
            c.execute(command)

getstudents("students.csv")

command = "CREATE TABLE courses (course TEXT, mark INTEGER, id INTEGER);"
c.execute(command)

def getcourses(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader: 
            course = row["code"]
            mark = int(row["mark"])
            id = int(row["id"])
            # print(course, mark, id)
            command = f"INSERT INTO courses VALUES ('{course}', {mark}, {id});"
            c.execute(command)

getcourses("courses.csv")

#==========================================================

db.commit() #save changes
db.close()  #close database


