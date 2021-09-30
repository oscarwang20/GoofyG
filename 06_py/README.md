# Summative Assesment/Description of 06_py
## Goofy Goobers
## Julia Nelson, Oscar Wang, Owen Yaggy

### File I/O (Mostly the I)
* We handled opening the file with Python's built-in open() function, which assigns the contents of the file to a variable (f in our case) 
* To read the file, we looked up Python's csv module documentation, which provided us everything we needed to store the contents of the csv file in a dictionary

### Using Dictionaries
* We used dictionaries to store the occupations and their respective probabilities from the `.csv` file
* Dictionaries are good for correlating a number of specific keys to their corresponding values (in our case, it was the 22 unique occupations and the probabilities of selecting them). 
* Dictionaries are created like this: `dict = {key: value}`
* Dictionaries are used to recall each of the values associated with the keys. To access these values, we use `dict[key]`, which returns the value associated with the key

### Lists
* Lists are objects that store multiple values in Python
* Lists are good for when multiple values need to be stored in a particular order, and they can also be sorted using python's built in sort() function
* They are created like this: `list = [a, b, c ...]`
* Lists can then be indexed using numbers (starting with 0) that correlate with the position of each element in the list
* So, calling `list[1]` would return the value associated with `b`
* For us, we used lists to extract and modify the values (probabilities) associated with each of the keys (occupations) in our dictionary
* In the end, this allwoed us to multiply all the probabilities by 10 so that we could use `random.randint()` to select a random occupation

### Basics of Github-Flavoured Markdown
* Hashtags are used to indicate headings - using less hastags indicates a heading of lower number / higher precedent and more hashtgs indicates a further subheading
* Using a single astrisk on each side of a chunk of text is one way to italicize it, two will make it bold
* More of github-flavoured markdown can be learned by perusing the documentation that github provides or asking questions in an appropriate discussion
<<<<<<< HEAD

### Weighed Randomized Selection
* We decided that the easiest way to implement weighted randomization would be to
pick a random number within the total percentage (up to 99.8).
* To do this, we wanted to put every occupation on one number line, with each occupation occupying a
section of the number line. The size of that section corresponds to the probability of
that section being picked.
* We accomplished this by iterating through our
dictionary and modifying the values to be the sum of all the values we had previously
iterated through.
=======
>>>>>>> 1cac7e3c1c6e9393e13e8b380095ea926a7d8dad
