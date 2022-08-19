import json
from ast import If
from crypt import methods
from flask import Flask , render_template , request , redirect ,flash

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

state_login_status = 0

@app.route("/state" , methods=['GET' , 'POST'])
def state():
    global state_login_status
    if state_login_status == 0:
        if request.method=='POST':
            if request.form['username'] == "state" and request.form['password'] == "state":
                state_login_status = 1
                return redirect("/state")
            else:
                flash('You were successfully logged in')
        else:
            return render_template("state/login.html")
    else:
        return render_template("state/index.html")

@app.route("/login_state" , methods=['GET' , 'POST'])
def login_state():
    if state_login_status == 0:
        return render_template("state/login.html")
    else:
        return render_template("state/index.html")


@app.route("/test" , methods=['GET' , 'POST'])
def test():

    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    if request.method=='POST':
            if request.form['username'] == "state" and request.form['password'] == "state":
                return("true")
            else:
                return("false")
                

    # convert into JSON:
    # y = json.dumps(x)

    # # the result is a JSON string:
    # # print(y)

    # # return("hello World")
    # return(y)



if __name__ == "__main__" :
    app.run(debug= True)