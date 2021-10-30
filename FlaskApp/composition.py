# create order class in the program
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#Sources: https://www.w3schools.com/python/python_classes.asp
#https://www.tutorialandexample.com/composition-in-python/
#shipping has a relationship with orders
#check https://www.youtube.com/watch?v=b4vxi3AXw54
#better use composition - inheritance means many hierarchical classes/subclasses etc...

class Orders:
     # define the components of the Orders class with default function
     #initializer (def__init__)to instantiate objects
     def __init__(self):
         # defining components of orders class as variables
         self.order_id = "order_id"
         self.customer_id = "customer_id"
         self.order_date = "order_date"
         self.shipping_date = "shipping_date"
         self.total = "total"

    #maybe should think of having a get.calculate total

     def setData(self,order_id,customer_id,order_date,shipping_date,total):
        self.order_id=order_id
        self.customer_id=customer_id
        self.order_date=order_date
        self.shipping_date=shipping_date
        self.total=total

     def showData(self):
        print("order_id: ", self.order_id)
        print("customer_id: ", self.customer_id)
        print("order_date: ", self.order_date)
        print("shipping_date: ", self.shipping_date)
        print("total: ", self.total)

#composition
#incomplete. I'm bugged
class shipping_detail:
    from shipping_detail import shipping_detail   
    def __init__(self):
        self.shipping_detail=Orders()
    def Orders(self):
        self.shipping_detail.Orders()
    def shipping_detail(self):
        print("is this composition?")




