#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[2]:


a=int(input("Enter The Number A:"))
b=int(input("Enter The Number B:"))
add=a+b
print("The Sum Of A And B Is",add)


# In[3]:


a=int(input("Enter The Number A:"))
b=int(input("Enter The Number B:"))
a=a+b
b=a-b
a=a-b
print("The value Of A and B after Swapping is",a,"And",b)


# In[1]:


dist=float(input("Enter The Distance In Km:"))
a=dist*0.62137119
print("The Distance In Miles=",a)


# In[5]:


a=int(input("Enter The Number:"))
if(a<0):
    print("It Is A Negative Number")
elif(a==0):
    print("The Number Is 0")
else:
    print("It Is A Positive Number")


# In[6]:


a=int(input("Enter A Year:"))
if((a%4==0)and(a%100!=0)or(a%400==0)):
    print("It Is A Leap Year")
else:
    print("It Is Not A Leap Year")


# In[7]:


start=int(input("Enter The Starting Range: "))
stop=int(input("Enter The Ending Range: "))
print("Prime numbers between", start, "and", stop, "are:")
for val in range(start, stop):
  if val > 1:
    for i in range(2, val):
      if (val % i) == 0:
        break
    else:
      print(val, end=" ")


# In[1]:


n1=0
n2=1
a=int(input("Enter The Range:"))
for n in range(0,a):
     n3=n1+n2
     print("The Fibonacci Sequence upto",a,"Is",n3)
     n1=n2
     n2=n3


# In[3]:


n=int(input("Enter A Number:"))
sum=0
t=n
while(n>0):
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
if(t==sum):
    print("The Entered Number Is An Armstrong Number")
else:
    print("The Entered Number Is Not An Armstrong Number")


# In[5]:


n=int(input("Enter The Range:"))
c=0
for i in range(0,n+1):
    c=c+i
    i+=1    
print("The Sum Of Natural Numbers upto",n,"Is",c)


# In[6]:


for i in range(0,6):
    print("*"*i)
    i+=1


# In[7]:


def remove_n_chars_from_start(string, n):
    return ''.join([string[i] for i in range(n,len(string))])
string = "hello world"
n = 3
new_string = remove_n_chars_from_start(string, n)
print(new_string)


# In[9]:


a=[]
def divisiable_by_5(list1):
   print("Given list",list1)
   for i in x:
       if i%5==0:
          a.append(i)

x=[5,18,155,18,20,25,10]
divisiable_by_5(x)
print("The list is",a)


# In[10]:


str="hiwelcome,hi"
str.count("hi")


# In[14]:


rows = int(input('Enter the Number Of Rows:'))
for i in range(rows+1):
    for j in range(i):
        print(i, end=' ')
    print('')


# In[16]:


n=int(input("Enter The Number:"))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=(sum*10)+r
    n=n//10
if(temp==sum):
    print("The Number Is Palindrome")
else:
    print("The Number Is Not Palindrome")


# In[18]:


list=[1,2,3,4,5]
list[0],list[-1]=list[-1],list[0]
print("The List After Interchanging The First and Last Element =",list)


# In[21]:


def swapList(sl,pos1,pos2):
    n = len(sl)     
    temp = sl[pos1]
    sl[pos1] = sl[pos2]
    sl[pos2] = temp
    return sl      
list= [10, 14, 5, 9, 56, 12]
pos1= 2
pos2= 5
print(list)
print("Swapped list: ",swapList(list,pos1-1,pos2-1))


# In[22]:


list=[1,2,3,4,5,6,7,8,9]
print(len(list))


# In[24]:


a=int(input("Enter The Value Of A:"))
b=int(input("Enter The Value Of B:"))
if(a>b):
    print("A Is Greater")
else:
    print("B Is Greater")


# In[25]:


a=int(input("Enter The Value Of A:"))
b=int(input("Enter The Value Of B:"))
if(a<b):
    print("A Is The Smallest Number")
else:
    print("B Is The Smallest Number")


# In[28]:


a='amaama'
half = int(len(string) / 2)
first_str = string[:half]
second_str =string[half:]
if first_str == second_str:
    print(a,'String Is symmetrical')
else:
    print(a,'String is Not symmetrical')
if first_str == second_str[::-1]:  
    print(a,'String Is Palindrome')
else:
    print(a,'String Is Not Palindrome')


# In[31]:


list=['Hey','Hi','Mate']
list.reverse()
print(list)


# In[37]:


string= "Programming"
new_str = string.replace('m', '')
print ("The string After Replacing The i'th Character: " + new_str)
new_str = string.replace('o', '', 1)
print ("The string After Removing The i'th Character: " + new_str)


# In[43]:


str="Hello!"
print(len(str))


# In[49]:


n="Im Vengeance"
s=n.split(" ")
for i in s:
  if len(i)%2==0:
    print(i)


# In[55]:


tup1= ("Life",53,37)
tup2= ("Is", "Boring")
tup3= ((1,2),(4,6),(7,2),(10,9))
print("Size of tuple1: ", sys.getsizeof(tup1), "bytes")
print("Size of tuple2: ", sys.getsizeof(tup2), "bytes")
print("Size of tuple3: ", sys.getsizeof(tup3), "bytes")


# In[59]:


a=(13,71,93,57,48)
print("Maximum element",max(a))
print("Minimum element",min(a))


# In[82]:


tuple = (10, 20, 30)
total = 0
for element in tuple:
    total += element
print("The Sum Of The Elements In The Tuple Is",total)


# In[3]:


a=(5, 10, 15, 20)
b=(3, 5, 7 ,9)
print("First Matrix ",a)
print("Second Matrix: ",b)
result = tuple(map(lambda x, y: x + y,a,b))
print("Tuple Matrix After Addition: ",result)


# In[2]:


l = [1,2,3,4,5]
p = [(i, pow(i, 3)) for i in l]
print("The Value of square Of The First 5 numbers:",p)


# In[5]:


Dict = {'ram': 24, 'raj': 46,'ravi': 36, 'raja': 27, 'raju': 45}
K= list(Dict.keys())
K.sort()
sdict={i: Dict[i] for i in K}
print("After Sorting:",sdict)


# In[6]:


d= {}
a,b,c= 5, 3, 10
p,q,r= 12, 6, 9
d["x-y+z"] = [a-b+c,p-q+r]
print(d)


# In[8]:


d={'x':400,'y':100,'z':300,'p':807 }
print("Dictionary: ", d)
print("sum: ",sum(d.values()))


# In[10]:


dic1 = {"A": 1,"B": 2,"C": 3}
print("Size of dic1: ",len(dic1))


# In[11]:


s={1,2,3,4,5}
print("Size of set: ",len(s))


# In[12]:


s=set("Hello_World")
for i in s:
    print(i)


# In[13]:


s={1,2,3,4,5}
print("Maximum of the set: ",max(s))
print("Minimum of the set: ",min(s))


# In[14]:


s={1,2,3,4,5}
print("Initial list: ",s)
s.remove(5)
print("Final list: ",s)


# In[16]:


s={1,2,3,4,5}
p={5,6,7,8,9}
for i in s:
    for j in p:
        if i==j:
            print("The Common Element is:", i)


# In[18]:


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print("My matrix is:")
for i in range(1, len(matrix)):
    matrix[i] = matrix[0]
print(matrix)


# In[19]:


matrix1 = [[1, 2], [3, 4]]
matrix2 = [[4, 5], [6, 7]]
print("Printing elements of first matrix")
for row in matrix1:
    for element in row:
        print(element, end=" ")
    print()
print("Printing elements of second matrix")
for row in matrix2:
    for element in row:
        print(element, end=" ")
    print()
result = [[0, 0], [0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
print("Subtraction of two matrix")
for row in result:
    for element in row:
        print(element, end=" ")
    print()


# In[20]:


elements = [1, 2, 3, 2, 1, 3, 4, 5, 4, 5, 5]
element_counts = {}
for element in elements:
    if element in element_counts:
        element_counts[element] += 1
    else:
        element_counts[element] = 1
num_rows = max(element_counts.values())
num_cols = len(element_counts)
matrix = [[None] * num_cols for _ in range(num_rows)]
for col, element in enumerate(element_counts):
    count = element_counts[element]
    for row in range(count):
        matrix[row][col] = element
for row in matrix:
    print(row)


# In[21]:


matrix = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 9))
row_sums = [sum(row) for row in zip(*matrix)]
print("Row-wise sums:")
for sum_value in row_sums:
    print(sum_value)


# In[22]:


def create_even_submatrix(n):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                matrix[i][j] = 1
    return matrix
n = 4
result = create_even_submatrix(n)
for row in result:
    print(row)


# In[23]:


import inspect
def my_function(Batman,Superman,Flash):
    pass
parameters = inspect.signature(my_function).parameters
parameter_names = list(parameters.keys())
print(parameter_names)


# In[24]:


name = "John"
age = 30
city = "Ohio"

print(name, age, city)


# In[25]:


def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)
base =int(input("Enter the base: "))
exponent =int(input("Enter the power: "))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")


# In[26]:


class grade:
    def __init__(self, a, b):
        self.a = a
        self.b = b
  
    def __repr__(self):
        return str((self.a, self.b))
g= [grade("ram", 'a'),
       grade("ravi", 'b'),
       grade("raj", 'c'),
       grade("mani", 'd'),
       grade("goku", 's')]

print(sorted(g, key=lambda x: x.b))


# In[27]:


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Guna", age=18, city="Keezhpaakam")


# In[ ]:




