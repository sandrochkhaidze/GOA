def plus (a,b):
    return a + b

print(plus(10,26))

def multiply (d,m):
    return d * m

print(multiply(10,67))

def division (n,l):
    return n / l

print(division(50,5))



def SayGoaBest():
    return 'GOA BEST'
for i in range(10):
    print('Goa Best')

SayGoaBest()


def rectangle(first_side, second_side, third_side, fourth_side):
    return first_side + second_side + third_side + fourth_side

print(rectangle(10,25,65,11))

num = 10

if 15 > num:
    print('The number is more than 10')
else:
    print('Number is not more than 10')

requiredage = 18

if requiredage >= 18:
    print('you are allowed to give your votes')
else:
    print('You dont have permission to give your votes')


num1 = 10
num2 = -15
num3 = 0

if num1 > num2:
    print('The number is positive')
elif num2 < 0:
    print('The number is negative')
elif num3 == 0:
    print('The number is 0')

age = 15

if age < 13:
    print('you are a kid')
elif age > 13 and age < 19:
    print('you are over the age of 18 or 13')
elif age > 19:
    print('You are an adult')

