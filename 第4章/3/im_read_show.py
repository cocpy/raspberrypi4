import cv2 as cv

# 读取一张名为buster.tiff的图片（需要先确认图片路径正确）
image = cv.imread('buster.tiff')

# 显示读取的图像，窗口名称为buster
cv.imshow('buster', image)

# 使程序停留，等待任意键按下，参数表示停留的时间，0表示无限长
k = cv.waitKey(0)

# 按下ESC键（ASCII码为27）后，销毁所有窗口，终止程序
if k == 27:
    cv.destroyAllWindows()
