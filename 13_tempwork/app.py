# Eccentric Pencil: Theodore Fahey, Oscar Wang, Edwin Zheng
# SoftDev
# K13: Template for Success
# 2021-10-08

from flask import Flask, render_template
import random
import csv
app = Flask(__name__) #create instance of class Flask

def openCSV(fname):
    # creates an empty dictionary and sets the temp_total and total to 0
    dict = {}
    temp_total = 0
    total = 0
    with open(fname) as f:
        # ensures that the column headers are not included in the dictionary 
        f.readline()
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            # separately saves the total of the probabilities for each occupation
            if 'Total' in row:
                total = float(row[1])
            else:
                # populates dictionary 'dict' with (key: value) pairs that represent
                #  occupations and their probabilities
                dict[row[0]] = [float(row[1]), row[2]]
                # keeps track of consecutive sum of the values
                temp_total += float(row[1])
        # if a total is not given, sets it to the sum of the value
        if total == 0:
            total = temp_total
        return dict, total

# picks an occupation based on the weighted percentages
def picker():
    jobDict, total = openCSV('data/occupations.csv')
    total = total * 10
    values = list(jobDict.values())
    occ = list(jobDict.keys())
    conDict = {}
    sum = 0
    for i in range(len(values)):
        percent = values[i][0]
        percent *= 10
        sum += percent
        values[i] = sum
    for i in range(len(occ)):
        conDict[occ[i]] = values[i]
    n = random.randint(0, total-1)
    for i in conDict:
        if (n < conDict[i]):
            return i

@app.route("/")       #assign fxn to route
def display():      #code to display the HTML on the webpage
    output = f'''
    <center><p style="font-size:100px"><a href="http://localhost:5000//occupyflaskst">GO HERE</a></p></center>
    '''
    return output

@app.route("/occupyflaskst")
def run():
    data, total = openCSV("data/occupations.csv")
    links = []
    for key in data:
        links.append([key,data[key][1]])
    picked = picker()
    randLink = ''
    for row in links:
        if row[0] == picked:
            randLink = row[1]
    return render_template("tablified.html", randOcc=picked, RL=randLink, collection=links)

app.debug = True
app.run()