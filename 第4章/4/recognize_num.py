import numpy as np
import cv2 as cv


img = cv.imread('/home/pi/opencv/samples/data/digits.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# 现在我们将图像分割为5000个单元格，每个单元格为20x20
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
# 使其成为一个Numpy数组。它的大小将是（50,100,20,20）
x = np.array(cells)
# 现在我们准备train_data和test_data。
train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)
# 为训练和测试数据创建标签
k = np.arange(10)
train_labels = np.repeat(k,250)[:,np.newaxis]
test_labels = train_labels.copy()
# 初始化kNN，训练数据，然后使用k = 1的测试数据对其进行测试
knn = cv.ml.KNearest_create()
knn.train(train, cv.ml.ROW_SAMPLE, train_labels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)
# 现在，我们检查分类的准确性
#为此，将结果与test_labels进行比较，并检查哪个错误
matches = result==test_labels
correct = np.count_nonzero(matches)

# 准确度
accuracy = correct*100.0/result.size
print( accuracy )

# 保存数据
np.savez('knn_data.npz',train=train, train_labels=train_labels)

# 现在加载数据
with np.load('knn_data.npz') as data:
    print( data.files )
    train = data['train']
    train_labels = data['train_labels']

    knn = cv.KNearest()
    knn.train(train, train_labels)

    letter = cv.imread('code.png')
    letter = cv.cvtColor(letter, cv.COLOR_BGR2GRAY)
    print(letter.shape)

    ret, result, neighbours, dist = knn.findNearest(letter, k=5)

    # letter = letter.reshape((1, 100))
    # letter = np.float32(letter)
    # print(letter.shape)
    #
    # ret, result, neighbors, dist = knn.find_nearest(letter, k=5)
    print(result)



# k = 80
# train_label = labels[:k]
# train_input = samples[:k]
# test_input = samples[k:]
# test_label = labels[k:]
#
# model = cv.ml.KNearest_create()
# model.train(train_input,cv.ml.ROW_SAMPLE,train_label)
#
# retval, results, neigh_resp, dists = model.findNearest(test_input, 1)
# string = results.ravel()
#
# print(test_label.reshape(1,len(test_label))[0])
# print(string)


retval, results=knn.predict(test[1003:1005])
# Docstring: predict(samples[, results[, flags]]) -> retval, results
print(retval, results)#(4.0, array([[ 4.],[ 4.]], dtype=float32))
#对比
cv.imwrite('test[1005].jpg',test[1005].reshape((20,20)))


trainingData = np.load('knn_data.npz')
train = trainingData['train']
trainLabels = trainingData['train_labels']

