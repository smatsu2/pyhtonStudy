import sounddevice as sd
from scipy.io.wavfile import write

record_second = 3
fs = 44100

print ("start rec")
myrecording = sd.rec(int(record_second * fs), samplerate=fs, channels=2)
sd.wait()
print ("end rec")
write('output.wav', fs, myrecording)

