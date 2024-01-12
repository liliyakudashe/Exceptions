import warnings


def divide(a, b):
    if abs(b) < 0.01:
        warnings.warn("Опасность деления на ноль", UserWarning)
    return a / b


warnings.simplefilter("always")
print(divide(10, 0.001))

warnings.simplefilter("ignore")
print(divide(10, 0.001))

warnings.simplefilter("error")
try:
    print(divide(10, 0.001))
except UserWarning as e:
    print("Ошибка: {}".format(str(e)))
