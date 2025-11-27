#how to define a function
# def hello():
#     print("Hello, how are you?")

#     # hello()


# def greet(yourname):
#     print(f"Hello {yourname}, how are you?")


# greet("Briley")



#rect 1 = 65, 89


# def area_rectangle(length, breath):
#     area = length * breath

#     return area
# rectangle1 = area_rectangle(65, 89)

# print(rectangle1)


# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.


# Test the function with multiple operations.
# print(calculator(10, 5, "+"))
# print(calculator(10, 5, "-"))
# print(calculator(10, 5, "*"))
# print(calculator(10, 5, "/"))

def calculator(number1, number2, op):
    # your code here

    if op == "+":
        output = number1 + number2
    elif op == "-":
        output = number1 - number2
    elif op == "*":
        output = number1 * number2
    elif op == "/":
        output = number1 / number2

    return output

num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
operation = input("Enter operation (+, -, *,/): ")

answer = calculator(num1, num2, operation)
print(f"{num1} {operation} {num2} = {answer}")