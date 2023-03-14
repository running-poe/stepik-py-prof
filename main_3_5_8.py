
# 3.5 - 8
from datetime import datetime


# param = input()
def choose_plural(i: int, index: int):
    ds = {0: ('дней', 'часов', 'минут'),
          1: ('день', 'час', 'минута'),
          2: ('дня', 'часа', 'минуты'),
          3: ('дня', 'часа', 'минуты'),
          4: ('дня', 'часа', 'минуты'),
          5: ('дней', 'часов', 'минут'),
          6: ('дней', 'часов', 'минут'),
          7: ('дней', 'часов', 'минут'),
          8: ('дней', 'часов', 'минут'),
          9: ('дней', 'часов', 'минут'),
          10: ('дней', 'часов', 'минут'),
          11: ('дней', 'часов', 'минут'),
          12: ('дней', 'часов', 'минут'),
          13: ('дней', 'часов', 'минут'),
          14: ('дней', 'часов', 'минут'),
          15: ('дней', 'часов', 'минут'),
          16: ('дней', 'часов', 'минут'),
          17: ('дней', 'часов', 'минут'),
          18: ('дней', 'часов', 'минут'),
          19: ('дней', 'часов', 'минут'),
          20: ('дней', 'часов', 'минут')}

    if (i % 100) < 21:
        return ds[i % 100][index]
    if i % 100 in [31, 51, 71, 92]:
        return ds[1][index]
    return ds[(i % 100) % 10][index]


def func(arg):
    curr_date = datetime.strptime(arg, "%d.%m.%Y %H:%M") - datetime.min
    release_date = datetime(year=2022, month=11, day=8, hour=12, minute=0) - datetime.min

    if release_date < curr_date:
        return 'Курс уже вышел!'

    diff_date = release_date - curr_date
    if diff_date.days > 0:  #1
        if diff_date.seconds//3600 > 0:  #1.1
            return f"До выхода курса осталось: {diff_date.days} {choose_plural(diff_date.days, 0)} и " \
                   f"{(diff_date.seconds // 3600) % 24} {choose_plural((diff_date.seconds // 3600), 1)}"
        else:
            return f"До выхода курса осталось: {diff_date.days} {choose_plural(diff_date.days, 0)}"
    else:
        if diff_date.seconds // 3600 > 0:  # 2.1
            if diff_date.seconds % 3600 > 0:
                # вывести кол-во часов и минут
                return f"До выхода курса осталось: {diff_date.seconds // 3600} " \
                   f"{choose_plural((((diff_date.seconds // 3600) % 24) % 12), 1)} и {(diff_date.seconds // 60) % 60} " \
                   f"{choose_plural(((diff_date.seconds // 60) % 12), 2)}"
            else:
                # вывести кол-во часов
                return f"До выхода курса осталось: {diff_date.seconds // 3600} " \
                       f"{choose_plural(diff_date.seconds // 3600, 1)}"

        else:
            if diff_date.seconds // 60 > 0:
                pass
                return f"До выхода курса осталось: {diff_date.seconds // 60} " \
                       f"{choose_plural(((diff_date.seconds // 60) % 10), 2)}"
                # вывести кол-во минут
            else:
                return "Курс уже вышел!"
                # время вышло



#func(param)

