#1.VALUE ERROR
# user_id=int(input('enter the user id:'))
# print(user_id)

# try:
#     user_id=int(input('enter the user id:'))
#     print(user_id)
# except ValueError as e:
#     prin(e)

#2.TYPE ERROR
# stu_name='juber'
# stu_id=98
# result=stu_name+stu_id
# print(result)

# stu_name=input('enter the name:')
# stu_id=int(input('enter the user id:'))
# try:
#     result=stu_name+stu_id
# except TypeError as e:
#     print(e)
# else:
#     print(result)

#3.FILENOTFOUND ERROR
# file=open('demo123.txt',mode='r')#FileNotFoundError: [Errno 2] No such file or directory: 'demo123.txt'
# read_data=file.read()
# print(read_data)
# file.close()

# try:
#     file= open('demo123.txt',mode='r')
#     read_data=file.read()
#     print(read_data)
#     file.close()
# except FileNotFoundError as e:
#     print(e)

#4 .ZERODIVISION ERROR
# num_1=11
# num_2=0
# try:
#     print(num_1/num_2)
# except ZeroDivisionError as e:
#     print(e)

#5.INDEXERROR
# string='shaikjuber'
# print(string[10])

# string='shaikjuber'
# try:
#     print(string[10])
# except IndexError as e:
#     print(e)

#6.KEY ERROR
# dict={1:'banana',2:'dragonfruit',3:'apple'}
# print(dict[5])

# fruits={1:'banana',2:'dragonfruit',3:'apple'}
# try:  
#     print(fruits[5])
# except KeyError as e:
#     print(f"KeyError: {e}")

#7.ATTRIBUTE ERROR
# name='juber'
# name.append('shaik')
# print(name)

# name='juber'
# try:
#     name.append('shaik')
# except AttributeError as e:
#     print(e)
# print(name)

#8.OVERFLOWERROR
# try:
#     print(float(10**1000))
# except OverflowError as e:
#     print(e)

#9.IO ERROR

# #10.EXCEPTION
# # try:
#     num_1=int(input('enter the number:'))#name
#     num_2=int(input('enter the second number:'))
#     print(num_1+num_2)
# except Exception as e:
#     print(e)
