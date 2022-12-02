import numpy as np
import matplotlib.pyplot as plt
'''
Given a rv X, the program estimates the slope beta of a linear transformation of X
Y = alpha + betaX + e, where e is the error term
'''

np.random.seed(1)

mu, sigma = 0, 1 # Variables of a normal distribution


n = int(1e5)

alpha = [2]*n
beta = 1

def mc_estimation(n):
    
    
    for i in range(n):
        
        e = 0.05 * np.random.normal(mu, sigma, n) # error terms are randomly distributed
        
        X = np.random.normal(mu, sigma, n)
        
        Y = alpha + beta * X + e

           