import datetime

def get_difference(date_1, date_2):
    difference_in_days = date_1 - date_2
    return difference_in_days.days


def get_profit(days, principal, rate):
    profit = 0
    if days < 31 and principal < 5_000:
        interest = principal*0.08*days/365
        profit = interest - 0.02*interest
    elif days == 31 and principal < 5_000:
        profit = principal*0.08*days/365
    elif days > 31:
        print(f"Your investment has already matured {days - 31} days ago.")
        profit = principal*0.08*31/365

    else:
        principal >= 5_000

    if days < 31 and rate == 0.08:
        interest = principal*rate*days/365
        profit = interest - 0.02*interest
    elif days == 31 and rate == 0.08:
        profit = principal*rate*days/365
    elif days > 31 and rate == 0.08:
        print(f"Your investment has already matured {days - 31} days ago.")
        profit = principal*rate*31/365

    elif days < 91 and rate == 0.23:
        interest = principal*rate*days/365
        profit = interest - 0.02*interest
    elif days == 91 and rate == 0.23:
        profit = principal*rate*days/365
    elif days > 91 and rate == 0.23:
        print(f"Your investment has already matured {days - 91} days ago.")
        profit = principal*rate*91/365

    elif days < 182 and rate == 0.25:
        interest = principal*rate*days/365
        profit = interest - 0.02*interest
    elif days == 182 and rate == 0.25:
        profit = principal*rate*days/365
    elif days > 182 and rate == 0.25:
        print(f"Your investment has already matured {days - 182} days ago.")
        profit = principal*rate*182/365

    elif days < 365 and rate == 0.26:
        interest = principal*rate*days/365
        profit = interest - 0.02*interest
    elif days == 365 and rate == 0.26:
        profit = principal*rate
    elif days > 365 and rate == 0.26:
        print(f"Your investment has already matured {days - 365} days ago.")
        profit = principal*rate
        
    else: 
        print("Your request is invalid...")
        
    returns = profit + principal
    return returns

year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

date_of_deposit  = datetime.date(year, month, day)
date_of_withdrawal = datetime.date.today()
    
days = get_difference(date_of_withdrawal, date_of_deposit)
principal = int(input("Principal: GHS"))
rate = float(input("Rate: "))

amount_to_withdraw = get_profit(days, principal, rate)

print(f"You received a total of GHS {amount_to_withdraw:,.2f} as principal plus interest for your investment.")
