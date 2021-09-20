import librosa
import IPython
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


filename = 'C:\\Users\\smatsu\\Desktop\\ESC-50-master\\ESC-50-master\\audio\\1-5996-A-6.wav'
wav, sr = librosa.load(filename, sr=44100)
print("load success")

IPython.display.Audio(data=wav, rate=sr)
print("sound")