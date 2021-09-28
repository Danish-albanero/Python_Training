#5-Pairwise swap elements of a given linked list

class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("empty")
            return
        itr=self.head
        ss=""
        while itr:
            ss +=str(itr.data) + "-->"
            itr=itr.next
        print(ss)
    def pairswap(self):
        a = self.head
        if a is None:
            return

        while(a and a.next):
            if(a.data!= a.next.data):
                a.data, a.next.data = a.next.data, a.data

            a=a.next.next

ll=LinkedList()
ll.insert(21)
ll.insert(522)
ll.insert(511)
ll.pairswap()
ll.print()
