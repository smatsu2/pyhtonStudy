import librosa

filename = 'C:\\Users\\smatsu\\Desktop\\ESC-50-master\\ESC-50-master\\audio\\1-5996-A-6.wav'
wav, sr = librosa.load(filename, sr=44100)
print("load success")

import librosa.display
import matplotlib.pyplot as plt

plt.figure()
plt.figure(figsize=(15,5))
librosa.display.waveplot(wav, sr)
plt.show()
print("plot displayed")
