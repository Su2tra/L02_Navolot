# Задача 1: Сумма двух чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
print("Сумма:", num1 + num2)

# Задача 2: Преобразование строки в целое число
number_str = input("Введите число: ")
number_int = int(number_str)
print("Тип данных:", type(number_int))

# Задача 3: Возраст пользователя
age = int(input("Введите ваш возраст: "))
if age <= 4:
    print(f"Вам {age} года.")
else:
    print(f"Вам {age} лет.")