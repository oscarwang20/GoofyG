# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021
# this version has the if __name__ == "__main__" conditional which runs the code if the file is not imported

# what does it mean for a file to be imported?

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
