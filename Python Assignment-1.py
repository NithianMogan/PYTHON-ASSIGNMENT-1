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


# In[ ]:





# In[ ]:





# In[ ]:




