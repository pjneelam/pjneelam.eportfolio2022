#Inheritance is the principle that allows classes to derive from other classes. 
#hierarchical inheritance for payment (parent class) created
#child class 1=gift voucher and child class 2=card details

#superclass =payment
class Payment:
    def __init__(self):
        self.customerid="customerid"
        self.orderid="orderid"
        self.paymentmode="paymentmode"
    def setData(self,customerid,orderid,paymentmode):
        self.customerid=customerid
        self.orderid=orderid
        self.paymentmode=paymentmode
    def showData(self):
        print("customer id: ", self.customerid)
        print("order id: ", self.orderid)
        print("payment mode: ", self.paymentmode)

#subclass Gift_Voucer; put superclass "Payment" to show that it inherits from Payment
class Gift_Voucher(Payment): #Inheritance
    def __init__(self):
        self.voucherno="voucherno"
        self.startdate="startdate"
        self.expirydate="expirydate"
        self.vouchervalue="vouchervalue"
    def setGift_Voucher(self,customerid,orderid,paymentmode,voucherno,startdate,expirydate,vouchervalue):
        self.setData(customerid,orderid,paymentmode)
        self.voucherno=voucherno
        self.startdate=startdate
        self.expirydate=expirydate
        self.vouchervalue=vouchervalue
    def showGift_Voucher(self):
        self.showData()
        print("voucherno: ", self.voucherno)
        print("startdate: ", self.startdate)
        print("expirydate: ", self.expirydate)
        print("vouchervalue: ", self.vouchervalue)



class Card_Details(Payment): #Inheritance
    def __init__(self):
        self.cardholder="cardholder"
        self.cardnumber="cardnumber"
        self.expirydate="expirydate"
        self.cardtype="cardtype"
        self.securitycode="securitycode"
    def setCard_Details(self,customerid,orderid,paymentmode,cardholder,cardnumber,expirydate,cardtype,securitycode):
        self.setData(customerid,orderid,paymentmode)
        self.cardholder=cardholder
        self.cardnumber=cardnumber
        self.expirydate=expirydate
        self.cardtype=cardtype
        self.securitycode=securitycode
    def showCard_Details(self):
        self.showData()
        print("cardholder: ", self.cardholder)
        print("cardnumber: ", self.cardnumber)
        print("expirydate: ", self.expirydate)
        print("cardtype: ", self.cardtype)
        print("securitycode: ", self.securitycode)

def main():
    print("Gift_Voucher Object")
    g=Gift_Voucher()
    g.setGift_Voucher(1,12,"Giftvoucher",1001,"15 October 2021","2 November 2021","$20")
    g.showGift_Voucher()
    print("Card_Details Object")
    cd = Card_Details()
    cd.setCard_Details(2, 13, "Credit Card", "Anne Mathews", 92923625, "2 December 2021", "Visa", 123)
    cd.showCard_Details()

if __name__=="__main__":
    main()

#or would it have been better to have a return from the superclass
#return super.something
#to check https://www.youtube.com/watch?v=0mcP8ZpUR38