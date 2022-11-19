import datetime
x = datetime.datetime.now()
print(type(x))

CurrYear = int(input("Enter current year: "))
CurrMonth = int(input("Enter current month: "))
CurrDate = int(input("Enter current date: "))

YearOfBirth = int(input("Enter year of birth: "))
MonthOfBirth = int(input("Enter month of birth: "))
DateOfBirth = int(input("Enter date of birth: "))

age_year = CurrYear-YearOfBirth
age_month = CurrMonth-MonthOfBirth
age_date = CurrDate-DateOfBirth
print(age_year,"Years",age_month,"Months",age_date,"Days")
