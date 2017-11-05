# coding=UTF-8
# liuyang
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

#可以使用尾递归对递归函数的多次调用导致栈
def fact_1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

if __name__ == '__main__':
    print fact(5)
    print fact_1(1000)
