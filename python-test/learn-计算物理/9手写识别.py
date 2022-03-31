#########################################
'''
学习目标
    接触成熟的机器学习库 tensorflow，keras
    使用 keras 制造简单的数字识别代码
    使用神经网络分类 Quark 与 Gluon 喷注
学习内容
    简单的编码数字识别，内容基于 keras 例子：https://keras.io/examples/vision/mnist_convnet/
    任务笔记神经网络（卷积神经网络）'''
#########################################
import numpy as np
from tqdm import tqdm
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as p