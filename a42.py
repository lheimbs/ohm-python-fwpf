#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def H(f):
    C = 1e-9
    R = 1590
    return 1 / (1 + 1j * 2*np.pi * f * C * R)

x = np.logspace(1, 7, num=50, dtype=complex)

plt.subplot(211)
plt.plot(x, H(x))
plt.subplot(212)
plt.plot(x, 20*np.log10(abs(H(x))))
plt.show()