# import os
#
# s = ' this  is my string '
#
# print(s.split())
# print(s.split(' '))
# print(s.strip())
#
# print([d for d in os.listdir('.')])

print('.' in list("PARTI"))
print('49.'.split('.'))

ex_list = ['1.', 'a']
for item in ex_list:
    print(item.replace('.', ' '))
    if ex_list.index(item) == len(ex_list) - 1:
        print('++')
    print(item)