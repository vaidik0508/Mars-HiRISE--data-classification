import numpy as np
from tensorflow import keras
import tensorflow as tf

def softmax(x):
    f_x = np.exp(x) / np.sum(np.exp(x))
    return f_x

def get_pred(img):
    
    map_label = {0: 'other',
     1: 'crater',
     2: 'dark dune',
     3: 'slope streak',
     4: 'bright dune',
     5: 'swiss cheese'
     }
    model = keras.models.load_model('model/final.h5')
    
    img = tf.expand_dims(img, axis=0)

    img = tf.image.resize(img, [227, 227])
    print(img)

    pred = model(img)
    pred = softmax(pred[0])
    
    i = int(tf.math.argmax(pred))
  
    return map_label[i], round(pred[i], 2)*100
