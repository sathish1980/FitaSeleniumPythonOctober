class tupleclass():

    course =("python","java","SQL","python")
    name="sathish"

    def getData(self):

        print(self.course)
        print(type(self.course))

        newcource = list(self.course)
        print(type(newcource))

        print(self.course[0])
        print(self.course[0:2])
        print(self.course[-1])
        print(self.course.count("python"))
        print(self.course.index("python"))
        print(len(self.course))
        if "SQL" in self.course:
            print("true")
        self.course
        #print(self.getMyName())

    def getMyName(self):
        print(self.name)



obj = tupleclass()
obj.getData()