class variable():
    global a
    a =10
    A = 20
    B=30
    a=A=B=10,20,30
    a=A=B=10
    course=["java","python","SQL"]
    def add(self):
        self.a = 10.4
        self.a = 2.4
        b = 20
        b =30
        name ="sathish"
        c = self.a+b
        print(type(name))
        print(type(self.a))
        print("the sum of ",str(self.a),"+",str(b) +" number is "+str(c))
        print(self.course)
        print(self.a>2.4)
        print("%%%%%%%%%%%%")
        for eachvalue in self.course:
            print(eachvalue in "SQL")

    def sub(self):
        a=30
        b=50
        c=b-self.a
        print(c)
        print(self.course)

    def mul(self):
        a=10
        a+=3


obj = variable()
obj.add()
obj.sub()