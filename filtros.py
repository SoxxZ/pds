import numpy as np
from scipy import signal, io
import matplotlib.pyplot as plt
import wave
import os

dirname = os.getcwd()

def plot_response(fs, w, h, title):
    plt.figure()
    plt.plot(0.5*fs*w/np.pi, 20*np.log10(np.abs(h)))
    #plt.ylim(-130, 5)
    #plt.xlim(0, 0.5*fs)
    plt.grid(True)
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.title(title)

def filter_create(fs, cutoff, transb, mo, W, n):
    print("Creating Filter")
    hn = signal.remez(n, [0, cutoff - transb, cutoff, 0.5*fs], mo, W, Hz=fs)
    w, h = signal.freqz(hn)
    print("Done Creating Filter")
    return hn, w, h

def filter_audio(filename, hn):
    print("Filtering Audio")
    fs, x = io.wavfile.read(filename)
    Ns = len(x) 
    y = signal.lfilter(hn, [1.],x)
    print("Done Filtering Audio")
    return y, Ns

filename = dirname + '/wav/sweep.wav'
filename_output = dirname+ '/wav/sweep_filtered.wav'

fs, x = io.wavfile.read(filename)     # frequencia de amostragem e amostras
cutoff = 4000   # frequencia de corte
transb = 600    # largura da banda de transicao
mo = [0,1]      # magnitudes
W = [5,1]       #fatores do filtroiltered_data
n = 227          # ordem do filtro

hn, w, h = filter_create(fs, cutoff, transb, mo, W, n)

y, Ns = filter_audio(filename, hn)
y = np.int16(y)

io.wavfile.write(filename_output,48000, y)



xx = abs(np.fft.fft(x))
xx = signal.decimate(xx,10)

xx_mag = xx[:int((len(xx)/2))]
xx_mag = 20*np.log10(np.abs(xx_mag))
xx_mag = np.interp(xx_mag,[np.amin(xx_mag), np.amax(xx_mag)], [-np.amax(xx_mag),0])
xx_freq = np.arange(len(xx[:int((len(xx)/2))]))

yy = abs(np.fft.fft(y))
yy = signal.decimate(yy,10)
yy_mag = yy[:int((len(yy)/2))]
yy_mag = 20*np.log10(np.abs(yy_mag))
yy_mag = np.interp(yy_mag,[np.amin(yy_mag), np.amax(yy_mag)], [-np.amax(yy_mag),0])
yy_freq = np.arange(len(yy[:int((len(yy)/2))]))


plot_response(fs, w, h, "Filtro Passa-Alta")

plt.figure()
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title("Sinal de Entrada")
plt.xlim(20, 20000)
plt.plot(xx_freq, xx_mag)

plt.figure()
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title("Sinal de Saída")
plt.xlim(20, 20000)
plt.plot(yy_freq, yy_mag)


plt.show()








xx = abs(np.fft.fft(x))
xx = signal.decimate(xx,10)

xx_mag = xx[:int((len(xx)/2))]
xx_mag = 20*np.log10(np.abs(xx_mag))
xx_mag = np.interp(xx_mag,[np.amin(xx_mag), np.amax(xx_mag)], [-np.amax(xx_mag),0])
xx_freq = np.arange(len(xx[:int((len(xx)/2))]))

yy = abs(np.fft.fft(y))
yy = signal.decimate(yy,10)
yy_mag = yy[:int((len(yy)/2))]
yy_mag = 20*np.log10(np.abs(yy_mag))
yy_mag = np.interp(yy_mag,[np.amin(yy_mag), np.amax(yy_mag)], [-np.amax(yy_mag),0])
yy_freq = np.arange(len(yy[:int((len(yy)/2))]))

plot_response(fs, w, h, "Filtro Passa-Alta")

plt.figure()
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title("Sinal de Entrada")
plt.xlim(20, 20000)
plt.plot(xx_freq, xx_mag)

plt.figure()
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title("Sinal de Saída")
plt.xlim(20, 20000)
plt.plot(yy_freq, yy_mag)

