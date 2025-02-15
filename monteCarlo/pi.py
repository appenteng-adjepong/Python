import math
import random

n = int(input("Number of Monte Carlo Trials: "))
points_in = 0
total_points = 0

for _ in range(n):
    t = (2*random.random()-1, 2*random.random()-1)
    if math.sqrt(t[0]**2 + t[1]**2) <= 1:
        points_in += 1
    total_points += 1    

print(f"Pi is approximately {4*points_in/total_points}")