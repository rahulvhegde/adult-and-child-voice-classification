import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import os
import cv2    
from tqdm import tqdm
import random as random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPool2D,BatchNormalization
from keras.models import Sequential
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
import tensorflow as tf
import warnings
import os
import wave
import pylab
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import os
import IPython as ip
from pathlib import Path
import librosa
import cv2
import numpy as np
def graph_spectrogram(wav_file):
    spectogram_path=os.getcwd() +'\\static\\img\\'
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    #pylab.title('spectrogram of %r' % wav_file)
    _=pylab.specgram(sound_info, Fs=frame_rate)
    filename='a.png'
    pylab.savefig(filename)
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate
def process():
    labels=['adult','child']
    path=os.getcwd() +'\\static\\img\\'
    fil=os.listdir(path)
    spectogram_path=Path(path)
    graph_spectrogram(path+'/'+fil[0])
    model = Sequential()

    model.add(Conv2D(64, kernel_size=(3, 3),activation='relu',padding='same',input_shape=(150,150,3)))
    model.add(MaxPool2D((2, 2),padding='same'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))

    model.add(Conv2D(128,kernel_size= (3, 3), activation='relu',padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2),padding='same'))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))

    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu',padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2),padding='same'))
    model.add(BatchNormalization())
    model.add(Dropout(0.3))

    model.add(Conv2D(256, kernel_size=(3, 3), activation='relu',padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2),padding='same'))
    model.add(BatchNormalization())
    model.add(Dropout(0.4))

    model.add(Conv2D(512, kernel_size=(3, 3), activation='relu',padding='same'))
    model.add(MaxPool2D(pool_size=(2, 2),padding='same'))
    model.add(BatchNormalization())
    model.add(Dropout(0.4))

    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dropout(0.3))
    model.add(BatchNormalization())

    model.add(Dense(2, activation='softmax'))

    model.load_weights(os.getcwd()+'\\model.h5')
    image=cv2.imread(os.getcwd()+'\\a.png',cv2.IMREAD_COLOR)
    image=cv2.resize(image,(150,150))
    predicters=np.array(image).reshape(1,150,150,3)
    y = np.array(predicters)
    y = y/255
    ans=model.predict(y)
    return labels[np.argmax(ans)]



        