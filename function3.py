def is_palindrome(s: str) -> bool:
    """判断字符串是否为回文数（忽略大小写、空格和非字母数字字符）"""
    # 预处理：转换小写并过滤非字母数字字符
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    
    # 双指针法检查回文
    left, right = 0, len(filtered_chars) - 1
    while left < right:
        if filtered_chars[left] != filtered_chars[right]:
            return False
        left += 1
        right -= 1
    
    return True

user_input = input("请输入一个字符串，我会判断它是否为回文: ")

# 使用用户输入进行判断并输出结果
if is_palindrome(user_input):
    print(f"'{user_input}' 是回文。")
else:
    print(f"'{user_input}' 不是回文。")