import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1.51, 50, 10000) # x tomará valores desde 1.51 (para 1.5 nos dará error
# por estar dividiendo entre cero, aunque mostrará la gráfica) hasta 50. Por debajo de 1.5 habrá  soluciones complejas.
y = ((x-0.5)/(x-1.5))**0.5

# Dibujamos la asíntota vertical:

fig, ax = plt.subplots()
ax.plot(x, y)
ax.axvline(x=1.5, ymin=0.0, ymax=6.0, color='r', linestyle='--')

# Representamos:

plt.plot(x, y, label = "line 1", color='b')

# Nos aseguramos de que la función corte a los ejes:

plt.axis(xmin=0.5,xmax=15,ymin=0,ymax=5)

# Nombramos el eje x

plt.xlabel('$\u03BA$', fontsize=15)

# Nombramos el eje y

plt.ylabel('$\\frac{\u03C9_{P\u03BA}}{\u03C9_P}$', fontsize=16) # \u208 para números, y \u209 para letras

# Le ponemos título a la gráfica, si queremos:

#plt.title('Two lines on same graph!')

# Le ponemos la malla para que se vea mejor.

plt.grid(True)

plt.savefig('FrecuenciaPlasma.png', format='png', dpi=1200)

plt.show()

# Códigos para letras griegas aquí: https://www.compart.com/en/unicode/block/U+0370