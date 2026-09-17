import numpy as np
import matplotlib.pyplot as plt
import random

# Function
def f(x):
    return 10 * np.sin(x) + 0.5 * x


def hill_climbing(x):

    step = 0.1

    while True:

        x_left = x - step
        x_right = x + step

        if x_left < 0:
            x_left = x

        if x_right > 20:
            x_right = x


        if f(x_left) > f(x):
            x = x_left

        elif f(x_right) > f(x):
            x = x_right

        else:
            break

    return x

results = []

for i in range(10):

    x0 = random.uniform(0, 20)

    x_max = hill_climbing(x0)

    results.append((x0, x_max, f(x_max)))

    print("Initial x =", round(x0, 2),
          "Maximum x =", round(x_max, 2),
          "f(x) =", round(f(x_max), 4))



best = max(results, key=lambda x: x[2])

print("\nGlobal Maximum:")
print("x =", round(best[1], 2))
print("f(x) =", round(best[2], 4))




x = np.linspace(0, 20, 500)

plt.plot(x, f(x))


for result in results:
    plt.scatter(result[1], result[2], s=50)

# Mark best result
plt.scatter(best[1], best[2], s=100)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Hill Climbing with 10 Random Initial Values")
plt.grid(True)
plt.show()