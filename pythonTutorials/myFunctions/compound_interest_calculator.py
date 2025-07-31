import datetime

def get_difference(date_1, date_2):
    difference_in_days = date_1 - date_2
    return difference_in_days.days


def get_profit(days, principal, rate):

    if days < 31 and rate == 0.08:
        interest = principal*(1 + rate)**(days/365)
        profit = interest - 0.02*interest
    elif days == 31 and rate == 0.08:
        profit = principal*(1 + rate)**(days/365)
    elif days > 31 and rate == 0.08:
        profit = principal*(1 + rate)**(days/365)

    elif days < 91 and rate == 0.23:
        interest = principal*(1 + rate)**(days/365)
        profit = interest - 0.02*interest
    elif days == 91 and rate == 0.23:
        profit = principal*(1 + rate)**(days/365)
    elif days > 91 and rate == 0.23:
        profit = principal*(1 + rate)**(days/365)

    elif days < 182 and rate == 0.25:
        interest = principal*(1 + rate)**(days/365)
        profit = interest - 0.02*interest
    elif days == 182 and rate == 0.25:
        profit = principal*(1 + rate)**(days/365)
    elif days > 182 and rate == 0.25:
        profit = principal*(1 + rate)**(days/365)

    elif days < 365 and rate == 0.26:
        interest = principal*(1 + rate)**(days/365)
        profit = interest - 0.02*interest
    elif days == 365 and rate == 0.26:
        profit = principal*(1 + rate)**(days/365)
    elif days > 365 and rate == 0.26:
        profit = principal*(1 + rate)**(days/365)
        
    else: 
        profit = principal*(1 + rate)**(days/365)
    return profit + principal


start_year = int(input("Start Year: "))
start_month = int(input("Start Month: "))
start_day = int(input("Start Day: "))

end_year = int(input("End Year: "))
end_month = int(input("End Month: "))
end_day = int(input("End Day: "))

date_of_deposit  = datetime.date(start_year, start_month, start_day)
date_of_withdrawal = datetime.date(end_year, end_month, end_day)
    
days = get_difference(date_of_withdrawal, date_of_deposit)
principal = int(input("Principal: GHS"))
rate = float(input("Rate: "))

amount_to_withdraw = get_profit(days, principal, rate)

print(f"""You have received a total of GHS {amount_to_withdraw:,.2f} as principal plus interest for your investment over
      the course of {days} days.""")
