a = list(map(int, input().split()))
x = 0
for i in reversed(a):
    if x == 1:
        print(i, end=" ")
        x = 0
    else:
        x += 1
