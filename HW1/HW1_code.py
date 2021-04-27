import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D://ComputerVision//lena.bmp',cv2.IMREAD_GRAYSCALE) #argument two : read lena as grayscale and BGR
height , width = img.shape[0] , img.shape[1] #shape[0] read img height , shape[1] read img width


#upside-down lena
def UpsideDown():
    new_img = np.zeros([height,width], dtype=img.dtype)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = img[height-i-1][j]## -1 是為了符合元素大小的規定，不然會多出來
    return new_img

def RightSideLeft():
    new_img = np.zeros([height,width], dtype=img.dtype)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = img[i][width-j-1] ## -1 是為了符合元素大小的規定，不然會多出來
    return new_img

def DiagonalFlip():
    new_img = np.zeros([height,width], dtype=img.dtype)
    for i in range(height):
        for j in range(width):
            new_img[i][j] = img[j][i] 
    return new_img

def ShowResult(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis('off')##don't show the axis 
    plt.show()

#
# ShowResult(img)
# ShowResult(UpsideDown())
# ShowResult(RightSideLeft())
ShowResult(DiagonalFlip())