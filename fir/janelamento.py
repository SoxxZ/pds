# -*- coding: utf-8 -*- Prof. Cláudio – Nov/2014
""" FPB FIR de compr. 5, fc = 800 Hz, fs = 8 kHz, usando a função janela de Hamming."""
from scipy.signal import firwin, freqz
from matplotlib.pylab import plot,subplot,xlabel,ylabel,grid,title,legend,ylim,text, show, style
from numpy import pi, log10, abs, sqrt, nonzero, ravel

style.use('rose-pine')

def find(condition):
    res, = nonzero(ravel(condition))
    return res

fs = 8000; fc = 2000 # freq. de amostragem e de corte do FPB FIR (Hz)
Wc = 2*pi*fc/fs # freq. de corte normalizada (rad/amostra)
N = 17 # ordem do FPB FIR de fase linear
b2 = firwin(N,Wc/pi,window='hamming', pass_zero=False); w,H2 = freqz(b2,1)
# traçado das curvas de Magnitude da Resp. em Freq. dos Filtros PB FIR (janelas)
title('FPB FIR, 4a. Ordem, $f_c = 0,2\pi$ rad/amostra'); ylim1 = ylim()
xlabel(u'frequência (x $\pi$ rad/amostra)'); ylabel('magnitude (dB)')
plot(w/pi,20*log10(abs(H2)),'r-.',linewidth=2)
legend(('Hamming')); plot([0,1],[-6,-6], 'k--')
text(0.01,-7.5,u'Meia Potência',fontsize=8); # meia potência
plot([Wc,Wc],[-6.02,ylim1[0]],'r--') # freq. de corte original
text(Wc+0.02,ylim1[0]+5,'$f_c$ desejada',fontsize=8,color=[1, 0, 0])
subplot(1,1,1); f = w/pi*fs/2 # Hz
title('FPB FIR, 4a. Ordem, $f_c$ = 2000 Hz'); xlabel(u'frequência (Hz)')
plot(f,abs(H2),'r-.',linewidth=2)
legend(('Hamming'))
plot([0, fs/2],[1./sqrt(2), 1./sqrt(2)],'k--') # linha de meia potência
text(10,1./sqrt(2)-0.02,u'Meia Potência',fontsize=8)
plot([0, fs/2],[1/sqrt(2), 1/sqrt(2)], 'k--') # linha de meia potência
text(10,1/sqrt(2)-0.02,'Meia Potência',fontsize=8)
show()