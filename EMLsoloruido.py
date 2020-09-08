import numpy as np
from scipy import constants
import matplotlib.pyplot as plt

np.random.seed(1234)
N = 2. ** 6  # increments


dt = 0.05
# Euler Maruyama Approximation Langevin -> EML
def EML(So, M, n, Tb, E, p, sigma0, T=10):
    beta_2 = (constants.e*E/(n*Tb*constants.Boltzmann))
    beta_2 *= beta_2
    beta_2 *= (M/(6*constants.m_e))
    res = [So] #Solucion para cada punto
    x = So
    for _ in range(int(T/dt)): # Veces que corre el programa.
        sigma = sigma0/(x**p)
        B = x*sigma + beta_2/(x*sigma)
        Bprima = ((1-p)*sigma0)/(x**p) + (beta_2*(p-1)*x**(p-2))/sigma0
        A = Bprima - 2*sigma*x**2 + 2*B/x
        D = 2*B
        x = x + A*dt + (D*dt)**0.5 * np.random.normal()
        res.append(x)
    return res

Xs = []

# A continuación, introducir dentro de EML() los argumentos. Para sigma0, escoger un valor con un orden de magnitud
# típico. Introducir valores de T y n_e de alguna fuente, según convenga; o bien introducir valores típicos.
# También es necesario introducir E, cuyo orden de magnitud influirá notablemente en el rango que cubre el eje de abscisas.


for _ in range(10000):
    X = EML(1,constants.m_p,3.28*(10**17),1334575,20000000,2,7*10**(-16))
    plt.plot(X, alpha=0.5) # X son las trayectorias estocásticas. Alpha es la intensidad con la que se ven en la gráfica.


plt.title('STOCHASTIC TRAJECTORIES')
plt.xlabel('TIME (s)')
plt.ylabel('FLUCTUATIONS REGARDING THE ORIGIN')

plt.show()

