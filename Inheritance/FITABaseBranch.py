class FITABaseBranch:

    courses=["Java","python","SQL","Testing"]

    def name(self):
        print("BaseBranch")
    def GetCourse(self,actualCourse):
        for eachcourse in self.courses:
            if(actualCourse==eachcourse):
                return True
        return False

    def GetInvoice(self,courseRequested,coursesfees):
        if self.GetCourse(courseRequested) :
            for eachcoursefee in coursesfees:
                coursenameandfee = eachcoursefee.split("-")
                coursename=coursenameandfee[0]
                coursefees = coursenameandfee[1]
                if (courseRequested == coursename):
                    print(coursefees)
                    return coursefees
        else:
            print("The requested course is not available")
            return 0

