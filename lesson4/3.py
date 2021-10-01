from collections import defaultdict
s = "hello world"
d = defaultdict(int)
for i in s:
    d[i] += 1
print(dict(d))
