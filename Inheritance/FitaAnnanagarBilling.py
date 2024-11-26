from Inheritance.FITABaseBranch import FITABaseBranch
from Inheritance.FitaAnnanagar import FitaAnnanagar


class FitaAnnanagarBilling(FitaAnnanagar,FITABaseBranch):

    discount =0.12

    def finalBillingAmount(self,course,coursefeesandlist):
        amountbeforeDsicount = self.FinalInvoice(course, coursefeesandlist)
        if(int(amountbeforeDsicount)>20000):
            discountamount = int(amountbeforeDsicount)*self.discount
            print("you are eligible for discount ", discountamount)
            finalamount = int(amountbeforeDsicount)-float(discountamount)
            print("after discount you have to pay ", finalamount)
        else:
            print("ypu are not eligible for discount, ",amountbeforeDsicount)


obj = FitaAnnanagarBilling()
obj.finalBillingAmount("python",FitaAnnanagar.Annanagercoursesfees)



