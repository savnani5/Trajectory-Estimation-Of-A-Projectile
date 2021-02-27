import time
import numpy as np
import matplotlib.pyplot as plt

from ransac import ransac
from sls import std_least_square
from tls import total_least_square
from video_process import video_process

def error_cal(data_points_x, data_points_y, result_sls, result_tls, result_ransac):
    
    error_sls = 0 
    error_tls = 0 
    error_ransac = 0
    for x, y in zip(data_points_x, data_points_y):
        error_sls += ((result_sls[0])*x**2 + (result_sls[1])*x + result_sls[2] - y)**2
        error_tls += ((result_tls[0])*x**2 + (result_tls[1])*x - y)**2
        error_ransac += ((result_ransac[0])*x**2 + (result_ransac[1])*x + result_ransac[2] - y)**2
        
    return error_sls, error_tls, error_ransac

if __name__ == "__main__":

    video = "Ball_travel_10fps.mp4"
    data_points_x, data_points_y = video_process(video)


    # Standard least Square
    tick = time.time()
    result_sls = std_least_square(data_points_x, data_points_y)
    tock1 = time.time() - tick  # time of execution for sls 
    
    # Total least 
    tick = time.time()
    result_tls = total_least_square(data_points_x, data_points_y)
    tock2 = time.time() - tick  # time of execution for tls 
    
    # RANSAC
    tick = time.time()
    result_ransac = ransac(data_points_x, data_points_y, 1)
    tock3 = time.time() - tick  # time of execution for ransac 

    print("Time of execution for sls: ", tock1, "s", "\n", "Time of execution for tls: ", tock2, "s", "\n", "Time of execution for ransac: ", tock3, "s", "\n" )
    
    #Error calculation
    error_sls, error_tls, error_ransac = error_cal(data_points_x, data_points_y, result_sls, result_tls, result_ransac)
    print("Error in SLS Fit: ", error_sls, "\n", "Error in TLS Fit: ", error_tls, "\n", "Error in RANSAC Fit: ", error_ransac, "\n" )

    #___________Plotting the fitted curve and scatter points________________________
 
    x = np.linspace(-20, 730, 1000) # X will remain common for all methods

    y_sls = (result_sls[0])*x**2 + (result_sls[1])*x + result_sls[2]
    y_tls = (result_tls[0])*x**2 + (result_tls[1])*x  # It is assumed that the data is normalized i.e it passes through origin, so result_tls has 2 elements
    y_ransac = (result_ransac[0])*x**2 + (result_ransac[1])*x + result_ransac[2]
    
    y = [y_sls, y_tls, y_ransac]
    title = ['Standard_Least_Square', 'Total_Least_Square', 'RANSAC']
    
    for i in range(3):
        plt.figure(i)
        plt.title(title[i])
        plt.scatter(data_points_x, data_points_y, c = 'r', label = 'Scatter plot of Data points')
        plt.plot(x, y[i], label = 'Fitted Curve') 
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc='best')
        plt.savefig(f'{video}_{title[i]}.png')
    
    plt.show()
    
    