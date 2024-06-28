
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=node('10')
node2=node('20')
node3=node('30')

node1.next=node2
node2.next=node3  

def remove(head,value):
    current=head
    prev=None
    
    if current is not None:
        if current.data == value:
            head=current.next
            current=None
            return head
        
        while current is not None:
            if current.data == value:
                break
            prev=current
            current=current.next
        
        if current == None:
            return head
        prev.next=current.next
        current=None
        
        return head    

def display(head):
    current=head
    while current is not None:
        print(current.data, end="->")
        current=current.next
    print('None')
    
def get_length(head):
    current=head
    length=0
    while current is not None:
        length+=1
        current=current.next
    return length    

length=get_length(node1)
print(f'length  of node is : {length} ')

new_node = node('50')
current = node1

while current.next is not None:
    current = current.next

current.next = new_node
        

display(node1)
node1=remove(node1,'20')
node1=remove(node1,'50')
length=get_length(node1)
print(f'length  of node is : {length} ')
display(node1)   

class student:
    def __init__(self,name,marks,age):
        self.name=name
        self._age=age
        self.__marks=marks
        
    def set_mark(self,marks):
        self.__marks=marks
        
    def get_marks(self):
        return self.__marks
    def print(self):
        return self.__marks
        
obj= student('ashwini',79,24)
print(obj.name)
print(obj.get_marks())
print(obj._age)
obj.set_mark(85)
print(obj.get_marks())          


stack=[]
stack.append('10')
stack.append('20')
print(stack)
print(stack.pop())
print(stack)

queue=[]
queue.append('1')
queue.append('2')
print(queue)
print(queue.pop(0))
print(queue)

list=['apple','mango','kiwi']
l=[]
for i in list:
    if 'a' in i:
        l.append(i)

print(l) 

d={'name':'Ash','age':24}
print(d)
print(d['age'])
set={3,2,4,3,7,6,1,2}
print(set)

a=lambda x,y:x*y
print(a(7,19))

def func(*arg):
    for i in arg:
        print(i)
func(1,2,3)  

def func(**kwarg):
    for key,value in kwarg.items():
        print(f'{{"key":"{key}","value":"{value}"}}')
func(name='ash',age=23)

def decorator(func):
    def wrapper():
        print('tansaction processing')
        func()
        print('transaction completed')
    return wrapper
    
def hello():
    print('excuting all the step of transaction')

h1=decorator(hello)
h1()

#control statement
for i in range(1,9):
    if i ==5:
     break
    print(i)
for i in range(1,10):
    if i ==5 or i==7:
        continue
    print(i)
for i in range(1,6):
    if i==5:
        pass
    print(i)
#iterator  
mytupe=(1,3,4,5)
my=iter(mytupe)

print(next(my))
print(next(my)) 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node('10')
node2 = Node('20')
node3 = Node('30')

node1.next = node2
node2.next = node3

def remove(head, value):
    current = head
    prev = None
    
    if current is not None:
        if current.data == value:
            head = current.next
            current = None
            return head
        
        while current is not None:
            if current.data == value:
                break
            prev = current
            current = current.next
        
        if current is None:
            return head
        
        prev.next = current.next
        current = None
        
        return head

def display(head):
    current = head
    while current is not None:
        print(current.data, end="->")
        current = current.next
    print("None")

display(node1)
node1 = remove(node1, '20')
display(node1)

def decorator(func):
    def wrapper():
        print('Transaction Processing')
        func()
        print('transcation completed')
    return wrapper
def hello():
    print('excute all the step of transaction')

hello1=decorator(hello)
hello1()

class p:
    def p_func(self):
        print(' this P_class function ')
        
class d:
    def p_func(self):
        print('this is a D_class function')
        
def make(animal):
    animal.p_func()

obj_d=d()
obj_p=p()
make(obj_d)
make(obj_d)

def func(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(" ",end="")
        k=k-1
        
        for j in range(0,i+1):
            print('*',end=" ")
        print()
n=5
func(n)                
    
