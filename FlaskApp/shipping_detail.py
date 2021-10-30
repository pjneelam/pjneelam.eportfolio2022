#create shipping_detail class
class shipping_detail:
     # define the components of the shipping class with default function
     def __init__(self):
         # defining components of shipping_detail class as variables
         self.shipping_id = "<shipping_id>"
         self.delivery_address = "<delivery_address>"
         self.shipping_price = "<shipping_price>"

     def setData(self,shipping_id,delivery_address,shipping_price):
        self.shipping_id=shipping_id
        self.delivery_address=delivery_address
        self.shipping_price=shipping_price

     def showData(self):
        print("shipping_id: ", self.shipping_id)
        print("delivery_address: ", self.delivery_address)
        print("shipping_price: ", self.shipping_price)


sd1 = ("40","4, Rose street, London", "$10")
print(sd1)
    


