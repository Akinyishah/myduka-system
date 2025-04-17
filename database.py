import psycopg2
from datetime import datetime #creating time as at now 

#create connection to DB the only thing that will be chnaging one the below will always be the DB.
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
 for product in products:  
  print(product)

def fetch_sales():
 cur.execute('select * from sales;')
 sales=cur.fetchall()
 for sale in sales:
  print(sale)

def insert_products():
    cur.execute("insert into products(name,buying_price,selling_price,stock_quantity)values('Apple cider Vinegar',1210.50,1579.00,80)")
    conn.commit

def insert_sales():
    cur.execute(f"insert into sales(pid,quantity,created_at)values(1,110,'{time}')")# when passing variable as a string use formated string f''
    conn.commit
    
fetch_sales() 
fetching_products()  








