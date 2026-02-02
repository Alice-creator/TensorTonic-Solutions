import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    numbers = np.array(x)
    return 1 / (1 + np.exp(-numbers))

# print(sigmoid([0, 2, -2]))