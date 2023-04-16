import numpy as np
import matplotlib.pyplot as plt

# Question 1 - Band gap as a Function of Temperature


T = np.linspace(0, 1000)


def energy(alpha, beta, eg0):
    return eg0 - (alpha * T ** 2)/(T + beta)


def plot_energy(func, title):
    plt.plot(T, func, 'blue')
    plt.title(title)
    plt.xlabel("T[K]")
    plt.ylabel("Eg[eV]")
    plt.show()


# Menu with user input to all materials
def menu():
    choice = -1
    while choice:
        print("Please choose material for Eg:\n1. Si\n2. GaAs.\n3. Other\nPress 0 to exit")
        choice = int(input())
        if choice not in [0, 1, 2, 3]:
            print("Wrong choice!\n")
            continue
            # Si
        if choice == 1:
            beta = 636
            alpha = 4.73e-4
            eg0 = 1.17
            si_energy = energy(alpha, beta, eg0)
            plot_energy(si_energy, r'Si Band Gap as a function of $T^2$:')

        if choice == 2:
            beta = 204
            alpha = 5.405e-4
            eg0 = 1.519
            galium_energy = energy(alpha, beta, eg0)
            plot_energy(galium_energy, r'GaAs Band Gap as a function of $T^2$:')

        if choice == 3:
            print("Enter beta coefficient:")
            beta = int(input())
            print("Enter alpha coefficient:")
            alpha = float(input())
            print("Enter Eg0 coefficient:")
            eg0 = float(input())
            material_energy = energy(alpha, beta, eg0)
            plot_energy(material_energy, r' Band Gap as a function of $T^2$:')
    return


menu()



