from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
    return "Hello World"

@app.route("/Home",)
def home():
    return "You are in the home page"
@app.route("/LogOut")
def logout():
    return "Logout as a user"

@app.route("/Reset Password")
def reset():
    return "Reset your password here"

@app.route("/UpdateEvent")
def updateevent():
    return "Update Events here"

@app.route("/DeleteEvents")
def delevent():
    return "Delete Events Here"

@app.route("/RetrieveEvent")
def retrieveevent():
    return "You are in the home page"

@app.route("/ReserveEvent")
def reserveevent():
    return "You can reserve your events here"
@app.route("/View")
def view():
    return "View all events"
    
if __name__== "__main__":
    app.run()
