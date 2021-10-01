def registration(log: str):
    with open("t.txt", "r+") as f:
        if log in f.readlines():
            login(log)
        else:
            pw = str(input())
            f.write(f"{log} {pw}")
            pass


#def login(log: str):
#    with open("t.txt", "r") as f:
#        if log in f.readlines():



while True:
    print("1 - login, 2 - registration, 3 - exit")
    ans = int(input("Choose 1 of 3 options: "))
    if ans == 1:
        login(str(input()))
    elif ans == 2:
        registration(str(input()))
    elif ans == 3:
        break
    else:
        print("Try again")

