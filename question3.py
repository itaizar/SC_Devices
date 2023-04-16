import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as const
from sklearn import datasets
import sympy as sp

k = const.Boltzmann * 6.25e18
def calc_energy():

    temperature = [1/(15+273), 1/(30+273), 1/(80+273), 1/(110+273), 1/(125+273), 1/(160+273), 1/(175+273), 1/(195+273)]
    resistance = [7180, 3170, 345, 120, 75, 28.5, 20, 12.5]
    resistance = [sp.ln(r) for r in resistance]
    plt.plot(temperature, resistance)
    a = (resistance[3] - resistance[1])/(temperature[3] - temperature[1])
    slope = (resistance[3] - resistance[1])/(temperature[3] - temperature[1])
    print(slope)
    e_g = -slope*2*k/(sp.ln(1100/(sp.sqrt(2.09e37))))
    print(e_g)


calc_energy()


