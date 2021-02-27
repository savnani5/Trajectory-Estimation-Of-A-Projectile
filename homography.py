from svd import svd
import numpy as np

# To compute the homography matrix we have to solve the homogeneous equation AH = 0, where H is the homography matrix

sp = [(5,5), (150,5), (150, 150), (5,150)]  # Source points
dp = [(100,100), (200,80), (220,80), (100,200)] # Destination points

# Constructing the A matrix
A = np.zeros(shape=(8,9))
c = 0
for i in range(0,len(2*sp),2):
    A[i] = np.array([-sp[c][0], -sp[c][1], -1, 0, 0, 0, sp[c][0]*dp[c][0], sp[c][1]*dp[c][0], dp[c][0]])
    A[i+1] = np.array([0, 0, 0, -sp[c][0], -sp[c][1], -1, sp[c][0]*dp[c][1], sp[c][1]*dp[c][1], dp[c][1]]) 
    c+=1


U1, s1, Vt1 = svd(A)
H1 = Vt1[-1,:]
H1 = H1.reshape(3,3)
print("H matrix constructed from my SVD function: \n", H1, "\n")

print ("--"*30)

U, s, Vt = np.linalg.svd(A)
H = Vt[-1,:]
H = H.reshape(3,3)
print("H matrix constructed from numpy's inbuilt function for cross checking: \n", H)


