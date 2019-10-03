import socket                                                               
import cv2
import time 
import imagezmq

cap = cv2.VideoCapture(1)
sender = imagezmq.ImageSender(connect_to='tcp://192.168.5.12:5555')
time.sleep(2)
while 1:
    _,image = cap.read()
#    image = cv2.resize(image,(2000,1000),image)
#    cv2.imshow('a',image)
#    cv2.waitKey(1)
    sender.send_image('aaa',image)

