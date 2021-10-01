from collections import Counter


def top3():
    with open("dir.txt", "r") as f:
        a = f.read().split()
        c = dict(Counter(a))
        x1 = 0
        y1 = None
        x2 = 0
        y2 = None
        x3 = 0
        y3 = None
    for i, j in c.items():
        if j > x1:
            x1 = j
            y1 = i
        elif j > x2:
            x2 = j
            y2 = i
        elif j > x3:
            x3 = j
            y3 = i
    print(f"""{x1} - {y1}
{x2} - {y2}
{x3} - {y3}""")


top3()
