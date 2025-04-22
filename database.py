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

# def fetching_products():
#  cur.execute('select * from products;')
#  products=cur.fetchall()
#  for product in products:  
#   # print(product)

# def fetch_sales():
#  cur.execute('select * from sales;')
#  sales=cur.fetchall()
#  for sale in sales:
#   # print(sale)

def insert_products():
     cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('Apple cider Vinegar',1210.50,1579.00,80)")
     conn.commit
     return "product inserted"

def insert_sales():
     cur.execute(f"insert into sales(pid,quantity,created_at)values(1,110,'{time}')")# when passing variable as a string use formated string f''
     conn.commit
     return "sales made"
    
# fetch_sales() 
# fetching_products()  

#TASK REVIEW- USED FOR ANY TABLE OF MY CHOICE 
# Modify your select and insert functions to be able 
# select and insert data from any table.
# Hint: let your functions take parameters(table,data)-USE A FORMATTED STRING

def fetch_data(table):
  cur.execute(f"select * from {table} ;")
  data=cur.fetchall()
  return data

products=fetch_data('products')
sales=fetch_data('sales')
print("products from fetch data func:\n", products)
#print("sales from fetch data func:\n", sales)


#INSERT PRODUCTS -METHOD 1 TAKES VALUES AS PARAMETERS;
def insert_products(values):
  #use placeholders which acts as temporary value
  insert_products="insert into products(name,buying_price,selling_price,stock_quantity)values(%s,%s,%s,%s)"
  cur.execute(insert_products,values)
  conn.commit()

#provide the product values
product_values=('potatoes',1000,1150,50)
insert_products(product_values)
products=fetch_data('products')
print("fetch data after modification func.\n",products)

