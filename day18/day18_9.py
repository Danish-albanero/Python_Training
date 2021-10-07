#9 remove last element
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
    def deleteend(self):
        prev=None
        if self.head is None:
            
            return
        itr=self.head
        
        while itr.next:
            prev=itr
            itr=itr.next
        prev.next = None
ll=LinkedList()
ll.insert(87)
ll.insert(65)
ll.insert(554)
ll.deleteend()
ll.print()
