class setConcepts():

    fruits = {"apple","grapes","mango","apple"}
    newfruits = ["pears","dragon","lichie"]


    course1 = {"python","java","c","testing"}
    course2 = {"java","selenium","react","python","c"}
    def getFruits(self):

        print(self.fruits)
        print(type(self.fruits))
        print(len(self.fruits))

        if "grapes" in self.fruits:
            print("yes")
        self.fruits.add("watermelon")
        print(self.fruits)
        self.fruits.update(self.newfruits)
        print(self.fruits)

        self.fruits.remove("lichie")
        print(self.fruits)

        self.fruits.discard("pears")
        print(self.fruits)

        print(self.course1.difference(self.course2))

        print(self.course1)
        #self.course1.difference_update(self.course2)
        #print(self.course1)
        print(self.course1.intersection(self.course2))
        print(self.course1)
        #self.course1.intersection_update(self.course2)
        print(self.course1)
        print(self.course1.issubset(self.course2))
        print(self.course1.issuperset(self.course2))

        print(self.course1.symmetric_difference(self.course2))


obj = setConcepts()
obj.getFruits()