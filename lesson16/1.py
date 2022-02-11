class Decor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(*args, **kwargs)
        print("Impossible counting")
        self.func(*args, **kwargs)
        print("Done!")


@Decor
def func(a, b):
    print(a + b)


func(53, 12)
