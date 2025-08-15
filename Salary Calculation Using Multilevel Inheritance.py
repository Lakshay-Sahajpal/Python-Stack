#contract_Employee
#Contractor(contract_Employee)
#Payment(Contractor)
    #time sheet from contractor
    #hours * rate of employee

vendor = "Akkodis"
company = "Salesforce"
class Contract_Employee:
    
    def __init__(self, emp_id, rate, hours):
        self.emp_id = emp_id
        self.rate = rate
        self.hours = hours

class Contractor(Contract_Employee):
    
    def __init__(self, emp_id, rate, hours, markup):
        super().__init__(emp_id, rate, hours)
        self.markup = markup
    
    def bill_rate(self):
        return self.rate + self.markup * self.rate / 100

class Salary(Contractor):

    def __init__(self, emp_id, rate, hours, markup):
        super().__init__(emp_id, rate, hours, markup)
        self.cost = self.bill_rate() * self.hours
        self.sal = self.rate * self.hours
    
    def __str__(self):
        return (
            f"Employee ID: {self.emp_id}\n"
            f"Hourly Rate: ${self.rate:.2f}\n"
            f"Weekly Hours: {self.hours} hrs\n"
            f"Vendor Bill Rate: ${self.bill_rate():.2f}/hr\n"
            f"Weekly Vendor Cost: ${self.cost:.2f}\n"
            f"Employee Salary: ${self.sal:.2f}"
        )

print("Please provide following dteails:")
x = int(input("Enter your employee code: "))
y = float(input("Enter your hourley rate in $: "))
z = float(input("Enter your total weekly working hours: "))

sona = Salary(5014, 55, 40, 30)
print("------------")
print()

#printing with __str_
print(sona)

print("------------")
print()

print(f"Sona's employee ID: {sona.emp_id}; Rate {sona.rate}; Weekly hours: {sona.hours}hrs")

print("------------")
print()

print(f"{vendor}'s bill rate is {sona.bill_rate()}")
print(f"{company}'s Weekly payment to the {vendor} for {sona.emp_id} is {sona.cost}")
print(f"Sonaly weekly salary: {sona.sal}")