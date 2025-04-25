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
def home():               #func 2  
    user={"name":"Akinyi","location":"Nairobi"}    
    num=[1,2,3,4,5]   
    return render_template("index.html",data=user,num=num)#declaring variable for variable e.g data=name

# TASK.
# Create 2 files products.html and sales.html 
# render them using flask render_template

@app.route('/products')
def products():
    return render_template("products.html")


@app.route('/sales')
def sales():
    return render_template("sales.html")

#running an application one has to tell FLASK 
app.run(debug=True)