import numpy as np


def std_least_square(data_points_x, data_points_y):
    """
    Standard least squares implemetation:
    To fit a parabola we need to satisfy the equation y = ax^2 + bx + c
    """
    # For forming the X and Y array:
    X = []
    for i in data_points_x:
        X.append([i**2, i, 1])

    X = np.array(X)
    Y = np.array(data_points_y)

    # Formula for fitting standard least squares (Xt*X)B = Xt*Y 
    Xt_X_inv = np.linalg.inv(np.dot(X.T,X))
    Xt_Y = np.dot(X.T,Y)
    result = np.dot(Xt_X_inv, Xt_Y)

    # print("SLS solution \n", result)
    return result
