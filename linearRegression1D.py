#Program by: Pritish Yuvraj
#Sample Input: "https://drive.google.com/file/d/0BwXeiCjEpkS8YlNoVTAybHMtSzA/view?usp=sharing"
#The below program is for 1D Linear Regression

from __future__ import division
import matplotlib.pyplot as plt

def h(theta,x):
	return (theta[0]+(theta[1]*x))

def costJ(m,x,y,theta,scene_set):
	temp_sum = 0
	for i in range(len(x)):
		if scene_set == 0:
			temp_sum += (h(theta,x[i])-y[i])
		elif scene_set == 1:
			temp_sum += ((h(theta,x[i])-y[i])*x[i])
	return temp_sum

def gradDescent(x,y,alpha,theta,m):
	temp0 = 0
	temp1 = 0
	for i in range(5000000):
		temp0 = theta[0] - (alpha/m)*costJ(m,x,y,theta,0)
		temp1 = theta[1] - (alpha/m)*costJ(m,x,y,theta,1)
		#print "Without change",theta
		theta[0] = temp0
		theta[1] = temp1
		#print "After Change", theta
	return theta

def findy(x,theta):
	a = []
	for i in x:
		a.append(theta[0]+i*theta[1])
	return a

ans_theta = []	
#x = [10,12,14,16,18,20]
#y = [8.2,10.1,11.8,10.3,12.7,12.9]
xyfile = open("input.txt","r")
temp = []
x = []
y = []
for line in xyfile:
	temp = line.split()
	x.append(int(temp[0]))
	y.append(int(temp[1]))
print x,y	
ans_theta = gradDescent(x[-4:],y[-4:],0.001,[0.5,0.5],len(x))	
print ans_theta

plt.scatter(x,y,color='black')
plt.plot(x,findy(x,ans_theta),color ='blue',linewidth=2.0)
plt.xticks(())
plt.yticks(())
plt.show(())
while (0):
	choice = raw_input("Please Enter X ");
	choice = int(choice)
	if choice == 0:
		break
	else:
		#print "Expected Y is ",ans_theta[0],ans_theta[1],choice,(ans_theta[0]+(ans_theta[1]*choice))
		print "Expected Y is: ",(ans_theta[0]+(ans_theta[1]*choice))
