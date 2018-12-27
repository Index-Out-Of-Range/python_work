def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


num = input("please input a number you want:")
move(int(num), "A", "B", "C")
