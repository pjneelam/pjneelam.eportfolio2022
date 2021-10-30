#Assignment 2
#Note: Global keywords are often used in Python to read and write a global variable inside a function. 
#connect mysql to Python (check https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)
#if you run it and nothing happens, it means the connection was successful
#can make this code more modular by making the connection with sql in another file
#import sql from the file which was created (sql_connection.py)
from sql_connection import get_sql_connection

def get_all_products(connection):
    
#for querying (from table 'product', for instance)
    cursor=connection.cursor()
    query="SELECT product.product_id, product.product_name, product.unit_id, product.product_price_unit, unit_description.unit_namel FROM assignment2.product inner join unit_description on product.unit_id=unit_description.unit_id"
    cursor.execute(query)
    

#store all in array and return it
    response=[]
#once query is executed, results are in a cursor, and you can use tuple (that is the column names)
    for (product_id, product_name,unit_id,product_price_unit,unit_namel) in cursor:
        response.append(
            {
                'product_id': product_id,
                'product_name': product_name,
                'unit_id':unit_id,
                'product_price_unit': product_price_unit,
                'unit_namel':unit_namel
                }
        )
        
#use response.append() instead of print(product_id, product_name,unit_id,product_price_unit,unit_namel), insert in ()
#a dictionary objects

    return response

# write a new function to add a new product
#parameterised query = %s
def insert_new_product (connection, product):
    cursor=connection.cursor()
    query=("insert into product"
     "(product_name, unit_id, product_price_unit)" "values (%s, %s, %s)")
    data=(product['product_name'], product['unit_id'], product['product_price_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid
     
#create a delete row function
def delete_product (connection, product_id):
    cursor=connection.cursor()
    query=("DELETE FROM product where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

#to make the code modular, create a new file, sql_connection 
if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection,8))
#this means must define the function #get_all_products; see line 5; remember to indent all lines
