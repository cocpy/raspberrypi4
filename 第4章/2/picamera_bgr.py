import time
import picamera
import numpy as np
import cv2


with picamera.PiCamera() as camera:
    # 设置分辨率
    camera.resolution = (320, 240)
    # 设置帧数
    camera.framerate = 24
    time.sleep(2)
    image = np.empty((240 * 320 * 3,), dtype=np.uint8)
    # 保存为OpenCV的bgr格式
    camera.capture(image, 'bgr')
    image = image.reshape((240, 320, 3))
    cv2.imshow("img", image)
    if cv2.waitKey(0) == ord('q'):
        exit(0)
