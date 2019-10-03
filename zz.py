# run this program on the Mac to display image streams from multiple RPis
import cv2
import imagezmq
import time
import numpy as np
image_hub = imagezmq.ImageHub()
cv2.namedWindow('..',cv2.WINDOW_NORMAL)
ori = time.time() * 1000
while True:  # show streamed images until Ctrl-C
    print("%7.3f"%(time.time() * 1000 - ori))
    ori = time.time() * 1000
    rpi_name, jpg_buffer = image_hub.recv_jpg()
    image = cv2.imdecode(np.fromstring(jpg_buffer, dtype='uint8'), -1)
    cv2.imshow('..', image) # 1 window for each RPi
    cv2.waitKey(1)
    image_hub.send_reply(b'OK')


