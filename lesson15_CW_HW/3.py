def check_decortator(role=1):
    def decor(func):
        def inner(*args, **kwargs):
            n = args[0]
            if role == 1:
                role1()
            elif role == 2:
                role2()
            else:
                role3()
        return inner
    return decor


def role1():
    print("Hello1")


def role2():
    print("Hello2")


def role3():
    print("Hello3")


@check_decortator(role=3)
def say(n):
    print(n)


say('Ola')
