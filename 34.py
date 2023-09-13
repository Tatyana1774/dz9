# 3) Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# 4) Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import json


def json_roots(func: callable):
    data = {}

    def wrapper(a, b, c):
        data_list = func(a, b, c)
        for item in data_list:
            for key, value in item.items():
                data[key] = value
        with open("ex_4.json", "w") as j_file:
            json.dump(data, j_file, indent=4)
        return data_list
    return wrapper


def csv_roots(func: callable):
    with open("ex_2.csv", "r", newline="") as c_file:
        csv_file = c_file.read().split()[1:]
    result_list = []

    def wrapper(a, b, c):
        for item in csv_file:
            a, b, c = list(map(int, item))
            result = {item: func(a, b, c)}
            result_list.append(result)
        return result_list
    return wrapper


@json_roots
@csv_roots
def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        x = (-b) / (2 * a)
        return round(x, 3)
    if discriminant < 0:
        return ()
    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return round(x1, 3), round(x2, 3)


result = roots(9, 6, 1)
for i in result:
    print(i)