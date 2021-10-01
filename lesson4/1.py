from collections import Counter
s = input()
c = dict(Counter(s))
x = 0
y = None
for i, j in c.items():
    if j >= x:
        x = j
        y = i
print(y)
