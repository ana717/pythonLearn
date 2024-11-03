# # 列表  也就是数组
# bike_list = ["1111", "222", "333", "444"]
# print(bike_list)
# #  打印效果：['trek', 'cannondale', 'redline', 'specialized']
# # 根据索引打印 -1 表示倒数第一个
# # print(bike_list[0])

# # 添加元素
# # 末尾添加 append
# bike_list.append("555")
# print("末尾添加一个", bike_list)
# # 指定位置添加 必须写索引， 不写会报错
# bike_list.insert(1, "1.5")
# print("在第二个添加", bike_list)
# # 删除元素
# del bike_list[0]
# print("删除第一个", bike_list)
# # 使用删除的元素 会删除最后一个并打印出来
# # 不输入索引就会默认删除最后一个
# pop_bike = bike_list.pop()
# print("pop 删除的元素", pop_bike)
# # 删除指定元素
# bike_list.remove("222")
# # 排序
# # sort 对列表永久修改， reverse=True 倒序
# print("排序前", bike_list)
# # bike_sort = bike_list.sort() 不会改变原数据， 这样会报错，不会返回新的列表， 因为返回值是None，
# bike_list.sort()
# print("排序hou", bike_list)
# bike_list.sort(reverse=True)
# print("倒序", bike_list)
# # 永久排序 倒叙 不是按字母顺序， 而是按列表顺序

# bike_list.reverse()
# # 临时排序： sorted 不影响原来数组的顺序
# bike_list_temp = sorted(bike_list)
# print("临时排序", bike_list_temp)
# bike_list_sorted = sorted(bike_list, reverse=True)

# # 列表长度
# print("列表长度", len(bike_list))
# 

# 元组 和 列表差不多， 但是不可变， 不能添加， 不能删除， 但是可以修改， 用括号分割
bike_tuple = ("111", "222", "333", "444")
for bike in bike_tuple:
    print(bike)
bike_tuple = ("11", "22", "33")
for bike in bike_tuple:
    print(bike)
