# Задача 1: Четность числа
num = int(input("Введите число: "))
print("Четное" if num % 2 == 0 else "Нечетное")

# Задача 2: Наибольшее из двух чисел
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("Наибольшее:", max(a, b))

# Задача 3: Проверка возраста для прав
age = int(input("Введите ваш возраст: "))
print("Можно получить права" if age >= 18 else "Нельзя получить права")