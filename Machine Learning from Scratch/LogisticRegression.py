'''
Two Variable Logistic Regression Implementation in Python
Finds the optimum parameters and plots decision boundary
'''
import math
import matplotlib.pyplot as plt
import pandas as pd

def hypothesis(theta_0, theta_1, theta_2, x1, x2):
    '''
    Hypothesis returns sigmoid(zeta), where zeta is ThetaTransposed * X
    since this is only two variable hypothesis, this is computed using the
    scalar products without using matrix multiplication
    '''
    zeta = theta_0 + (theta_1 * x1) + (theta_2 * x2)
    return sigmoid(zeta)

def sigmoid(zeta):
    '''Sigmoid hypothesis for a given zeta value, returns value between 0 and 1'''
    ret = 1 / (1 + (math.exp(-1 * zeta)))
    return ret

def compute_cost(theta_0, theta_1, theta_2, df):
    '''cost function'''
    cost = 0
    for i in range(1, len(df)):
        cur_sig = hypothesis(theta_0, theta_1, theta_2, df.iloc[i-1]['X1'], df.iloc[i-1]['X2'])
        if df.iloc[i-1]['Y'] == 1 and cur_sig != 0:
            cost = cost + math.log(cur_sig)
        elif cur_sig != 1:
            cost = cost + math.log(1 - cur_sig)
    return cost * (-1/len(df))

def derivative(cost_fn, theta_0, theta_1, theta_2, partial, df):
    '''Computes the numerical partial derivative of a function.'''
    change_in_input = 0.000001
    cost_one = cost_fn(theta_0, theta_1, theta_2, df)
    if partial == 1: # theta_0
        theta_0 = theta_0 + change_in_input
    elif partial == 2: # theta_1
        theta_1 = theta_1 + change_in_input
    elif partial == 3: # theta_2
        theta_2 = theta_2 + change_in_input
    cost_two = cost_fn(theta_0, theta_1, theta_2, df)
    change_in_output = (cost_two - cost_one)
    slope = change_in_output / change_in_input
    return slope

def gradient_descent(costfn, df):
    '''Computes gradient_descent of given cost function'''
    theta_0 = -100
    theta_1 = 1
    theta_2 = 1
    min_cost = costfn(theta_0, theta_1, theta_2, df)
    while True:
        cur_cost = costfn(theta_0, theta_1, theta_2, df)
        if cur_cost < min_cost:
            min_cost = cur_cost
        do_0 = derivative(costfn, theta_0, theta_1, theta_2, 1, df)
        do_1 = derivative(costfn, theta_0, theta_1, theta_2, 2, df)
        do_2 = derivative(costfn, theta_0, theta_1, theta_2, 3, df)
        alpha = 0.01
        theta_0 = theta_0 - (alpha * do_0)
        theta_1 = theta_1 - (alpha * do_1)
        theta_2 = theta_2 - (alpha * do_2)
        print("cost:%0.10f | theta:%0.10f, %0.10f, %0.10f" % (cur_cost, theta_0, theta_1, theta_2))
        # stopping at a reasonable cost
        if (abs(min_cost) < 0.5) and (abs(do_0) <= 0.1 and abs(do_1) <= 0.1 and abs(do_2) <= 0.1):
            return [theta_0, theta_1, theta_2]


# You can find this csv @ https://github.com/avannaldas/Machine-Learning/blob/master/Datasets/student_admit_prediction.csv
df = pd.read_csv('student_admit_prediction.csv')
print(df.head())
print(df.tail())

theta_vec = gradient_descent(compute_cost, df)
print('Final theta_vec')
print(theta_vec)

plt.scatter(df[df['Y'] == 1]['X1'], df[df['Y'] == 1]['X2'], marker='o', c='b')
plt.scatter(df[df['Y'] == 0]['X1'], df[df['Y'] == 0]['X2'], marker='x', c='r')

decision_boundary = [(((theta_vec[1] * i) + theta_vec[0])/(-1 * theta_vec[2])) for i in range(0,110)]
plt.plot(range(0, 110), decision_boundary)

plt.show()
