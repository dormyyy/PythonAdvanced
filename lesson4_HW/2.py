s = list(map(int, input().split()))
d = {}
for i in s:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)
