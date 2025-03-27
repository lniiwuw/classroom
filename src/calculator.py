def add(a, b):
    """返回两个数的和"""
    return a + b

def subtract(a, b):
    """返回两个数的差"""
    return a - b

def multiply(a, b):
    """返回两个数的积"""
    return a * b

def divide(a, b):
    """
    返回两个数的商
    :raises ValueError: 当除数为0时
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(num):
    """检查数字是否为偶数"""
    return num % 2 == 0