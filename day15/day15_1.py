#1- Insertion , deletion,length of linked list
class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next
class linked:
    def __init__(self):
        self.head = None
    def insert(self,data):
        node = Node(data, self.head)
        self.head = node

    def end(self,data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = Node(data,None)
    def disp(self):
        if self.head is None:
            return print("empty")
        else:
            itr = self.head
            while itr:
                print(itr.data," --> ",end="")
                itr = itr.next
    def insertAt(self, pos,data):
        if pos == 0:
            self.insert(data)
            return
            
        i=0
        itr = self.head
        while itr:
            if i == pos-1:
                n = Node(data, itr.next)
                itr.next = n
                break
            
            itr = itr.next
            i += 1
            
    def dele(self,pos):
        if pos == 0:
            self.head = self.head.next
            return
        else:
            i=0
            itr = self.head
            while itr:
                if i == pos-1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                i +=1
    def get_len(self):
        i=0
        itr = self.head
        while itr:
            
            itr = itr.next
            i +=1
        print('length is', i)
            
        
        
            
        
l= linked()
l.insert(5)
l.insert(4)
l.insert(3)
l.insert(2)
l.end(6)
l.insertAt(0,21)
#l.dele(2)
l.get_len()
l.disp()
