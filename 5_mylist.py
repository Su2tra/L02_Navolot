# Задача 1: Сумма списка
numbers = [1, 2, 3, 4, 5]
print("Сумма:", sum(numbers))

# Задача 2: Максимальное число
numbers = [3, 5, 1, 7, 2]
print("Максимум:", max(numbers))

# Задача 3: Удаление дубликатов
def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

numbers = [1, 2, 2, 3, 4, 4, 5]
print("Без дубликатов:", remove_duplicates(numbers))