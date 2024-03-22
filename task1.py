from pulp import *

# Створення моделі
model = LpProblem("Maximize_Production", LpMaximize)

# Змінні
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Функція цілі: максимізувати загальну кількість продукції
model += lemonade + fruit_juice

# Обмеження
model += 2*lemonade + 1*fruit_juice <= 100, "ліміт води"
model += 1*lemonade <= 50, "ліміт цукру"
model += 1*lemonade <= 30, "ліміт лимонного соку"
model += 2*fruit_juice <= 40, "ліміт фруктового пюре"

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Production plan:")
print("Lemonade:", lemonade.varValue)
print("Fruit Juice:", fruit_juice.varValue)
