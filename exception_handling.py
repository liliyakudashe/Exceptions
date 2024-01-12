def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        print("Ошибка: Не удалось преобразовать строку в число")
        return None


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except (FileNotFoundError, IOError):
        print("Ошибка: Не удалось прочитать файл")
        return None


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
        return None
    except TypeError:
        print("Ошибка: Неверный тип данных")
        return None


def access_list_element(lst, index):
    try:
        return lst[index]
    except (IndexError, TypeError):
        print("Ошибка: Не удалось получить элемент списка")
        return None
