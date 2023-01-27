"""
Задание 3. Создать список и заполнить его элементами различных типов данных.
Реализовать проверку типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

Пример:
для списка [5, "string", 0.15, True, None]
результат

<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
<class 'NoneType'>
"""

my_str = [False, 3.25, None, "list", 9]
print(type(my_str[0]))
print(type(my_str[1]))
print(type(my_str[2]))
print(type(my_str[3]))
print(type(my_str[4]))