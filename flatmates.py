from flat import Bill, FlatMate
from reports import PdfReport

the_amount = float(input('enter amount '))
the_period = input('enter period  ')
the_bill = Bill(the_amount, the_period)

flatmate1_name = input('enter flatmate 1 name : ').capitalize()
flatmate1_days_in_house = int(input('enter days in the house : '))
john = FlatMate(flatmate1_name, flatmate1_days_in_house)

flatmate2_name = input('enter flatmate 2 name : ').capitalize()
flatmate2_days_in_house = int(input('enter days in the house : '))
mary = FlatMate(flatmate2_name, flatmate2_days_in_house)

print(john.pays(the_bill, mary))
print(mary.pays(the_bill, john))

pdf_report = PdfReport(the_bill.period+'.pdf')
pdf_report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)
