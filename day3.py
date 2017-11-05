# coding=UTF-8
# liuyang
from collections import Iterable
import os

def power(x, n=2):
    s = 1

    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender, age = 6, city = 'Beijing'):
    print 'name:', name
    print 'age:', age
    print 'gender:', gender
    print 'city:' , city

def add_end(L=[]):
    L.append('end')
    return L

def add_end_1(L=None):
    if L is None:
        L = []
    L.append('end')
    return L

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def calc_1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:',  kw

def Iteration(L=[]):
    for key in L:
        print key

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a+b
        n = n + 1

def fib_1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
def f(x):
    return x * x

def add(x, y):
    return x + y
def fn(x, y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def strChange(str):
    return str.capitalize()
def prod(l):
    return reduce(lambda x,y: x*y, l)
if __name__ == '__main__':
    '''
    print power(31,5)

    name = ['Micheal', 'Sarah', 'Tracy']
    print name[0:2]
    print name[:2]
    l = range(100)
    print l[:10:2]
    #enroll('liuyang','F')
    #enroll('ly', 'F', city='xi\'an')
    #print add_end([1, 2, 3])
    #print add_end()
    #print add_end()#默认参数要指定不变对象
    #print add_end_1()
    #print add_end_1()
    #print calc([1, 2, 3])
    #print calc_1(1, 2, 3)
    #print calc_1(0)
    #person('Bob', 35, city = 'Beijing')
    #Iteration([1, 3, 5])
   
    d = {'a': 1, 'b': 2, 'c': 3}
    for value in d.itervalues():
        print value

    for k, v in d.iteritems():
        print k, v

    print isinstance(d, Iterable)

    for i, value in enumerate(['A', 'B', 'C']):
        print i, value
 
    print range(1, 11)

    print [x * x for x in range(1, 11)]

    print [x * x for x in range(1, 11) if x % 2 == 0]

    print [m + n for m in 'ABC' for n in 'XYZ']

    print [d for d in os.listdir('.')]

    L = ['Hello', 'World', 'IBM', 'Apple']

    print [s.lower() for s in L]

    L = ['Hello', 'World', 18, 'Apple', None]

    print [s.lower() for s in L if isinstance(s, str)]

    print [isinstance(s,str) and s.lower() or s for s in L]

    print [s.lower() if isinstance(s,str) else s for s in L ]

    g = (x * x for x in range(10))
    print  g.next()
  
    fib(5)
    for n in fib_1(6):
        print n 
   
    print f(-10)
    print map(f, [1,2,3,4,5,6,7,8,9])
    print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]) 

    print reduce(add, [1, 3, 5, 7])
    print reduce(fn, [1, 3, 5, 7, 9])
    print reduce(fn, map(char2num, '13579'))
    
    '''
    print map (strChange, ['adam', 'LISA', 'barT'])
    print prod([1, 3, 5 ,7])