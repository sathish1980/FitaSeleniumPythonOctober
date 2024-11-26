class dictonary():

    item =["Idly","pongal","poori"]
    itemprice ={"Idly":20,"pongal":40,"poori":60,"Idly":70}

    def dictomantyimplementation(self):
        print(type(self.item))
        print(type(self.itemprice))
        print(self.itemprice)
        print(len(self.itemprice))
        # toretrieve
        print(self.itemprice["pongal"])
        print(self.itemprice.get("pongal"))
        print(self.itemprice.keys())
        print(self.itemprice.values())
        print(self.itemprice.items())
        if "pongals" in self.itemprice:
            print(self.itemprice["pongal"])
        else:
            print("item not available")
        #update
        self.itemprice["pongals"]=90
        print(self.itemprice["pongal"])

        self.itemprice.update({"pongal":100})
        print(self.itemprice["pongal"])
        print(self.itemprice)
        #remove

        self.itemprice.pop("pongal")
        self.itemprice.popitem()
        print(self.itemprice)

        #del self.itemprice
        print(self.itemprice)

        for eachval in self.itemprice.keys():
            print(eachval)
obj = dictonary()
obj.dictomantyimplementation()