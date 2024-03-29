# Anatoli Gutovski
# Date: 20/02/2024
# Description: Homework 2
# Grodno IT Academy Python 3.11.7

# Объяснение работы с функциями:
# формат определения функции (то есть: мы ее создаем) - def func(arg1, arg2, arg3)
# arg1, arg2, arg3 - это аргументы, которые передаются в функцию при ее вызове (то есть, мы ее запускаем)

# оценивается: чистота кода, наличие комментариев (PEP8), прохождение всех тестов
# нельзя менять названия функций/файлов/входные данные. Можно менять решение, менять/добавлять return.

# пример названия репозитория для гитхаба: kazukevich_homework2
# добавьте в репозиторий с домашним задание файл readme.md с датой сдачи, фамилией и именем выполнившего и кратким
# описанием каждой задачи (коротко, что использовали, алгоритм функции), оформленным в стиле markdown


# Напишите программу, ĸоторая считает общую цену.
# Вводится m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
# Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
# Уточнение:
# Используйте функцию return чтобы ответ был в рублях и копейках.
# Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"

# * Для одного из тестов нужно применять какую-то библиотеку =)

import math


def common_price(m, n, s, l):
    # Проверка на отрицательные значения
    if m < 0 or n < 0 or s < 0 or l < 0:
        return False

    # Вычисляем общую стоимость
    obj_stoim = l * k / s

    # Разделяем на рубли и копейки
    a = obj_stoim // 100
    z = obj_stoim % 100
    v = round(z, 2)    # Округляем до 2 знаков после запятой

    # Возвращаем результат в виде строки
    return "Общая цена составляет " + str(a) + " рублей и " + str(v) + " копеек за " + str(l) + " товаров"


# Пример использования:
m = int(input("Введите количество рублей: "))
n = int(input("Введите количество копеек: "))
k = m + n / 100  # оъединение рублей и копеек в 1 переменную
s = int(input("Введите количество товара: "))
l = int(input("Введите количество единиц товара: "))
result = common_price(m, n, s, l)
print(result)


# Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если нет, вывести False.
# Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.


def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        print("Это не треугольник, так как одна из сторон больше либо равна сумме двух других сторон.")
        return False


def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 4)


a = float(input("Введите длину первой стороны треугольника: "))
b = float(input("Введите длину второй стороны треугольника: "))
c = float(input("Введите длину третьей стороны треугольника: "))

if triangle(a, b, c):
    area = calculate_triangle_area(a, b, c)
    print(area)


# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении могут быть знаки препинания.
# Пример: если введено "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"


def longest_word(sentence):
    vse_slova = sentence.split()  # Разбиваем предложение на слова
    max_dlin_slovo = max(vse_slova, key=len)  # Находим самое длинное слово
    return max_dlin_slovo


sentence = input("Введите предложение: ")
max_dlin_slovo = longest_word(sentence)
print(f"Самое длинное слово в предложении: {max_dlin_slovo}")


# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".


def uniques(repeating_string):
    repeating_string = repeating_string.replace(
        " ", "")   # Удаляем все пробелы из строки
    unique_chars = ""
    for char in repeating_string:        # Пройдемся по каждому символу
        if char not in unique_chars:
            unique_chars += char
    return unique_chars


input_string = input("Введите строку: ")
result = uniques(input_string)
print(result)


# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.


def count_string_capitalization(mixed_string):
    # Cоздадим переменные для подсчета количества строчных и прописных букв
    lowercase_count = 0
    uppercase_count = 0

    # Пройдемся по каждому символу в строке
    for char in mixed_string:
        # Проверяем, является ли символ строчной буквой
        if char.islower():
            lowercase_count += 1
        # Проверяем, является ли символ прописной буквой
        elif char.isupper():
            uppercase_count += 1

    # Возвращаем количество строчных и прописных букв в виде кортежа
    return (lowercase_count, uppercase_count)


# Пример использования функции
input_string = input("Введите строку: ")
result = count_string_capitalization(input_string)
print("Количество строчных букв:", result[0])
print("Количество прописных букв:", result[1])
