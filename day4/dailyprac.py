'''
1-Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.


def binary(arr,low, high, target):
    if(low<high):
        mid = (low + high)//2
        if arr[mid] == target:
            return 1
        elif target< arr[mid]:
            return binary(arr,low,mid-1,target)
        elif target > arr[mid]:
            return binary(arr,mid+1,high,target)
    else:
        return -1
arr=[1,2,3,4,6,7,8,9]
k=int(input())
low=0
high=len(arr)-1
a=binary(arr,low,high,k)
if(a == 1):
    print("found")
else:
    for i in range(len(arr)):
        if arr[i]<k:
            continue
        else:
            print("if target exist then its index would be: ",i)
            break
-----------------------------------------------------------------------------
'''



'''
2-Largest sum in Contiguous Subarrays


def MaxSubSum(arr):
    max=0
    cur=0

    for i in range(len(arr)):
        cur = cur + arr[i]
        if(cur > max):
            max = cur
        if(cur<0):
            cur =0

    return max

arr=[5,-3,-2,6,1]

a=MaxSubSum(arr)
print(a)
------------------------------------------------------------------------------------
'''
        



'''
3-Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.


nums = [-1,0,1,2,-1,-4]
list1=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(i+2,len(nums)):
            if (nums[i]+nums[j]+nums[k]) == 0:
                list1.append(nums[i])
                list1.append(nums[j])
                list1.append(nums[k])
                list1.append("--")

print(list1)
------------------------------------------------------------------------------
'''



'''
4-Find First and Last Position of Element in Sorted Array


list1 = [5,7,7,8,8,10]
target=int(input())
li=[] #to store occurence


j=len(list1)-1
for i in range(len(list1)):
    if list1[i] == target:
        
        li.append(i)
        break

for j in range(len(list1)-1,0,-1):
    if list1[j] == target:
        
        li.append(j)
        break
print(li)
---------------------------------------------------------------------
'''



'''
5-Given an array of strings strs, group the anagrams together.
You can return the answer in any order

list1 = ["eat","tea","tan","ate","nat","bat"]
li=[]
for i in range(len(list1)):
    #str=list1[i]
    for j in range(i+1,len(list1)):
        #str2=list1[j]
        if sorted(list1[i]) == sorted(list1[j]):
            li.append(list1[i])
            li.append(list1[j])
print(li)
----------------------------------------------------------------
'''



'''
6-Print first letter of every word in the string


s=input()
v=True
St=""

for char in s:
    if char == " ":
        v=True
    elif char !=" " and v == True:
        St += char + " "
        v = False
print(St)
-------------------------------------------------------------------
'''
'''
7-Wave Array

n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))
i=0

while(i<n-1):
    temp=li[i]
    li[i]=li[i+1]
    li[i+1]=temp
    i+=2
print(li)
-----------------------------------------------------------
'''



'''
8-Linked list insertion operation

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
ll.insert(23)
ll.insert(42)
ll.insert(532)
ll.insertend(35)
ll.print()
------------------------------------------------------------------------
'''



'''
9-Delete Nth node from the end of the given linked list
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

-----------------------------------------------------------------------------
'''



'''
10-Pairwise swap elements of a given linked list

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
---------------------------------------------------------------------------------

'''

        
        


        


    
    
        























               

