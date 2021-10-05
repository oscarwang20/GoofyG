# Goofy Goobers - Oscar Wang, Owen Yaggy, Julia Nelson
# SoftDev
# K06 -- Return a random professional field based on the percentage of jobs in that field
# 2021-09-28

## OUR APPROACH ##
# We first figured out how to read a CSV file using the documentation for the csv module
# After reading the data and storing it in a dictionary, we converted that dictionary to
# one where the keys/percentages are consecutive sums of all of the percentages of the
# prior keys in the dictionary. We decided to do this because it allows us to treat the
# dictionary as one continuous scale, making it easy to randomly pick a point along that
# scale and associate it with a profession. We divided our program into functions for
# readability and ease of use. This also allowed us to test our program with a separate
# function.

# import csv to process the csv file and random to pick a random occupation
import csv
import random

# reads the .csv file and returns a dictionary with (key: value) pairs correlating to 
#  the occupation and its chance of being picked, along with the sum of these chances
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
    jobDict, total = openCSV('occupations.csv')
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

# runs n trials to determine if the probability of the resulting occupations matches 
#  those listed in the .csv file
def test_probs(n):
    testResults, total = openCSV('occupations.csv')
    for i in testResults:
        testResults[i] = 0
    for i in range(n):
        testResults[picker()] += 1
    for i in testResults:
        testResults[i] = [testResults[i], round(testResults[i] / n * 10000) / 100]
    print(testResults)


def main():
    print(picker())
    # test_probs(10000)

# calls main() as the main function
if __name__ == "__main__":
    main()
