# -*- coding: utf-8 -*-

"""Specific data provider for Russia (ru)."""

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.typing import Seed
import random, csv
from itertools import product, islice, chain, cycle, repeat, tee

__all__ = ['BelarusSpecProvider']


def csv_reader(file_path):
    with open(file_path, "r", encoding='utf-8') as f_obj:
        reader = csv.reader(f_obj)
        ar = list(reader)[1:]
        ar = list(list(zip(*ar))[0])
        random.shuffle(ar)
        return ar


class BelarusSpecProvider(BaseSpecProvider):
    """Class that provides special data for Russia (ru)."""

    def __init__(self, seed: Seed = None):
        """Initialize attributes."""
        super().__init__(seed=seed)
        self.pull(self._datafile)
        self.gender = None

        self.m_name1 = csv_reader("DATA/M_name1.txt")
        self.m_name2 = csv_reader("DATA/M_name2.txt")
        self.m_name3 = csv_reader("DATA/M_name3.txt")
        self.w_name1 = csv_reader("DATA/W_name1.txt")
        self.w_name2 = csv_reader("DATA/W_name2.txt")
        self.w_name3 = csv_reader("DATA/W_name3.txt")
        self.city = csv_reader("DATA/BY_city.csv")
        self.street = csv_reader("DATA/street.csv")
        # houses = lambda: random.randrange(1, 101, 1)
        self.houses = list(range(1, 101))
        self.apartment_numbers = list(range(1, 200))

        random.shuffle(self.houses)
        random.shuffle(self.apartment_numbers)

        #a1 = lambda: random.choice((29, 33, 44))
        #a2 = lambda: random.randint(100, 1000)
        #a3 = lambda: random.randint(1000, 10000)
        #self.gen_telephone = lambda: "+375-({})-{}-{}".format(a1(), a2(), a3())
        a = list(range(10))
        a2 = list(range(5,10))
        self.iter_gen_phone = cycle(product(a2, a2, a2, a, a, a, a))
        self.get_code_operator = cycle((29, 33, 44))

        self.iter_m_name1 = cycle(self.m_name1)
        self.iter_m_name2 = cycle(self.m_name2)
        self.iter_m_name3 = cycle(self.m_name3)
        self.iter_w_name1 = cycle(self.w_name1)
        self.iter_w_name2 = cycle(self.w_name2)
        self.iter_w_name3 = cycle(self.w_name3)
        self.iter_city = cycle(self.city)
        self.iter_street = cycle(self.street)
        self.iter_houses = cycle(self.houses)
        self.iter_apartment_numbers = cycle(self.apartment_numbers)

    class Meta:
        """The name of the provider."""
        name = 'be'

    def first_name(self):
        if self.get_bool():
            return next(self.iter_m_name1)
        else:
            return next(self.iter_w_name1)

    def last_name(self):
        if self.get_bool():
            return next(self.iter_m_name2)
        else:
            return next(self.iter_w_name2)

    def patronymic(self):
        if self.get_bool():
            return next(self.iter_m_name3)
        else:
            return next(self.iter_w_name3)

    def full_name(self):
        if self.get_bool():
            return "%s %s %s" % (next(self.iter_m_name1), next(self.iter_m_name2), next(self.iter_m_name3))
        else:
            return "%s %s %s" % (next(self.iter_w_name1), next(self.iter_w_name2), next(self.iter_w_name3))

    def city_name(self):
        return next(self.iter_city)

    def street_name(self):
        return next(self.iter_street)

    def houses_number(self):
        return str(next(self.iter_houses))

    def house_apartment(self):
        return str(next(self.iter_apartment_numbers))

    def telephone(self):
        return self.gen_telephone()

    def gen_telephone(self):
        ar = next(self.iter_gen_phone)
        return "+375-({})-{}{}{}-{}{}{}{}".format(next(self.get_code_operator),
                                                  ar[0], ar[1], ar[2], ar[3], ar[4], ar[5], ar[6])

    def get_bool(self):
        return self.gender and self.gender == Gender.MALE or not self.gender and bool(random.getrandbits(1))

    def set_gender(self, gender: Gender):
        self.gender = gender
