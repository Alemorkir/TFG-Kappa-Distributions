import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1.5, 50, 1000) # x tomará valores desde 1.5 hasta 50. Por debajo de 1.5 habrá  soluciones complejas.
y = ((x-1.5)/(x-0.5))**0.5

# Representamos:

plt.plot(x, y, label = "line 1")

# Nos aseguramos de que la función corte a los ejes:

plt.axis(xmin=0,xmax=40,ymin=-0.05,ymax=1)

# Nombramos el eje x

plt.xlabel('$\u03BA$', fontsize=17)

# Nombramos el eje y

plt.ylabel('$\\frac{\u03BB_\u03BA}{\u03BB_D}$', fontsize=16) # \u208 para números, y \u209 para letras

# Le ponemos título a la gráfica, si queremos:

#plt.title('Two lines on same graph!')

# Le ponemos la malla para que se vea mejor.

plt.grid(True)

# Marcamos el punto correspondiente a k = 1.5

plt.scatter(1.5, 0, marker='x', s=50, c='red',alpha=1)

plt.savefig('LongitudDebye.png', format='png', dpi=1200)

plt.show()