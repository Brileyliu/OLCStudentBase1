# use the while loop and print out numbers from 0 to 5

# number = 0
# while number < 6:
#     print(number)
#     number = number + 1


# use the while loop and print out numbers from 1 to 5
# number = 1
# while number < 6:
#     print(number)
#     number = number + 1



# use the while loop and print out multiples of 5 from 5 to 50

# number = 5
# while number < 51:
#     print(number)
#     number = number + 5



# use the while loop and print out numbers from 10 to 1

number = 10
while number > 0:
    print(number)
    number = number - 1


# Write a program to help sort students to primary, secondary and jc
while True:
    age = input("Enter your age")
if age.isdigit():
    age = int(age)

    if age > 16:
        print("You go to JC")
    elif age > 12:
        print("You go to secondary school")
    elif age > 6:
        print("You go to primary school")
    break
else:
        print("This is not a number")