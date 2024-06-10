
'''''
 'Списки  списках, кортежи, словари, множества, строки'  
'''''

from random import sample
def print_nested_elements(nested_list):
    for element in nested_list:
        if isinstance(element, list):  # Проверяем, является ли элемент списком
            print("List:", end=" ")
            for sub_element in element:
                print(sub_element, end=" ")
            print()  # Переходим на новую строку после вывода списка
        elif isinstance(element, tuple):  # Проверяем, является ли элемент кортежем
            print("Tuple:", end=" ")
            for sub_element in element:
                print(sub_element, end=" ")
            print()  # Переходим на новую строку после вывода кортежа
        elif isinstance(element, dict):  # Проверяем, является ли элемент словарем
            print("Dictionary:", end=" ")
            for key, value in element.items():
                print(f"{key}: {value}, ", end="")
            print()  # Переходим на новую строку после вывода словаря
        elif isinstance(element, set):  # Проверяем, является ли элемент множеством
            print("Set:", end=" ")
            for item in element:
                print(item, end=" ")
            print()  # Переходим на новую строку после вывода множества
        else:
            print(element, end=" ")  # Если элемент не является ни одним из вышеперечисленных типов, просто выводим его
    print()  # Переходим на новую строку после вывода всех вложенных элементов

# Пример использования функции:
nested_list = [
    ["apple", "banana"],
    ("kiwi", "melon"),
    {"name": "John", "age": 30},
    {"hobbies": {"sports": "football", "arts": "painting"}},
    {"fruits": {"apple", "banana", "kiwi"}},
    {"vegetables": {"carrot", "potato", "tomato"}},
]

print_nested_elements(nested_list)