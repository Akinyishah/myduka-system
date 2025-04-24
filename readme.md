
from flask import Flask

#instantiate your application:-initializion of flask.
#flask instance

app=Flask(__name__)


#(__name__)-the name is a special inbuilt variable  which 
# It represents the name of the current file where the application is built e.g mine is main.py
#tells Flask where my project/application starts 

#-this is a route part of a URL that determines what functions to execute.
#def home is dependent on the app,route function function that determines behaviour of another function

@app.route('/products') -FUNC 1
def home():  -FUNC 2
    return "My home Page" 
route connects functions to the URL 

#running an application one has to tell FLASK 
app.run()