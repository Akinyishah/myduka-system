#this is where the APPLICATION IS app=Flask(__name__) MUST BE THERE 
#Import flask to use it.

from flask import Flask, render_template,request,redirect,url_for
from database import fetch_products,fetch_sales,insert_products_method_2,insert_sales_method_2,profit_per_product,sales_per_product

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
  products=fetch_products()
  return render_template("sales.html",sales=sales,products=products)                    #products=products-declare a nother variable to hold the 1st variable


@app.route('/make_sale',methods=['POST'])
def make_sale():
    product_id=request.form['pid']
    quantity=request.form['quantity']
    new_sale=[product_id,quantity]
    insert_sales_method_2(new_sale)
    return redirect(url_for('sales'))
 

@app.route('/Dashboard')
def Dashboard():
    profit_product=profit_per_product()
    sale_product=sales_per_product()
    product_name=[i [0] for i in profit_product]
    p_product=[float(i[1])for i in profit_product]
    s_product=[float(i[1]) for i in sale_product]

    return render_template("dashboard.html",product_name=product_name,p_product=p_product,s_product=s_product,)

#running an application one has to tell FLASK 
app.run(debug=True)