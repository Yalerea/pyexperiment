# 1
def count_developers(lst):
    lst2 = [d for d in lst
            if d['continent']=='Europe' and d['language']=='JavaScript']
    return len(lst2)

# 2
def zero(fun=None): return fun(0) if fun else 0 
def one(fun=None): return fun(1) if fun else 1
def two(fun=None): return fun(2) if fun else 2
def three(fun=None): return fun(3) if fun else 3
def four(fun=None): return fun(4) if fun else 4
def five(fun=None): return fun(5) if fun else 5
def six(fun=None): return fun(6) if fun else 6
def seven(fun=None): return fun(7) if fun else 7
def eight(fun=None): return fun(8) if fun else 8
def nine(fun=None): return fun(9) if fun else 9

def plus(y): return lambda x:x+y
def minus(y): return lambda x:x-y
def times(y): return lambda x:x*y
def divided_by(y): return lambda x:x//y

# 3
# filter():过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
# filter(function, iterable)
def shorten_number(suffixes, base):
    def filter(data):
        try:
            number = int(data)
            
        except (TypeError, ValueError):
            return str(data)
        
        else:
            i = 0
            
            while number//base>0 and i<len(suffixes)-1:
                number = number//base
                i = i + 1
            return str(number) + suffixes[i]
        
    return filter
        
# 4
def find_senior(lst): 
    max_age = max(d['age'] for d in lst)
    
    return [d for d in lst if d['age']==max_age]

# 5
# 1、将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。
# 示例：
# add = lambda x, y: x+y
# 相当于定义了加法函数lambda x, y: x+y，并将其赋值给变量add，这样变量add就指向了具有加法功能的函数。
# 这时我们如果执行add(1, 2)，其输出结果就为 3。
# 2、将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。
# 3、将lambda函数作为参数传递给其他函数。
from inspect import signature
from functools import partial

def curry_partial(main_func, *args):
    
    if not(callable(main_func)):
        return main_func
    
    p = len(signature(main_func).parameters)
    func = partial(main_func)
    
    for a in args:
        if len(func.args) == p: break
        func = partial(func, a)
    
    if len(func.args) < p:
        return partial(curry_partial, main_func, *func.args)

    return func()


