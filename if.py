# if else
# 跟js差不多 == 或 !=
# 多个条件  and ，or
# 检查是否在列表中
list = ["a", "b"]
ex = "a" in list
print(ex)
# 检查不在列表中
ex2 = "c" not in list
print(ex2)

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
