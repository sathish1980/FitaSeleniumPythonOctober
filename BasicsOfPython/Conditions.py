class conditions():

    def trafficsignal(self):
        color = input("Enter color: ")
        vehicle = input("Enter the type of vehicle: ")
        patient = input("Enter Y /N : (patient): ")
        if color == "green":
            print("You are good to go")
        elif( color == "red"):
            if(vehicle=="ambulance" and patient == "Y"):
                print("please give me a way i am ambulance")
            else:
                print("you have to stop")
        elif (color == "orange"):
            print("you are about to start /stop")
        else:
            print("you have entered incorrect color")

        if(name=="sathish"):
            pass

obj = conditions()
obj.trafficsignal()