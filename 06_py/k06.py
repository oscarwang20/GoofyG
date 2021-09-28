import csv
import random

# Random float from 0 to 99.8
# With each item in dict get consecutive sum
# If rand int < sum return item associated with key

def openCSV(fname):
    dict = {}
    with open(fname) as f:
        f.readline()
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            dict[float(row[1])] = row[0]
        return dict

def picker(a):
    a = openCSV('occupations.csv')


def main():
    print(openCSV('occupations.csv'))

if __name__ == "__main__": 
    main()
