
#check how many sentence in string is vowels or consonants
'''
string=input("enter a string:")
vowels=0
consonant=0

for i in string:
    if i in ('a','e','o','i','u','A','I','O','E','U'):
        vowels+=1
    elif i.isalpha():
        consonant+=1
print("vowels",vowels,"Consonant",consonant)
'''

#removing space
'''
string=input("enter a string : ")

result=''

for i in string:
        if i != ' ':
              result+=i
print("String after removing the spaces:", result)  
'''
#convert fahrenheit to celusis
'''
fahrenheit=float(input('please give you fahreheit value :'))
celusis=((fahrenheit-32)*5)/9
print("celusis",celusis)
'''

# find smallest number
'''
a=int(input('enter a value for a : '))
b=int(input('enter a value for b : '))
c=int(input('enter a value for c : '))

if a<=b and a<=c:
    print("a is smallest")
elif b<=a and b<=c:
    print("b is smallest")
elif c<=a and c<=b:
    print("c is smallest")        
'''  

#factorial using recursion
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

num=int(input('enter a value to check factorial : '))

if num < 0:
    print('factorial is not calculated in negative')
elif num ==0:
    print('factorial is 1')
else:
    print('factorial is',num,'is',fact(num))        
'''
#without recursion
'''
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *=i
    return result


num=int(input('enter a number to calculate its factorial : '))
result=fact(num)
print(f"factorial of {num} is {result}")
'''

#LCM
'''
num1=int(input('enter a first number'))
num2= int(input('enter a second number'))

if num1>num2:
    greater=num1
else:
    greater=num2

while(True):
    if(greater % num1==0 and greater % num2==0):
        lcm=greater
        break
    greater+=1
print('LCM is',num1,'and',num2,'is',greater)          
'''

#even or odd
'''
num=int(input('enter a number to check even /odd : '))

if(num%2==0):
    print('number is even')
else:
    print('number is odd')    
'''

#check vowel or consonant
'''
ch=input('enter a character to check vowel/consonant : ')

if(ch=='a' or ch=='A' or ch=='i'or ch=='I' or ch=='e' or ch=='E' or ch=='o' or ch=='O' or ch=='u' or ch=='U'):
    print("character",ch, "is vowel")
else:
    print("character",ch,"is consonant")    
'''
#square
'''
num=int(input('enter a number : '))

print('square is',num*num)
'''

#cube
'''
num=int(input('enter a number : '))

print('cube is',num*num*num)
'''
# find Largest number
'''
a=int(input('enter a value for a : '))
b=int(input('enter a value for b : '))
c=int(input('enter a value for c : '))

if a>=b and a>=c:
    print("a is largest")
elif b>=a and b>=c:
    print("b is largest")
elif c>=a and c>=b:
    print("c is largest")        
'''

#pattern alphabate
'''
def contalpha(n):
    num=65
    for i in range(0, n):
        for j in range(0, i+1):
            ch=chr(num)
            print(ch, end=" ")
            num = num + 1
        print()
n=8
contalpha(n)    
'''

#number pattern
'''
def number(n):
    num=1
    for i in range(0, n):
        for j in range(0, i+1):
            print(num, end=" ")
            num= num+1
        print()
n=5
number(n)
'''
#repeat same number pattern
'''
def renum(n):
    num=1
    for i in range(0, n):
        for j in range(0, i+1):
            print(num, end=" ")
        num=num+1
        print()
n=5
renum(n)
'''            

#alphabate repeat pattern
'''
def alpha(n):
    num=65
    for i in range(0,n):
        for j in range(0, i+1):
            ch=chr(num)
            print(ch, end=" ")
        num=num+1
        print()
n=5
alpha(n)          
'''  

#pattern number start from 1
'''
def number(n):
    num=1
    for i in range(0,n):
        num=1
        for j in range(0, i+1):
            print(num, end=" ")
            num=num +1
        print()
n=5
number(n)         
'''
# * pattern
'''  
def myfunc(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print('*',end="")
        print()
n=5
myfunc(n)            
'''

# * center pattern 
'''
def myfunction(n):
    k = n-1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*", end=" ")
        print()
n=5
myfunction(n)
'''

#find number is posttive or negative
'''
num=float(input('enter a number: '))
if num > 0:
    print('Postive number')
elif num == 0:
    print('zero')
else:
    print('negative number')        
'''
#write a program to find sum of two number
'''
num1=int(input('enter a first number : '))
num2=int(input('enter a second number : '))

print('sum of number is',num1+num2)
'''

#check the prime or not
'''
n=int(input('enter a number'))
count=0
for i in range(1,n+1):
    if n%i==0:
        count = count+1
if count == 2:
    print('prime number')
else:
    print("Composite number")            
'''
# check the number is palindrome number
'''
n=int(input('enter a number : '))
copy=n
rev=0
while n > 0:
    z = n%10
    rev = rev * 10 + z
    n = n//10 
if copy == rev:
    print('Palindrome number')
else:
    print('Not Palindrome number')   
'''
# reverse number
'''
n=int(input('enter a number : '))
rev=0
while n>0:
    z = n%10
    rev = rev * 10 + z
    n = n//10
print(rev)    
'''

#how many factors of PARTICULAR number
'''
n=int(input('enter a number : '))
for i in range(1, n+1):
    if n%i == 0:
        print(i)
'''
#fibonacci squence
'''
n=int(input('enter a number : '))
count=0
n1, n2=0,1

if n<=0:
    print('please enter apostive number')
elif n==1:
    print('fibonacci squence upto',n,':')
else:
    print('fibonacci sequence')
    while count < n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count +=1    
 '''  
# calculate the fibonacci number at given position
'''
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function with an example
n = int(input("Enter the position to find the Fibonacci number: "))
fib_number = fibonacci_iterative(n)
print(f"The Fibonacci number at position {n} is {fib_number}.")
'''

#leap year
'''
year=int(input('enter a year'))

if (year % 4 == 0) and (year % 100 != 0):
    print(f'{year} is leap year')
elif(year % 100 == 0) and  (year % 400 == 0):
    print(f'{year} is leap year')  
else:
    print('not a leap year')     
'''

#how factors of your numbers
'''
n=int(input('enter a number : '))
count=0
for i in range(1, n+1):
    if n%i == 0:
        print(i)
        count=count+1
'''        

#reverse string
'''
s=input('enter a string : ')
reversed_string = s[::-1]
print(reversed_string)
'''

#maximum of two number
'''
def maximum(num1,num2):
    if num1>= num2:
        return num1
    else:
        return num2
    
num1=int(input('enter a number : '))
num2 =int(input('enter a number : '))

print(maximum(num1,num2))
'''
#minimum of two number
'''
def minimum(a,b):
    if a<=b:
        return a
    else:
        return b
    
a= int(input('enter a number : '))
b= int(input('enter a number : '))

print(minimum(a,b))
'''

#check number is armstrong
'''
num = int(input('enter a number : '))
sum = 0
temp = num
while temp >0:
    digit = temp %10
    sum +=digit ** 3
    temp//=10

if num==sum:
    print(num,'number is armstrong')
else:
    print(num,'not a armstrong number')    
'''
#alphabate in center
'''
def alpha(n):
    k = n - 1
    num = 65  # ASCII value for 'A'
    
    for i in range(0, n):
        # Print leading spaces
        for j in range(0, k):
            print(" ", end="")


        k = k - 1
        
        # Print letters in the pattern
        for j in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1  # Move to the next letter
        
        # Move to the next line
        print()

n = 5
alpha(n)
'''


#pattern right side 
'''
def pattern(n):
    k = n - 1
    for i in range(0, n):
        # Print leading spaces
        for j in range(0, k):
            print(" ",end="")
        k = k - 1
        
        # Print the asterisks for the current row
        for j in range(0, i + 1):
            print('*', end="")
        print()  # Move to the next line

n = 8
pattern(n)

'''

#plaindrom string
'''
s=input('enter a string : ')
b=''
for i in range(len(s)-1,-1,-1):
    b=b +s[i]

if s==b:
    print('palindrom string')
else:
    print('not palindrom string')    
'''
# count how many sdigit,special charachert and alphate in given string

str='@34!%&hryesjp*9'
chr=0
digi=0
spchr=0

for i in str:
    if i.isdigit():
        digi=digi+1
    elif i.isalpha():
        chr=chr + 1
    else:
        spchr=spchr+1     

print(f"your counting are\nnumber={digi}\ncharater={chr}\nspecialcharacter={spchr}")           

#maximum in list
'''
l=[56,89,80,67,45,23]
print(max(l))
'''
#minimum in list
'''
l=[9,8,6,4,2]
print(min(l))
l[0],l[-1]=l[-1],l[0]
print(l)
#length of list
print(len(l))
#swap the two elment in the list
def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
    
list=[5,7,8,5,9,3]
pos1,pos2=1,3
print(swap(list,pos1-1,pos2-1))
#reversed the string
str='hello world all good'
s=str.split()[::-1]
li=[]
for i in s:
    li.append(i)
    
print(" ".join(li))

#remove the duplicate from string
n=input('enter a string : ')
l=[]
for ch in n:
    if ch not in l:
        l.append(ch)
        
print(" ".join(l))
'''   
#remove the duplicate from list
'''
a = input("enter a number : ")
lis = []
r = set()
for digit in a:
    if digit not in r:
        r.add(digit)
        lis.append(digit)
        
print(" ".join(lis))

a = input("Enter a number: ")  # Take input as a string
lis = []
r = set()
for digit in a:
    if digit not in r:  # Check if the digit is not already in the set
        r.add(digit)  # Add digit to the set to track it
        lis.append(digit)  # Append digit to the list

print("".join(lis))  # Join the list into a string without spaces and print it
#list reversed by slicing
list=[8,7,6]
l=list[::-1]
print(l)
#list reverse using list method revesed()
lst = [8, 7, 6]
lst.reverse()
print(lst) 
'''
#reversed
'''
lst=[3,4,5,6]
rev=reversed(lst)
print(list(rev))

set={1,2,2,3,4}
print(set)
dic={'name':'ash','age':24}
print(dic)
a=lambda x,y:x*y
print(a(7,19))



for i in range(1,10):
    if i == 4:
        pass
    print(i)

import array

a=[1,2,4,5,6]
r=[]
a[2]=3
for i in range(len(a)):
    if i + 1 != a[i]:
        print(i+1)
        break


def myfunc(n):
           for i in range(0,n):
                for j in range(0,i+1):
                     print("*",end="")
                print()
n=5
myfunc(n)           
              
'''
#decorator example
'''
def decorator(func):
    def wrapper():
        print('Transaction Processing')
        print('transcation completed')
    return wrapper
def hello():
    print('excute all the step of transaction')

hello1=decorator(hello)
hello1()
'''    
#overridding example
'''
class animal:
    def make(self):
        return 'anything'

class dog(animal):
    def make(self):
        return 'make_sound'

Animal=animal()
Dog=dog()
print(Animal.make())
print(Dog.make())
'''
#overloading example
'''
class mathoperation:
     def add(self,a,b,c):
          return a+b+c
oper_math=mathoperation()
print(oper_math.add(1,2,7))
print(oper_math.add(1,2,3))     
'''

#abstraction example
class per:
    def per_func(self):
        raise NotImplementedError('subclass of abstract method')
class bird(per):
    def per_func(self):
        print('bird voice')
    def bird_func(self):
        print('bulbul voice')       
class dog(per):
    def per_func(self):
        print('dog voice')

    def dog_func(self):
        print('labra voice')
d=dog()
b=bird()
b.per_func()
b.bird_func()
d.per_func()
d.dog_func()

#another way abstract example
from abc import ABC,abstractmethod
class person(ABC):
    @abstractmethod
    def per_func(self):
        pass
class bird(person):
    def per_func(self):
        print(' birds voice')

class dog(person):
    def per_func(self):
        print('dogs voice')
obj_b=bird()
obj_d=dog()
obj_b.per_func()
obj_d.per_func() 
'''
#class and object example
class student:
    def __init__(self,fullname):
        self.name=fullname
        
s1=student('karan patel')
print(s1.name)


#overloading example

class mathoperation:
    def add(self,a,b,c):
        return a+b+c

obj=mathoperation()
print(obj.add(1,5,8))


#overridding example
class a:
    def make(self):
        return 'anything here'
class b(a):
    def make(self):
        return 'anyone here'
        
obj_a=a()
obj_b=b()
print(obj_a.make())
print(obj_b.make())

# single inheritance
class parentclass:
    def par_func(self):
        print(' this is parent class')

class childclass(parentclass):
    def class_func(self):
        print('this is child class')
        
obj=childclass()
obj.par_func()
obj.class_func()


#multilevel inheritance

class Animal:
    def sound(self):
        print('making sound')
class Horse(Animal):
    def hor(self):
        print('horse sound')
class donkey(Horse):
    def don(self):
        print('donkey sound')
obj=donkey()
obj.sound()
obj.hor()
obj.don()

#multiple inheritance
class parent1:
    def part1_func(self):
        print('this is first parent')
class parent2:
    def part2_func(self):
        print('this is second parent')
class child(parent1,parent2):
    def class_func(self):
        self.part1_func()
        self.part2_func()
obj1=child()
obj1.class_func()
#hericical inheritance

class Parentclass:
    def parent_func(self):
        print('this is from parent class')
class child1(Parentclass):
    def child1_func(self):
        print('this is from first child class')
class child2(Parentclass):
    def child2_func(self):
        print('this is from second child class')

obj_a=child1()
obj_b=child2()
obj_a.child1_func()
obj_a.parent_func()
obj_b.child2_func()
obj_b.parent_func()

class ParentClass:
    def parent_func(self):
        print('This is from ParentClass')

class Child1(ParentClass):
    def child1_func(self):
        print('This is from First Child class')

class Child2(ParentClass):
    def child2_func(self):
        print('This is from Second Child class')

obj_a = Child1()
obj_b = Child2()

obj_a.child1_func()
obj_a.parent_func()

obj_b.child2_func()
obj_b.parent_func()


#inheritance example
class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printforperson(self):
        print(self.firstname,self.lastname)
        
obj_p=person("Ashwini","Patle")
obj_p.printforperson()

#Abstraction example
from abc import ABC,abstractmethod


class Per(ABC):
    @abstractmethod
    
    def per_func(self):
        pass
    
class bird(Per):
    def per_func(self):
        print('bird voice')
class dog(Per):
    def per_func(self):
        print('dog voice')

obj_Bird=bird()
obj_d=dog()
obj_Bird.per_func()
obj_d.per_func()


#encapsulation example
class student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks
    def get(self):
        return self.__marks
stu1=student('rajam',70)
stu2=student('Ashwini',79)
print("Name: {} marks:{}".format(stu1.name,stu1.get()))
print('Name:{} marks:{}'.format(stu2.name,stu2.get()))

#polymorphism example
class B:
    def make_sound(self):
        print('brid voice chirp')
class D:
    def make_sound(self):
        print('Dog voice woof')
        
def make_sound_for(animal):
    animal.make_sound()
    
objb=B()
objd=D()
make_sound_for(objb)
make_sound_for(objd)

#stack example
stack=[]

stack.append('a')
stack.append('b')
stack.append('c')

print('intial stack')
print(stack)

print('\nremove stack element using pop ')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\n stack after element popped')
print(stack)

#queue example
queue=[]

queue.append('q')
queue.append('r')
queue.append('s')
print('intial queue')
print(queue)

print('\nremove the element from queue')
#print(queue.pop())
print(queue.pop())
#print(queue.pop())
print('\n queue after the elemment popped from it')
print(queue)

#dequeue example
from collections import deque
q=deque()
q.append('2')
q.append('4')
q.append('6')
print('\n dequeue using pop')
print(q.popleft())
print('\n dequeue after elment removed')
print(q)

#array example
import array as arr
a=arr.array('i',[1,2,3])
print('created first array: ',end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print() 
a.insert(2,4)
print("Array after insertion : ", end=" ")
for i in (a):
    print(i,end=" ")
print()    
print('array accessing',a[2])
print(a.pop(2))
print('\n array after popped ',end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print()    
'''

'''
#example of linkedlist
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=node('10')
node2=node('20') 
node3=node('30') 
node4=node('40')  

node1.next=node2
node2.next=node3
node3.next=node4

def display(head):
    current=head
    while current is not None:
        print(current.data,end="->")
        current=current.next
    print('none')    
display(node1) 


#insertion in linkedlist
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=node('10') 
node2=node('20')    
node3=node('30')    
node4=node('40')     

node1.next=node2
node2.next=node3
node3.next=node4

def display(head):
    current=head
    while current is not None:
        print(current.data,end="->")
        current=current.next
    print('none')

new_node=node('50')
current=node1
while current.next is not None:
    current=current.next
current.next=new_node

print('new node after inserted : 50')
display(node1)    

#remove  elemnt from linkedlist
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=node('10')
node2=node('20')
node3=node('30')
node4=node('40')

node1.next=node2
node2.next =node3
node3.next=node4

def removed_function(head,value):
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

    prev.next = current.next
    current = None
    return head

def display(head):
    current = head 
    while current is not None:
        print(current.data, end="->")
        current=current.next 
    print('none')

print('original node')
display(node1)

new_node=node('50')
current=node1
while current.next is not None:
    current=current.next
current.next=new_node
print('new nide add is :50')
display(node1)
node1 = removed_function(node1,'30')
print('node after removing element : 30')
display(node1)    

#length of linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=node('10')
node2=node('20')
node3=node('30')

node1.next=node2
node2.next=node3        

def display(head):
    current=head
    while current is not None:
        print(current.data, end="->")
        current=current.next
    print('none')

def get_length(head):
    length=0
    current=head
    while current is not None:
        length += 1
        current=current.next
    return length    
print('node')
display(node1)
length=get_length(node1)
print(f"Length of the linked list: {length}")
'''
# Initial array
'''
a = [1, 2, 4, 5, 6]

# Finding the index where value doesn't match the index plus one
index_to_remove = None
for i in range(len(a)):
    if i + 1 != a[i]:
        index_to_remove = i
        break

# Removing the element at the found index
if index_to_remove is not None:
    del a[index_to_remove]

# Printing the modified array
print(a)  # Output: [1, 2, 5, 6]
'''
#missing value in array
def missing(arr):
    n=len(arr)
    total = n *(n+1)//2
    return total-sum(arr) 
arr=[3,0,1]
print(missing(arr))

#duplicate number in  array
arr=[2,1,3,1,4,5]
a=b=arr[0]
while True:
    a=arr[a]
    b=arr[arr[b]]
    if a==b:
        break
a=arr[0]
while a!=b:
    a=arr[a]
    b=arr[b]

duplicate=b
print(duplicate)

#merge two array
def merged(arr1,arr2):
    merge=[]
    i=j=0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i +=1
        else:
            merge.append(arr2[j])
            j +=1

    while i < len(arr1):
        merge.append(arr[i])
        i +=1
    while j< len(arr2):
        merge.append(arr2[j])
        j +=1
    return merge    

arr1=[1,3,5]
arr2=[2,4,6]
print(merged(arr1,arr2))


#list comprehension
f=['mango','apple','kiwi'] 
l=[]
for i in f:
    if 'a' in i:
        l.append(i)
print(l)                      
'''
select employee_id,emlpoyee_name,employee_salary
from employee   
select * employee    

select max(salary)
where sal not in(max(sal)from employee);
from employee
'''