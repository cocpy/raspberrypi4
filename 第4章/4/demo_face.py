import cv2
import numpy as np

img = cv2.imread("face.png")

b_channel, g_channel, r_channel = cv2.split(img)

alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255
# 最小值为0
alpha_channel[:, :int(b_channel.shape[0] / 2)] = 100

img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))

cv2.imwrite("lena.png", img_BGRA)
