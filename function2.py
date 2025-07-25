def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 生成前10个斐波那契数
print(list(fibonacci(10)))  