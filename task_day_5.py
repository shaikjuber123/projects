#EXERCISE 1
''' Write a Python program that takes a character as input and checks whether 
it is a vowel or not. Use the if-else statement'''
# char=input('enter the a character:')
# if char in ['a','e','i','o','u']:
#     print('it is vowel character')
# else:
#     print('it is non_vowel character')

#EXERCISE 2
'''Age Group Classification
 Write a program that takes an age as input and classifies the person into one of the following age groups:
 ->Child: 0-12 years
 ->Teenager: 13-17 years
 ->Adult: 18-64 years
 ->Senior: 65 years and older'''
# age=int(input('enter user age:'))
# if age>=0 and age<=12:
#     print(f'you are child and age is{age}')
# elif age>=13 and age<=17:
#     print(f'you are teenager and age is{age}')
# elif age>=18 and age<=64:
#     print(f'you are adult and age is{age}')
# elif age>=65:
#     print(f'you are senior and older age is{age}')
# else:
#     print('invalid input' )

#EXERCISE 3
'''Number Classifier:
 Write a program that takes an integer as input and classifies it as positive, negative, or zero. Use the 
if-elif-else statement.'''
# integer=int(input('enter the a integer:'))
# if integer>0:
#     print(f"{integer} it is positive_integer")
# elif integer<0:
#     print(f"{integer} it is negative_integer")    
# elif integer==0:
#     print(f"{integer} it is zero")
# else:
#     print("invaild integer")

#EXERCISE 4
''' Leap Year Checker:
Create a program that checks whether a given year is a leap year or not. A 
leap year is divisible by 4, but not by 100 unless it is divisible by 400'''
# year=int(input("enter any a year:"))
# if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
#     print("it is a leap year")
# else:
#     print("it is not leap year")

#EXERCISE 5
'''Calculator:
 Build a simple calculator program that takes two numbers and an operator 
(+, -, *, /) as input and performs the corresponding operation'''
# num_1=int(input('enter a number:'))
# num_2=int(input('enter second number:'))
# operation=input('select a operation from(+,-,*,/):')
# if operation == '+':
#     print('num_1+num_2:',num_1+num_2)
# elif operation == '-':
#     print('num_1-num_2:',num_1-num_2)
# elif operation == '*':
#     print('num_1*num_2:',num_1*num_2)
# elif operation == '/':
#     print('num_1/num_2:',num_1/num_2)
# else:
#     print('invalid inputs')

#EXERCISE 6
'''Short Hand If:
 Rewrite the following code using the short-hand 
if statement:
x = 8
 if x % 2 == 0: result = "Even"
 else: result = "Odd"  '''
# x=8
# print("even")if x%2==0 else print('odd')

#EXERCISE 7
'''Discount Calculator:
 Create a program that calculates the final price after applying a discount. 
The program should take the original price and the discount percentage as 
input'''
# product_price=int(input('enter the prouduct price:'))
# discount=int(input('enter the discount:'))
# total=product_price*(discount/100)
# product_price-=total
# print(product_price)

#EXERCISE 8
'''BMI Calculator:
 Write a program that calculates the Body Mass Index BMI using the 
formula: BMI = weight (kg) / (height (m))^2. The program should take 
weight and height as input'''
# weight=int(input('enter body weight in kg:'))
# height=int(input('enter body height in m:'))
# BMI=weight / (height)**2
# print(BMI)
