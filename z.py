# run this program on the Mac to display image streams from multiple RPis
import cv2
import imagezmq
import time
image_hub = imagezmq.ImageHub()
cv2.namedWindow('..',cv2.WINDOW_NORMAL)
ori = time.time() * 1000
while True:  # show streamed images until Ctrl-C
    print("%7.3f"%(time.time() * 1000 - ori))
    ori = time.time() * 1000
    rpi_name, image = image_hub.recv_image()
    cv2.imshow('..', image) # 1 window for each RPi
    cv2.waitKey(1)
    image_hub.send_reply(b'OK')


