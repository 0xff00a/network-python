import numpy as np

def step_function(x):
    """
    step function
    """
    y = x > 0
    return y.astype(np.int)

def sigmoid(x):
    """
    sigmoid function
    """

    return 1/(1+np.exp(-x))


