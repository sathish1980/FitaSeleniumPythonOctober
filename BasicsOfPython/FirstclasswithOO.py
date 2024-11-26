class firstclass:
    print("""sath"ish"'s""")
    """print('kumar')"""

    def __init__(self,name):
        print("i am constructor", name)

    def add(self):
        result = 5+3
        print(result)

    def subtraction(self,first,second):
        result = int(second)-int(first)
        print(result)

    def totalamount(self,firstvalue,secondvalue,thirdvalue):
        total=firstvalue+secondvalue+thirdvalue
        print(total)
        return total
    def taxamount(self,amount):
        taxamount=amount*0.15
        print(taxamount)
        return taxamount+amount

    def Invoice(self,firstvalue,secondvalue,thirdvalue):
        finalamount =self.totalamount(firstvalue,secondvalue,thirdvalue)
        tax =self.taxamount(finalamount)
        print(tax)



f = firstclass("FITA")
f.add()
first1 =input("Enter first number")
second1 =input("Enter second number")
f.subtraction(first1,second1)
f.Invoice(78,65,100)

