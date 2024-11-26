class Loops():

    def printNext10number(self):
        numbers = input("Enter the first number: ")
        next10digit = int(numbers)+10
        while(int(numbers) < next10digit):
            print(numbers)
            numbers=int(numbers)+1

    def printNext10(self):
        for eachvalue in range(1,10):
            if(eachvalue==5):
                continue
            print(eachvalue)

obj= Loops()
#obj.printNext10number()
obj.printNext10()