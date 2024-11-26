class StringConcept():

    name = " Fita \"Technologies\" annanagar "
    course = "python course is good course"

    def Stringimplementation(self):
        print(self.name)
        print(self.name[0])
        print(self.name[len(self.name)-1])
        print(len(self.name))
        for eachvalue in self.name:
            print(eachvalue)
        if "annanagars" in self.name:
            print("yes its available ")
        print( "annanagars" not in self.name)
        print("python" == self.course)
        print(self.name==self.course)
        print(self.name[1:6])
        print(self.name.upper())
        afterupper =self.name.upper()
        print(self.name.isupper())
        print(afterupper.isupper())
        print(self.name.lower())
        print(self.name.strip())
        print(self.name.replace(" T",""))
        print(self.name.split(" "))
        print(self.name+self.course)
        var = self.course.capitalize()
        print(var)

        print(self.course.count("course"))

obj = StringConcept()
obj.Stringimplementation()