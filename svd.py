import numpy as np

def svd(X):
    """
    Let X be an m*n matrix, so to find SVD we have 3 conditions depending on the values of m and n:
    
    1) m = n : Here the X matrix is a square matrix i.e the number of coefficients is equal to the number of data points. Also, here the sigma matrix will be square so it is simple to calculate.
    2) m < n : Here the X matrix is a rectangular matrix i.e number of coefficients is more than the number of data points, thus this can't be the case for fitting the parabola, but will be used in homography.
    3) m > n : Here the X matrix is a rectangular matrix i.e number of coefficients is less then the number of data points (overdefined situation), and we'll be dealing with this case in total least squares.    
    """

    #_________________ Calculating Vt matrix________________________

    r_values, r_vectors = np.linalg.eig(np.dot(X.T,X))

    # Sorting the values and vectors in descending order
    idx = r_values.argsort()[::-1]   
    r_values = r_values[idx]
    r_vectors = r_vectors[:,idx]
    Vt = r_vectors.T
    V = Vt.T
    # print("vt", Vt)
    
    #________________Calculating Sigma matrix_______________________

    # Removing "zero valued" eigen values
    index = []
    for i in range(len(r_values)):
        if r_values[i] <= 0.001:
            index.append(i)

    r_values = np.delete(r_values, index)

    s = np.zeros(shape=(X.shape))
    for i in range(len(r_values)):
        s[i,i] = r_values[i]**0.5
    # print("s", s)

    #__________________Calculating U matrix____________________________

    l_values, l_vectors = np.linalg.eig(np.dot(X,X.T))
    idx = l_values.argsort()[::-1]   
    l_values = l_values[idx]
    l_vectors = l_vectors[:,idx]
    U = l_vectors.real
    # print("U",U)
    
    return U, s, Vt


