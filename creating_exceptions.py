class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def generate_exception(data):
    if isinstance(data, str):
        raise InvalidDataException("Неверный тип данных")
    elif isinstance(data, int):
        raise ProcessingException("Ошибка обработки данных")
    else:
        raise Exception("Неизвестная ошибка")


def process_data(data):
    try:
        generate_exception(data)
    except InvalidDataException as e:
        print(f"Ошибка: {(str(e))}")
    except ProcessingException as e:
        print(f"Ошибка обработки данных: {(str(e))}")
    except Exception as e:
        print(f"Неизвестная ошибка: {(str(e))}")
    else:
        print("Данные успешно обработаны")


data1 = "test"
data2 = 10

process_data(data1)
process_data(data2)
