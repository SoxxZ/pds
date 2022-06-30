import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def plot_response(fs, w, h, title):
    plt.figure()
    plt.plot(0.5*fs*w/np.pi, 20*np.log10(np.abs(h)))
    plt.ylim(-130, 5)
    plt.xlim(0, 0.5*fs)
    plt.grid(True)
    plt.xlabel('Frequência (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.title(title)


fs = 12000       # frequencia de amostragem
cutoff = 4000    # frequencia de corte
transb = 600  # largura da banda de transicao
mo = [0,1] # magnitudes
W = [5,1]#fatores do filtro
n = 59      # ordem do filtro

hn = signal.remez(n, [0, cutoff - transb, cutoff, 0.5*fs], mo, W, Hz=fs)
w, h = signal.freqz(hn)

plot_response(fs, w, h, "Filtro Passa-Alta")
plt.show()
