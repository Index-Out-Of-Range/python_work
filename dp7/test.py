# from decimal import Decimal
#
# class Fees(object):
#     def __init__(self):
#         self._fee = None
#
#     def get_fee(self):
#         return self._fee
#
#     def set_fee(self, value):
#         if isinstance(value, str):
#             self._fee = Decimal(value)
#         elif isinstance(value, Decimal):
#             self._fee = value
#
#     fee = property(get_fee, set_fee)
#
# f = Fees()
# f.set_fee("1")
# print(f.fee)
# f.fee = "2"
# print(f.get_fee())


# class Company(object):
#     def __init__(self, employee_list, mood_list):
#         self.employee = employee_list
#         self.mood = mood_list
#
#     def __getitem__(self, item):
#         return self.employee[item], self.mood[item]
#
# company = Company(['tom', 'bob', 'jane'], ['Happy', 'Sad', 'Calm'])
# # for em in company:
# #     print(em)
# company1 = company[:2]
# print(company1)


# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n = n + 1
#     return 'done'
#
# # for n in fib(6):
# #     print(n)
#
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break


# class Common:
#     def __init__(self, goods_list, people_list):
#         self.goods = goods_list
#         self.people = people_list
#         self.count = -1
#
#     def __getitem__(self, item):
#         return self.goods[item]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count >= len(self.people)-1:
#             raise StopIteration
#         else:
#             self.count += 1
#             return self.people[self.count]
#
#
# common = Common(['rice', 'apple', 'banana'], ['people1', 'people2', 'people3'])
# for i in common:
#     print(i)

a = "hello"
b = "hello"
c = a
print(id(a), id(b), id(c))

from copy import *

aa = ["hello", [1, 2]]
bb = copy(aa)
cc = deepcopy(aa)
print(id(aa[1]), id(bb[1]), id(cc[1]))

bb[1].append(3)
print(id(aa[1]), id(bb[1]))
print(aa, bb)

bb[0] = "world"
print(id(aa[0]), id(bb[0]))
print(aa, bb)