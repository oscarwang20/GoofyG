# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021
# this is different from v1 in that it shows when it is about to print the name of the file before it does
# this will probably appear in the terminal right before the line where it prints the name

# it actually doesn't

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

