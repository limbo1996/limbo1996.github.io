"""
Author: limbo1996
Date: 2021-04-12 21:54:52
LastEditTime: 2021-04-12 21:55:05
FilePath: /limbo1996.github.io/_test/test.py
"""
# 用f.string取代str.format方法

a = 0b10111011
b = 0xC5F

print("Binary is %d, hex is %d" % (a, b))
# Binary is 187, hex is 3167
"""
%的意义是右面对应的数值会以不同形式替换原来的内容， 
这来自C语言的printf函数，其中的不同选项%s, %x, %f在python中都有，
并且还可以指定填充和对齐方式，以及控制小数点的位数
"""
"""
这种风格主要有四个缺点：
* 如果%右侧的值在类型和顺序上有变化，程序可能会发生错误
"""
key = "my_var"
value = 1.234
formatted = "%-10s = %.2f" % (key, value)
print(formatted)
# my_var     = 1.23
# 但是如果把key和value互换位置
reordered = "%-10s = %.2f" % (value, key)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: must be real number, not str
# 不出意外的会报错

"""
* 填充模板前，往往要对准备填进去的值做修改，但是这样会让表达值变得更长更加混乱
"""
pantry = [("avocados", 1.25), ("banbanas", 2.5), ("cherries", 15)]
for i, (item, count) in enumerate(pantry):
    print("#%d: %-10s = %.2f" % (i, item, count))

# 如果想要对打印信息做出调整
for i, (item, count) in enumerate(pantry):
    print("#%d: %-10s = %.2f" % (i + 1, item.title(), round(count)))
# 表达式会进一步拉长

"""
* 如果想一个值填充多次，必须在%右端多次重复，
* 而如果想更新某个值， 也必须多次修改
"""
"""
为了解决上面的问题，python的%允许用dict取代tuple，
这样就可以让格式字符串的说明符与dict的键对应起来，
这样解决了上述第一个问题，右侧的顺序不再重要，同时解决了第三个问题
多个相同值需要替换时不在需要重复，但是这让问题二更甚，
字典化让表达式更加冗长
"""
old_way = "%-10s = %.2f" % (key, value)

new_way = "%(key)-10s = %(value).2f" % {"key": key, "value": value}
reordered = "%(key)-10s = %(value).2f" % {"value": value, "key": key}

assert old_way == new_way == reordered
# python3 添加了高级字符串格式化方法，不再使用%操作符，
# 只需要调用format函数即可

a = 1234.5678
formatted = format(a, ",.2f")
# 逗号表示显示千位分隔符
print(formatted)

b = "my string"
formatted = format(b, "^20s")
# ^表示居中对齐
print(formatted)

key = "my_var"
value = 1.234

formatted = "{} = {}".format(key, value)
print(formatted)

formatted = "{:<10} = {:.2f}".format(key, value)
print(formatted)