# 接收用户输入的一行字符
input_str = input()
# 初始化计数器
letter_count = 0  # 英文字符
digit_count = 0   # 数字
space_count = 0   # 空格
other_count = 0   # 其他字符
# 遍历每个字符进行分类统计
for char in input_str:
    if char.isalpha():  # 判断是否为英文字符
        letter_count += 1
    elif char.isdigit():  # 判断是否为数字
        digit_count += 1
    elif char == ' ':  # 判断是否为空格
        space_count += 1
    else:  # 其余情况归为其他字符
        other_count += 1
# 按要求格式输出结果
print(f"英文字符: {letter_count}")
print(f"数字: {digit_count}")
print(f"空格: {space_count}")
print(f"其他字符: {other_count}")
