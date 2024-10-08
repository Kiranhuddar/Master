# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# n= 12345
# b =""
# for i in n:
#     b + =i
#
# print(b)

# n1 = int(input("Enter first number :"))
# n2 = int(input("Enter second number:"))
#
# n1,n2 = n2,n1
# print("value after swapping is",n1)
# print("value after swapping is",n2)

# n = int(input("Enter number:"))
#
# b = 1
# for i in range(1,n+1,1):
#     b = b*i
#
# print(b)

# a = 0
# b = 1
# for i in range(0,20,1):
#     c = a + b
#     print(c)
#     a,b = b ,c
#     if c ==20:
#         break
# a = [1,2,3]
# b= 0
# for i in a:
#     b +=i
# print(b)

# l = [10,20,30,40,50]
# print(len(l))

# l = [1,2,3,4,5,6,7,8,9]
# l[0],l[-1]=l[-1],l[0]
#
# print(l)

# l =[1,2,3,4,5,6,7]
# b = 3
# l2 = []
# for i in range(len(l)):
#     if l[i]==b:
#         i =i+1
#     else:
#         l2.append(l[i])
# print(l2)

# l = [1,2,3,4,5,6,7]
# n = int(input("Search element:"))
# count = 0
# flag = 0
# for i in l:
#     if l[i] == n:
#         print("It is present")
#         count += 1
# if count == 1:
#     print("present")
# else:
#     print("not present")

# l = [1,2,3,4,5,6]
# # l.clear()
# # print(l)
# del l[:]
# print(l)

# a = [1,2,5,6]
# b = a.copy()
# print(b)

# l = [15,6,7,10,12,10,20,10]
# n = 10
# count = 0
# for i in range(len(l)):
#
#     if l[i]==n:
#         count += 1
#
# print(count)
# l = [5,10,15,20]
# sum = 0
# for i in range(len(l)):
#     sum += l[i]
# print(sum)
#
# l = [1,2,3,4,5,6]
# b = 1
# for i in range(len(l)):
#     b *=l[i]
# print(b)

# l= [100,20,35,14,5,6]
# l.sort()
# print(l[-2])

# n = input("Enter string :")
# if n == n[::-1]:
#     print("Its a palidrome")
# else:
#     print("its not a palidrome")

# str = "Welcome to python programming"
# words = str.split(" ")
# reversed = " ".join(words[::-1])
#
# print(reversed)

# sentence = "Welcome to python programming"
# words = sentence.split(" ")
# reversed_sentence = " ".join(words[::-1])
# print(reversed_sentence)


# str = "Welcome to python programming"
# sub_str = "python"
# found = 0
# for i in str.split(" "):
#     if i ==sub_str:
#         found = 1
#         break
# if found  == 1:
#     print("pre")
# else:
#     print("pasda")
#
# n= int(input("enter number :"))
# for i in range(1,11,1):
#     print(f"{n}*{i}={n*i}")
#
# a =int(input("enter number :"))
# # b =int(input("Enter second number :"))
# # if a==6 or b==6 or a+b==6 or abs(a-b)==6:
# #     print(True)
# # else:
# #      print(False)
#
# # n = "Kiranki"
# # l = len(n)//2
# # print(l)
# # print(n[l-1:l+2:1])
# a= 'Kiran'
# b ='Hudar'
# print(a+b)
# n = input("Enter string")
# if n==n[::-1]:
#     print("It is a palindrome")
# else:
#     print("its not a palidrome")


# for i in range(1,101,1):
#     for j in range(1,11,1):
#         if i == 3 or j==3:
#             print("buzz")
#         elif i==5 or j==5:
#             print("fuzz")
#         elif (i==5 and j==3) or (i==3 or j==5):
#             print('FUZZBIZZ')
#         else:
#             print(i*j)

# n= int(input("enter number which we need factorial :"))
# factorial = 1
# for i in range(1,n+1,1):
#     factorial *=i
# print(factorial)
# l=[1,2,3,4,5,6]
# l.reverse()
# print(l)

# l =[1,1,2,3,4,5,6,7,9]
# for i in range(1,len(l)+1,1):
#     if i in l:
#         continue
#     else:
#         print(i)
#
# n1= input("Enter first string:")
# n2 = input("Enter second string :")
# first_word = n1.replace("","").lower()
# second_word = n2.replace("","").lower()
#
# if sorted(first_word) == sorted(second_word):
#     print("Its a panagram")
# else:
#     print("it is not a panagram")

# l =[1,2,3,4,5,6,7,8,1,2,1,2,1,2]
# l1 =[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# l = "sdalnsldkfsodhjnosdnflk"
# alphabe = 0
# betsr = 0
# for i in l:
#     if i in "aeiou":
#         alphabe +=1
#     else:
#         betsr+=1
# print(f"Number of owels are {alphabe} and numbers of consonent are {betsr}")
# n = int(input("Enter number:"))
# l =[1,5,4,7,8,9,5,4,7,5,8,9,6,5,4,7,8]
# new_list = l.sort()
# print(new_list)
# for i in new_list:
#     if i== n:
#         print(f"the index of the given number is {i}")

# def binary_search(10, 100):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# n= int(input("power of something :"))
# n1 = int(input("Enefsbk"))
# print(n1**n)

# def grret(n):
#     return n*n
# print(grret(8))

# def greet(name):
#     print("how"+name+"you ?")
# greet("kiran")

# def ad(x,y):
#     print(x+y)
# ad(5,4)

# def mul(x):
#     return x*x
# square = mul(8)
# print(square)

# global_var = 10
# def example():
#      local_var = 5
#      print(global_var+local_var)
# example()


# def generic(ui,address):
#     ui_address
# def list(*args):
#     for arg in args:
#         print(arg)
# list("apple","orange","pineapple","ant")

# def power(x,n):
#     print(x**n)
# power(2,3)

# def palindrome(n):
#     if str(n) == str(n)[::-1]:
#         print("Its a palidrome")
#     else:
#         print("its not a palidrome")
# palindrome(121)

# def list(l1,l2):
#     l3=[]
#     for i in l1 :
#         if i not in l2:
#             l2.append(i)
#             return l2
# print(list([1,2,3,4,5],[2,3,5,6,9,8]))

# def square(n):
#     square_root = n**.5
#     if square_root.is_integer():
#         return "perfect square"
#     else:
#         return "not a perfect square"
#
# print(square(100))

# def reverse_str(sentence):
#     word = sentence.split(" ")
#     reverse_word = word[::-1]
#     return " ".join(reverse_word)
# print(reverse_str("hello how are you"))

# def prime_number(n):
#     count = 0
#     for i in range(1,n+1,1):
#         if n%i ==0:
#             count+=1
#     if count == 2:
#         print("its a prime")
#     else:
#         print("its not a prime")
# prime_number(6)

# def anagrams(str1,str2):
#     first_letter =sorted(str1)
#     second_letter = sorted(str2)
#     if first_letter == second_letter:
#         print('its a panagram')
#     else:
#         print("Its not a panagram")
# anagrams("listen","silent")

# def longest(words):
#     if not str:
#         return " "
#     words.sort()
#
#     prefix = ""
#     for i,j in zip(words[0],words[-1]):
#         if i==j:
#             prefix+=i
#         else:
#             break
#     return prefix
# words = ['flower','flow','working']
# print(longest(words))
# def longest_common_prefix(words):
#     if not words:
#         return ""
#
#     words.sort()
#
#     prefix = ""
#     for i, j in zip(words[0], words[-1]):
#         if i == j:
#             prefix += i
#         else:
#             break
#
#     return prefix
#
# word_list = ['flower', 'flow', 'working']
# print(longest_common_prefix(word_list))

# def majorit_element(list):
#     l =[]
#     n = len(list)//2
#     for num in list:
#         if num>n:
#             l.append(num)
#     return l
# list = [1,2,3,4,5,6,7,8,9]
# print(majorit_element(list))

# def missing_number(n):
#     for i in range(1,len(n)+1,1):
#         if i in n:
#             continue
#         else:
#             return i
# n= [1,2,3,4,5,6,8]
# print(missing_number(n))

def alphabets(num):
    ones = ['zero',"One","Two","three","four","five","six","seven","eight","nine"]
    tens = ["","eleven",'twelve','thirteen',"fourteen","fifteen","Sixteen","Seventeen","Eighteen","Ninteen"]
    tesns = [" ","ten","twenty","thirty","fourty","fifty",'sixty',"seventy","eighty","ninty"]
#############################################################################

# aabbcc
#aabbccde
#abcabc aabbcc
#abcabcd
#acaaabb [a,a,a,a,b,b,c]aabcbaa
#str[0::2]aabc,str[-2:0:-2]baa
# str = "aabbcc"
# print(sorted(str))

#print(str[-1:0:-2])
# def palidrome(str):
#     sorted(str)
#     if len(str)%2==0:
#         palidrome_word =str[::2]+str[-1:0:-2]
#         if palidrome_word == palidrome_word[::-1]:
#             print("given str in a palidrome")
#         else:
#             print("given str is not a palidrome")
#     elif len(str)%2 !=0:
#         palidrome_word =str[0::2] +str[-2:0:-2]
#         if palidrome_word == palidrome_word[::-1]:
#             print("given string for odd length is a palidrome")
#         else:
#             print("Given string for odd lenght is not a palidrome")
#
# # palidrome("aaaaabbccdd")#abcdaaadcba
# def is_palindrome(string):
#     # Compare the string with its reverse
#     return string == string[::-1]
#
# # Example usage:
# input_string = "aaaaabbccdd"
# if is_palindrome(input_string):
#     print(f'"{input_string}" is a palindrome.')
# else:
#     print(f'"{input_string}" is not a palindrome.')

import logging
from selenium import webdriver

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

driver = webdriver.Chrome()
logger.info("google")
driver.get("google")
























































































































































































































































































































































