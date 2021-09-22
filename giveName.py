import random

#opens the specified file and returns a list of each line's element
def extract(fname):
    f = open(fname)
    s = f.read()
    s = s.split('\n')
    return s

#takes a list and prints a random element from the list
def giveName(list):
    print(list[random.randint(0,len(list))])

#main function that executes on run
def main():
    giveName(extract('Names.txt'))

if __name__ == '__main__':
    main()