'''Task 1: Set Intersection
 Write Python code to find and print the intersection of the following two sets'''
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.intersection(set2))

'''Task 2: Set Union
 Write Python code to find and print the union of the following two sets'''
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.union(set2))

''' Task 3: Set Difference
Write Python code to find and print the elements present in set1 but not in set2'''
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.difference(set2))

'''Task 4: Set Symmetric Difference
Write Python code to find and print the symmetric difference of the following two sets:'''
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.symmetric_difference(set2))

'''Task 5: Set Membership Test
 Write Python code to check if the element 3 is present in the set''' 
# my_set = {1, 2, 3, 4, 5}
# print(3 in my_set)

'''Exercise 1: Set Intersection
 Write a Python script that finds and prints the intersection of two sets.'''
# set1 = {'akhil','juber','barlu'}
# set2 = {'abdul','khasim','gouse','juber'}
# print(set1.intersection(set2))

''' Exercise 2: Set Union
 Write a Python script that finds and prints the union of two sets'''
# set1 = {'akhil','juber','barlu'}
# set2 = {'abdul','khasim','gouse','juber'}
# print(set1.union(set2))

'''Exercise 3: Set Difference
 Write a Python script that finds and prints the difference between two sets'''
# set1 = {'akhil','juber','barlu'}
# set2 = {'abdul','khasim','gouse','juber'}
# print(set1.difference(set2))

'''Exercise 4: Set Symmetric Difference
 Write a Python script that finds and prints the symmetric difference between two sets'''
# set1 = {'akhil','juber','barlu'}
# set2 = {'abdul','khasim','gouse','juber'}
# print(set1.symmetric_difference(set2))


###############tuple################
'''Coding Exercise:
 
1:Create a Tuple Write a program that creates a tuple containing three elements: your name, your age, and your favorite color.
Then print the tuple'''
# my_tuple=('juber','19','gray')
# print(my_tuple)

'''Access Tuple Elements Write a program that creates a tuple containing the days of the week. Then, print the third element of
the tuple.'''
# week=('sun','mon','tues','wednes','thurs','fri','satur')
# print(week[2])

''' 3. Tuple Concatenation Write a program that creates two tuples, one containing odd numbers from 1 to 5 and another containin
even numbers from 2 to 6. Concatenate these two tuples and print the result'''
# odd=(1,3,5)
# even=(2,4,6)
# print(odd+even)#(1, 3, 5, 2, 4, 6)

'''4. Tuple Unpacking Write a program that defines a tuple containing the dimensions of a rectangle (length and width). Then,
unpack this tuple into two variables and calculate the area of the rectangle'''
# rectangle=(10,5)
# length,width=rectangle
# print('area:',length*width)
# sir this  program chartgpt reference
'''5.Check if an Element Exists Write a program that checks if a given element exists in a tuple'''
# tuple=(1,2,3,4,5)
# print( 2 in tuple)#true

'''6.Write a Python program to generate a bill for a supermarket purchase. The program should store the items and their pricess
in a list of tuples. It should then iterate over this list to print out each item along with its price. Finally, calculate and 
print the total cost of all the items'''
# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# print("Item\t Price")
# print("-"*25)
# total=0
# for i,j in items:
#     print(f"{i}\t {float(j)}")
#     total+=j
# print('-'*25)    
# print(f'Total\t {float(total)}')

