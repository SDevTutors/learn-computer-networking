from numpy import pi, sin

print(2*sin(6284*0 + pi/4))
print(2*sin(6284*0.1 + pi/4))
print(2*sin(6284*0.2 + pi/4))

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#$$y(t) = 2sin(6284t + \frac{\pi}{4}\text{rads})$$
#Sketch the sine wave, clearly labelling each axis with appropriate units.

amplitude = 1
f = 1_000
phi = pi/4
t = np.linspace(0, 0.01, 1000)

y = amplitude * sin(2*pi*f*t + phi)

plt.figure()
plt.plot(t*1_000, y)
plt.title('Sine wave: y(t) = 2sin(6284t + \frac{pi}{4}\text{rads})')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude (V)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(-2.5, 2.5)
plt.xlim(0, 2/ f*1_000)
plt.show()
