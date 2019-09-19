#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def H(f):
    C = 1e-9
    R = 1590
    return 1 / (1 + 1j * 2*np.pi * f * C * R)

x = np.logspace(1, 6, num=50, dtype=complex)

plt.plot(x, H(x))
plt.show()