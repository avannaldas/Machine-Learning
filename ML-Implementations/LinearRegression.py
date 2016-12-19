'''
Linear Regression Implementation using Python, NumPy, Pandas
'''
#import pandas as pd
from random import randint
import numpy as np
import matplotlib.pyplot as plt

def hypothesis(theta, small_x):
    '''Hypothesis for a particular theta_0, theta_1 and sample point'''
    return theta * small_x

def predict(theta):
    '''Returns predictions list all entries in X with theta_0 and theta_1'''
    return [hypothesis(theta, p) for p in X]

def compute_cost(theta):
    '''Computes cost at theta_0 and theta_1'''
    one_over_2m = 0.005 # 1 / 2 * 100
    cost = 0
    for i in range(len(X)):
        cost = cost + pow((hypothesis(theta, X[i]) - Y[i]), 2)
    #print('Current cost of hypothesis at theta:%f is:%f' % (theta, cost))
    return one_over_2m * cost

def gradient_descent():
    '''
    Computes gradient_descent
    Naive, Bruteforce implementation
	TO DO: Update with proper gradient descent
    '''
    min_cost = 999999999999
    local_theta = 0
    for i in range(0, 10):
        cur_cost = compute_cost(i)
        if cur_cost < min_cost:
            min_cost = cur_cost
            local_theta = i
            print('At theta %f, cost is %f' % (local_theta, min_cost))
    return local_theta

X = [randint(820, 2500) for p in range(0, 100)]
Y = [(((randint(4000, 5000) * p) if (randint(0, 3) == 1) else (randint(4000, 6000) * p))/1000) for p in X]
P = [hypothesis(gradient_descent(), p) for p in X]

# PLOT DATA
plt.scatter(X, Y)
plt.plot(X, [hypothesis(3, p) for p in X], 'r')
plt.plot(X, [hypothesis(5.5, p) for p in X], 'b')
plt.plot(X, [hypothesis(5, p) for p in X], 'y')
plt.plot(X, P, 'g')
plt.xlabel('Area in Sq Ft')
plt.ylabel('Cost in Rupees per Sq Ft in thousands')
plt.title('Housing price trends randomly generated')
plt.show()
