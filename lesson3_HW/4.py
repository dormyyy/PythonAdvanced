def mm(m: int, a: list):
    if len(a) == 1:
        return m
    else:
        if a[0] < m:
            return mm(a[0], a[1:])
        else:
            return mm(m, a[1:])


a = list(map(int, input().split()))
m = a[0]
print(mm(m, a))
