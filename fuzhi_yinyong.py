# 赋值和引用
a=12
b=a
print(id(a),id(b))
b=13
print(id(a),id(b))
# 起初b=a,b获得了a的引用,所以ab的地址相同,而给b赋新值时,重新创建了对象,然后把b贴上去了,所以之后ab的地址不同.

mylist= [12,13,1234]
anotherlist = mylist
anotherlist.append(999)
print(mylist,id(mylist),id(anotherlist))
del mylist[0]
print(anotherlist,mylist)

del anotherlist
print(mylist,id(mylist))

alist = [12,12,12,[12,23],23213]
blist = alist[:]
blist.append(777)
blist[3][0]=21
alist[3][1]=32
print(alist,blist)