from random import randint
#import numpy as np

# #hit roll 5+ z rerollem
#
# ile=0
# liczba = 10000000
#
# for i in range(liczba):
#     if(randint(1,6)<5):
#         if(randint(1,6)>4):
#             ile += 1
#     else:
#         ile +=1
#
#
# print(ile/liczba)


from datetime import date, time
import sounddevice as sd
from scipy.io.wavfile import write

from playsound import playsound

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import datetime

from time import gmtime, strftime
timestamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())

ts = str(timestamp)+".wav"
print(ts)


fs = 44100  # Sample rate
seconds = 5 # Duration of recording


myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write(ts, fs, myrecording)  # Save as WAV file

#playsound(ts)


import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
rate, data = wav.read(ts)
data1=numpy.absolute(data)  # uzyskiwanie samych dodatnych wartosci
data1=numpy.sort(data1, axis = 0)   # posortowanie wartosci 

wartoscGlosnosci = int(len(data1)/100*95)  # bierzemy 95 percentyl

# print(int(data1[wartoscGlosnosci][0]))




poziomHalasu= round(20*numpy.log10(int(data1[wartoscGlosnosci][0])),2)
print("Poziom halasu: "+ str(poziomHalasu)+" dB")
#plt.plot(data)
#plt.show()


import os

list = os.listdir(r".")

nazwa = "dane.txt"


#jakiestam przetwarzanie ocena tego czy jest glosno czy cicho, najlepiej w dB
# moze cos takiego https://github.com/SuperShinyEyes/spl-meter-with-RPi

if nazwa in list:
    f = open("dane.txt", "a")
    f.write(str(poziomHalasu)+"\n")
    f.close()
else:
    f = open("dane.txt", "x")
    f.write(str(poziomHalasu)+"\n")
    f.close()
    
with open("dane.txt",'r') as f:
    x = f.readlines()
    
sum= 0    
min=100
max=0    
for value in x:
    a = float(value)
    sum += a
    if a<min:
            min=a
    if a>max:
            max=a
average = sum / len(x)
average = round(average,2)

print(str(average))
print(min)
print(max)
    
# dzielimy przedzial na 5 czesci i zaleznie od tego w ktorej czesci znajduje sie probka bedzie okreslane czy glosno, cicho itp     
poczatek = 0 
if (min+max)/2 >= average :
    print("srodek powyzej sredniej")
    szerokoscPoziomu = (average - min) /(2.5)
    print(szerokoscPoziomu)
    poczatek = min
else: 
    print("srodek ponizej sredniej")
    szerokoscPoziomu = (max - average) /(2.5)
    print(szerokoscPoziomu)
    poczatek = max - 5* szerokoscPoziomu




if( poczatek + szerokoscPoziomu  > poziomHalasu and poziomHalasu >= 0):
    print("bardzo cicho")
if( poczatek + 2* szerokoscPoziomu  > poziomHalasu and poziomHalasu >= poczatek + szerokoscPoziomu ):
    print("cicho")
if( poczatek + 3* szerokoscPoziomu  >= poziomHalasu and poziomHalasu >= poczatek + 2* szerokoscPoziomu):
    print("przecietnie glosno")
if( poczatek + 4* szerokoscPoziomu  >= poziomHalasu and poziomHalasu > poczatek + 3* szerokoscPoziomu):
    print("glosno")
if( 150  >= poziomHalasu and poziomHalasu > poczatek + 4* szerokoscPoziomu):
    print("bardzo glosno")
