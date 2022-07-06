import numpy as np
from scipy import signal, io
import matplotlib.pyplot as plt
import wave
import os

dirname = os.getcwd()

def filter_audio(filename, b, a):
    print("Filtering Audio")
    fs, x = io.wavfile.read(filename)
    Ns = len(x) 
    y = signal.lfilter(b, a, x)
    print("Done Filtering Audio")
    return y, Ns


b, a = signal.iirfilter(76, 2*np.pi*4000, rp=0.5 , rs=60, btype='high', analog=True, ftype='cheby2')

w, h = signal.freqs(b, a)

y = 20 * np.log10(np.maximum(abs(h), 1e-5))
x = w / (2*np.pi)

plt.figure()
plt.plot(x, y)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title("Filtro Analógico")
plt.xlim(20, 20000)
plt.show()

b, a = signal.iirfilter(76, 4000, rs=60, btype='high', analog=False, ftype='cheby2', fs=48000, output='ba')

w, h = signal.freqz(b, a, 48000, fs=48000)


yd = 20 * np.log10(np.maximum(abs(h), 1e-5))
xd = w

plt.figure()
plt.plot(xd, yd)
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title("Filtro Digital")
plt.xlim(20, 20000)


filename = dirname + '/wav/sweep.wav'
filename_output = dirname+ '/wav/sweep_filtered_iir.wav'

y, Ns = filter_audio(filename, b, a)
y = np.int16(y)

io.wavfile.write(filename_output,48000, y)

plt.show()