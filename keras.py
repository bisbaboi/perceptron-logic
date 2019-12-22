import numpy as np
import keras 
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.utils import np_utils
from keras.models import Sequential

(x_train,y_train) , (x_test,y_test)=keras.datasets.mnist.load_data()

#print(x_train.shape)
plt.imshow(x_train[0])

#one hot encoding

y_train =np_utils.to_categorical(y_train)

y_test =np_utils.to_categorical(y_test)

print(y_train[0])

x_train=x_train.reshape(len(x_train),-1)
x_test=x_test.reshape(len(x_test),-1)
print(x_train.shape)

model = Sequential()

model.add(Dense(256,input_dim = 784, activation = 'relu')) #784 ki jagah num_input
model.add(Dense(256,activation = 'relu'))
model.add(Dense(128,activation = 'relu'))

model.add(Dense(10, activation = 'softmax')) # 10 ki jagah num_classes

model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

final = model.fit(x_train,y_train,epochs=30,batch_size=100,verbose=1)
