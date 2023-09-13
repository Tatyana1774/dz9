# 2) Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.

from random import randint
import csv


def csv_decorator(func: callable):
    data = []

    def wrapper():
        result = func()
        for item in result:
            data.append({"name": item})

        with open("ex_2.csv", "w", newline='') as file:
            fieldnames = ["name"]
            csv_file = csv.DictWriter(file, fieldnames=fieldnames)

            csv_file.writeheader()
            csv_file.writerows(data)
    return wrapper


@csv_decorator
def random_numbers():
    num_list = []
    for _ in range(5, randint(5, 50)):
        num_list.append(randint(100, 1000))
    return num_list


random_numbers()