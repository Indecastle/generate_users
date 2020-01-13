import csv, re, random, requests
from bs4 import BeautifulSoup as BS


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    ar = list(reader)[1:]
    ar = list(zip(*ar))[0]
    return ar


def csv_writer(data, path):
    with open(path, "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


def regex_street(data):
    newData = []
    for street in data:
        newData.append([re.sub(r"(.+) (пер\.|ул\.|бульвар|площадь|проезд)", r"\2 \1", street[0])])
    return newData


def parsing_address_ru():
    address = []
    for i in range(2, 33):
        print(i, end=" ")
        r = requests.get("https://ato.by/streets/letter/" + str(i))
        html = BS(r.content, 'html.parser')
        for el in html.select(".intro > div > ul > li > a"):
            address.append([el.text])

    print("\ncount streets: %d" % len(address))
    address = [["street"]] + regex_street(address)
    csv_writer(address, "DATA/street.csv")



if __name__ == "__main__":
    #parsing_address_ru()
    pass