import matplotlib.pyplot as plt
import itertools
import numpy as np

x = np.linspace(0.5, 50, 10000) # x será M
yk = [(((k-0.5)/(k-1.5))-(1/(x**2)))**(-1/2) for k in [2, 2.2, 2.4, 2.6, 2.8, 3]] # Representaremos curvas para 6 valores de k

# Representamos:

colors = itertools.cycle(["b", "g", "r", "y", "m", "k"]) # Especificamos los colores y su orden

for y in yk:
    plt.plot(x, y, color=next(colors))
    plt.legend([2, 2.2, 2.4, 2.6, 2.8, 3], title="\u03BA", fontsize= 'large', title_fontsize="15")

# Nos aseguramos de que la función corte a los ejes:

plt.axis(xmin=0.5,xmax=2.5,ymin=0.5,ymax=2)

# Nombramos el eje x

plt.xlabel('M', fontsize=16)

# Nombramos el eje y

plt.ylabel('W', fontsize=16)

# Le ponemos la malla para que se vea mejor.

plt.grid(True)

plt.savefig('CriterioBohm.png', format='png', dpi=1200)

plt.show()

# Ejemplo para poner colores:
# https://stackoverflow.com/questions/12236566/setting-different-color-for-each-series-in-scatter-plot-on-matplotlib