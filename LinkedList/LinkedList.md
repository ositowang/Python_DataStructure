# 单链表
和线性结构不同，链式结构内存不连续的，而是一个个串起来的，这个时候就需要每个链接表的节点保存一个指向下一个节点的指针。
这里可不要混淆了列表和链表（它们的中文发音类似，但是列表 list 底层其实还是线性结构，链表才是真的通过指针关联的链式结构）。
看到指针你也不用怕，这里我们用的 python，你只需要一个简单赋值操作就能实现，不用担心 c 语言里复杂的指针。

先来定义一个链接表的节点，刚才说到有一个指针保存下一个节点的位置，我们叫它 next， 当然还需要一个 value 属性保存值

```py
class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```
然后就是我们的单链表 LinkedList ADT

```py
class LinkedList(object):
    """ 链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """
```

来看下时间复杂度：

链表操作                      | 平均时间复杂度 |
------------------------------|----------------|
linked_list.append(value)     | O(1)           |
linked_list.appendleft(value) | O(1)           |
linked_list.find(value)       | O(n)           |
linked_list.remove(value)     | O(n)           |


# 双链表
# 循环双端队列
单链表虽然 append 是 O(1)，但是它的 find 和 remove 都是 O(n)的，
因为删除你也需要先查找，而单链表查找只有一个方式就是从头找到尾，中间找到才退出。
这里我之前提到过如果要实现一个 lru 缓存（访问时间最久的踢出），我们需要在一个链表里能高效的删除元素，
并把它追加到访问表的最后一个位置，这个时候单链表就满足不了了，
因为缓存在 dict 里查找的时间是 O(1)，你更新访问顺序就 O(n)了，缓存就没了优势。
