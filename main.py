import uuid
import requests
import pprint
import hashlib
import queue
import base64
import json
import asyncio
import time
import websockets
import wget

from dataclasses import dataclass

'''

@dataclass
class Card:
    rank: str
    suit: str


card = Card("Q", "hearts")
print(card)
print(card.rank)
print(card.suit)

numbers = [1, 2, 3]
letters = ['b', 'a', 'c']
res = list(zip(numbers, letters))
print(res)


def s(x):
    return x * 2 + 1


a, b = 0, 1
a, b = b, a

mapped_numbers = list(map(lambda x: x % 2 == 0, [s(n) * 2 for n in [11, 12, 24, 36, 42, 55]]))
print(mapped_numbers)


def s(i: int) -> int:
    return 0


def a(i: int) -> bytes:
    return [0]


u = uuid.uuid4()
print(u)

url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
pprint.pprint(users)
print('=======================')
pprint.pprint(users['results'][0]['registered']['age'])
# print(wget.download(users['results'][0]['picture']['large']))   #скачать в текущую директорию с дефолтным именем
print('=======================\n\n\n')

sha = hashlib.sha1()
sha.update('12345'.encode())
h = sha.digest().hex()

base64_bytes = base64.b64encode(h.encode())
base64_message = base64_bytes.decode('ascii')

print("/base64")
print(base64_bytes)
print(base64_message)
print("\\base64\n")

user = {'body':
    {
        'name': 'vasya',
        'surname': 'ivanov',
        'uuid': str(uuid.uuid4())
    },
    'passw':
        {
            'login': 'vasya',
            'password': h
        }
}

print(user)
s = json.dumps(user)
pprint.pprint(s)

start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


async def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('gr1 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr1 ended work: {}'.format(tic()))


async def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print('gr2 started work: {}'.format(tic()))
    await asyncio.sleep(2)
    print('gr2 Ended work: {}'.format(tic()))


async def gr3():
    print("Let's do some stuff while the coroutines are blocked, {}".format(tic()))
    await asyncio.sleep(2)
    print("Done!")


async def main():
    task1 = asyncio.create_task(gr1())
    task2 = asyncio.create_task(gr2())
    task3 = asyncio.create_task(gr3())

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2
    await task3

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())

qw = ([], ()) * 5
print(qw)

a = 0.1 + 0.2
b = float(0.3)
print(a == b)
print(a)
print(b)


def fff():
    for i in range(10):
        yield i, i * 10


c = {key: key for key in fff()}
print(c)

rn = [*range(5)]
print("Range")
print(rn)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, " равен ", x, " * ", n // x)
            break
        else:  ## выполнится, если цикл завершен нормально, а не выход по break
            print(n, ' простое')


def hide_card(card):
    return str(12 * '*') + str(card).replace(' ', '')[12:]


def test_n(n):
    if n % 2 == 0:
        return n


def same_parity(l):
    if not l:
        return []
    if l[0] % 2 == 0:
        return list(filter(lambda x: x % 2 == 0, l))
    else:
        return list(filter(lambda x: x % 2 != 0, l))


def is_valid(pin) -> bool:
    if not pin:
        return False

    if ' ' in pin:
        return False

    if len(pin) not in [4, 5, 6]:
        return False

    for n in pin:
        if str.isnumeric(n):
            continue
        else:
            return False

    return True



print(is_valid('4367'))


def print_given(*args, **kwargs):
    o = sorted(kwargs.items())

    for n in args:
        print(str(n) + ' ' + str(type(n)))
    for n in o:
        print(str(n[0]) + ' ' + str(n[1]) + ' ' + str(type(n[1])))


print(same_parity([6, 0, 67, -7, 10, -20]))

print(hide_card('12 123456 678 1 7890'))

print(is_valid('123 4'))


print_given([1, 2, 3, 4], ('a', 'b', 'c', 'd'), name='Timur', age=29, city='Moscow')

def convert(s: str) -> str:
    count_upper: int = 0
    count_lower: int = 0

    for c in s:
        if str(c).isupper():
            count_upper += 1

    for c in s:
        if str(c).islower():
            count_lower += 1

    if count_upper > count_lower:
        s = s.upper()
    elif count_upper <= count_lower:
        s = s.lower()

    return s


print(convert('beerGEEEK!!!!'))


def filter_anagrams(word: str, words: list[str]) -> list[str]:
    s_word = sorted(word)
    return list(filter(lambda x: x if s_word == sorted(x) else False, words))


print(filter_anagrams('aabb', ['baba', 'babc', 'bbaa']))


def likes(names: list[str]) -> str:
    match len(names):
        case 0:
            return 'Никто не оценил данную запись'
        case 1:
            return str(names[0]) + ' оценил(а) данную запись'
        case 2:
            return str(names[0]) + ' и ' + str(names[1]) + ' оценили данную запись'
        case 3:
            return str(names[0]) + ', ' + str(names[1]) + ' и ' + str(names[2]) + ' оценили данную запись'
        case _:
            return str(names[0]) + ', ' + str(names[1]) + ' и ' + str(len(names) - 2) + ' других оценили данную запись'


print(likes([]))
print(likes(['Тимур']))
print(likes(['Том']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))


def index_of_nearest(arr: list[int], i: int) -> int:
    if not arr:
        return -1
    _list = list(map(lambda x: abs(x - i), arr))
    return _list.index(min(_list))


print(index_of_nearest([], 17))


def spell(*words) -> []:
    return {_.lower()[0]: len(_) for _ in sorted(words, key=lambda _: len(_))}


words = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']

print(spell(*words))

# print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))

def choose_plural(i: int, words: set):
    suffixes = {
        0: 2, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2,
        11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 2, 20: 2
    }

    if (i % 100) < 21:
        return str(i) + ' ' + words[suffixes[i % 100]]
    if i % 100 in [31, 51, 71, 92]:
        return str(i) + ' ' + words[1]
    if i % 100 in [32, 33, 34, 52, 53, 54, 72, 73, 74, 92, 93, 94]:
        return str(i) + ' ' + words[1]
    return str(i) + ' ' + words[suffixes[(i % 100) % 10]]


print(choose_plural(240, ('курица', 'курицы', 'куриц')))


def bubble(num: list, sub):
    for i in range(0, len(num) - 1):
        for k in range(0, len(num) - i - 1):
            sub(num, k)


def first(num, k):
    a = int(str(f'{num[k]}{num[k+1]}'))
    b = int(str(f'{num[k+1]}{num[k]}'))
    if b > a:
        num[k], num[k + 1] = num[k + 1], num[k]


def second(num, k):
    if str(num[k])[0] == str(num[k + 1])[0] and len(str(num[k + 1])) == 1:
        num[k], num[k + 1] = num[k + 1], num[k]
    else:
        l1 = len(str(num[k]))
        l2 = len(str(num[k+1]))
        if l1 > l2:
            if str(num[k])[1:l2]>str(num[k+1]):
                num[k], num[k + 1] = num[k + 1], num[k]


def get_biggest(*nums):
    if not nums or len(list(*nums)) == 0:
        return -1

    num = list(*nums)

    bubble(num, first)
   # bubble(num, second)
    return int("".join(list(map(str, num))))
'''
# print(get_biggest([0, 0, 0, 0]))
# print(get_biggest([61, 228, 9, 3, 11]))
# print(get_biggest([7, 71, 72]))
# print(get_biggest(['998', '9686', '9842', '9721', '9603', '9811', '9719', '9845', '9627', '9859', '9705', '9784', '9662', '9622', '9926', '9777', '9866', '9811', '96', '9664', '9766', '9788', '9826', '9745', '9693', '9880', '9621', '96', '9671', '975', '9623']))
# print(get_biggest([7, 71, 732]))
# print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))
# 78554656558534233433222211113
# 78554656558534233433222211311
### Элегантное решение от Леши
'''
def get_biggest(numbers: list[int]) -> int:
    def find_big_number(a: int,b: int):
        v1 = int(f'{str(a)}{str(b)}')
        v2 = int(f'{str(b)}{str(a)}')
        if v1 < v2:
            return True
        else:
            return False

    if numbers:
        for i in range(len(numbers) - 1):
            for j in range(len(numbers) - i - 1):
                if find_big_number(numbers[j],numbers[j+1]):
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return int(''.join([str(_) for _ in numbers]))
    else:
        return -1


a: int = 1
b: int = 2
print(f'{str(a)}{str(b)}')

ssss = input()
print(ssss)
wwww = list(map(int, list(ssss.split(' '))))
n = int(wwww[0])
print(n)
X = int(wwww[1])
Y = int(wwww[2])
A = int(wwww[3])
B = int(wwww[4])


def frev(l, a, b):
    i = 0
    for n in reversed(l[a-1:b]):
        l_1[a-1+i] = n
        i += 1


l_1 = [str(x) for x in range(1, n + 1)]


frev(l_1, X, Y)
frev(l_1, A, B)


print(" ".join(l_1))




s = input()
l = list(map(int, list(s.split(' '))))
s = set(x for x in l if l.count(x) > 1)
print(" ".join(list(map(str,sorted(s)))))

'''

'''
# для последовательности чисел 1..n вывести максимальный размер группы чисел последовательности, которые имеют одинаковую сумму собственных чисел
s = input()
p = sorted([sum(map(int, list(str(_)))) for _ in range(1, int(s)+1)])
l = max([p.count(i) for i in p])
print(l)
'''

'''
1
китайский, испанский, английский, французский, португальский
английский, испанский, китайский, португальский, французский
'''

'''
count = input()
l: list = []
for i in range(int(count)):
    s = input()
    l.append(set(s.split(', ')))


res = l[0]
for i in range(1, int(count)):
    res &= l[i]

if not res:
    print("Сериал снять не удастся")
else:
    print(", ".join(map(str, sorted(res))))
'''

'''
# сравним слова по шаблону расположения гласных в слову (индексах)
def test(word: str):
    l_vov = list('ауоыиэяюёе')
    l_cons = list('бвгджзйклмнпрстфхцчшщ')
    l_v = [i for i, l in enumerate(word) if l in l_vov]
    l_c = [i for i, l in enumerate(word) if l in l_cons]
    # неважно расположение согласных после последней гласной
    return l_v, l_c[:len(l_v)-1]

words = []
word_ = input()
count_ = input()
for i in range(int(count_)):
    words.append(input())

for i in range(int(count_)):
    if test(word_) == test(words[i]):
        print(words[i])


'''

# выдаем адреса корппочты новым сотрудникам
'''n_exists = int(input())
exists = []
for i in range(n_exists):
    exists.append(input())
'''
n_exists = 6
exists = ['ivan-petrov@beegeek.bzz', 'petr-ivanov@beegeek.bzz', 'ivan-petrov1@beegeek.bzz', 'ivan-ivanov@beegeek.bzz',
          'ivan-ivanov1@beegeek.bzz',
          'ivan-ivanov2@beegeek.bzz']

'''
n_new = int(input())
new = []
for i in range(n_new):
    new.append(input())
'''

'''
n_new = 3
new = ['ivan-ivanov', 'petr-petrov', 'petr-ivanov']
new_res = []

for k, n in enumerate(new):
    print(f'{k} {n}')
    for i in range(len(exists)):
        if n in exists[i]:
            s = str(exists[i]).split('@')[0]
            print(f's: {s}')
            index = s.find(n)
            print(f'index: {index}')
            s = s[(index - 1) + len(str(n)) + 1: len(s) + 1]
            print(f'num:{s}')

            new_res.append(f'{str(s)} {s}@beegeek.bzz')

print(new_res)

print('a-b' in 'a-b10@r.ru')


from datetime import date

def get_date_range(start_date, end_date):
    l = []
    d1 = start_date.toordinal()
    d2 = end_date.toordinal()
    while d1 <= d2:
        l.append(date.fromordinal(d1))
        d1 += 1

    return l


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')


def saturdays_between_two_dates(date1, date2):
    d = [x for x in range(*sorted([date1.toordinal(), date2.toordinal() + 1])) if date.fromordinal(x).weekday() == 5]
    return len(d)


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 6)

print(saturdays_between_two_dates(date1, date2))


from datetime import date, time

given_date = date(2021, 7, 17)

print(given_date.strftime('%A %d %B %Y'))
print(given_date.strftime('%Y/%m/%d'))
print(given_date.strftime('%d.%m.%Y (%A, %B)'))
print(given_date.strftime('Day of year: %j, week number: %U'))



from datetime import date, time
date1, date2 = date.fromisoformat(input()), date.fromisoformat(input())
d = min(date1, date2)
print(d.strftime('%d-%m (%Y)'))



from datetime import date, time
d = []
n = int(input())
for i in range(n):
    d.append(date.fromisoformat(str(input())))

d = sorted(d)
for i in d:
    print(i.strftime('%d/%m/%Y'))



from datetime import date, time

def print_good_date(dates: list[date]) -> None:
    d_list = list(filter(lambda x: x if x.year == 1992 and (x.month + x.day) == 29 else False, dates))
    d_list = sorted(d_list)
    for i in d_list:
        print(i.strftime('%B %d, %Y'))



from datetime import date, time


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        d = date(int(year), int(month), int(day))
        return True
    except ValueError:
        return False

s = ''
d = []
c = 0
while True:
    try:
        s = input()
        if s == 'end':
            break
        year, month, day = s.split('.')
        dt = date(int(year), int(month), int(day))
        d.append('Корректная')
        c += 1
    except ValueError:
        d.append('Некорректная')

for i in d:
    print(i)

print(c)



from datetime import datetime

times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26),
                      datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59),
                      datetime(2017, 10, 2, 6, 37, 10), datetime(2017, 10, 2, 6, 42, 53),
                      datetime(2017, 10, 2, 8, 56, 45), datetime(2017, 10, 2, 9, 18, 3),
                      datetime(2017, 10, 2, 12, 23, 48), datetime(2017, 10, 2, 12, 45, 5),
                      datetime(2017, 10, 2, 12, 48, 8), datetime(2017, 10, 2, 12, 10, 54),
                      datetime(2017, 10, 2, 19, 18, 10), datetime(2017, 10, 2, 12, 31, 45),
                      datetime(2017, 10, 3, 20, 57, 10), datetime(2017, 10, 4, 7, 4, 57),
                      datetime(2017, 10, 4, 7, 13, 31), datetime(2017, 10, 4, 7, 13, 42),
                      datetime(2017, 10, 4, 7, 21, 54), datetime(2017, 10, 4, 14, 22, 12),
                      datetime(2017, 10, 4, 14, 50), datetime(2017, 10, 4, 15, 7, 27),
                      datetime(2017, 10, 4, 12, 44, 49), datetime(2017, 10, 4, 12, 46, 41),
                      datetime(2017, 10, 4, 16, 32, 33), datetime(2017, 10, 4, 16, 34, 44),
                      datetime(2017, 10, 4, 16, 46, 59), datetime(2017, 10, 4, 12, 26, 6)]

print('До полудня') if len(list(filter(lambda x: x.hour <= 12, times_of_purchases))) > len(times_of_purchases)/2 \
    else print('После полудня')




from datetime import datetime

from datetime import datetime

data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
        'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
        'Анна': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'), 
        'Илина': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'), 
        'Герман': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'), 
        'Руслан': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'), 
        'Лера': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'), 
        'Егор': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'), 
        'Максим': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'), 
        'Саша': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'), 
        'Марина': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

data = sorted([(k, datetime.strptime(l[1], '%d.%m.%Y %H:%M:%S').timestamp()-
         datetime.strptime(l[0], '%d.%m.%Y %H:%M:%S').timestamp()) for k, l in data.items()], key=lambda k: k[1])[0][0]
print(data)


# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021'
# print(is_available_date(dates, some_date))





a = {(1,2), (4,5)}
a1 = {(3)}

print(a & a1)

'''
'''
from datetime import datetime

with open("diary.txt", "r", encoding="utf-8") as f:
    data = f.read()

res = []

data = data.split('\n\n')

for k, line in enumerate(data):
    dt = datetime.strptime(line[:18], '%d.%m.%Y; %H:%M\n').timestamp()
    res.append((dt, line+'\n'))

res.sort(key=lambda x: x[0])
for l in res:
    print(repr(l[1]))

tup = res.pop(len(res)-1)
d = tup[0]
s = tup[1]
s = s[:len(s)-1]
res.append((d, s))
for n in res:
    print(n[1])


new_rec = True
res = []
dt = None
s = ''
for line in lines:
    if new_rec:
        dt = datetime.strptime(line, '%d.%m.%Y; %H:%M\n').timestamp()
        s += line
        new_rec = False
        continue
    if line != '\n':
        s += line
    else:
        res.append((dt, s))
        new_rec = True
        s = ''
res.sort(key=lambda x: x[0])






from datetime import datetime


def is_available_date(booked_dates: list[str], date_for_booking: str):
    def get_dates_list(dates: list) -> list:
        res = []
        for s in dates:
            ss = s.split('-')
            if len(ss) == 1:
                res += [datetime.strptime(ss[0], '%d.%m.%Y').toordinal()]
            else:
                res += [_ for _ in range(datetime.strptime(ss[0], '%d.%m.%Y').toordinal(),
                                         datetime.strptime(ss[1], '%d.%m.%Y').toordinal()+1)]
        return res

    booked_dates_list = get_dates_list(booked_dates)
    booking_dates = get_dates_list([date_for_booking])
### запомнить!!!!!
    return not any([_ in booking_dates for _ in booked_dates_list])


from datetime import datetime, timedelta

dt = datetime(2021, 11, 4, 13, 6) + timedelta(days=7, hours=12)

print(dt.strftime('%d.%m.%Y %H:%M:%S'))




dates = ['14.09.2022-14.10.2022','12.12.2022']
some_date = '20.09.2022-25.09.2022'
is_available_date(dates, some_date)


list1 = [1,2,3,4]
list2 = [1,2]

for elem in list1:
    print(elem, ['нету', 'есть'][elem in list2])

print([_ in list2 for _ in list1])
print([_*2 for _ in list1])


from datetime import date, timedelta


date1 = datetime.strptime(input(), "%d.%m.%Y")

date_before = date1 - timedelta(hours=24)
date_after = date1 + timedelta(hours=24)
print(datetime.strftime(date_before, "%d.%m.%Y"))
print(datetime.strftime(date_after, "%d.%m.%Y"))
'''

'''
print((datetime.strptime(input(), "%H:%M:%S")-datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)).seconds)

t = datetime.strptime(input(), "%H:%M:%S")
n = int(input())
res = t + timedelta(seconds=n)
print(datetime.strftime(res, "%H:%M:%S"))
'''

from datetime import datetime, timedelta

'''
def num_of_sundays(year: int):
    return len([_ for _ in range(*sorted([datetime(year=year, month=1, day=1).toordinal(),
                                   datetime(year=year+1, month=1, day=1).toordinal()]))
                if date.fromordinal(_).weekday() == 6])


print(num_of_sundays(2021))

r = datetime.strptime(input(), "%d.%m.%Y")
print(datetime.strftime(r, '%d.%m.%Y'))
for i in range(1, 10):
    r = r + timedelta(hours=24*i+24)
    print(datetime.strftime(r, '%d.%m.%Y'))


dates = [datetime.strptime(d, '%d.%m.%Y') for d in str(input()).split(' ')]
l = []
for i in range(1, len(dates)):
    l.append(abs((dates[i]-dates[i-1]).days))

print(l)


def fill_up_missing_dates(dates: list):
    new_dates = sorted([datetime.strptime(_, '%d.%m.%Y') for _ in dates])
    mind = min(new_dates)
    maxd = max(new_dates)
    return [datetime.strftime(datetime.fromordinal(_), "%d.%m.%Y") for _ in range(mind.toordinal(), maxd.toordinal()+1)]

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']
print(fill_up_missing_dates(dates))


from datetime import datetime, time, timedelta
d = date(2023, 1, 1)
start = datetime.combine(d, datetime.strptime(input(), '%H:%M').time())
end = datetime.combine(d, datetime.strptime(input(), '%H:%M').time())
if start < end:
    curr = start
    while curr <= end - timedelta(minutes=45):
        next = curr + timedelta(minutes=45)ё
        print(f'{curr.strftime("%H:%M")}-{next.strftime("%H:%M")}')
        next += timedelta(minutes=10)
        curr = next


from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]
d = date(2023, 1, 1)

minutes = [(datetime.combine(d, datetime.strptime(_[1], '%H:%M').time()) -
            datetime.combine(d, datetime.strptime(_[0], '%H:%M').time())).seconds//60 for _ in data]

print(sum(minutes))

from datetime import date, time, datetime, timedelta
l = [0, 0, 0, 0, 0, 0, 0]
for _ in range(date(1, 1, 1).toordinal(), date(9999, 12, 31).toordinal()+1):
    d = date.fromordinal(_)
    if d.day == 13:
        l[d.weekday()] += 1

for i in l:
    print(i)


from datetime import date, time, datetime, timedelta
curr = datetime.strptime(input(), "%d.%m.%Y %H:%M")
rasp = [
    (timedelta(hours=9), timedelta(hours=18)),
    (timedelta(hours=9), timedelta(hours=18)),
    (timedelta(hours=9), timedelta(hours=18)),
    (timedelta(hours=9), timedelta(hours=18)),
    (timedelta(hours=9), timedelta(hours=18)),
    (timedelta(hours=10), timedelta(hours=21)),
    (timedelta(hours=10), timedelta(hours=21))
]

wd = curr.weekday()
t = datetime.combine(date.min, curr.time()) - datetime.min

if not rasp[wd][0] <= t < rasp[wd][1]:
    print('Магазин не работает')
else:
    print((rasp[wd][1]-t).seconds // 60)


# наиболее тошнотная задача. надо иметь в виду, что отсчет здесь начинается просто с даты
# которая мес+день - нечетная, а вот вывод теперь каждые три дня, если не пн и чт
from datetime import datetime, timedelta
d1 = datetime.strptime(input(), "%d.%m.%Y")
d2 = datetime.strptime(input(), "%d.%m.%Y")
dates = [*range(d1.toordinal(), d2.toordinal() + 1)]

c = 0
found_first: bool = False

for d in dates:
    dd = datetime.fromordinal(d)
    if not found_first and (dd.day + dd.month) % 2 != 0:
        found_first = True
        if dd.weekday() not in [0, 3]:
            print(dd.strftime("%d.%m.%Y"))
        continue

    if found_first:
        if c == 2:
            if dd.weekday() not in [0, 3]:
                print(dd.strftime("%d.%m.%Y"))
            c = 0
        else:
            c += 1

from datetime import datetime, timedelta
n = int(input())
dates = {}
for i in range(n):
    s = input()
    s = s.split(' ')
    dates.update({f'{str(s[0])+" "+str(s[1])}': datetime.strptime(s[2], "%d.%m.%Y").toordinal()})

rev_dict = {}
for key, value in dates.items():
    rev_dict.setdefault(value, set()).add(key)

print(rev_dict)

elem = sorted(rev_dict.keys())
print(elem)
l = len(rev_dict[elem[0]])
print(rev_dict)

if l > 1:
    print(f'{str(datetime.strftime(datetime.fromordinal(elem[0]),"%d.%m.%Y")) + " " + str(l)}')
else:
    print(f'{str(datetime.strftime(datetime.fromordinal(elem[0]),"%d.%m.%Y")) + " " + str(*rev_dict[elem[0]])}')


# 3.5 - 6
from datetime import datetime, timedelta
n = int(input())
dates = {}
for i in range(n):
    s = input()
    s = s.split(' ')
    dates.update({f'{str(s[0])+" "+str(s[1])}': datetime.strptime(s[2], "%d.%m.%Y").toordinal()})

rev_dict = {}
for key, value in dates.items():
    rev_dict.setdefault(value, set()).add(key)

new_rev = []
for key, value in rev_dict.items():
    new_rev.append((key, len(value)))

new_rev.sort(key=lambda _: _[0])

# получим список дат, в которые ДР более 1 раза
lst = list(filter(lambda _: _[1] > 1, new_rev))
if not lst:
    # если у нас нет пересечений дат рождения, тогда выводим полный список всех дат
    for e in new_rev:
        print(datetime.strftime(datetime.fromordinal(e[0]), "%d.%m.%Y"))
else:
    # а тут вывеведем из списка все даты ДР
    for e in lst:
        print(datetime.strftime(datetime.fromordinal(e[0]), "%d.%m.%Y"))






# 3.5 - 7
from datetime import date, time, datetime, timedelta
dates = []
curr_date = datetime.strptime(input(), "%d.%m.%Y")

n = int(input())

for i in range(n):
    s = input()
    s = s.split(' ')
    dates.append((f'{str(s[0]) + " " + str(s[1])}', datetime.strptime(s[2], "%d.%m.%Y").toordinal()))

dates.sort(key=lambda _: _[1], reverse=True)
tmp = None
for e in dates:
    c = datetime.fromordinal(e[1]).replace(year=curr_date.year) - datetime.min
    if 1 <= (c.days - (curr_date - datetime.min).days) % 365 <= 7:
        tmp = e[0]
        break

if not tmp:
    print("Дни рождения не планируются")
else:
    print(tmp)

'''

# 3.5 - 8
from datetime import date, time, datetime, timedelta

param = input()


def func(p: str):
    curr_date = datetime.strptime(p, "%d.%m.%Y %H:%M") - datetime.min
    release_date = datetime(year=2022, month=11, day=8, hour=12, minute=0) - datetime.min
    ds = {0: ('дней', 'часов', 'минут'),
          1: ('день', 'час', 'минута'),
          2: ('дня', 'часа', 'минуты'),
          3: ('дня', 'часа',  'минуты'),
          4: ('дня', 'часа', 'минуты'),
          5: ('дней', 'часов', 'минут'),
          6: ('дней', 'часов', 'минут'),
          7: ('дней', 'часов', 'минут'),
          8: ('дней', 'часов', 'минут'),
          9: ('дней', 'часов', 'минут')}

    if release_date < curr_date:
        print('Курс уже вышел!')
    else:
        diff_date = release_date - curr_date
        if diff_date.days > 0:
            if diff_date.seconds//3600 == 0:
                print(f"До выхода курса осталось: {diff_date.days} {ds[diff_date.days % 10]}")
            if diff_date.seconds//3600 > 0:
                print(f"До выхода курса осталось: {diff_date.days} дней и {(diff_date.seconds//3600) % 24} часов")

        if diff_date.days == 0:
            if diff_date.seconds//3600 == 0:
                print(f"До выхода курса осталось: {diff_date.seconds//3600}")
            if diff_date.seconds//3600 > 0:
                if diff_date.seconds//60 == 0:
                    print(f"До выхода курса осталось: {diff_date.seconds//3600} часов и {diff_date.seconds//60} минут")
                if diff_date.seconds//60 > 0:
                    print(f"До выхода курса осталось: {diff_date.seconds // 3600} часов и {diff_date.seconds // 60} минут")


func(param)


