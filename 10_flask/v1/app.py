# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021
# This time app.py doesn't have print(__name__) in the hello_world() function
# this probably won't print the name of the file in the terminal 

# it doesn't actually 

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

