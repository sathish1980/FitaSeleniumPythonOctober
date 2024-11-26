from FoodApp.Hotels import Hotels
from FoodApp.Items import Items


class swiggy(Items):

    def GetOrder(self):
        hotelname = input("enter Hotel name")
        if hotelname == self.GetHotelExist(hotelname):
            itemName = input("Enter item Name")
            if itemName.lower() == self.GetItem(itemName):
                print(itemName, " is available now and its cost as ",self.GetItemPricebyDictonary(itemName.lower()))
            else:
                print(itemName, " is not available ,Please try some time later")
        else:
            print(hotelname," is not avaialble now ")

obj = swiggy()
obj.GetOrder()