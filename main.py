from lxml import html
import requests
import os


def flatten_list(lst):
    flat_list = []
    for sublist in lst:
        for item in sublist:
            flat_list.append(item)
    return flat_list


def powerball_info():
    try:
        url = "https://www.powerball.com"
        r = requests.get(url)
        tree = html.fromstring(r.content)
        numbers = []
        for i in range(1, 6):
            num = tree.xpath(f'/html/body/div[2]/ul/li[{i}]/div/text()')
            numbers.append(num)
        prize = tree.xpath('/html/body/div[2]/h2/text()')
        next_drawing = tree.xpath('/html/body/div[2]/h1/text()')
        flat_numbers = flatten_list(numbers)

        data = [prize, next_drawing]
        with open('output.txt', 'w') as f:
            for val in flat_numbers:
                f.write(val + '\t')
            for _list in data:
                for _string in _list:
                    f.write(str(_string) + '\n')
            f.close()

        with open('output.txt', 'r') as old, open('powerball.txt', 'w+') as new:
            for line in old:
                if line.strip():
                    new.write(line)
            os.remove('output.txt')
            new.close()
    except IOError:
        print("IO operation failed")
    except ConnectionRefusedError:
        print("Refusing to connect to the website")




def mega_info():
    url = "https://www.megamillions.com/"
    r = requests.get(url)
    tree = html.fromstring(r)
    numbers = []
    for i in range(1, 6):
        num = tree.xpath()


if __name__ == '__main__':
    powerball_info()

