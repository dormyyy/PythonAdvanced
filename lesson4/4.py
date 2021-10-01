n = str(input("Ваше имя: "))
a = str(input("Ваш возраст: "))

with open("t.txt", "a") as f:
    f.write(f"{n} {a}\n")
