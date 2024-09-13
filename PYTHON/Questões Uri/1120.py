while True:
    d, n = map(int, input().split(" "))
    if d == 0 and n == 0:
        break
    string = (str(n).replace(str(d), ""))
    if string == "":
        print(0)
    else:
        print(int(string))