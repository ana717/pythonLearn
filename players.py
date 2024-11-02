# 列表切片
# 这是一个切片，包含列表中的前3个元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# 如果没有索引开头, 那么就会默认是0 或结尾
# print(players[2:])
# print(players[:4])
# 复制切片
new_players = players[:]

# try
news = "The first three items in the list are:"
print(news[:3])
