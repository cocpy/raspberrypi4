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


def nopoint(img):
    """去干扰线，需输入灰度图"""
    pix = img.load()
    w, h = img.size
    for y in range(1,h-1):
        for x in range(1,w-1):
            count = 0
            if pix[x,y-1] > 245:
                count = count + 1
            if pix[x,y+1] > 245:
                count = count + 1
            if pix[x-1,y] > 245:
                count = count + 1
            if pix[x+1,y] > 245:
                count = count + 1
            if count > 2:
                pix[x,y] = 255
    return img


if __name__ == '__main__':
    image = Image.open('Π.png')

    # 转化为灰度图
    img = image.convert('L')

    # 把图片变成二值图像
    img = binaryzation(img, 190)

    # 去干扰线
    # img = nopoint(img)
    img.show()

    code = pytesseract.image_to_string(img)
    print ("数字是:" + str(code))