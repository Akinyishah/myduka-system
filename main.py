#this is where the APPLICATION IS app=Flask(__name__) MUST BE THERE 
#Import flask to use it.
from flask import Flask

#instantiate your application:-initializion of flask
#flask instance

app=Flask(__name__)



#(__name__)--#the name is now a special inbuilt variable  which 
# It represents the name of the current file where the application is built e.g mine is main.py
#tells Flask where my project/application starts 

@app.route('/products')
def home(): #def home is dependent on the app,route function
    return "My home Page" 


#running an application one has to tell FLASK 
app.run()