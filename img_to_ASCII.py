#importing OpenCV module to work with image
import cv2

fname=input("Get file path")

s=""

#Removing the quotations at the ends of file path
for i in range(1, len(fname)-1):
    s+=fname[i]

#Storing it in a 2 dimm matrix, in black-and-white
img=cv2.imread(s, 0)

# print(img)

h=img.shape[0]
w=img.shape[1]

#traversing through said image matrix and converting to appropriate signage depending on its value
#255->pure white, 0->pure black
for i in range (h):
    for j in range (w):
        if(img[i][j]>230):
            print('#',end='')
        elif(img[i][j]>190):
            print('X', end='')
        elif(img[i][j]>150):
            print('%', end='')
        elif(img[i][j]>110):
            print('&', end='')
        elif(img[i][j]>70):
            print('*', end='')
        elif(img[i][j]>40):
            print('+', end='')
        else:
            print('/', end='')
    print('\n')