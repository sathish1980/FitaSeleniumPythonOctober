class ListConcept():

    courses =["python","Java" ,"SQL","python","testing"]

    fruits =["apple","orange","Mango"]
    def Listimplementaion(self):
        print(self.courses)
        oldcourses = self.courses.copy()
        userinput = input ("Enter the course: ")
        #self.courses.append(userinput)
        self.courses.insert(1,userinput)
        print(self.courses)
        #print(self.courses.count())
        print(self.courses.index("Java"))
        print(self.courses.remove("python"))
        print(self.courses.pop(3))
        print(self.courses)
        self.courses[0]="ReactJS"

        print(self.courses)
        #print(self.courses.reverse())
        var1 = self.courses.sort()
        print(var1)

        for eahvalue in self.courses:
            print(eahvalue)

        if "SQL" in self.courses:
            print("yes")

        print(self.courses[-1])

        self.fruits[1:3]=["grapes"]
        print(self.fruits)

        self.fruits.clear()
        print(self.fruits)
        del self.fruits
        print(self.fruits)


obj = ListConcept()
obj.Listimplementaion()