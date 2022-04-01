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
#In[]
import numpy as np
from tqdm import tqdm
from tensorflow import keras
from keras import layers
import matplotlib.pyplot as plt 
'''
#准备数据¶
#手写数字识别任务：深度学习界的 “hello world”

#目标：对手写数字 0 到 9 共 10 个数字进行识别

训练样本：60000 个

测试样本：10000 个

每个样本： 28 * 28 个像素， 一个标签（0-9）
'''
# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")


# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
'''
x_train shape: (60000, 28, 28, 1)
60000 train samples
10000 test samples
'''
x_train.shape
#plt.imshow(x_train[])
(60000, 28, 28, 1)
# 观察第一个样本及其标签
plt.imshow(x_train[0, :, :, 0])
#<matplotlib.image.AxesImage at 0x1cace169220>

# to_categorical 函数将 5 变成 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0] 
# 这种表示称为 one-hot 表示， 用于多个类别的分类任务

print(y_train[0])
#[0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]


#In[]构建一个简单的卷积神经网络
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()
'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 26, 26, 32)        320       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 11, 11, 64)        18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 5, 5, 64)          0         
_________________________________________________________________
flatten (Flatten)            (None, 1600)              0         
_________________________________________________________________
dropout (Dropout)            (None, 1600)              0         
_________________________________________________________________
dense (Dense)                (None, 10)                16010     
=================================================================
Total params: 34,826
Trainable params: 34,826
Non-trainable params: 0
_________________________________________________________________
'''



#In[]训练神经网络
# 将 60000 个训练样本按照每 128 个分批输入神经网络 
batch_size = 128
# 神经网络遍历所有的训练数据 15 次（每个样本使用了15次）
epochs = 15
# 分类一般使用交叉熵损失函数 cross entropy
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)
'''
422/422 [==============================] - 9s 22ms/step - loss: 0.0361 - accuracy: 0.9882 - val_loss: 0.0295 - val_accuracy: 0.9923
Epoch 14/15
422/422 [==============================] - 9s 22ms/step - loss: 0.0354 - accuracy: 0.9884 - val_loss: 0.0307 - val_accuracy: 0.9915
Epoch 15/15
422/422 [==============================] - 9s 22ms/step - loss: 0.0318 - accuracy: 0.9894 - val_loss: 0.0307 - val_accuracy: 0.9918
'''

#训练后怎么办教程没写.....
# %%
