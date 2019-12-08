import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Sampling frequency
fs = 5000
t = np.arange(1000) / fs

# with frequency of 100
signala = np.sin(2*np.pi*100*t) 
#plt.plot(t,signala,label = 'a')

# with frequency of 20
signalb = np.sin(2*np.pi*20*t) 
#plt.plot(t,signalb,label = 'b')

#create original signal
signalc = signala + signalb
plt.plot(t, signalc, label = 'Original')

# Cut-off frequency of the filter
fc = 30

# Normalize the frequency
w = fc / (fs / 2)

#low pass filter
b, a = signal.butter(5, w, 'low')

#visualizing result
output = signal.filtfilt(b, a, signalc)
plt.plot(t, output, label='Filtered')
plt.legend()
plt.grid()
plt.show()
