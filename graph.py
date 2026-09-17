import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 10*np.sin(x) + 0.5*x

x = np.linspace(0, 20, 500)

plt.plot(x, f(x))

x_max = 1.6
plt.scatter(x_max, f(x_max), s=60)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Hill Climbing Graph")
plt.grid(True)
plt.show()