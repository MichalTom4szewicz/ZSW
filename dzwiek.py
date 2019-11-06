import sounddevice as sd
from scipy.io.wavfile import write
from time import gmtime, strftime
from scipy.io import wavfile as wav
import os

timestamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())

ts = str(timestamp)+".wav"
print(ts)


fs = 44100  # Sample rate
seconds = 5  # Duration of recording


myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write(ts, fs, myrecording)  # Save as WAV file

rate, data = wav.read(ts)

min = 0
max = 0

print(int(data[10][0]))
for i in data:
    for j in i:
        a = float(j)
        if a < min:
            min = a
        if a > max:
            max = a

print("minimum: " + str(min))
print("maximum: " + str(max))

list = os.listdir(r".")

nazwa = "dane.txt"


#jakiestam przetwarzanie ocena tego czy jest glosno czy cicho, najlepiej w dB
# moze cos takiego https://github.com/SuperShinyEyes/spl-meter-with-RPi

if nazwa in list:
    f = open("dane.txt", "a")
    f.write(str(timestamp) + " " + str(min) + " " + str(max)+"\n")
    f.close()
else:
    f = open("dane.txt", "x")
    f.write(str(timestamp) + " " + str(min) + " " + str(max)+"\n")
    f.close()


