'''Task 1:Reverse List:
Write Python code to reverse the order of elements in the given list Print the reversed list'''
# my_list = [10, 20, 30, 40, 50, 11]
# my_list.reverse()
# print(my_list)

'''Task 2:Common Elements:
Given two lists them.list1 and list2 , find and print the common elements between'''
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# empty_list=[]
# for i in list1:
#     for j in list2:
#         if i==j:
#             empty_list.append(i)    
# print(empty_list)

'''Task 3:Unique Elements:
create a new list unique_list containing only the unique elements from the given list original_list . Print the unique list.'''
# original_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list=[]
# for i in original_list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)   

'''Task 4:Remove Duplicates:
Remove duplicate elements from the given list without duplicates while preserving the order.duplicated_list and print the list '''
# duplicated_list = [1, 2, 2, 3, 4, 4, 5]  
# unique_list=[]
# for i in duplicated_list:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)     


'''Exercise 1: List Concatenation:
Write a Python script that concatenates two lists and prints the result'''
# list_1=[1,2,3,4,5]
# list_2=[6,7,8,9,10]
# print(list_1 + list_2)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''Exercise 2: List Repetition
Write a Python script that repeats a list three times and prints the result.'''
# list= [1, 2, 3, 4, 5]
# print(list*2)#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

'''Exercise 3: List Removal
Write a Python script that removes the elements at even indices from a list'''
# list= [1, 2, 3, 4, 5]
# new_list=[]
# for i in list:
#     if list.index(i)%2==0:
#         continue
#     else:
#         new_list.append(i)
# print(new_list)

'''Exercise 4 List Insertion:
Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list'''
# my_list = [20, 30, 40, 50]
# my_list.insert(0,10)
# my_list.insert(1,11)
# my_list.insert(2,12)
# print(my_list)


#list comprehensions
'''1.Square Numbers Create a list of squares of numbers from 1 to 10.'''
#print([i*i for i in range(1,11)])

'''2. Even Numbers Generate a list of even numbers from 1 to 20.'''
#print([i for i in range(1,21) if i%2==0])

'''3.Words Lengths Given a list of words, create a list containing the lengths of 
each word.'''
# words = ["apple", "banana", "cherry", "date"]
# print([len(i) for i in words ])