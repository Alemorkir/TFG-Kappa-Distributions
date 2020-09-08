# Used to describe the equilibrium distributions of particles.


import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

maxwell = stats.maxwell
data = maxwell.rvs(loc=0, scale=50, size=100000)

params = maxwell.fit(data, floc=0)
print(params)
# (0, 4.9808603062591041)

plt.hist(data, bins=40, normed=True)
x = np.linspace(0, 250)
plt.plot(x, maxwell.pdf(x, *params), lw=3, color='r')

# Ponemos la malla:
plt.grid(True)

# Nombramos el eje x:
plt.xlabel('v', fontsize=13)

# Nombramos el eje y
plt.ylabel('${f    (v)}$', fontsize=15)


plt.show()
