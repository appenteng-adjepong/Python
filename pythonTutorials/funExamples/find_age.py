import datetime
from dateutil.relativedelta import relativedelta

def get_age(date_of_birth):

    current_date = datetime.date.today()
    age = relativedelta(current_date, date_of_birth)

    return age

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

birthday = datetime.date(year, month, day)

age = get_age(date_of_birth=birthday)
print(f"You are {age.years} years, {age.months} months and {age.days} days old.")