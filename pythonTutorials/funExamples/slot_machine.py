import random
def play_slot_machine():

    return random.randint(0, 10) 




def estimate_average_slot_payout(n_runs):

    balance = 0
    for n in range(n_runs):
        value = play_slot_machine()
        if value == 0:
            balance -= 1
        else:
            balance += value
            
    return balance/n_runs

# using a list comprehension

def average_slot_payout_estimator(n_runs):
    balance = [play_slot_machine() - 1 for n in range(n_runs)]
    return sum(balance)/n_runs

print(estimate_average_slot_payout(20), average_slot_payout_estimator(20))   

        
