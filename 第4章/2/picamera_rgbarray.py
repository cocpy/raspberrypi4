from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


# 初始化相机
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera)

# 预热1秒
time.sleep(1)

# 从相机捕获数据
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Frame", image)
    # 准备数据流
    rawCapture.truncate(0)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
