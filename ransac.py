import math
import numpy as np
import random as rd
from sls import std_least_square
from scipy.optimize import fmin_cobyla


def ransac(data_points_x, data_points_y, video_type):
    """
    RANSAC implemetation
    Parameters: 
    1) p : Desired probability that its a good sample
    2) e : Probability that a point is an outlier (# outliers / # datapoints)
    3) s : Minimum no. of points to fit the model
    4) N : No. of iterations
    5) t : threshold for inliners
    """
    data_points = list(zip(data_points_x, data_points_y))
    no_of_samples = len(data_points)
    
    if video_type == 1:
        # Video without noise
        t = 13  # Euclidean distance ascertained through visual inspection 
        no_of_outliers =  6 # Initial estimate

    else:
        # Video with noise
        no_of_outliners = 10
        t = 35  # Euclidean distance ascertained through visual inspection 
     
    p =  0.999999 # 99.9999% accuracy
    e = no_of_outliers/no_of_samples  # otliner ratio
    s = 3  # Minimum 3 points required to fit a parabola
    N = int(math.log(1-p)/math.log(1-(1-e)**s))  # Formula to get the number of iterations

    best_model = np.array([])
    max_inlier_count = 0

    for i in range(N):
        print(f"\n.....................iteration {i}......................\n",)
        
        inlier_count = 0
        sample_points = rd.sample(data_points, s)
        print("Sample points", sample_points)
        list_x, list_y = zip(*sample_points)
        result = std_least_square(list_x, list_y)
        # print(result)

        for point in data_points:
            # print("point", data_points.index(point)," ", point)

            #___________________Constraint optimization problem solution for minimum distance from point to parabola__________________

            def f(x):
                return (result[0])*x**2 + (result[1])*x + result[2]

            def objective(X):
                x,y = X
                distance = np.sqrt((x - point[0])**2 + (y - point[1])**2)
                return distance

            def c1(X):
                x,y = X
                return y - f(x)

            def c2(X):
                x,y = X
                return f(x) - y

            X = fmin_cobyla(objective, x0=[point[0], point[1]], cons=[c1, c2])

            distance = round(objective(X), 2)
            # print("Distance:", distance)

            # Condition to check inliner counts
            if distance <= t:
                inlier_count +=1
        
        # Condition to assign to best model
        if inlier_count > max_inlier_count:
            max_inlier_count = inlier_count
            best_model = result    
    
    print("Max inliner count for ransac: ", max_inlier_count, "\n")
    # print("RANSAC solution \n", best_model)
    
    return best_model
