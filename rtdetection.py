import cv2
import numpy as np
camera=cv2.VideoCapture(0)
def filter(image,type):
    f_img=image.copy()
    if type=='r':
        f_img[:,:,0]=0
        f_img[:,:,1]=0
    elif type=='g':
        f_img[:,:,0]=0
        f_img[:,:,2]=0
    elif type=='b':
        f_img[:,:,1]=0
        f_img[:,:,2]=0
    elif type=='s':
        sobelx=cv2.Sobel(cv2.cvtColor(f_img,cv2.COLOR_BGR2GRAY),cv2.CV_64F,1,0,ksize=3)
        sobely=cv2.Sobel(cv2.cvtColor(f_img,cv2.COLOR_BGR2GRAY),cv2.CV_64F,0,1,ksize=3)
        sobel=cv2.bitwise_or(sobelx.astype('uint8'),sobely.astype('uint8'))
        f_img=sobel
    elif type=='c':
        canny=cv2.Canny(f_img,100,300)
        f_img=canny
    return f_img
while True:
    r,cap=camera.read()
    cv2.imshow('win',cap)
    key=cv2.waitKey(1)&0b11111111
    if key==ord('r'):
        cap=filter(cap,'r')
    if key==ord('g'):
        cap=filter(cap,'g')
    if key==ord('g'):
        cap=filter(cap,'b')
    if key==ord('s'):
        cap=filter(cap,'s')
    if key==ord('c'):
        cap=filter(cap,'c')
