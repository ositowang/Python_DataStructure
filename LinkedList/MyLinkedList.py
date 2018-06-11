# -*- coding: utf-8 -*-

# 单链表的实现

"""
首先定义节点的类
"""
class Node(object):
    def __init__(self,value=None,next=None):
        self.value,self.next = value,next


""" 链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
"""
class linkedlist(object):
    def __init__(self,maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0 
        self.tailnode = None
    
    def __len__ (self):
        return self.length

    def append(self,value):
        if self.maxsize is not None and len(self)>self.maxsize:
            raise Exception("Linked list is full")
        node = Node(value)  # 构造节点
        tailnode = self.tailnode 
        if tailnode is None: # 还是空链表，追加到root节点之后即可
            self.root.next = node
        else:
            tailnode.next = node  #非空列表，直接追加到tailnode节点之后即可
        self.tailnode = node 
        self.length += 1
    
    def appendleft(self,value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node 
        node.next = headnode
        self.length += 1
    
    def iter_node(self):
        """
        遍历 从head节点到tail节点
        """
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode
    
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    
    def remove(self,value):
        """
        删除包含值的一个节点，将其前一个节点的 next 指向被查询节点的下一个即可
        """
        prevnode = self.root
        curnode = self.root.next
        while curnode.next is not None:
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode: # 如果当前节点是尾节点，更新尾节点
                    self.tailnode = prevnode
                del curnode 
                self.length -= 1
                return 1
            else:
                prevnode = curnode # 如果此次匹配不成功，更新前节点为当前节点，这样找到元素时候才能正确的把指针指到下一个元素
        return -1 


    def find(self,value):
        """
        查找一个节点，返回序号，从 0 开始
        """
        index = 0 
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1
    
    def popleft(self):
        """
        删除第一个节点
        """
        if self.root.next is None:
            raise Exception("pop from empty linked list")
        headnode = self.root.next
        self.root.next = headnode.next 
        self.length -= 1
        value = headnode.value 
        del headnode 
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
    

