# compare 2 numbers to see which one is bigger
num1 = 10
num2 = 20

# use if condition
if num1 > num2:
    # if the above condition is true, run this code
    print(f"{num1} is more than {num2}")
elif num1 == num2:
    print(f"{num1} is equal to {num2}")

else:
    print(f"{num1} is not more than {num2}")

# PASSWORD PROGRAM
# password = "password"
# for i in range(3):
#     inputpassword = input("Enter a passowrd: ")
#     if inputpassword == password:
#         print("Access Granted")
#         break
#     else:
#         print("Access Denied")

# else:
#     print("Account locked.")

# import random #
# for i in range(30):
#     num1 = random.randint(1,1000)
#     print(num1)

# import random # this happens once
# marks = 0
# for i in range(10):
# # MAKE A MATH QUIZ
    
#     num1 = random.randint(20, 50)
#     num2 = random.randint(20, 50)

#     answer = int(input(f"What is {num1} + {num2}? : "))

#     if answer == num1 + num2:
#         print("CORRECT.")
#         marks += 1
#     else:
#         print("WRONG.")

# print(f"You scored {marks} out of 10. ")




# RADOM NUMBER GUESSING PROGRAM

# Generate a random number
# need to loop for 7 times
# input the number
# check if bigger or smaller
# bigger
# smaller
# equal

# import random

# number = random.randint(1, 100)

# for i in range(6, -1, -1):
#     guess = int(input("guess a number from 1-100: "))
#     if guess > number:
#         print(f"guess is too big,chances left :{i}")
#     elif guess < number:
#         print(f"guess is too small,chances left :{i}")
#     else:
#         print("your guess is correct!, the number was", number)
#         break
# if i == 0:
#     print(f"you have no more chances, the answer was: {number}")


# Recap and Warm up - DO THIS

# write a program to help categorise how much bus fare to pay

# ask user to input an age

# check if age is a valid number # <str>.isdigit()

# use if, elif and else
# age < 7, free
# between 7 to 12, $2.00
# between 13 to 21, $4.00
# between 22 to 60, $10.00
# 61 and above, $1.00

# Print out the correct fare according to the age.
while True:
    age = input("How old are you: ")
    if age.isdigit():
        age = int(age)
        if age < 7:
            print("your bus fare is free. ")
        elif 7 <= age <= 12:
            print("your bus fare is $2.00. ")
        elif 13 <= age <= 21:
            print("you bus fare is $4.00. ")
        elif 22 <= age <= 60:
            print("your bus fare is $10.00. ")
        else:
            print("your bus fare is $1.00. ")
    else:
        print("your age is not a number")
