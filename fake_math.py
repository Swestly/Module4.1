# В модуле fake_math создаем функцию divide, которая принимает два параметра first и second
def divide(first, second):
    if second != 0:
        return first / second
    if second == 0:
        return 'Ошибка'