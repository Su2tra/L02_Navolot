# Задача 1: Обработка ввода числа
try:
    num = float(input("Введите число: "))
except ValueError:
    print("Ошибка: введено не число")

# Задача 2: Обработка открытия файла
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Файл не найден")