d = {1: 2, 3: 4, 2: 3, 4: 1}
while True:
    print("commands:'add', 'del', 'edit', 'find', 'print', 'sort', 'exit'")
    c = str(input())
    if c == "add":
        print("enter 2 digits")
        d.update({int(input()): int(input())})
    elif c == "del":
        print(d)
        print("enter key of the element you want to del")
        del d[int(input())]
    elif c == "edit":
        print(d)
        print("enter key of the element you want to edit and edited element")
        d.update({int(input()): int(input())})
    elif c == "find":
        lst = str(d)
        l = lst.find(input())
        if l % 2 == 0:
            print("found in keys")
        elif l != -1:
            print("found in elements")
        else:
            print("not found")
    elif c == "print":
        print(d)
    elif c == "sort":
        list_keys = list(d.keys())
        list_keys.sort()
        for i in list_keys:
            print(i, ':', d[i], end=", ")
        print()
    elif c == "exit":
        exit(0)
    else:
        print("unknown command")