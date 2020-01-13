import csv
import itertools
from itertools import product, islice, chain
import random


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    ar = list(reader)[1:]
    ar = list(zip(*ar))[0]
    return ar


def RU(count):
    with open("DATA/M_name1.txt", "r", encoding='utf-8') as f_obj:
        name1 = csv_reader(f_obj)
    with open("DATA/M_name2.txt", "r", encoding='utf-8') as f_obj:
        name2 = csv_reader(f_obj)
    with open("DATA/M_name3.txt", "r", encoding='utf-8') as f_obj:
        name3 = csv_reader(f_obj)
    with open("DATA/BY_city.csv", "r", encoding='utf-8') as f_obj:
        city = csv_reader(f_obj)
    with open("DATA/street.csv", "r", encoding='utf-8') as f_obj:
        street = csv_reader(f_obj)
    houses = list(range(1, 101))

    print(len(name1), len(name2), len(name3), len(city), len(street))
    #print(len(name1) * len(name2) * len(name3) * len(city) * len(street))

    combinations = list(islice(product(name1, name2, name3), 1000000))
    combinations = list(random.sample(combinations, count))
    combinations2 = list(islice(product(city, street, houses), 1000000))
    combinations2 = list(random.sample(combinations2, count))

    result = list(zip(combinations, combinations2))
    result = [list(chain.from_iterable(d)) for d in result]
    #random.shuffle(combinations)
    return result


if __name__ == "__main__":
    count, region, errors = 50, "BY", 0

    combinations = RU(count)
    print(len(combinations))
    print(*combinations, sep="\n")