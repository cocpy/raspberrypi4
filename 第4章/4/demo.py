#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
from urllib import request
import numpy as np
import sys
from numpy import *
import operator
import time
from os import listdir


def classify(inputPoint,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]  #已知分类的数据集（训练集）的行数
    #先tile函数将输入点拓展成与训练集相同维数的矩阵，再计算欧氏距离
    diffMat = tile(inputPoint,(dataSetSize,1))-dataSet  #样本与训练集的差值矩阵
    sqDiffMat = diffMat ** 2     #差值矩阵平方
    sqDistances = sqDiffMat.sum(axis=1)   #计算每一行上元素的和
    distances = sqDistances ** 0.5     #开方得到欧拉距离矩阵
    sortedDistIndicies = distances.argsort() #按distances中元素进行升序排序后得到的对应下标的列表
    #选择距离最小的k个点
    classCount = {}
    for i in range(k):
        voteIlabel = labels[ sortedDistIndicies[i] ]
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    #按classCount字典的第2个元素（即类别出现的次数）从大到小排序
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]
def img2vector(filename):
    returnVect = []
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect.append(int(lineStr[j]))
    return returnVect
def classnumCut(fileName):
    fileStr = fileName.split('.')[0]
    classNumStr = int(fileStr.split('_')[0])
    return classNumStr
#构建训练集数据向量，及对应分类标签向量
def trainingDataSet():
    hwLabels = []
    trainingFileList = listdir('E:/VS2013Project/picsolve/trainingDigits')     #获取目录内容
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))        #m维向量的训练集
    for i in range(m):
        fileNameStr = trainingFileList[i]
        hwLabels.append(classnumCut(fileNameStr))
        trainingMat[i,:] = img2vector('E:/VS2013Project/picsolve/trainingDigits/%s' % fileNameStr)
        #print type(trainingMat)
    return hwLabels,trainingMat

img = cv2.imread('5.jpg')
#显示原图
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
cv2.waitKey(0)
#sp[0] rows sp[1] cols sp[2] pixels
sp=img.shape
#转化为灰度图
grayimg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#转化为二值图
retval,dstimg = cv2.threshold(grayimg,120,255,cv2.THRESH_BINARY)
dst_sp=dstimg.shape
print(dst_sp[0])
print(dst_sp[1])
#圈出数字区域
roi_img = dstimg[850:890,620:750]
roi_sp = roi_img.shape
cv2.namedWindow("roi",cv2.WINDOW_NORMAL)
cv2.imshow("roi",roi_img)
cv2.waitKey(0)
#切分图片
roi_img = roi_img[2:35,7:130]
cv2.namedWindow("roi1",cv2.WINDOW_NORMAL)
cv2.imshow("roi1",roi_img)
cv2.waitKey(0)
dst_sp2=roi_img.shape
print(dst_sp2[0])
print(dst_sp2[1])
index=[0,0,0,0,0]
k=0
for i in range(6):
    if i == 2:
       continue
    elif i == 0:
       roi_img1 = roi_img[1:180,i*20:i*20+20]
    else :
       roi_img1 = roi_img[1:180,i*20:i*20+20]
    cv2.namedWindow("roi2",cv2.WINDOW_NORMAL)
    cv2.imshow("roi2",roi_img1)
    cv2.waitKey(0)
#归一化 32X32
    res=cv2.resize(roi_img1,(32,32),interpolation=cv2.INTER_CUBIC)
#0/1矩阵
#    fid=open(str(i)+'.txt','w')
    pic=[]
    for i in range(32):
        for j in range(32):
            if res[i][j]<=200:
                res[i][j]=0
            else:
                res[i][j]=1
            pic.append(int(res[i][j]))
 #           fid.write(str(res[i][j]))
 #       fid.write("\n")
 #   fid.close()
    hwLabels,trainingMat = trainingDataSet()
    classifierResult = classify(pic, trainingMat, hwLabels, 3)
    index[k]=classifierResult
    k=k+1
    print (classifierResult)
print(index)
num1 = index[0]*10+index[1]
num2 = index[2]*100+index[3]*10+index[4]
print(num1)
print(num2)
cv2.destroyAllWindows()
