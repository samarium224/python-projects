# Student_height = input("Input a list of student heights ").split()

# for n in range(0, len(Student_height)):
#     Student_height[n] = int(Student_height[n])
# print(Student_height)
# Sum = 0
# a = 0

# for num in Student_height:
#     Sum = Sum + num
#     a = a+1

# if Sum == sum(Student_height) and a == len(Student_height):
#     print("True")

# avg = round(Sum/a)
# print(f"sum of the list is {Sum}")
# print(f" total number of list is {a}")
# print(f"The avarage is {avg}")



## Fizz Buzz


# for i in range(1,101):

#     if i%3 == 0 and i%5 ==0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)


#pypassword generator
import string
import random
letter_list = list(string.ascii_letters)
number_list = ['0','1','2','3','4','5','6','7','8','9']
symbol_list = ['!','#','$','%','&','(',')','*','+']
password = []
randfactor = []

print("Welcome to the Pypassword Generator!")
print("How many latters would you like in your password?")
a = input()
a = int(a)
b = input("How many symbols would you like?")
c = input("How many numbers would you like?")
b = int(b)
c = int(c)
total_number = a+b+c

for i in range(0,a):
    password.append(letter_list[random.randint(0,len(letter_list)-1)])



for i in range(0,b):       #symbols

    symbol_num = random.randint(0,len(symbol_list)-1)
    password.append(symbol_list[symbol_num])

for i in range(0,c):
    num_num = random.randint(0,len(number_list)-1)
    password.append(number_list[num_num])


random.shuffle(password)

password = ''.join(password)

print(password)
