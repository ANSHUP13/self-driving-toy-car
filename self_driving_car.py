# -*- coding: utf-8 -*-
"""self driving car

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZhA5yY2XBHIvDf9GUHPgYpM_eRl4pSFa
"""

import csv
import numpy as np
from google.colab import files
import os
import zipfile
import random
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from shutil import copyfile
import matplotlib.pyplot as plt
import cv2
from tqdm import tqdm
from keras import optimizers
from keras.utils import to_categorical

from google.colab import drive
drive.mount('/content/drive')

#for second model


local_zip = '/content/drive/My Drive/handwrittenmathsymbols.zip'
zip_ref   = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/content')
zip_ref.close()

DATADIR = "/content/drive/My Drive/data/photo"

CATEGORIES = ["1","2","3","new"]

for category in CATEGORIES:  # do dogs and cats
    path = os.path.join(DATADIR,category)  # create path to dogs and cats
    for img in os.listdir(path):  # iterate over each image per dogs and cats
        img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
        plt.imshow(img_array, cmap='gray')  # graph it
        plt.show()  # display!

        break  # we just want one for now so break
    break  
print(img_array)
print(img_array.shape)

#TO CHANGE THE SIZE OF IMAGE
IMG_SIZE = 250

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap='gray')
plt.show()

source_images_m1 = []
source_path_m1 = []
DATADIR = "/content/drive/My Drive/data/photo"

def create_source_data():
    for category in CATEGORIES:  # do dogs and cats

        path = os.path.join(DATADIR,category)  # create path to dogs and cats
        class_num = CATEGORIES.index(category)  # get the classification  (0 or a 1). 0=dog 1=cat
        for img in tqdm(os.listdir(path)):
          img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)
          new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE)) 
          new_array = np.array(new_array).astype('float32') / 255.
          source_images_m1.append(new_array)
          source_path_m1.append(class_num)
            
create_source_data()

print(len(source_images_m1))
print(len(source_path_m1))

source_path_m1 = np.array(source_path_m1)
i = 0
while(i<6074):
  if source_path_m1[i] == 2 && source_path_m1[i] == 3:
    source_path_m1[i] = 1
  if source_path_m1[i] == 5 && source_path_m1[i] == 6 :
    source_path_m1[i] = 2
  if source_path_m1[i] == 6 &&  :
    source_path_m1[i] = 3
  if source_path_m1[i] == 8 :
    source_path_m1[i] = 4
    
  i = i+1
  
print(len(source_path_m1))

#for second model


source_images_m2 = []
source_path_m2 = []


def create_source_data():
    for category in CATEGORIES(2):  # do dogs and cats

        path = os.path.join(DATADIR(2),category)  # create path to dogs and cats
        class_num = CATEGORIES(2).index(category)  # get the classification  (0 or a 1). 0=dog 1=cat

        for img in tqdm(os.listdir(path)):  # iterate over each image per dogs and cats
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
                source_images_m2.append(new_array)
                source_path_m2.append(class_num)# add this to our training_data
            except Exception as e:  # in the interest in keeping the output clean...
                pass
            #except OSError as e:
            #    print("OSErrroBad img most likely", e, os.path.join(path,img))
            #except Exception as e:
            #    print("general exception", e, os.path.join(path,img))

create_source_data()

print(len(source_images_m2))
print(len(source_path_m2))

X = np.array(source_images_m1)
Y = np.array(source_path_m1)

# print(source_images_m1[1])
# print(source_path_m1)

from keras.utils import to_categorical

Y = to_categorical(Y , num_classes = 4)

print(X.shape)
print(Y.shape)

#source_images_m2 = np.array(source_images_m2)
#source_path_m2 = np.array(source_path_m2)
#print(source_images_m2.shape)
#print(source_path_m2.shape)
#print(source_images_m2[1])
#print(source_path_m2)
#print(b[1,0])
#training_images = np.array(b[:,0])

import sklearn.model_selection as model_selection
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, train_size=0.9,test_size=0.1)
# print ("X_train_m1: ", X_train_m1)
# print ("y_train_m1: ", y_train_m1)
# print ("X_test_m1: ", X_test_m1)
# print ("y_test_m1: ", y_test_m1)
# print (X_train_m1.shape)
#X_train:  [4, 9, 3, 5, 7, 6, 1]
#y_train:  [16, 81, 9, 25, 49, 36, 1]
#X_test:  [8, 2, 0]
#y_test:  [64, 4, 0]


#X_train_m2, X_test_m2, y_train_m2, y_test_m2 = model_selection.train_test_split(source_images_m2, source_path_m2, train_size=0.9,test_size=0.1, random_state=101)
#print ("X_train_m2: ", X_train_m2)
#print ("y_train_m2: ", y_train_m2)
#print ("X_test_m2: ", X_test_m2)
#print ("y_test_m2: ", y_test_m2)
#print (X_train_m2.shape)

X_train = np.expand_dims(X_train, axis=3)
X_test = np.expand_dims(X_test, axis=3)


# print(X_train_m1_images.shape)
# print(X_test_m1_images.shape)


#print(X_train_m2_images.shape)
#print(X_test_m2_images.shape)

print(y_test.shape)
print(X_test.shape)

from keras import optimizers
from keras import regularizers

from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten, BatchNormalization
from keras.models import Sequential

model = Sequential()
model.add(Conv2D(16 , kernel_size = (3,3) , strides = (1,1) , activation = 'relu' , padding = 'same' , input_shape = (250,250,1)))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(BatchNormalization())

# model.add(Conv2D(32 , kernel_size = (3,3) , strides = (1,1) , activation = 'relu' , padding = 'same'))
# model.add(MaxPooling2D(pool_size = (2,2)))
# model.add(BatchNormalization())

# model.add(Conv2D(64 , kernel_size = (3,3) , strides = (1,1) , activation = 'relu' , padding = 'same' ))
# model.add(MaxPooling2D(pool_size = (2,2)))
# model.add(BatchNormalization())

model.add(Flatten())

# model.add(Dense(1024 , activation = 'relu'))
# model.add(BatchNormalization())
# model.add(Dropout(0.25))

model.add(Dense(128 , activation = 'relu'))
model.add(BatchNormalization())
model.add(Dropout(0.25))

model.add(Dense(4 , activation = 'softmax'))

sgd = optimizers.SGD(lr=0.0001, decay=1e-4, momentum=0.9, nesterov=True)

model.compile(loss= 'categorical_crossentropy' ,
              optimizer="sgd",
              metrics=["accuracy"])
# history = model.fit_generator(train_datagen.flow(X_train_m1_images, y_train_m1, batch_size=32),
#                               steps_per_epoch=len(X_train_m1_images) / 32,
#                               epochs=15,
#                               validation_data=validation_datagen.flow(X_test_m1_images, y_test_m1, batch_size=32),
#                               validation_steps=len(X_test_m1_images) / 32)
history = model.fit(X_train , y_train , epochs = 10 , batch_size = 16 , validation_split = 0.2)

acc = model.evaluate(X_test , y_test)

acc

import matplotlib.pyplot as plt
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'r', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()

plt.plot(epochs, loss, 'r', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()

rounded_prediction = model.predict_classes(X_test)

print(rounded_prediction)

model.save('/content/drive/My Drive/signimage5.h5')

from keras.models import load_model

m = load_model('/content/drive/My Drive/signimage.h5')



import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD

model = Sequential()
# input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = optimizers.SGD(lr=0.1, decay=1e-4, momentum=0.9, nesterov=True)

model.compile(loss= 'sparse_categorical_crossentropy' ,
              optimizer="sgd",
              metrics=["accuracy"])
history = model.fit_generator(train_datagen.flow(X_train_m2_images, y_train_m2, batch_size=32),
                              steps_per_epoch=len(X_train_m2_images) / 32,
                              epochs=15,
                              validation_data=validation_datagen.flow(X_test_m2_images, y_test_m2, batch_size=32),
                              validation_steps=len(X_test_m2_images) / 32)

model.evaluate(X_test_m2_images, y_test_m2)

import matplotlib.pyplot as plt
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'r', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()

plt.plot(epochs, loss, 'r', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()



from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))