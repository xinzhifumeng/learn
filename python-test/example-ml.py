'''
from sklearn.datasets import load_boston
data,target = load_boston(return_X_y = True)
print(data.shape)
print(target.shape)
print(target.size)
'''
#加载手写数字数据集
from sklearn.datasets import load_digits
import matplotlib.pylab as plt
digits = load_digits
print(digits)
plt.matshow(digits.images[6])
plt.show()