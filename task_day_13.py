'''Task 1: Add Function Write a Python function named returns their sum'''
# def add(a,b):
#     print(a+b)
# add(7,7)

'''Task 2: Square Functionadd that takes two arguments a and b and Write a Python function named square that takes a number 
x as input and returns its square'''
# def square(x):
#     print(x**2)
# square(5)

''' Task 3: Factorial Function Write a Python function named input and returns its factorial.'''
# def factorial():
#     n=int(input('enter:'))
#     mul=1   
#     for i in range(1,n+1):
#         mul*=i
#     print(mul)
# factorial()

'''Task 4: Maximum Function Write a Python function named n as maximum that takes a list of numbers as input and returns 
the maximum value in the list.'''
# my_list=input('enter the numbers:').split(',')
# def maximum():
#     print(max(my_list))
# maximum()

'''Task 5: Reverse Function Write a Python function named reverse that takes a string returns its reverse.'''
# s=input('enter the word:')
# def reverse():
#     print(s[::-1])
# reverse()

'''Task 6: Check Prime Function Write a Python function named is_prime that takes a positive integer n as input 
and returns true if n is prime, otherwise False '''
# def is_prime(n):
#     if n<=1:
#         return False
#     for  i in range(2,n):
#         if n%i ==0:
#             return False
#         return False
# print(is_prime(4))
#6-9 IS CHART GPT REFERNCE SIR

'''Task 7: Fibonacci Function Write a Python function named  fibonacci that takes a positive integer 
n as input and return  the n th Fibonacci number.'''
# def fibonacci(n):
#     if n<=0:
#         print('gives positive integers')
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         a,b=0,1
#         for _ in range(2,n):
#             a,b=b,a+b
#         return b
# print(fibonacci(7))

'''Task 8: Palindrome Function Write a Python function named is_palindrome that takes a string returns 
True if s is a palindrome, otherwise False .'''
# def is_palindrome(s):
#     s=s.lower().strip()
#     return s==s[::-1]
# print(is_palindrome('juber'))

'''Task 9: Sum of Squares Function Write a Python function named sum_of_squares that takes a list of numbers as 
input and returns the sum of the squares of those numbers.'''
# list=[9,2,3]
# def sum_of_squares():
#     sum=0
#     for i in list:
#         sum+= i**2
#     print(sum)
# sum_of_squares()

'''Task 10: Average Function Write a Python function named average that takes a list of numbers as input and returns the average value'''
# num=[10,20,30]
# def average():
#     n=len(num)
#     sum=0
#     for i in num:
#         sum+=i
#     print(sum/n)
# average()




