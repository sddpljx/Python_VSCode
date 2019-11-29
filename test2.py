'''
r = eval(input("请输入表达式："))
print(r)
print([1, 3, 5, 'list'])
a = 3 + 4j
b = 1 + 2j
print(a + b, a - b, a * b, a / b)
测试 = 1
print(测试)
x, y = 5, 10
print(x, y)
x, y = y, x
print(x, y)

a, b, c = 10, 0o10, 0x10
d = True
e = False
print(a, b, c, d, e)
f = None
print(f)

import sys
print(sys.float_info)

c1, c2, c3 = complex(), complex(5), complex(2, 3)
print(c1, c2, c3)
print(int('2') + int('3'))
s1 = 'He\tllo, \
Wor\\ld\'\"!'
print(s1)
print(s1[0:1])

ls = [1, 2.5, 'test', 3 + 4j, True, [3, 1.63], 5.3]
print(ls)
ls[1] = '2323'
print(ls[1:3])
ls[2:3] = [1 + 2j, 12]
print(ls)
'''

# t = (1, 2.5, 'test', 3 + 4j, [3, 1.63], 5.3)
# print(t)
# print(t[1:3],'\n','123')

# st1 = 'ahat is your name'
# print(st1.capitalize())
# first_name = 'Christ'
# last_name = 'Harrison'
# print('Hello ' + first_name + ' ' + last_name)
# output = 'Hello, {0} {1}'.format(first_name, last_name)
# print(output)
# output = f'Hello, {first_name} {last_name}'
# print(output)
# first_num = input('num1: ')
# second_num = input('num2: ')
# print(int(first_num) ** int(second_num))
# days_in_Feb = 28
# print(str(days_in_Feb) + ' total days in February')
# from datetime import datetime, timedelta

# current_data = datetime.now()
# print(str(current_data))
# print(str(current_data.day))
# print(str(current_data.month))
# print(str(current_data.year))
# print(str(current_data.hour))
# print(str(current_data.minute))
# print(str(current_data.second))
# print(str(current_data.microsecond))

# # birthday = input('When (dd/mm/yyyy)')
# # birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
# # print(str(birthday_date))
# today = datetime.now()
# one_day = timedelta(minutes=10)
# yesterday = today - one_day
# print(str(yesterday))
# x = 10
# y = 0
# try:
#     print(x / y)
# except ZeroDivisionError as e:
#     print('Not allowed to divide by zero.')
# else:
#     print('Something else went wrong.')
# finally:
#     print('This is our cleanup code.')
# price = 1
# if price >= 1.00:
#     tax = .07
# else:
#     tax = 0
# print(tax)
# print()

# country = 'CANADA'
# if country.lower() in ('canada', 'america'):
#     if price == 1:
#         tax = 1
#     elif price == 2:
#         tax = 2
#     print('111')
# elif country.lower() == '12':
#     print('12')
# else:
#     print('1')

# from testinvoke import a
# b = a
# print(b)

# from array import array
# x = {1, 2, 3}  # set
# print(type(x), x)
# x = [1, 2, 3]  # list
# print(type(x), x)
# x = (1, 2, 3)
# print(type(x), x)  # tuple
# print(isinstance(x, tuple))
# y = []
# y.append(98)
# print(y)
# y.append(99)
# print(y)
# z = array('d')
# z.append(97)
# print(z)
# test = x[0:1]
# print(test)

# christopher = {}
# christopher['first'] = 'Christopher'
# christopher['last'] = 'Harrison'

# susan = {'first': 'Susan', 'last': 'Ibach'}
# print(christopher)
# print(susan)

# people = [christopher, susan]
# people.append({'first': 'Bill', 'last': 'Gates'})
# presenters = people[0:2]
# # print(people)
# # print(presenters)
# print(len(presenters))

for name in ['Christopher', 'Susan']:
    print(name)
for index in range(0,5):
    print(index)
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    print(names[index])
    index += 1

people = ['Christopher', 'Susan']
for name in people:
    print(name)

index = 0
while index < len(people):
    print(people[index])
    index = index + 1
    