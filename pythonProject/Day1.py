# s = 'abracadabraca'
# d={}
# for i in s:
#     d[i]=s.count(i)
# print(d)
# s = "hello world"
# d={}
# for i in s:
#     if i in "aeiou":
#         d[i]=s.count(i)
# print(d)
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# c=[]
# for i,j in zip(a,b):
#     c.append(i+j)
# print(c)
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
# d={}
# for i in names:
#     if names.count(i)>1:
#         d[i]=names.count(i)
# print(d)
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# d={}
# for i,j in enumerate (names):
#     if names.count(j)==1:
#         d[j]=names.index(j)
#     else:
#         d[j]+=names.index(j)
# print(d)
# a=15
# if isinstance(a,str):
#     print("string")
# else:
#     print("not a str")
# a="hello"
# for i in a:
#     if a.index(i)%2==0:
#         print(i)
# a="hello"
# print(a[::2])
#
#
# a="hello"
# print(a[::-1])
#
# a="hello"
# for i in a:
#     if ord(i)<=ord("Z"):
#         print(chr(i))
#     else:
#         print(chr(ord(i)-32))
#
# a="HELLO"
# for i in a:
#     if ord(i)<=(ord("a")):
#         print(chr(ord(i)+32))
#     else:
#         print(chr(i))
# a="hello"
# n=input("enter substring")
# for i in a:
#     if i==n:
#         print("substring present")
#         break
#     else:
#         print("no")

a="hello123"
# for i in a:
#     if ord(i)<ord("A"):
#         print((i))
# for i in a:
#     if i.isdigit():
#         print(i)
# for i in a:
#     if ord(i)>=ord("A"):
#         print(i)
a="hello123456!@#$$%^"
# for i in a:
#     if ord(i)<ord("1"):
#         print(i)
# for i in a:
#     if not i.isalnum():
#         print(i)
# for i in a:
#     if ord(i)>=ord("1"):
#         print(i)
# for i in a:
#     if i.isalnum():
#         print(i)
n=["eye"]
# if n==n[::-1]:
#     print("palidrome")
# else:
#     print("not a palidrome")
# if n==list(n.reverse()):
#     print("palidrome")
# else:
#     print("no")
# a="hi how are you"
# print(a.replace("hi","kiran"))
# a="hello world"
# for i in a:
#     if i in "aeiou":
#         print(a.replace(i,"*"))
#
# a="kiran"
# print(list(a))
# a=["kiran"]
# print(str(a))
a="hello world how are you?"
# b=max(a.split(" "),key=lambd.a x:len(x))
# print(b)
# b=0
# for i in a:
#     if i.isspace():
#         b+=1
# print(b)
# data="hello world hi apple you yahoo to you"
# b=min(data.split(" "),key=lambda x:len(x))
# print(b)

# a="kiran"
# b=[]
# for i in a:
#     b+=i
#     print(b)

# from selenium.webdriver import Chrome
# driver=webdriver.Chrome()
# driver.get("url")
# First_name=driver.find_element("xpath","//input[@id='RESULT_TextField-1']")
# First_name.send_keys("Kiran")
# last_name=driver.find_element("xpath","//input[@id='RESULT_TextField-2']")
# last_name.send_key("huddar")


# def Factorial(n):
#     if n<=1:
#         return n
#     else:
#          print(n*Factorial(n-1))
# Factorial(5)
# start=int(input("enter number:"))
# if start/2==0 or start/3==0 or start/5==0:
#      print("its not a prime number")
# else:
#     print("its a print number")
# n=int(input("enter number:"))
# if n==1:
#     print("Factorial of Number is ",n)
# factorial=1
# if n>1:
#     for i in range(1,n+1):
#         factorial=factorial*i
# print(factorial)
# n=int(input("enter number:"))
# count=0
# for i in range(1,n+1):
#     if n%2==0:
#         count+=1
# if count==2:
#     print(n,"is a prime Number")
# else:
#     print("its not a prime number")

my_module = 3.142







