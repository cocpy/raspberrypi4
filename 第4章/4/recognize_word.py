from PIL import Image
import pytesseract


def binaryzation(img,threshold):
    """二值化"""
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


if __name__ == '__main__':
    image = Image.open('word.png')

    # 转化为灰度图
    img = image.convert('L')

    # 把图片变成二值图像
    img = binaryzation(img, 190)

    code = pytesseract.image_to_string(img)
    print ("字符是:" + str(code))