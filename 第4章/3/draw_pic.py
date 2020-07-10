import cv2 as cv


# 设置颜色
COLOR_MAP = {
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
    "red": (0, 0, 255),
    "white": (255, 255, 255)
}

# 读取图像
img = cv.imread('buster.tiff')

# 绘制线
cv.line(img, pt1=(0, 0), pt2=(900, 900), color=COLOR_MAP["green"])

# 绘制圆
cv.circle(img, center=(500, 500), radius=200, color=COLOR_MAP["green"])

# 绘制矩形
cv.rectangle(img, (100, 100), (600, 600), COLOR_MAP['red'])

# 绘制椭圆
cv.ellipse(img=img,center=(100,100), axes=(200,100), angle=0, startAngle=0, endAngle=360, color=(100, 200, 0), thickness=-1)

# 文字
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img=img, text="cocpy", org=(10, 250), fontFace=font, fontScale=2, color=(0, 0, 255),thickness=1)

# 显示图像
cv.imshow("draw", img)

# 使程序停留，等待任意键按下，参数表示停留的时间，0表示无限长
k = cv.waitKey(0)

# 按下ESC键（ASCII码为27）后，销毁所有窗口，终止程序
if k == 27:
    cv.destroyAllWindows()
