import matlab
import matlab.engine
import time
import operator
start=time.perf_counter()
engine = matlab.engine.start_matlab()
a=engine.add1(2,3)
print(a)
print("测试画图")
engine.eval("b = [1,2,3,4,5];",nargout=0)
engine.eval("plot(b)")
print("测试画图结束")
end=time.perf_counter()
print("final is in ",end-start)
input("请输入任意字符继续...")
operator.add(2,3)