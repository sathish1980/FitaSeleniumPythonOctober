class exceptionhandle():


    def add(self,a,b):
        c=a+b
        print(c)

    def div(self,a,b):
        try:
            #if(b>0):
                c=a/b
                print(c)
        except ZeroDivisionError:
            print("u have tried dividing by zero")
        except:
            print(Exception)
        finally:
            print("finally code")


obj=exceptionhandle()
obj.div(3,0)
obj.add(2,3)