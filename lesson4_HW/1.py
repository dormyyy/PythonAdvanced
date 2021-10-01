def registration(log: str):
    with open("t.txt", "r+") as f:
        iib = False
        for i in f.readlines():
            x = i.split(" ")
            if x[0] == log:
                print("This login already exist, please enter password to log in")
                iib = True
                login(log)
        if not iib:
            pw = str(input())
            f.write(f"{log} {pw}\n")
            pass


def login(log: str):
    with open("t.txt", "r") as f:
        iib = False
        for i in f.readlines():
            x = i.split()
            if x[0] == log:
                iib = True
                break
        y = str(x[1])[:len(x[1])]
        if iib:
            pw = str(input())
            while pw != y:
                pw = str(input("Incorrect password. Please try again: "))
            print("Successfully")
            pass
        elif not iib:
            print("This login isn`t registered, please enter password to registration")
            registration(log)


while True:
    print("1 - login, 2 - registration, 3 - exit")
    ans = str(input("Choose 1 of 3 options: "))
    if ans == "1":
        login(str(input()))
    elif ans == "2":
        registration(str(input()))
    elif ans == "3":
        break
    else:
        print("Try again")
