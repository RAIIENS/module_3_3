# Создайте функцию print_params(a = 1, b = 'строка', c = True),
# которая принимает три параметра со значениями по умолчанию
# (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.
# Создаём функцию print_params
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)
print_params(c=[1,2,3])
print_params()
# Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
values_list = ['Оля', 77, [555, 777, 999]]
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам
# функции print_params, и значениями разных типов.
values_dict = {'a': [555, 777, 999], 'b': 'Оля', 'c': 77}
# Передайте values_list и values_dict в функцию print_params, используя распаковку
# параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
# Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
# Исходный код:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
# Вывод на консоль:
# 54.32 'Строка' 42
# Проверьте, работает ли print_params(*values_list_2, 42)
