def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 测试10以内的素数
for i in range(10):
    print(f"{i} 是素数: {is_prime(i)}")  