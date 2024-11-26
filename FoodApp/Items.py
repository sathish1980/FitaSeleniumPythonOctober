from FoodApp.Hotels import Hotels


class Items(Hotels):

    HotelItems=["idly","vada","pongal","poori"]
    HotelItemValus = {"idly": 15,"vada":20,"pongal":30,"poori":40}

    def GetItem(self,actualItem):
        for eachitem in self.HotelItems:
            if str(actualItem).lower() == eachitem:
                return eachitem
        return "Null"

    def GetItemPricebyDictonary(self,itemName):
        if itemName in self.HotelItemValus:
            return self.HotelItemValus[itemName]
        else:
            return 0

    def GetItemPrice(self,actualItem):
        for eachitem in self.HotelItems:
            splititemandprice = eachitem.split("-")
            itemname = splititemandprice[0]
            itemprice = splititemandprice[1]
            if actualItem == itemname:
                return itemprice
        return "0"


    def GetItemExist(self, actualItem):
        for eachitem in self.HotelItems:
            splititemandprice = eachitem.split("-")
            itemname = splititemandprice[0]
            if itemname == actualItem:
                return itemname
        return "NoItem"


