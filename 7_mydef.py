# Задача 1: Сумма двух чисел
def add(a, b):
    return a + b

print("Сумма 5 и 3:", add(5, 3))

# Задача 2: Проверка на простое число
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("7 простое?", is_prime(7))

# Задача 3: Среднее значение
def average(lst):
    return sum(lst) / len(lst)

numbers = [2, 4, 6, 8]
print("Среднее:", average(numbers))