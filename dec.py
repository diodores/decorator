from datetime import datetime

def decorator(old_f):
    def new_f(*args, **kwargs):
        print(f'Вызвана функция {old_f.__name__}, с аргументами {args}, {kwargs}')
        res = old_f(*args, **kwargs)
        print(f'Итог {res}')
        return res
    return new_f


def log(old):
    def new_f(*args, **kwargs):
        with open('logs.txt', 'w') as file:
            t = str(datetime.now())
            res = old(*args,)
            string = f'функция {old.__name__}, вызвана в {t}, с следующими аргументами {args},'\
            f'результат работы функции равен {res}'
            file.write(string)
            return res
    return new_f