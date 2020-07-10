import cv2 as cv


def main():
    """显示图像"""
    while True:
        # 读取图像(frame就是读取的视频帧)
        ret, frame = cap.read()
        # 将图像灰度化处理
        img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("img", img)
        # 图像不处理的情况
        cv.imshow("frame", frame)
        input = cv.waitKey(20)
        # 如过输入的是break，就结束图像显示，鼠标点击视频画面输入字符
        if input == ord('break'):
            break


if __name__ == '__main__':
    # 调用摄像头
    # 参数‘0’是打开电脑自带摄像头
    # 参数‘1’是打开外部摄像头
    cap = cv.VideoCapture(0)
    width, height = 1280, 960
    cap.set(cv.CAP_PROP_FRAME_WIDTH, width)  # 设置图像宽度
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)  # 设置图像高度

    main()

    # 释放摄像头
    cap.release()
    # 销毁窗口
    cv.destroyAllWindows()
