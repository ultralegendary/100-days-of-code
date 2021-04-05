#day 14
#doubly linked list

#https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    d=DoublyLinkedList()
    f=0
    while(head):
        if(head.data>data and not f):
            d.insert_node(data)
            f=1
        d.insert_node(head.data)
        head=head.next
    if not f:
        d.insert_node(data)
    return d.head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()


#https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
def reverse(head):
    if not head:
        return None
    h=DoublyLinkedListNode(head.data)
    head=head.next
    while(head):
        n=DoublyLinkedListNode(head.data)
        n.next=h
        h.prev=n
        h=n
        head=head.next
    return h

#circular
#https://practice.geeksforgeeks.org/problems/circular-linked-list/1
def isCircular(head):
    l=[]
    while head:
        if head in l:
            return 1
        l.append(head)
        head=head.next
    return 0