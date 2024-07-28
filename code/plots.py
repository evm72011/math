import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_theme()


p1 = lambda x: (x**4 + x**2 + 10*x) / 50

#p2 = lambda x: (x**6 + 1) / (x**3 * (x + 1) * (x**2 - x + 1))

x = np.linspace(-5, 5, 100)
fig, axs = plt.subplots(1, 2)
axs[0].plot(x, p1(x))
#axs[1].plot(x, p2(x))
plt.show()


