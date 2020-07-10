import cv2 as cv


# 读取一张名为buster.tiff的图片（需要先确认图片路径正确）
image = cv.imread('buster.tiff')

# 创建窗口
cv.namedWindow('buster native', cv.WINDOW_NORMAL)
# 设置大小
cv.resizeWindow('buster native', 320, 240)
cv.namedWindow('buster gray', 0)
cv.resizeWindow('buster gray', 320, 240)

# 显示读取的图像
cv.imshow('buster native', image)

# 将读取后的图片转换为灰度图片
img_gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

# 显示灰度图像
cv.imshow("buster gray", img_gray)

# 保存灰度图像
cv.imwrite("buster_gray.png", img_gray)

# 使程序停留，等待任意键按下，参数表示停留的时间，0表示无限长
k = cv.waitKey(0)

# 按下ESC键（ASCII码为27）后，销毁所有窗口，终止程序
if k == 27:
    cv.destroyAllWindows()
