def nod(a: int, b: int):
    if a == b:
        return a
    if a > b:
        return nod(a-b, b)
    else:
        return nod(a, b-a)


a, b = map(int, input().split())
print(nod(a, b))