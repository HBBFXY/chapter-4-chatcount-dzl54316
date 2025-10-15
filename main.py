# 接收用户输入的一行字符
input_str = input()

# 初始化计数器
letter = 0  # 英文字符（仅a-z、A-Z）
digit = 0   # 数字（0-9）
space = 0   # 空格
other = 0   # 其他字符

# 遍历字符并分类统计
for char in input_str:
    # 判断是否为英文字符（限定a-z、A-Z）
    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        letter += 1
    # 判断是否为数字
    elif '0' <= char <= '9':
        digit += 1
    # 判断是否为空格
    elif char == ' ':
        space += 1
    # 其余归为其他字符
    else:
        other += 1

# 按作业要求格式输出
print(f"英文字符: {letter}")
print(f"数字: {digit}")
print(f"空格: {space}")
print(f"其他字符: {other}")
