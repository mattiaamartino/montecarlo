import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

np.random.seed(36)

n = int(1000) # number of plays at max
money= 10000 # initial amount of money
bet = 100 # how much the palyer bets every turn


# function to play color
def color():
    outcome = np.random.randint(0,101) 
    if outcome <= 51:
        return False
    elif outcome > 51:
        return True

# function to play a specific number
def number(num):
    outcome = np.random.randint(1,37) # we play french roulette (without 00)
    if outcome == num:
        return True
    else:
        return False


def game(n, money, bet):
    
    default_m = deepcopy(money)
    it = 1
    curr_amount_c = []
    curr_amount_n = []    
    
    # we simulate first the bet on a color, we pick one and we stick with it
    while it <= n and money >= bet:
        if color():
            money += bet
            curr_amount_c.append(money)
        else:
            money -= bet
            curr_amount_c.append(money)
            
        it += 1
        
    plt.plot([i for i in range(1, it)], curr_amount_c)
    
    it = 1
    money = default_m
    num = np.random.randint(0,37)
    while it <= n and money >= bet:
        if number(num):
            money += bet*35
            curr_amount_n.append(money)
        else:
            money -= bet
            curr_amount_n.append(money)
        
        it += 1
        
        
    plt.plot([i for i in range(1, it)], curr_amount_n)
    
    res_n = curr_amount_n[-1]
    res_c = curr_amount_c[-1]
    return res_c, res_n

# In this part there is a simulation 100 games to see if (statistically) there is
# an optimal amount of games to play to win. (Short answer: no!)


# check_n = []
# check_c = []
# for j in range(101):
#     final_n = game(1000, money, bet)[1]
#     check_n.append(final_n)
#     final_c = game(1000, money, bet)[0]
#     check_c.append(final_c)
    

# avg_n = sum(check_n)/len(check_n)
# avg_c = sum(check_c)/len(check_c)

# print(avg_c)
# print(avg_n)
