# def square(x):
#     '''
#     计算平方并返回结果
#     >>> square(2)
#     4
#     >>> square(3)
#     9
#     '''
#     return x * x
#
# if __name__ =='__main__':
#     import doctest, my_math
#     doctest.testmod(my_math)


class Base:
    def __init__(self):
        print("base")


class b(Base):
    def __init__(self):
        super().__init__()
        print("B")

class d(Base):
    def __init__(self):
        super().__init__()
        print("A")





class c(d, b):
    def __init__(self):
        super().__init__()
        print("c")

ccc = c()