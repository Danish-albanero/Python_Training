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
    def insertend(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
ll=LinkedList()
ll.insert(55)
ll.insert(55)
ll.insert(55)
ll.insertend(34)
ll.print()


    

    
      
