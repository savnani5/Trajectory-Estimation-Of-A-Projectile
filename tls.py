import numpy as np
from svd import svd

def total_least_square(data_points_x, data_points_y):
    """
    Total least squares implemetation
    As we are taking the data to be normalized here to fit a parabola we need to satisfy the equation ax^2 + bx = cy  (The constant d is dropped here, assuming the data is passes through the origin.)
    """
    # For forming the X and Y array:
    X = []
    for i in data_points_x:
        X.append([i**2 , i])

    X = np.array(X)
    y = np.array(data_points_y)

    if X.ndim is 1: 
        n = 1 # the number of variable of X
        X = X.reshape(len(X),1)
    else:
        n = np.array(X).shape[1] 

    Z = np.vstack((X.T,y)).T
    U, s, Vt = svd(Z)

    V = Vt.T
    Vxy = V[:n,n:] # Extracting the first 2 coefficients
    Vyy = V[n:,n:] # Extracting the y coefficient
    result = - Vxy / Vyy # Dividing by the y's coefficient(c) 
    
    # print("TLS solution \n", result)  # This will have 2 coefficients because we divided by y in previous step(a/c, b/c)
    return result.flatten()