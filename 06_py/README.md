# GOOFY GOOBERS
## Julia Nelson, Oscar Wang, Owen Yaggy

### File I/O (Mostly the I)
* We handled opening the file with Python's built-in open() function, which assigns the contents of the file to a variable (f in our case) 
* To read the file, we looked up Python's csv module documentation, which provided us everything we needed to store the contents of the csv file in a dictionary

### Using Dictionaries
* We used dictionaries to store the occupations and their respective probabilities from the `.csv` file
* Dictionaries are good for correlating a number of specific keys to their corresponding values (in our case, it was the 22 unique occupations and the probabilities of selecting them). 
* Dictionaries are created like this: `dict = {key: value}`
* Dictionaries are used to recall each of the values associated with the keys. To access these values, we use `dict[key]`, which returns the value associated with the key

### Using Lists
* Lists are objects that store multiple values in Pyhton 
* They are created like this: `list = [a, b, c ...]`
* Lists can then be indexed using numbers (starting with 0) that correlate with the position of each element in the list
* So, calling `list[1]` would return the value associated with `b`
* For us, we used lists to extract and modify the values (probabilities) associated with each of the keys (occupations) in our dictionary
* In the end, this allwoed us to multiply all the probabilities by 10 so that we could use `random.randint()` to select a random occupation
