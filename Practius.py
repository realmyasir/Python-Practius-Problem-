# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 17:10:55 2023

@author: Web 123
"""
# fact=1
# user = int(input('Enter a Factorial Digit'))
# for user in range(1,user+1):
#     fact*=user
# print(f'You enter Digit {user} factorial is ',fact)    

# user = int(input('Enter a Factorial Digit: '))
# fact = 1

# for i in range(1, user + 1):
#     fact *= i

# print(f'The factorial of {user} is {fact}')



# user = input('Enter Your Name And Reverse Your name')

# rev= reversed(user)
# for char in rev:
#     print(char,end=' ')

# user = input('Enter Your Name: ')
# reversed_name = reversed(user)
# print('Reversed Name:', end=' ')
# for char in reversed_name:
#     print(char, end='')


# user = int(input('Enter a Verbaliy Number >>'))
# if user%2==0:
#     print('You Enter A even Number ')
# else:
#     print('You Enter a Odd Number')
    

# n=20
# for i in range(1,n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i,'Fizz Buzz')
#     elif i % 3 == 0:
#         print(i ,'Fizz')
#     elif i % 5 == 0:
#         print(i ,'Buzz')
#     else:
#         print(i)        
        
# n=10
# for i in range(1,n+1):
#     if i % 5 == 0:
#        print(i ,'Buzz')
#     elif i % 3 == 0:
#         print(i ,'Fizz')
#     elif  i % 3 == 0 and i % 5 == 0:
#         print(i,'FizzBuzz')
#     else:
#         print(i)     

# print(list(range(11)))
# print(list(range(0,41,4)))

# print(type(range(20)))

# question No 1

# n1=int(input('Enter the First Number 1 - 100>>'))
# n2=int(input('enter the Second Number 1 - 100>>'))
# while n1 < 0 or n2 < 0 or n1 > 100 or n2 > 100 or n1 == n2:
#     print('Number Must be  Different between 1 - 100')
#     n1=int(input('Enter the First Number 1 - 100>>'))
#     n2=int(input('enter the Second Number 1 - 100>>'))

# if n1 < n2:
#     for i in range(n1,n2+1):
#         print(i,end=' ')
# else:
#     for i in range(n2,n1+1):
#         print(i,end=' ')
            

# n1 = int(input('Enter the First Number 1 - 100: '))
# n2 = int(input('Enter the Second Number 1 - 100: '))

# while n1 < 0 or n2 < 0 or n1 > 100 or n2 > 100 or n1 == n2:
#     print('Numbers must be different and between 1 - 100.')
#     n1 = int(input('Enter the First Number 1 - 100: '))
#     n2 = int(input('Enter the Second Number 1 - 100: '))

# if n1 < n2:
#     for i in range(n1, n2 + 1):
#         print(i, end=' ')
# else:
#     for i in range(n2, n1 + 1):
#         print(i, end=' ')


# Question Number 2 reverse String

# user=input('Please Enter The Word : >>')

# reversed_string = ''
# for char in user:
#     reversed_string = char + reversed_string
# print(reversed_string)

# print(user[::-1])

# Question Number 3

# user=input('Please Enter a number Between 1 and 12 : >')
# while (not user.isdigit()) or (int(user)) <1 or int(user) >12 :
#     print('Must be Integer Between 1 and 12')
#     user = input('please make  Selection : >')
# user = int(user)
# print('===========')
# print()
# print(f'This is the {user} Time Table')
# print()
# for i in range(1,13):
#     print(f'{i} x {user} = {i*user}')
    
    # question Number 4
# for i in range(1,13):
#     print('=======================')
#     print()
#     print(f'This is The {i} Time table')
#     print()
#     for j in range(1,13):
#         print(f'{j} x {i} = {j*i}')

# Question Number 5

# user=input('Enter A Number List type exit to stop')
# numbers=[]
# while user.lower() != 'exit':
#     while not user.isdigit():
#         print('This is not a number ? Please enter the Number')
#         user=input('Try Again')
#     numbers.append(int(user))
#     user=input('please Enter Next Number')
# total = 0
# for number in numbers :
#     total += number
# print(f'Mean is {total/len(numbers)}')
# print('sum is',sum(numbers)/len(numbers))    

# user = input('Enter The Number :>')
# numbers=[]
# while user.lower() != 'exit':
#     while not user.isdigit():
#         print('That is not a numbers ! Number only')
#         user=input('Try Again')
#     numbers.append(int(user))
#     user=input('Enter The Next Numbers')
# total=0
# if
#    print(total =total + numbers)
# print(f'Mean is {total/len(numbers)}')
# print('Sum is',sum(numbers)/len(numbers))


# question number 6

# n=int(input('Enter A Factorial Number :>'))
# # n=10
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)


# Question Number 7

# Fabinoci series

# # n=int(input('Enter febnocii Series Limit'))
# n=20
# a,b=0,1
# fib=[]
# for i in range(n):
#     fib.append(a)
#     a,b=b,a+b
#     print(f'Your Enter The Limit {n} Fibonacci Number Are , {fib}')


# question Number 8


# star = '*'

# for i in range(1,7):
#     for j in range(1,6):
#         if i == 1 and j < 6:
#             print(star,end='')
#         elif i == 2 and j == 1:
#             print()
#             print(star)
#         elif i == 3 and j < 5:
#             print(star,end='')
#         elif i == 4 and j == 1:
#             print()
#             print(star)  
#         elif i == 5 and j == 1:
#             print(star)
#         elif i == 6 and j == 1:
#             print(star)   

# s='*'
# for i in range(1,7):
#     for j in range(1,6):
#         if i== 1 and j < 6:
#             print(s,end=' ')
#         elif i == 2 and j == 1:
#             print(s,end=' ')
#         elif i == 3 and j == 5:
#             print(s,end=' ')
#         elif i == 4 and j == 1:
#             print(s,end=' ')
#         elif i == 5 and j == 1:
#             print(s,end=' ')
#         elif i == 6 and j == 1:
#             print(s,end=' ')

s='*'
for i in range(1, 7):
    for j in range(1, 6):
        if i == 1 and j < 6:
            print(s, end=' ')
        elif i == 2 and j == 1:
            print()
            print(s)
        elif i == 3 and j == 5:
            print(s, end=' ')
        elif i == 4 and j == 1:
            print(s)
        elif i == 5 and j == 1:
            print(s)
        elif i == 6 and j == 1:
            print(s)

        
































