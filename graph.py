import matplotlib.pyplot as plt

def f(x):
    return -x**2 + 4*x + 6

# x values
x = [i * 0.1 for i in range(201)]

# y values
y = [f(i) for i in x]

# Plot graph
plt.plot(x, y)

# Maximum point
x_max = 2
y_max = f(x_max)

plt.scatter(x_max, y_max, s=60)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graph of f(x) = -x² + 4x + 6")
plt.grid(True)

plt.show()