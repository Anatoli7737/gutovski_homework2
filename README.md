## 1 задание ДЗ

Anatoli Gutovski
Date: 20/02/2024

Условие: напишите программу, ĸоторая считает общую цену.
Вводится m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
Уточнение:
Используйте функцию return чтобы ответ был в рублях и копейках.
Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"

* Для одного из тестов нужно применять какую-то библиотеку =)

Пояснение: функция common_price(m, n, s, l) принимает на вход количество рублей m, количество копеек n, количество товара s и количество единиц товара l. Внутри функции вычисляется общая стоимость за все товары. Затем общая цена переводится обратно в рубли и копейки. Далее производим округление копеек до 2 знаков после запятой. Функция возвращает строку с информацией об общей цене за указанное количество товаров. Пользователю предлагается ввести количество рублей, копеек, товара и количество единиц товара. Программа выводит общую цену за указанное количество товаров в рублях и копейках.


## 2 задание ДЗ

Условие: даны: три стороны треугольника.
Требуется: проверить, действительно ли это стороны треугольника.
Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
Если нет, вывести False.
Бонусом - с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.

Пояснение: программа начинается с импорта модуля math, который понадобится для вычисления квадратного корня. Функция triangle(a, b, c) проверяет, являются ли заданные стороны треугольником. Если условие для образования треугольника выполняется, функция возвращает True, иначе выводит сообщение об ошибке и возвращает False. Пользователю предлагается ввести длины трех сторон треугольника. Если стороны образуют треугольник, программа вычисляет площадь и выводит её на экран.


## 3 задание ДЗ

Условие: найти самое длинное слово в введенном предложении. Учтите что в предложении могут быть знаки препинания. Пример: если введено "This is a sample sentence where the longest word is in the middle!", то надо вернуть "sentence".

Пояснение: этот код просто разбивает введенное предложение на слова с помощью метода split(), а затем находит самое длинное слово с помощью функции max() с параметром key=len. Знаки препинания в этом случае не учитываются, так как они не влияют на длину слова.


## 4 задание ДЗ

Условие: вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы. Например, если было введено "abc cde def", то должно быть выведено "abcdef".

Пояснение: в данной задаче функция uniques() принимает введенную строку, удаляет из нее все пробелы и затем проходится по каждому символу. Если символ еще не встречался в строке unique_chars, то он добавляется к ней. Таким образом, после завершения цикла в unique_chars останутся только уникальные символы. После выполнения кода программа попросит ввести строку, а затем выведет результат без повторяющихся символов и пробелов.


## 5 задание ДЗ

Условие: посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке. Проверка рассчитана только на английские буквы.

Пояснение: в этой функции использовал методы строк islower() и isupper(), которые проверяют, является ли символ строчной или прописной буквой соответственно. Мы также используем цикл for для прохода по каждому символу во введенной строке и увеличиваем счетчики lowercase_count и uppercase_count соответственно. В конце функция возвращает кортеж с количеством строчных и прописных букв.