import csv
import random

# Random float from 0 to 99.8
# With each item in dict get consecutive sum
# If rand int < sum return item associated with key

def openCSV(fname):
    dict = {}
    total = 0
    with open(fname) as f:
        f.readline()
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            if 'Total' in row:
                total = float(row[1])
            else: 
                dict[row[0]] = float(row[1])
        return dict, total

def picker():
    jobDict, total = openCSV('06_py/occupations.csv')
    total = total * 10
    nums = jobDict.values()
    # print(sum(nums))
    occ = jobDict.keys()
    conDict = {}
    sum = 0
    for i in range(len(nums)):
        nums[i] *= 10.0
        sum += nums[i]
        nums[i] = sum
    for i in range(len(occ)):
        conDict[occ[i]] = nums[i]
    print(jobDict)
    print(conDict)
    

    # for i in occ:





def main():
    picker()

if __name__ == "__main__": 
    main()
