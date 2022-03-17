# python常用函数、功能

## 基本语法

写if else 时可以
```python
if
else if
else if
```
- 不一定必须是else结尾的，可以清除地展现所有条件


## 内置函数

1.map函数 map() 会根据提供的函数对指定序列做映射

map(function, iterable, ...)

```python
a = list(map(int, str))
```

2.zip函数

将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

```python
a = [1,2,3]
b = [4,5,6]
zipped = list(zip(a,b))  # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
list(zip(*zipped))
# [(1, 2, 3), (4, 5, 6)]
```

3.enumerate 函数

将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中

```python
res = [2,5,6]
for i, elment in enumerate(res):
    print(i, elment)
# 0 2
# 1 5
# 2 6
```

4.sorted 函数

- sorted() 函数对所有可迭代的对象进行排序操作。
- sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。 
- list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作

```python
st = [3,7,5]
ts = "657"
# key = "".join(sorted(st))
key = sorted(st)
print(key) # 输出 [3,5,7]
key1 = sorted(ts)
print(key1) # 输出 ['5','6','7']
```

5.reversed 函数

reversed 函数返回一个反转的迭代器。
```python
str = ['the', 'sky', 'is', 'blue']
print(reversed(str))
# 输出blue is sky the
```


## 常用函数
1.choice() 方法

-返回一个列表，元组或字符串的随机项。

```python
import random # 要导入random
print(random.choice([1, 2, 3, 5, 9]))
# 输出是1,2,3,5,9中的任意一个
```


## 字符串

1.把一个字符串反过来
```python 
a = '234'
b = a[::-1]
```

2.连接字符串
```python
res = '2'
res = res + str(4) # res 在右边连接上4 res变成 24
res = str(8) + res  # res 在左边连接上8 res变成 824
```

3.find()方法
str.find(str, beg=0, end=len(string))
```python
a = '345678'
b = a.find('7')
print(b) # 输出 4 a[4]= '7'
```
- 参数  
- str : 指定检索的字符串
- beg : 开始索引，默认为0。
- end : 结束索引，默认为字符串的长度。

- 返回值 如果包含子字符串返回开始的索引值，否则返回-1。

4.访问字符串的第n个元素
```python
a = '3456'
print(a[2]) # 输出 5
```

5.join 方法
Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

str.join(sequence) # str 指定字符 sequence 指定需要连接的元素序列
```python
s1 = ''
seq = ['r', 'k', 's', 'p']
print(s1.join(seq)) # 输出 rksp
```

6.index 方法

跟find()方法一样，只不过如果str不在字符串中会报一个异常。

```python
seq = 'ihjy'
print(seq.index('j'))
# 輸出 2 
```

7.lstrip() 方法 去除**头部**的字符（不能去除中间）

strip() 方法 用来去除**头部和尾部**字符

rstrip：用来去除**结尾**字符

str.lstrip([chars])
- chars --指定截取的字符。

```python
# 截掉空格
str = "abcddd"
print(str.lstrip('a')) 
# 输出 "bcddd
```

8.split() 方法

通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。

```python
str = "I love china  "
str = str.split()
print(str)
# ['I', 'love', 'china']
```



## 数组

pop() 函数
- 用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
```python
res = [2, 3, 4]
res.pop(0) # 2 res = [3,4]
```


















