# 遍历列表
magicians = ['alice', 'david', 'carolina']
# 缩进很重要， 根据缩进来判断循环的结束
# ： 冒号也很重要！ 没有冒号，就没有循环了
for magician  in magicians:
    print(magician)
    print("下一个")
print("完成了")

# 获取index  enumerate(）函数 返回枚举对象
for index, magician in enumerate(magicians):
    print(magician)
    print(index)
print("完成了2.0")

# 创建数值列表
#  使用 range() 函数
for value in range(1, 5):
    print(value)
# 打印结果 1  2 3 4 没有5
# 创建数字列表
numbers = list(range(6))
print(numbers)
# [0, 1, 2, 3, 4, 5]
# 设置步长, 第三位就是步长
list(range(0, 10, 2))
# 列表最小值
min(numbers)
# 列表最大值
max(numbers)
# 列表求和
sum(numbers)
