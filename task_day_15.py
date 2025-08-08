'''Coding exercises:
1.Write a Python function square_all(numbers) that takes a list of numbers as input and returns a new list containing the square of 
each number in the input list. Use the map() function with a lambda function to implement this'''
# input=[1,2,3,4,5,6,7,8,9]
# print(list(map(lambda a:a**2,input)))

'''2.Write a Python function filter_positive(numbers) that takes a list of numbers as input and returns a new list containin
only the positive numbers from the input list. Use the filter() function with a lambda function to implement this'''
# list_1=[-4,-3,-2,-1,0,1,2,3,4]
# print(list(filter(lambda a:a>0,list_1)))

'''3. Write a Python function calculate_factorial(n) that calculates the factorial of a given number n. Use the reduce() function 
with an appropriate lambda function to implement this.'''
# from functools import reduce
# def calculate_factorial (n):
#     fact=1
#     if n==0 or n==1 :
#         return 1
#     else:
#         return reduce(lambda a,b:a*b,range(1,n+1))
# obj=calculate_factorial(4)
# print(obj)
'''4. Write a Python function count_vowels(string) that takes a string as input and returns the count of vowels (a, e, i, o, u) 
in the input string. Use the reduce() function with an appropriate lambda function to implement this'''
# from functools import reduce
# def count_vowels(string):
#     vowels=['a','i','o','e','u','A','E','I','O','U']
#     return reduce(lambda count,char: count+(1 if char in vowels else 0),string,0)#here right hand function use 
# print(count_vowels('hello friends!'))


