import psycopg2
from datetime import datetime #creating time as at now 

#create connection to DB the only thing that will be changing one the below will always be the DB.
conn=psycopg2.connect(user='postgres',
                      password='Newsa2019@',
                      host='localhost',
                      port='5432',
                      database='myduka' 
                      )

#THis is a global variable 
cur = conn.cursor()                      
time=datetime.now() # creating time as at now 
#should be outside the def function./this is a global variable, local variable is a variable inside a function.
#query fetching products
#for product in products: #On loop you must always print the iteration e.g (i or product)
#for sale in sales: #for loop if you want your data to look presentable and readable.

def fetch_products():
    cur.execute('select * from products;')
    products=cur.fetchall()
    return products

def fetch_sales():
  cur.execute('select * from sales;')
  sales=cur.fetchall()
  return sales

def fetch_users():
   cur.execute('select * from users;')
   users=cur.fetchall()
   return users


# fetch_sales() 
# fetch_products()  
# fetct_users()

#TASK REVIEW- USED FOR ANY TABLE OF MY CHOICE 
# Modify your select and insert functions to be able 
# select and insert data from any table.
# Hint: let your functions take parameters(table,data)-USE A FORMATTED STRING cause its a variable uses F string 

def fetch_data(table):
    cur.execute(f"select * from {table} ;")
    data=cur.fetchall()
    return data

products=fetch_data('products')
sales=fetch_data('sales')
users=fetch_data('users')
#print("products from fetch data func:\n", products)
# print("sales from fetch data func:\n", sales)
# print("users from fetch data func:\n", users)



# INSERTING PRODUCTS 
def insert_products():
     cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('Apple cider Vinegar',1210.50,1579.00,80)")
     conn.commit
     return "product inserted"

def insert_sales():
     cur.execute(f"insert into sales(pid,quantity,created_at)values(1,110,'{time}')")
     conn.commit
     return "sales made"

#INSERT PRODUCTS -METHOD 1 TAKES VALUES AS PARAMETERS AND USES placeholders which acts as temporary value;
#Number of Placeholders have to Match Number of Columns
def insert_products(values):
    insert_products="insert into products(name,buying_price,selling_price,)values(%s,%s,%s,)"
    cur.execute(insert_products,values)
    conn.commit()

#provide the product values that you want to add.
product_values1=('potatoes',1000,1150,50)
product_values2=('blenders',9600,11150,30)
# insert_products(product_values1)
# insert_products(product_values2)
# products=fetch_data('products') # CALL IT AFTER INSERT SO AS TO SEE IF ITS ADDED
#print("fetch data after modification func.\n",products)

 #INSERT PRODUCTS -METHOD 2 still TAKES VALUES AS PARAMETERS BUT DOES NOT USE PLACEHOLDERS USES A FORMATED STRING
#INSTEAD WE USE PLACEHOLDERS WITH{VALUES} PARAMETER IN A FOMARTED STRING 

def insert_products_method_2(values):
    insert = f"insert into products(name,buying_price,selling_price,)values{values}"
    cur.execute(insert)
    conn.commit()

product1=("laptop",24500,32600,70) #should be outside the def function.After conn.commit remove indentation
# insert_products_method_2(product1)
# products=fetch_data('products')
# print("fetching prods using method2:\n",products)

#INSERT SALES METHOD 2
def insert_sales_method_2(values):
    insert ="insert into sales(pid,quantity,created_at)values(%s,%s,'now()')"
    cur.execute(insert,values)
    conn.commit()

#INSERT PRODUCTS METHOD 2
def insert_products_method_2(values):
    insert = f"insert into products(name,buying_price,selling_price)values{values}"
    cur.execute(insert)
    conn.commit()
#product1=("laptop",24500,32600,70) #should be outside the def function.After conn.commit remove indentation
# insert_products_method_2(product1)
# products=fetch_data('products')
# print("fetching prods using method2:\n",products)

#PROFIT PER PRODUCT:
def profit_per_product():
   cur.execute("""SELECT products.name,SUM((products.selling_price-products.buying_price)*sales.quantity) AS Totalprofit FROM products inner join sales
               ON products.id=sales.pid group by products.name;""")
   profit_per_product=cur.fetchall()
   return profit_per_product


#SALES PER PRODUCT:
def sales_per_product():
   cur.execute("""SELECT products.name,SUM(products.selling_price*sales.quantity) AS Total_Sales FROM 
               products INNER JOIN sales ON products.id = sales.pid GROUP BY (products.name);""")
   sales_per_product=cur.fetchall()
   return sales_per_product


#SALES PER DAY:
def sales_per_day():
   cur.execute("""SELECT date(sales.created_at) AS date, SUM(products.selling_price*sales.quantity)AS revenue FROM 
               sales INNER JOIN products ON products.id = sales.pid GROUP BY date  ORDER BY date ASC;""")
   sales_per_day=cur.fetchall()
   return sales_per_day


#PROFIT PER DAY:
def profit_per_day():
   cur.execute("""SELECT date(sales.created_at) AS date, SUM((products.selling_price-products.buying_price)*sales.quantity) AS Totalprofit FROM 
               products INNER JOIN sales ON products.id=sales.pid GROUP BY  date ORDER BY date ASC ;""") 
   profit_per_day=cur.fetchall()
   return profit_per_day


#POINT OF THIS IS TO RETURN 1 USER IF RETURNS INFOR IT MEANS USER ALREDAY EXISTS SO LOG IN
def check_user(email):
   query="select * from users WHERE email = %s"
   cur.execute(query,(email,)) #the comma is after email so as it can be recognized as tuple
   user=cur.fetchone()
   return user


def add_users (user_details):
   query="insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)"
   cur.execute(query,user_details)
   conn.commit()


def fetch_stock():
  cur.execute('select * from stock;')
  stock=cur.fetchall()
  return stock


def insert_stock(values):
    insert ="insert into stock(pid,stock_quantity,created_at)values(%s,%s,'now()')"
    cur.execute(insert,values)
    conn.commit()

def available_stock(pid):
    cur.execute("select coalesce(sum(stock_quantity), 0) from stock where pid =%s", (pid,))
    total_stock=cur.fetchone()[0]
    cur.execute("select coalesce (sum(sales.quantity),0) from sales where pid =%s", (pid,))
    total_sold=cur.fetchone()[0] or 0
    return total_stock-total_sold    


def product_name(pid):
    cur.execute("select name FROM products WHERE id = %s",(pid,))
    product=cur.fetchone()[0] or "Unknown Prod"
    return product

def update_prod(values):
    cur.execute("update products set name = %s,buying_price =%s, selling_price = %s where id = %s",values)
    conn.commit()


   










