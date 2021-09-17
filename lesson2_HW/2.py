dict = {1: 2, 3: 4, 2: 3, 4: 1}
lst = []
for i,j in dict.items():
    lst.append(i)
    lst.append(j)
s = set(lst)
for k in s:
    print(f"'{k}' - {lst.count(k)} ")