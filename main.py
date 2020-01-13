import csv
import itertools
from itertools import product, islice, chain, cycle, repeat, tee
import random


def csv_reader(file_path):
    with open(file_path, "r", encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj)
        ar = list(reader)[1:]
        ar = list(list(zip(*ar))[0])
        random.shuffle(ar)
        return ar


def RU(count):
    name1 = csv_reader("DATA/M_name1.txt")
    name2 = csv_reader("DATA/M_name2.txt")
    name3 = csv_reader("DATA/M_name3.txt")
    city = csv_reader("DATA/BY_city.csv")
    street = csv_reader("DATA/street.csv")
    #houses = lambda: random.randrange(1, 101, 1)
    houses = list(range(1, 101))
    apartment_numbers = list(range(1, 101))

    random.shuffle(city)
    random.shuffle(street)
    random.shuffle(houses)
    random.shuffle(apartment_numbers)

    print(len(name1), len(name2), len(name3), len(city), len(street))
    #print(len(name1) * len(name2) * len(name3) * len(city) * len(street))

    combinations = list(islice(product(name1, name2, name3), 1000000))
    combinations = list(random.sample(combinations, count))
    #combinations2 = list(islice(product(city, street, houses), 1000000))
    #combinations2 = list(random.sample(combinations2, count))

    #result = list(zip(combinations, combinations2))
    #result = [list(chain.from_iterable(d))+[next(iter)] for d in result]
    #result = [f"{' '.join(d[0])}; Беларусь, г.{d[1][0]}, ул.{d[1][1]}, д.{d[1][2]}, кв.{next(iter)}; [number]" for d in result]
    iter_city = cycle(city)
    iter_street = cycle(street)
    iter_houses = cycle(houses)
    iter_apartment_numbers = cycle(apartment_numbers)
    rr = random.randrange(0, 10, 1)
    #number = [ itertools.repeat(rr, 9), itertools.repeat(rr, 9)]
    #iter_number = product(*number)
    result = ["%s; Беларусь, г.%s, %s, д.%s, кв.%s; [number]"
              % (' '.join(d), next(iter_city), next(iter_street), next(iter_houses), next(iter_apartment_numbers)) for d in combinations]
    #random.shuffle(combinations)
    return result


if __name__ == "__main__":
    count, region, errors = 5, "BY", 0

    combinations = RU(count)
    print(len(combinations))
    print(*combinations, sep="\n")