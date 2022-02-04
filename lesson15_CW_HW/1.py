def decor1(n):
    def decor(func):
        def inner(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return inner
    return decor


@decor1(n=4)
def hello():
    print("hello world")


hello()
