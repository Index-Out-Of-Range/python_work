# class MuffledCalculator:
#     muffled = False
#     def calc(self, expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print('Division by zero is illegal')
#             else:
#                 raise
#
# if __name__ == '__main__':
#     cal = MuffledCalculator()
#     print(cal.calc('10/0'))

# from warnings import warn
#
# warn("Warning")

# a = input()
# if a:
#     print("not null")
# else:
#     print("null")
# [{'name': '1', 'qq': '2', 'phone': '3', 'email': '4'},
# {'name': 'q', 'qq': 'w', 'phone': 'e', 'email': 'r'}]
import json
# with open("output.json", "w") as f1:
#     list = [{'name': '1', 'qq': '2', 'phone': '3', 'email': '4'},
#             {'name': 'q', 'qq': 'w', 'phone': 'e', 'email': 'r'}]
#     f1.write("[\n")
#     for item in list:
#         load_dict = json.dump(item, f1)
#         print(list.index(item))
#         if list.index(item) != len(list)-1:
#             f1.write(",\n")
#     f1.write("\n]")
#     f1.close()
# print("-" * 10)
with open("output.json", "r") as f2:
    try:
        data = json.load(f2)
    except:
        data = []
    print(data)
    print(type(data))
    f2.close()