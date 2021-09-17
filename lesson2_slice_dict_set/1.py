d = {}
d["first"] = "value"
print(d)
d.update({1: 2, 2: 3, 4: 5})
print(d.pop(1))
print(d.keys())
for key in d.keys():
    print(key)

for key, val in d.items():
    print(key, val)

print(2 in d.keys())