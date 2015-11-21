import numpy as np
from numpy.linalg import inv
no = raw_input("")
no = no.split()
feature = int(no[0])
x_matrix = np.empty((0,feature+1),float)
y_matrix= np.empty((0,1),float)
input_matrix = np.empty((0,feature+1),float)
m = int(no[1])
for i in range(m):
	rough = raw_input("")
	rough = rough.split()
	rough.insert(0,1)
	rough1 = []
	#print rough[:-1]
	x_matrix = np.append(x_matrix,np.array([rough[:-1]]), axis=0)
	#print [rough[-1]]
	y_matrix = np.append(y_matrix,np.array([[rough[-1]]]), axis=0)
	#print y_matrix
x_input = int(raw_input(""))
for i in range(x_input):
	temp_x = []
	rough = raw_input("")
	rough = rough.split()
	rough.insert(0,1)
	input_matrix = np.append(input_matrix, np.array([rough[:]]), axis = 0)
#print x_matrix,y_matrix,input_matrix

#theta = np.empty((0,1),float)
#print inv(x_matrix)
x_mat = x_matrix.astype(np.float)
y_mat = y_matrix.astype(np.float)
input_mat = input_matrix.astype(float)
#inv = np.linalg.pinv(x_mat)
x_trans = x_mat.transpose()
first_x = np.dot(x_trans,x_mat)
first_inv = np.linalg.pinv(first_x)
second_mul = np.dot(first_inv,x_trans)
third_mul = np.dot(second_mul,y_mat)
#print third_mul
ans = np.dot(input_mat,third_mul)
for i in range(len(ans)):
	print int(ans[i])


'''
First line contains no of features followed by no of sample data
After input is taken it is followed by input data whose result need to be calculated

Example Input:
2 100
0.44 0.68 511.14
0.99 0.23 717.1
0.84 0.29 607.91
0.28 0.45 270.4
0.07 0.83 289.88
0.66 0.8 830.85
0.73 0.92 1038.09
0.57 0.43 455.19
0.43 0.89 640.17
0.27 0.95 511.06
0.43 0.06 177.03
0.87 0.91 1242.52
0.78 0.69 891.37
0.9 0.94 1339.72
0.41 0.06 169.88
0.52 0.17 276.05
0.47 0.66 517.43
0.65 0.43 522.25
0.85 0.64 932.21
0.93 0.44 851.25
0.41 0.93 640.11
0.36 0.43 308.68
0.78 0.85 1046.05
0.69 0.07 332.4
0.04 0.52 171.85
0.17 0.15 109.55
0.68 0.13 361.97
0.84 0.6 872.21
0.38 0.4 303.7
0.12 0.65 256.38
0.62 0.17 341.2
0.79 0.97 1194.63
0.82 0.04 408.6
0.91 0.53 895.54
0.35 0.85 518.25
0.57 0.69 638.75
0.52 0.22 301.9
0.31 0.15 163.38
0.6 0.02 240.77
0.99 0.91 1449.05
0.48 0.76 609.0
0.3 0.19 174.59
0.58 0.62 593.45
0.65 0.17 355.96
0.6 0.69 671.46
0.95 0.76 1193.7
0.47 0.23 278.88
0.15 0.96 411.4
0.01 0.03 42.08
0.26 0.23 166.19
0.01 0.11 58.62
0.45 0.87 642.45
0.09 0.97 368.14
0.96 0.25 702.78
0.63 0.58 615.74
0.06 0.42 143.79
0.1 0.24 109.0
0.26 0.62 328.28
0.41 0.15 205.16
0.91 0.95 1360.49
0.83 0.64 905.83
0.44 0.64 487.33
0.2 0.4 202.76
0.43 0.12 202.01
0.21 0.22 148.87
0.88 0.4 745.3
0.31 0.87 503.04
0.99 0.99 1563.82
0.23 0.26 165.21
0.79 0.12 438.4
0.02 0.28 98.47
0.89 0.48 819.63
0.02 0.56 174.44
0.92 0.03 483.13
0.72 0.34 534.24
0.3 0.99 572.31
0.86 0.66 957.61
0.47 0.65 518.29
0.79 0.94 1143.49
0.82 0.96 1211.31
0.9 0.42 784.74
0.19 0.62 283.7
0.7 0.57 684.38
0.7 0.61 719.46
0.69 0.0 292.23
0.98 0.3 775.68
0.3 0.08 130.77
0.85 0.49 801.6
0.73 0.01 323.55
1.0 0.23 726.9
0.42 0.94 661.12
0.49 0.98 771.11
0.89 0.68 1016.14
0.22 0.46 237.69
0.34 0.5 325.89
0.99 0.13 636.22
0.28 0.46 272.12
0.87 0.36 696.65
0.23 0.87 434.53
0.77 0.36 593.86
4
0.05 0.54
0.91 0.91
0.31 0.76
0.51 0.31
'''
