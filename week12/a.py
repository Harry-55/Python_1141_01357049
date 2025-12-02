import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    return np.exp(-x**2)

x = np.linspace(-1, 3, 100)
y = f(x)
plt.plot(x, y, color="blue")

x_fill = np.linspace(0, 2, 300)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, color="orange", label="Integral region 0 ≤ x ≤ 2")

I, _ = integrate.quad(f, 0, 2)

plt.text(1, 0.6,
         r"$\int_0^2 e^{-x^2}\, dx = $" + f"{I:.6f}",
         fontsize=16, color="darkred")


plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()

print("Definite integral of f(x) from 0 to 2 =", I)
