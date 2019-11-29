from datetime import datetime

def print_time():
    print('task complete')
    print(datetime.now())
    print()

def print_time1(task_name):
    print(task_name)
    print(datetime.now())
    print()

def get_time():
    print(datetime.now())

print_time()

for x in range(0, 10):
    print(x)
    print_time1('test')

get_time()
print_time()
