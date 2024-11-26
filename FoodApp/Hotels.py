class Hotels():

    hotelName=["SVB","A2B","GB","SGP"]

    def GetHotelExist(self,actualHotel):
        for eachhotel in self.hotelName:
            if eachhotel == actualHotel:
                return eachhotel
        return "Null"