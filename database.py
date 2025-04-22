import psycopg2
from datetime import datetime #creating time as at now 

#create connection to DB the only thing that will be changing one the below will always be the DB.
conn=psycopg2.connect(user='postgres',
                      password='Newsa2019@',
                      host='localhost',
                      port='5432',
                      database='myduka' 
                      )
#executes DB operations
#THis is a global variable 
cur = conn.cursor()                      
time=datetime.now() # creating time as at now 
#should be outside the def function./this is a global variable, local variable is a variable inside a function.
#query fetching products
#for product in products: #On loop you must always print the iteration e.g (i or product)
#for sale in sales: #for loop if you want your data to look presentable and readable.

def fetching_products():
  cur.execute('select * from products;')
  products=cur.fetchall()
  return products
#   print(product)

def fetch_sales():
 cur.execute('select * from sales;')
 sales=cur.fetchall()
 return products
# print(sale)

# fetch_sales() 
# fetching_products()  

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
#print("products from fetch data func:\n", products)
#print("sales from fetch data func:\n", sales)

# INSERTING PRODUCTS 
def insert_products():
     cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('Apple cider Vinegar',1210.50,1579.00,80)")
     conn.commit
     return "product inserted"

def insert_sales():
     cur.execute(f"insert into sales(pid,quantity,created_at)values(1,110,'{time}')")# when passing variable as a string use formated string f''
     conn.commit
     return "sales made"

#INSERT PRODUCTS -METHOD 1 TAKES VALUES AS PARAMETERS AND USES placeholders which acts as temporary value;
#NUMBER OF PLACEHOLDERS HAVE TO MATCH NUMBER OF COLUMNS
def insert_products(values):
  insert_products="insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"
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
  insert = f"insert into products(name,buying_price,selling_price,stock_quantity)values{values}"
  cur.execute(insert)
  conn.commit()

product1=("laptop",24500,32600,70) #should be outside the def function.After conn.commit remove indentation
insert_products_method_2(product1)
products=fetch_data('products')
#print("fetching prods using method2:\n",products)









