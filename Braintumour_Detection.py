import numpy as np
from matplotlib import pyplot as plt
import cv2
from PIL import Image as im
path = input("Enter the path :")
frame = cv2.imread(path)
x=np.shape(frame)
gray=np.zeros((x[0],x[1]))
print (np.shape(frame))
n=0#for storing maximum value
#converts rgb image in to gray
for i in range(0,x[0]):
	for k in range(0,x[1]):
		y=frame[i][k]
		gray[i][k]=0.2989* y[0] + 0.5870 * y[1] + 0.1140 * y[2]
		if (n<gray[i][k]):
			n=gray[i][k]
n=int(n)
print (n)
y=np.zeros(n)
print (gray)
#histogram approximation of gray image
for i in range(0,n):
	k=0
	for m in range(0,x[0]):
		for z in range(0,x[1]):
			if(int(gray[m][z])==i ):
					k=k+1
	y[i]=k#store how many times i occurs
y=np.round(y)
print (y)
plt.subplot(133)
plt.plot(y)
count=0
#for converting gray image to binary
for i in range(0,x[0]):
	for k in range(0,x[1]):
		if(gray[i][k]<150):
			gray[i][k]=1
		else:
			gray[i][k]=0
			count=count+1
p=0.264;
size=np.sqrt(count)*p
print (size)
print (gray)
plt.subplot(131)
plt.imshow(gray,cmap='gray')
plt.title("Tumer detected")
plt.subplot(132)
plt.imshow(frame)
plt.title("Original image")
plt.show()
