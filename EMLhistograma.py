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


# Valores recomandados de n, Tb y E para cada caso, con p=2 y sigma0 = 7*10**(-16):

# Corona solar: 1*(10**15),1*(10**7),1*(10**8.5)
# Viento Solar: 1*(10**6),69630,1*(10**-2.8)
# Magnetosfera: 1*(10**6),580250,1*(10**-2)
# Tokamak: 1*(10**20),34815000,1*(10**14)



for _ in range(10000):
    X = EML(1,constants.m_p,1*(10**6),580250,1*(10**-2),2,7*10**(-16))
    Xs += X



#5,constants.m_p,6,1*(10**18),34815000,20000000,1,7*10**(-16)


plt.hist(Xs, bins=100, color = 'blue', edgecolor = 'black', normed=True) # Hacemos que las trayectorias se muestren como un histograma de 100 barras, normalizando por el total.
plt.grid(True)
plt.title('Solar Wind', fontsize=15)
plt.xlabel('Density', fontsize=15)
plt.ylabel('Populations', fontsize=15)
plt.axis(xmax=6)


plt.show()

# Si quiero poner un recuadro con información:
# https://matplotlib.org/3.1.0/gallery/recipes/placing_text_boxes.html#sphx-glr-gallery-recipes-placing-text-boxes-py