

# Input the necessary figures

n =int(input('Profit before tax:  '))
de =int(input('Disallowable Expenses for the period: '))
a =int(input('Allowable Expenses for the period: '))
capital_allowance = int(input("Capital_allowance for the period: "))

# Where n = Net_profit, de = Disallowed expenses, a = Allowable expenses

class Company_tax():
    def __init__(self, n,de,a,capital_allowance,tax_rate =0.3):
        self.n = n
        self.de = de
        self.a = a
        self.tax_rate =tax_rate
        self.capital_allowance = capital_allowance

   
    def calculate_adjusted(self):
        adjusted = self.n + self.de - self.a
        return adjusted

   
    def calculate_assessible(self):
        adjusted_profit = tax.calculate_adjusted()
        assessible =  adjusted_profit - self.capital_allowance
        return assessible


    def calculate_education_tax(self):
        assessible_profit = tax.calculate_assessible()
        edu_tax = assessible_profit * 0.02
        return edu_tax

   
    def  calculate_income_tax(self):
        assessible_profit = tax.calculate_assessible()
        income_tax = assessible_profit * self.tax_rate
        return income_tax



# Results

tax = Company_tax(n, de, a,capital_allowance)

print("Net_profit before tax: {}".format(tax.n))

print("Disallowed expenses: {}".format(tax.de))

print("Tax rate is 30%")

answer = tax.calculate_adjusted()
answer_2 = tax.calculate_assessible()
answer_3 = tax.calculate_education_tax()
answer_4 = tax.calculate_income_tax()


print("Adjusted Profit is {}".format(answer))
print("Assesible Profit is {}".format(answer_2))
print("Education Tax is {}".format(answer_3))
print("Company income is {}".format(answer_4))
