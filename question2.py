# Itai Zaretsky 205946114

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as const
import sympy as sp

# Question 2 - Si intrinsic concentration
eg_si = 1.12
ni_ge = 2.5e13
nc_si_300k = 2.82e19
nv_si_300k = 1.05e19
k = const.Boltzmann * 6.25e18
T = sp.Symbol('T')

for T in range(300, 490):
    nc_si = nc_si_300k * (T/300)**(3/2)
    nv_si = nv_si_300k * (T/300)**(3/2)
    n = sp.sqrt(nc_si * nv_si) * sp.exp(-eg_si/(2 * k * T))
    T += 1
    if ni_ge <= n:
        break

print("The temperature in which the Si intrinsic concentration will be the same as Ge is:\n", T, "[K]")




