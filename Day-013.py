


#https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node


# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    while(head):
        print(head.data)
        head=head.next

if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)



#https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    n=0
    temp=head
    while temp:
        n+=1
        temp=temp.next
    temp=head
    new=SinglyLinkedList()
    for i in range(n,0,-1):
        temp=head
        for j in range(i-1):
            temp=temp.next
        new.insert_node(temp.data)
        
        
    return new.head
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()



#https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
import os
import sys
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    
    while llist1 and llist2:
        if llist1.data!=llist2.data:
            return 0
        llist1,llist2=llist1.next,llist2.next
    return not(llist1 or llist2)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()


#https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
def mergeLists(head1, head2):
    new=SinglyLinkedList()
    while head1 and head2:
        if head1.data< head2.data:
            new.insert_node(head1.data)
            head1=head1.next
        else:
            new.insert_node(head2.data)
            head2=head2.next
    while head1:
        new.insert_node(head1.data)
        head1=head1.next
    while head2:
        new.insert_node(head2.data)
        head2=head2.next
    return new.head


#https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
def getNode(head, p):
    n,h=0,head
    while h:
        n+=1
        h=h.next
    n=n-p
    h=head
    for i in range(n-1):
        h=h.next
    return h.data

#https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
def removeDuplicates(head):
    a=head.data
    s=SinglyLinkedList()
    s.insert_node(a)
    while head:
        if a==head.data:
            head=head.next
        else:
            a=head.data
            s.insert_node(a)
            head=head.next
    return s.head

#https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
def has_cycle(head):
    l=[]
    while head:
        if head in l:
            return 1
        else:
            l.append(head)
            head=head.next
    return 0

#https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
def findMergeNode(head1, head2):
    l=[]
    while head1:
        l.append(head1)
        head1=head1.next
    while head2:
        if head2 in l:
            return head2.data
        head2=head2.next
        
        