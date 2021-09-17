d = {1: 2, 2: 3, 3: 4}
x = 0
x1 = 0
for i, j in d.items():
    if i > x:
        x = i
    if j > x:
        x = j
    if (i < x) and (i > x1):
        x1 = i
    if (j < x) and (j > x1):
        x1 = j
print(x1)
