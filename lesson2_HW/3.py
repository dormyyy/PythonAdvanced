a = ['1', '2', 'a', 'h', 'r', 'f', '2']
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
x=0
for i in a:
    if x == 2 and i in letters:
        print(i, end=" ")
        x = 0
    else:
        x += 1
