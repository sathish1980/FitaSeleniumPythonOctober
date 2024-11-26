from Inheritance.FITABaseBranch import FITABaseBranch


class FitaTambaram(FITABaseBranch):
    Tambarmcoursesfees=["Java-10000", "python-15000", "SQL-19000", "Testing-21000"]

    def FinalInvoice(self, course, tambaramcoursefeesandlist):
        self.GetInvoice(course, tambaramcoursefeesandlist)




obj = FitaTambaram()
obj.FinalInvoice("Testing",FitaTambaram.Tambarmcoursesfees)