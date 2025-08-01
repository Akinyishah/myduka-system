from flask import Flask, render_template,request,redirect,url_for,flash,session
from database import fetch_products,fetch_sales,insert_products_method_2,insert_sales_method_2,profit_per_product,sales_per_product,sales_per_day,profit_per_day,check_user,add_users,fetch_stock,insert_stock,available_stock,edit_product
from flask_bcrypt import Bcrypt
from functools import wraps

#instantiate your application:-initializion of flask.
app=Flask(__name__)

# must be there in order for flash messages to work and it should be below flask where it is now/used in cookies
app.secret_key="asjk@!ky3456!" 

#initializion of bcrypt.
bcrypt=Bcrypt(app) #used in this application


@app.route('/')    
def home():            
    user={"name":"Akinyi","location":"Nairobi","area":"Luanda"}    
    num=[1,2,3,4,5]   
    return render_template("index.html",data=user,num=num)

#defines a decorator function which protects the pages so that just not anyone can log in
#checks whether a session exists or not 
# this function can only come after home because it cant come below the pages you wana protect.

def login_required(f):                               
    @wraps(f)                                          
    def protected(*args,**kwargs):                    
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)                          
    return protected                                      


@app.route('/products')
@login_required
def products():
    fruits=["apple","oranges","tangerines","cauliflower","grapes"]
    products=fetch_products()                                           
    return render_template("products.html",fruits=fruits,products=products)

@app.route('/add_products',methods=["GET","POST"])
def add_products():
    product_name=request.form["p-name"]
    buying_price=request.form["b-price"]
    selling_price=request.form["s-price"]
    new_product=(product_name, buying_price,selling_price,)
    insert_products_method_2(new_product)
    return redirect(url_for('products'))

@app.route('/update_product',methods=['GET','POST'])
def update_product():
    if request.method=='POST':
        pid=request.form['pid']
        name=request.form['name']
        buying_price=request.form["buying_price"]
        selling_price=request.form["selling_price"]        
        edited_product=(name,buying_price,selling_price,pid)
        edit_product(edited_product)
        flash("product edited successfully","success")
        return redirect(url_for('products'))

@app.route('/sales')
@login_required
def sales():
  sales=fetch_sales()
  products=fetch_products()
  return render_template("sales.html",sales=sales,products=products)

@app.route('/stock')
def stock():
    #GET STOCKS using products 
    products=fetch_products()
    stock=fetch_stock()
    return render_template('stock.html',products=products,stock=stock)

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method=='POST':
        pid=request.form['pid']
        quantity=request.form['quantity']
        new_stock=(pid,quantity)
        insert_stock(new_stock)
        flash('stock added successfully','success')
        return redirect(url_for('stock'))
   
   
@app.route('/make_sale',methods=['POST'])
def make_sale():
    product_id=request.form['pid']
    quantity=request.form['quantity']
    new_sale=[product_id,quantity]
    stock_available=available_stock(product_id)
    if stock_available is None:
        flash("invalid product ID or no stock information","danger")
        return redirect(url_for('sales'))
    
    if stock_available <float(quantity):
        flash("insufficient stock","info")
        return redirect(url_for('sales'))
    insert_sales_method_2(new_sale)
    flash("sale made","success")
    return redirect(url_for('sales'))
 

@app.route('/dashboard')
@login_required
def dashboard():
    profit_product=profit_per_product()
    sale_product=sales_per_product()
    sale_day=sales_per_day()
    profit_day=profit_per_day()

#LIST COMPREHENSION TO GET INDIVIDUAL DATA POINTS

    product_name=[i [0] for i in profit_product]
    p_product=[float(i[1])for i in profit_product]
    s_product=[float(i[1]) for i in sale_product]


    date=[str(i [0]) for i in sale_day]
    p_day=[float(i [1])for i in profit_day]
    s_day=[float(i [1])for i in sale_day]


    return render_template("dashboard.html",
                           product_name=product_name,p_product=p_product,s_product=s_product,
                           date=date,s_day=s_day,p_day=p_day)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phone_number=request.form['phone']
        password=request.form['pass']
        hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
        user=check_user(email)
        
        if not user:
            new_user=(name,email,phone_number,hashed_password)
            add_users(new_user)
            return redirect(url_for('login')) #passing name of the function
        else:
            print('already registered')
    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['pass']

        user=check_user(email)
        if not user:
            flash("User not found,Please Register","danger") #use of flash message if user is not found MESSAGE CATEGORY
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(user[-1],password):#confirming password but start with hashed password then password input
                flash("logged in","success")
                session['email']=email                                  #storing data sessions in cookies
                return redirect(url_for('dashboard'))
            else:
                flash("incorrect password","danger")
    return render_template('login.html')

@app.route('/Contact Us')
def contact_Us():
    return render_template('contact_us.html')


@app.route('/logout')
@login_required
def logout():
    session.pop('email',None)
    flash('You have logged out','info')
    return redirect(url_for('login'))



#running an application one has to tell FLASK 
app.run(debug=True)

