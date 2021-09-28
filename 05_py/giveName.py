##
# Tomas Acuna, Aryaman Goenka, Oscar Wang
# Soft Dev
#
# K05: Better Living Through Amalgamation/Refresehing on Python/Refactoring code to generate random name from the 2 periods of softdev
#
# 2021/09/27
##

# SUMMARY OF TRIO DISCUSSION
# We decided to take the winner takes all approach and use Aryaman's code.
# We discussed how Ary's code works and talked about parameterizing the code. 
# We then went over our plans for refactoring our code to organize the names into 
# dictionaties using keys to separate the folks from period 1 and period 2. 

# DISCOVERIES
# Dictionaries are more useful than lists when working with two-dimensional data 
# (ie names from two class periods)

# QUESTIONS
# Should we parameterize our functions to take the output of other functions 
# instead of calling them inside other functions?

# COMMENTS
# None

import random

# Reads the file and returns each line as an element in a list
def read():
    lines = []
    with open('studentnames.txt') as f:
        lines = f.readlines()
    return lines

# Using the list given by read(), creates and populates a dictionary
#  calles softdev with keys corresponding to periods and values 
#  corresponding to a list of names in the respective periods
def divideClass():
    lines = read()
    softdev = { 
        "pd1": [],
        "pd2": []
    }

    # parse through the list of names, differentiating the period 1 
    # students and sorting everyone accordingly
    for i in lines:
        if "PD1" in i:
            num = i.index(" PD1")
            i = i.replace(" PD1", "", num)
            softdev["pd1"].append(i)
        else:
            softdev["pd2"].append(i)

    return softdev

# Gives the name of a random student from either period 1 or 2
def generateRandomStudent():
    softdev = divideClass()
    lenpd1 = len(softdev['pd1'])
    lenpd2 = len(softdev['pd2'])
    randompd = random.randint(1,2)

    if randompd == 1:
        randomstudent = random.randint(0, lenpd1 - 1)
        return (softdev['pd1'][randomstudent])
  
    elif randompd == 2:
        randomstudent = random.randint(0, lenpd2 - 1)
        return (softdev['pd2'][randomstudent])

def main():
    print(generateRandomStudent())
        
if __name__ == "__main__":
    main()