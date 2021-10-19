# Forgotten Charger: Lewis Cass, Aryaman Goenka, Oscar Wang
# Softdev
# K15: Sessions Greetings
# 2021-10-18

from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )

una = "admin"
pwo = "admin"

@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():  # prints debug stuff in the terminal
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.headers ***")
    print(request.headers)

    #stores variables
    username = request.args["username"] # stores the username from the form in a variable
    password = request.args["password"]
    method = request.method # stores the form method in a variable
    succ = True
    reason = "Error: "

    #conditionals
    if username != una:
        succ = False
        reason += "Incorrect username"
    if password != pwo:
        succ = False
        if reason == "Error: Incorrect username":
            reason += " and incorrect password"
        else: 
            reason = f"Incorrect password for username '{username}'"

    return render_template("response.html", success=succ, reason=reason, username=una, password=pwo, method=method)  #response to a form submission

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()