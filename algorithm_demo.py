# -------------------------------排序------------------------------------
# 格式 sorted(iterable, key=None, reverse=False)
a = [2, 3, 56, 32, 12, 7, 10]
b = sorted(a)
print(b)
# 不会影响输入参数a
print(a)

# a是一个存储了tuple的列表
a = [('c', 1), ('z', 4), ('a', 5), ('e', 2), ('g', 6)]
print(a)
# 使用 key 指定 sorted() 按照 tuple 的第 2 个值进行排序，并且降序排序
b = sorted(a, key=lambda x: x[1])
print(b)

# 对列表 list 的排序方法有两种：
# 调用系统的排序函数 sorted(a)，这个函数返回一个新的有序列表，而不影响输入的列表的。
# 使用列表 list 的函数 a.sort()，这个函数直接对列表进行排序，是原地排序的，无返回值。

# 对哈希表排序只能用sorted函数

a = 3
print(-(a))