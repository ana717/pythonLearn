import sys

# 1.1.1
# 打印   代码运行    Ctrl + alt + N
print("hellow world!")
# 变量定义
message = "hellow woRld22!"

# 首字母大写
print(message.title())
# 全大写
print(message.upper())
# 全小写
print(message.lower())

# 1.1.2
first_name = "王权"
last_name = "富贵"
# f 字符串。f 是 format（设置格式）的简写，因为 Python 通过把花括号内的变量替换为其值来设置字符串的格式。
full_name = f"{first_name}{last_name}"  # 拼接两个名字
# 写中文会报错
sys.stdout.reconfigure(encoding="utf-8")
print(full_name)

# 删除字符串的空白
name = "1  王权 1 "
# 右侧
print(name.rstrip())
#  左侧
print(name.lstrip())
# 两端
print(name.strip())
# 删除前缀
print(name.removeprefix("1"))
