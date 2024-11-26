from Inheritance.FITABaseBranch import FITABaseBranch


class FitaAnnanagar():
    Annanagercoursesfees = ["Java-20000", "python-25000", "SQL-15000", "Testing-18000"]

    def Invoice(self,courseRequested):

        if self.GetCourse(courseRequested) :
            for eachcoursefee in self.Annanagercoursesfees:
                coursenameandfee = eachcoursefee.split("-")
                coursename=coursenameandfee[0]
                coursefees = coursenameandfee[1]
                if (courseRequested == coursename):
                    print("selected course fees is ",coursefees)
                    return
        else:
            print("The requested course is not available")

    def name(self):
        print("FITA Anna nagar")
    def FinalInvoice(self, course, coursefeesandlist):
        self.name()
        return self.GetInvoice(course,coursefeesandlist)


