# Pearson Correlation Coefficient: https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

import math

# Reading input from stdout for x and y
print("Enter values for X:")
x = [int(x) for x in input().split()]
print("Enter values for Y:")
y = [int(x) for x in input().split()]

if((len(x) != len(y)) or (len(x) < 2)):
  raise ValueError("Please enter atleast two values for X and Y, enter same number of values for both")

# Computing and printing mean values for x and y
x_bar = sum(x)/len(x)
y_bar = sum(y)/len(y)
print('x_bar: %f' % x_bar)
print('y_bar: %f' % y_bar)

# Covariance of x and y
num = sum(((x[i] - x_bar) * (y[i] - y_bar)) for i in range(0, len(x)))
print('num: %f' % num)

# Denominator part Standard Deviation of x
sd_x = sum(((x[i] - x_bar) * (x[i] - x_bar)) for i in range(0, len(x)))
print('den_x: %f' % sd_x)

# Denominator part Standard Deviation of y
sd_y = sum(((y[i] - y_bar) * (y[i] - y_bar)) for i in range(0, len(y)))
print('den_y: %f' % sd_y)

# Denominator product of x sd and y sd
den = math.sqrt(sd_x) * math.sqrt(sd_y)
print('den: %f' % den)

r = num / den
print('Answer: %0.3f' % r) # Printing answer upto 3 decimal places
