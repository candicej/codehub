# 解题思路：一旦出现键和值，就要使用Hash表，在O(1)时间内找到键和值
# 对于有出入顺序的问题，想到栈、队列或者链表

# 需要随机访问
# 需要设置把数据源插入头部或者尾部
# 结合双向链表和Hash表
# 哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。
# 首先使用哈希表进行定位，找出缓存项在双向链表中的位置，随后将其移动到双向链表的头部，即可在 O(1)O(1) 的时间内完成 get 或者 put 操作。具体的方法如下
# 参考https://leetcode-cn.com/problems/lru-cache/solution/lru-ce-lue-xiang-jie-he-shi-xian-by-labuladong/ 原理
# https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/ 代码


# -------3.14 更新---------------------------------------------------------------------------------------------------
# LRU的操作：
# 新的数据插入队头，最久未使用的排在队尾
# 访问已有的数据，需要提前至队头
# 缓存容量已满，需要删除内容空出位置
# 优先删除久未使用的数据，也就是队尾的数据：双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的

# LRU算法设计
# put和get方法的时间复杂度为O(1) 需要插入块，查找快，删除快，有顺序之分
# 哈希表查找快，但是数据无固定顺序；链表有顺序之分，插入删除快，但是查找慢。所以结合一下，形成一种新的数据结构：哈希链表
# 使用双向链表，删除一个节点不光要得到该节点本身的指针，也需要操作其前驱节点的指针，而双向链表才能支持直接查找前驱，保证操作的时间复杂度 O(1)。


class DLinkedNode:
    # 双链表
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # hash 表 包含链表的位置信息 可以通过O(1)时间去访问链表
        self.cache = dict()
        # 使用伪头部和伪尾部节点  方便插入和删除操作
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        # 容量
        self.capacity = capacity
        # 现在已经有了多少元素
        self.size = 0

    def get(self, key: int) -> int:
        # 不存在
        if key not in self.cache:
            return -1
        # 通过字典里 key的值找到 key在链表的位置
        node = self.cache[key]
        # 移动到头部
        self.moveToHead(node)
        # 返回值
        return node.val

    def put(self, key: int, value: int) -> None:
        # key值在链表中有了
        if key in self.cache:
            node = self.cache[key]
            # 更改值
            node.val = value
            self.moveToHead(node)
        else:
            # 创建一个链表节点
            node = DLinkedNode(key, value)
            # cache中存储节点的位置 指向链表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            # 如果超出容量，删除双向链表的尾部节点
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removedTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1

    def addToHead(self, node):
        # 新插入节点的前一个节点是伪头部节点
        node.prev = self.head
        # 新插入节点的后一个节点是伪头部节点的原先的下一个节点
        node.next = self.head.next
        # 双向链表 所以还需要再指向一边
        # 伪头部节点的原先的下一个节点的前一个节点是node
        self.head.next.prev = node
        self.head.next = node

    def removedNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removedNode(node)
        self.addToHead(node)

    def removedTail(self):
        node = self.tail.prev
        self.removedNode(node)
        return node









