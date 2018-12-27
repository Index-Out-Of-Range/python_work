from math import ceil, floor
from PIL import Image


def dp_function():
    print("*" * 34)
    print('{0:<}{1:^26}{0:>}'.format("==", "欢迎来到DP系统V1.0"))
    print('{0:<}{1:^28}{0:>}'.format("==", "功能一"))
    print('{0:<}{1:^28}{0:>}'.format("==", "功能二"))
    print('{0:<}{1:^28}{0:>}'.format("==", "功能三"))
    print('{0:<}{1:^28}{0:>}'.format("==", "功能四"))
    print('{0:<}{1:^28}{0:>}'.format("==", "功能五"))
    print("*" * 34)
    while True:
        chance = input("请输入你想要的功能（输入Q或q退出程序）：")
        if chance == "q" or chance == "Q":
            break
        elif chance == "1":
            function1()
        elif chance == "2":
            function2()
        elif chance == "3":
            function3()
        elif chance == "4":
            function4()
        elif chance == "5":
            function5()
        else:
            print("please input '1~5', 'q' or 'Q'!")


def function1():
    print("function1，please input your name, QQ, telephone and address:")
    info = {}
    dict = ["name", "QQ", "telephone", "address"]
    for i in range(len(dict)):
        info[dict[i]] = input()
    print("*" * 34)
    for i in range(len(dict)):
        print("{:10}:{}".format(dict[i], info[dict[i]]))
    print("*" * 34)


def function2():
    print("function2, please input a number:")
    number = input()
    length = len(number)
    answer = 0
    try:
        number = int(number)
    except Exception:
        print("please input a number!", Exception)
    for i in range(length):
        answer += (number % 10)
        number = number // 10
    print("The answer is:", answer)


def function3():
    print("function3, please input a number:")
    number = input()
    try:
        number = int(number)
    except:
        print("please input a number!")
    answer = []
    for i in range(2, number):
        is_prime = True
        for j in range(2, floor(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            answer.append(i)
    print(answer, len(answer))


def function4():
    print("function4, it will print the multiplication table.")
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{} * {} = {:<3}".format(i, j, i * j), end=' ')
        print()


def function5():
    print("function5, image to text")

    IMG = 'D:\\pycharm\\python_work\\dp1\\Google.png'
    WIDTH = 60
    HEIGHT = 45

    ascii_char = list(
        "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    def get_char(r, g, b, alpha=256):
        if alpha == 0:
            return ' '
        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
        unit = (256.0 + 1) / length
        return ascii_char[int(gray / unit)]

    if __name__ == '__main__':
        im = Image.open(IMG)
        im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
        txt = ""
        for i in range(HEIGHT):
            for j in range(WIDTH):
                txt += get_char(*im.getpixel((j, i)))
            txt += '\n'
        print(txt)
        # with open("output.txt", 'w') as f:
        #     f.write(txt)


if __name__ == "__main__":
    dp_function()
