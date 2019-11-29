import time
import operator
start=time.perf_counter()
'''
    程序执行
'''
print(operator.add(2,3))
end=time.perf_counter()
print("final is in ",end-start)
