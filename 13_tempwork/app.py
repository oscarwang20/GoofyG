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
                dict[row[0]] = float(row[1])
                # keeps track of consecutive sum of the values
                temp_total += float(row[1])
        # if a total is not given, sets it to the sum of the value
        if total == 0:
            total = temp_total
        return dict, total

# picks an occupation based on the weighted percentages
def picker():
    jobDict, total = openCSV('data/occupations.csv')
    # we multiply the total by 10 for random.randint() to produce an int to 
    #  simulate randomly selecting an occupation
    total = total * 10
    # stores a list of occupations and their corresponding probabilities in 
    #  two separate lists
    nums = list(jobDict.values())
    occ = list(jobDict.keys())
    conDict = {}
    sum = 0
    # populates conDict such that each (key: value) pair represents the occupation
    #  and 10 times the sum of the probabilities preceding that occupation
    for i in range(len(nums)):
        nums[i] *= 10.0
        sum += nums[i]
        nums[i] = sum
    for i in range(len(occ)):
        conDict[occ[i]] = nums[i]

    # picks a random int from 0 inclusive to the total exclusive so that the number of
    #  integers picked equals the possibility for probabilities
    n = random.randint(0, total-1)
    # returns the occupation if its probability is within range of the consecutive sum
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
    links = [
        ["Management","https://www.themuse.com/advice/how-to-convince-a-company-youre-ready-for-a-manager-role-before-youre-a-manager"],
        ["Business and Financial operations","https://www.wikipedia.org/"],
        ["Computer and Mathematical","https://www.wikipedia.org/"],
        ["Architecture and Engineering","https://www.wikipedia.org/"],
        ["Life, Physical and Social Science","https://www.wikipedia.org/"],
        ["Community and Social Service","https://www.wikipedia.org/"],
        ["Legal","https://www.wikipedia.org/"],
        ["Education, training and library","https://www.wikipedia.org/"],
        ["Arts, design, entertainment, sports and media","https://www.wikipedia.org/"],
        ["Healthcare practioners and technical","https://www.wikipedia.org/"],
        ["Healthcare support","https://www.wikipedia.org/"],
        ["Protective service ","https://www.wikipedia.org/"],
        ["Food preparation and serving ","https://www.wikipedia.org/"],
        ["Building and grounds cleaning and maintenance","https://www.wikipedia.org/"],
        ["Personal care and service","https://www.wikipedia.org/"],
        ["Sales","https://www.wikipedia.org/"],
        ["Office and administrative support","https://www.wikipedia.org/"],
        ["Farming, fishing and forestry","https://www.wikipedia.org/"],
        ["Construction and extraction","https://www.wikipedia.org/"],
        ["Installation, maintenance and repair","https://www.wikipedia.org/"],
        ["Production","https://www.wikipedia.org/"],
        ["Transportation and material moving","https://www.wikipedia.org/"]
    ]

    picked = picker()
    randLink = ''
    for row in links:
        if row[0] == picked:
            randLink = row[1]
    return render_template("tablified.html", randOcc=picked, RL=randLink, collection=links)

app.debug = True
app.run()