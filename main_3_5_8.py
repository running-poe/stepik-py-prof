
# 3.5 - 8
from datetime import datetime


# param = input()


def func(arg, *args):
    curr_date = datetime.strptime(arg, "%d.%m.%Y %H:%M") - datetime.min
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
        return 'Курс уже вышел!'

    diff_date = release_date - curr_date
    if diff_date.days > 0:  #1
        if diff_date.seconds//3600 > 0:  #1.1
            return f"До выхода курса осталось: {diff_date.days} дней и " \
                   f"{(diff_date.seconds // 3600) % 24} {ds.get(((diff_date.seconds // 3600) % 24) % 10)[1]}"
        else:
            return f"До выхода курса осталось: {diff_date.days} {ds.get(diff_date.days % 10)[0]}"
    else:
        if diff_date.seconds // 3600 > 0:  # 2.1
            if diff_date.seconds // 60 > 0:
                pass
            # вывести кол-во часов и минут
            else:
                pass
                # вывести кол-во часов
        else:
            if diff_date.seconds // 60 > 0:
                pass
                # вывести кол-во минут
            else:
                pass
                # время вышло


'''
        else:
            if diff_date.seconds // 60 > 0:
            # вывести часы и минуты
            else:
            # вывести часы
    else:
        if diff_date.seconds//3600 > 0:
        # вывыести кол-во часов и дней
        else:
        # вывести дни


            
        if diff_date.seconds//3600 > 0:
                

        if diff_date.days == 0:
            if diff_date.seconds//3600 == 0:
                return f"До выхода курса осталось: {diff_date.seconds//3600} " \
                       f"{ds.get((diff_date.seconds//3600) % 10)[2]}"
            if diff_date.seconds//3600 > 0:
                if diff_date.seconds//60 == 0:
                    return f"До выхода курса осталось: {diff_date.seconds//3600} " \
                           f"{ds.get((diff_date.seconds//3600)%10)[1]} и {diff_date.seconds//60} " \
                           f"{ds.get((diff_date.seconds//60) % 10)[2]}"
                if diff_date.seconds//60 > 0:
                    return f"До выхода курса осталось: {diff_date.seconds//3600} " \
                           f"{ds.get((diff_date.seconds//3600)%10)[1]} и {diff_date.seconds//60} " \
                           f"{ds.get((diff_date.seconds//60) % 10)[2]}"
'''

#func(param)

