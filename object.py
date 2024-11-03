# 字典  就是js中的对象
cat = {'color': 'red', 'age': 3}
# 获取字典中的值
print(cat['color'])
# 新增键值对
cat['name'] = 'kitty'
#  删除键值对
del cat['age']
# 获取键值对的key值没有的时候会报错， 可以用get获取
print(cat.get('age', 'no age'))
# 在调用 get() 时，如果没有指定第二个参数且指定的键不存在，Python 将返回值 None
