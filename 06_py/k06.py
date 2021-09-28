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
                total = float(row.split(',')[1])
            else: 
                dict[float(row[1])] = row[0]
        return dict, total

def picker(a):
    jobDict, total = openCSV('06_py/occupations.csv')



def main():
    print(openCSV('06_py/occupations.csv'))

if __name__ == "__main__": 
    main()
