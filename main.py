import csv
import math, itertools, functools
from itertools import product, islice, chain, cycle, repeat, tee
import random
from mimesis import Generic, Person, Address
from mimesis.enums import Gender, Locale
from mimesis.builtins import RussiaSpecProvider
from provider import BelarusSpecProvider
import time
import sys


def get_error(persons, full_errors, locale):
    full_errors = math.floor(full_errors) if random.random() < full_errors % 1 else math.ceil(full_errors)
    iter_index = cycle(range(6 if locale == 'by' else 8 if locale == 'ru' else 7))
    i3 = 0
    for i, p in enumerate(cycle(persons)):
        if (i >= full_errors):
            break
        i2 = next(iter_index)
        i3 = i3 + 1 if len(p[i2]) < i3 else 0
        if locale == "by":
            if i2 in (0, 1, 2):
                p[i2] = p[i2][:i3] + "'" + p[i2][i3:]
            elif i2 in (3, 4):
                p[i2] = p[i2] + "0000"
            else:
                p[i2] = '+573' + p[i2][4:]
        elif locale == "ru":
            if i2 in (0, 1, 2, 3, 4):
                p[i2] = p[i2][:i3] + 'Ъ' + p[i2][i3:]
            elif i2 in (5, 6):
                p[i2] = p[i2] + "0000"
            else:
                p[i2] = '+0' + p[i2][2:]
        elif locale == "en":
            if i2 in (0, 1, 2, 3):
                p[i2] = p[i2][:i3] + 'Q' + p[i2][i3:]
            elif i2 in (4, 5):
                p[i2] = p[i2] + "0000"
            else:
                p[i2] = p[i2] + "9999"


def RU(count, full_errors):
    generic = Generic(locale=Locale.RU)
    generic.add_provider(RussiaSpecProvider)
    persons = [[generic.person.full_name(), generic.russia_provider.patronymic(), generic.address.city(),
                generic.address.street_suffix(), generic.address.street_name(), generic.address.street_number(),
                str(generic.numeric.integer_number(start=1, end=100)), generic.person.telephone()] for _ in range(count)]

    get_error(persons, full_errors, 'ru')

    result = [("{} {}; г.{}, {} {}, {}, {}; {}".format(*p)) for p in persons]
    return result


def EN(count, full_errors):
    generic = Generic(locale=Locale.EN)
    persons = [[generic.person.full_name(), generic.address.city(),
                generic.address.street_suffix(), generic.address.street_name(), generic.address.street_number(),
                str(generic.numeric.integer_number(start=1, end=100)), generic.person.telephone()] for _ in range(count)]

    get_error(persons, full_errors, 'en')

    result = [("{}; г.{}, {} {}, {}, {}; {}".format(*p)) for p in persons]
    return result


def BY(count, full_errors):
    generic = Generic()
    generic.add_provider(BelarusSpecProvider)
    # generic.be.set_gender(Gender.FEMALE)
    persons = [[generic.be.full_name(), generic.be.city_name(),
                generic.be.street_name(), generic.be.houses_number(), generic.be.house_apartment(),
                generic.be.telephone()] for _ in range(count)]

    get_error(persons, full_errors, 'by')

    result = [("{}; г.{}, {}, {}, {}; {}".format(*p)) for p in persons]
    return result


if __name__ == "__main__":
    #count, region, errors = 5, "BY", 0
    count, region, errors = int(sys.argv[1]), sys.argv[2], float(sys.argv[3])
    full_errors = errors * count
    #start_time = time.monotonic()
    if region == "be_BY":
        combinations = BY(count, full_errors)
    elif region == "ru_RU":
        combinations = RU(count, full_errors)
    elif region == "en_US":
        combinations = EN(count, full_errors)
    else:
        combinations = EN(count, full_errors)

    #print("time: ", time.monotonic() - start_time)
    #print(len(combinations))
    print(*combinations, sep="\n")
