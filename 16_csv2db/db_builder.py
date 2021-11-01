# Forgotten Charger: Lewis Cass, Aryaman Goenka, Oscar Wang
# Softdev
# K16: All About Database
# 2021-10-21
# time spent: 45 minutes

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# creates the table for students.csv
# command = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);"
# c.execute(command)    # run SQL statement

# stores the contents of students.csv into the previously created table
def getstudents(file):
    '''
    uses f strings to run sqlite commands that insert the data from each
    row of the csv into the database
    '''
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader: 
            name = row['name']
            age = int(row['age'])
            id = int(row['id'])
            # print(name, age, id)
            command = f"INSERT INTO students VALUES ('{name}', {age}, {id});"
            c.execute(command)

# calls the function
# getstudents("students.csv")

# creates the table for courses.csv
command = "CREATE TABLE courses (course TEXT, mark INTEGER, id INTEGER);"
c.execute(command)

# stores the contents of courses.csv into the previously created table
def getcourses(file):
    '''
    uses f strings to run sqlite commands that insert the data from each
    row of the csv into the database
    '''
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader: 
            course = row["code"]
            mark = int(row["mark"])
            id = int(row["id"])
            try: 
                test = row["test"]
                print(test)
                command = f"INSERT INTO courses VALUES ('{course}', {mark}, {id}, {test});"
            except:
                command = f"INSERT INTO courses (course, mark, id) VALUES ('{course}', {mark}, {id});"
            # print(course, mark, id)
            c.execute(command)

# calls the function
getcourses("courses.csv")

#==========================================================

db.commit() #save changes
db.close()  #close database


