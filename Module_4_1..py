from fake_math import divide as fake_divide  # Импорт функции divide из модуля fake_math
from true_math import divide as true_divide  # Импорт функции divide из модуля true_math

# Передача аргументов аргументов, первый произвольное число != 0, второй == 0
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

# Вывод результатов вызовов функций на экран (в консоль)
print(result1)
print(result2)
print(result3)
print(result4)