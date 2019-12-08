import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
fs = 5000  # Sampling frequency
t = np.arange(1000) / fs
signala = np.sin(2*np.pi*100*t) # with frequency of 100
#plt.plot(t,signala,label = 'a')
signalb = np.sin(2*np.pi*20*t) # with frequency of 20
#plt.plot(t,signalb,label = 'b')
signalc = signala + signalb
plt.plot(t, signalc, label = 'Original')
fc = 30  # Cut-off frequency of the filter
w = fc / (fs / 2) # Normalize the frequency
b, a = signal.butter(5, w, 'low')
output = signal.filtfilt(b, a, signalc)
plt.plot(t, output, label='Filtered')
plt.legend()
plt.grid()
plt.show()
