#Explanation Source: https://gist.github.com/MainaKamau92/9998039c9119dca35cbcc1f198d66434

class shopping_basket (object):
        def __init__(self):
                self.total = 0
                self.items = {}
        def add_item(self,product_id,quantity,price):
                self.total += price*quantity
                self.items.update({product_id:quantity})
                return self.total,self.items
        def remove_item(self,product_id,quantity,price):
                if product_id in self.items:
                        if quantity < self.items[product_id] and quantity > 0:
                                self.items[product_id] -= quantity
                                self.total -= price*quantity
                elif quantity >= self.items[product_id]:
                        self.total -= price*self.items[product_id]
                del self.items[product_id]
                return self.items,self.total
        def checkout(self,paid):
            if paid >= self.total:
                return paid - self.total
            else:
                return "Rejected"
#to learn how to connect orders class here and order files and payments

class order(shopping_basket):

    def __init__(self):
        self.quantity = 100
        
    def remove_item(self):
        if self.quantity > 0:
            self.quantity = self.quantity - 1
        return self.quantity
        
        
Object = shopping_basket()
Object.add_item("toothbrush",2,2.00)
Object.add_item("rice",3,2.00)
print(Object.add_item("carrots",4,2.00))
#print(Object.remove_item("Carrots",2,2.00))
#print(Object.checkout(200))
#Object = Shop()
#print(Object.remove_item())