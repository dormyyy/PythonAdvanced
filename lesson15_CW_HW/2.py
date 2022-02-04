def check_decortator(startswith='', text=''):# задание 4: первый декоратор
    def decor(func):# задание 4: второй декоратор
        def inner(*args, **kwargs): #задание 1: пример 1
            n = args[0]
            if startswith == n[:len(startswith)] and text == '':
                func(*args, **kwargs)# задание 2: пример 2
            elif text == n:
                func(*args, **kwargs)
            else:
                print("No")
        return inner
    return decor


@check_decortator(startswith='O')
def say(n):
    print(n)


say('Ola')
