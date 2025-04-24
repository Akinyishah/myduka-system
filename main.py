#this is where the APPLICATION IS app=Flask(__name__) MUST BE THERE 
#Import flask to use it.

from flask import Flask, render_template

#instantiate your application:-initializion of flask.
app=Flask(__name__)

#this is a route part of a URL that determines what functions to execute.route connects functions to the URL 
#mapping url to a function
#Decorator-function that wraps another function to modify its behaviour
#Functions MUST HAVE unique NAME

@app.route('/')          #func 1
def home():              #func 2   
    return render_template("index.html")

#running an application one has to tell FLASK 
app.run(debug=True)