#to create the flask page
#import flask
#flask library was installed in the command line/computer terminal first
#Source: PythonHow https://pythonhow.com/python-tutorial/flask/How-making-a-website-with-Python-works/
#Python assigns the name "__main__" to the script when the script is executed.
#The debug parameter is set to true, to trace Python errors. 
# To note: in a production environment, it must be set to False to avoid any security issues.
#returning HTML in Flask, create a homepage.html in another folder
#add render_template method



from flask import Flask, render_template
#pip install flask-mysqldb in cmd
#from flask_mysqldb import MySQL
#from mysql.connector.connection import MySQLConnection
#from sql_connection import get_sql_connection
#connection with mysql not established


app = Flask(__name__)



@app.route('/')
#to go directly to the home page, add another route
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

#add another page: market page
@app.route('/flask_server')
#this python file should have been called Market (like the webpage created!!!)
#add list / dictionaries
#Iteration will be necessary - access in html
                
def market():
    
    items = [
    {'product_id': 1, 'product_name': 'rice', 'unit_id': '2', 'product_price_unit': 1.65},
    {'product_id': 2, 'product_name': 'toothpaste', 'unit_id': '1', 'product_price_unit': 1.40},
    {'product_id': 3, 'product_name': 'soap', 'unit_id': '1', 'product_price_unit': 0.45},
    {'product_id': 4, 'product_name': 'toothbrush', 'unit_id': '1', 'product_price_unit': 1.20},
    {'product_id': 5, 'product_name': 'flour', 'unit_id': '2', 'product_price_unit': 0.90},
    {'product_id': 6, 'product_name': 'facemask', 'unit_id': '1', 'product_price_unit': 2.95}
    ]
#send some random data from Python to market.html: add key name 'items'
    return render_template('market.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
#to style your web page, can use styling framework "Bootstrap" - https://getbootstrap.com/docs/4.5/getting-started/introduction/#starter-template
#copy and page in html page created
#IP/page set up: http://127.0.0.1:5000/
#page created: http://127.0.0.1:5000/market
#to synchonise your updates in the codes and the web page, RUN the program and check if Debug mode is on in the Terminal below
#to turn it on, run code: set FLASK_DEBUG=1