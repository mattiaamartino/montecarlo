import numpy as np


# We define the function that we want to find the integral of
def f(x):
    return np.cos(x)

# Extrema of integration
a = -np.pi/2
b = np.pi

n = int(1e5)
r_nums = np.random.uniform(a, b, n)

integral_approx = 0

for i in range(n):
    integral_approx += f(r_nums[i])
    
final_approx = (b-a)/n*integral_approx
print(final_approx)