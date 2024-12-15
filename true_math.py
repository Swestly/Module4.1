# Импортируем бесконечность из встроенной библиотеки math
from math import inf

def divide(first, second):
    if second != 0:
        return first/second
    if second == 0:
        return inf