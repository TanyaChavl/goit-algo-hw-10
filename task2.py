import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()

# Використання методу Монте-Карло для обчислення інтеграла
N = 100000  # Кількість точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)
below = y_random < f(x_random)
above = np.invert(below)

# Обчислення інтеграла
integral_MC = below.sum() / N * (b - a) * f(b)

# Обчислення точного значення інтеграла
integral_exact, _ = quad(f, a, b)

# Відключила зображення графіка щоб вивести результати обчислень в консоль
#plt.show(),
print(f"Значення інтеграла, обчислене за допомогою методу Монте-Карло: {integral_MC}")
print(f"Точне значення інтеграла, обчислене за допомогою функції quad{integral_exact}")
