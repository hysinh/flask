import os
from flask import Flask, render_template #importing Flask class

app = Flask(__name__)  # creates an instance of the Flask class and stores in variable called "app", the first argment of the Flask class = name of the application's module (our package) "__name__" is a built-in Python variable

@app.route("/") #use the route decorator to tell Flask what URL should trigger the function that follows
def index(): #creates a function called "index" which returns the string "hello world"
    return "Hello this is not working"

#__main__ is the name of the default module in Python
if __name__ == "__main__":  #references the built-in variable - if both are equal, we will run our app with the following arguments
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), #uses the os module from the standard library to get the IP environment variable if it exists and set a default if not found
        port=int(os.environ.get("PORT", "5000")),#same with PORT, "5000" is a common port used by Flask
        debug=False #allows us to debug our code much easier during the development stage
    )
