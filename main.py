#this is where the APPLICATION IS app=Flask(__name__) MUST BE THERE 
#Import flask to use it.

from flask import Flask, render_template,request,redirect,url_for
from database import fetch_products,fetch_sales,insert_products_method_2

#instantiate your application:-initializion of flask.
app=Flask(__name__)

#this is a route part of a URL that determines what functions to execute.route connects functions to the URL 
#mapping url to a function
#Decorator-function that wraps another function to modify its behaviour
#Functions MUST HAVE unique NAME

@app.route('/')          #func 1
def home():               #func 2  
    user={"name":"Akinyi","location":"Nairobi","area":"Luanda"}    
    num=[1,2,3,4,5]   
    return render_template("index.html",data=user,num=num)#declaring variable for variable e.g data=name

@app.route('/products')
def products():
    fruits=["apple","oranges","tangerines","cauliflower","grapes"]
    products=fetch_products()                                                                # calling the function so that it can store the function from the database.
    return render_template("products.html",fruits=fruits,products=products)                    #products=products-declare a nother variable to hold the 1st variable

@app.route('/add_products',methods=["GET","POST"])
def add_products():
    product_name=request.form["p-name"]
    buying_price=request.form["b-price"]
    selling_price=request.form["s-price"]
    stock_quantity=request.form["stock"]
    new_product=(product_name, buying_price,selling_price, stock_quantity)
    insert_products_method_2(new_product)
    return redirect(url_for('products'))

@app.route('/sales')
def sales():
  sales=fetch_sales()
  return render_template("sales.html",sales=sales)

@app.route('/Dashboard')
def Dashboard():
    return render_template("dashboard.html")

#running an application one has to tell FLASK 
app.run(debug=True)