# planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
# # retrieve the value from the list
# print(planets[2])

# planets[3] = "Denzelland"
# print(planets)# prove
# # remove an item from list
# del planets[6]
# print(planets)

 
 # remove item using name
# planets.remove("mercury")

# # add to a list
# planets.append("Jiajieland")
# print(planets)

# count = len(planets)
# print(count)

# # loop through the list
# for i in planets:
#     print(i)

# students = []

# for i in range(5):
#     name = input("Enter your name: ").upper()
#     students.append(name)
# for j in students:
#     print(f"Hello {j}")

    # print(f"Hello {}")
# print(students)
    



# Exercise 9: Summing Numbers in a List
# Write a program to calculate the sum of numbers in a list.
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]


# print(sum(list1))
#### find the total of all the numbers
total = 0

# to do this without the sum()
for i in list1:
    # add the current number to total
    total = total + i

print(total)


##### find the average of this list of numbers
count = len(list1)
print(count)

average = total / count
print(average)

#### find the biggest number in this list
maxnum = list1[0]

for i in list1:
    if i > maxnum:
        maxnum = i
print(maxnum)




#### find the smallest number in this list

# minnum = min(list1)
# print(minnum)

minnum = list1[0]

for i in list1:
    if i < minnum:
        minnum = i
print(minnum)





# string variable
# integer, float
# boolean >> True False

# List
###################################################
# Part 1: Learning Exercises

# Exercise 1: Accessing List Elements by Index
# Write a program to access and print the first, second, and last 
# elements of a list using indexing.

# fruits = ["apple", "orange", "banana","durian"] # my list
# print(fruits[2]) # retrieve a specific value from the list



#------------------------------------------------------------
# Exercise 2: Adding Elements to a List
# Write a program to add an element to the end of a list using 
# append(), and add another element at a specific index using 
# insert().


# fruits.append("durian") # add a new item to the list, adds at the back

# fruits.insert(1, "grapes") # add at specific position





#------------------------------------------------------------
# Exercise 3: Using del() to Remove an Element by Index
# Write a program to delete an element at a specific index.
# Example: Remove the second color.

# del(fruits[1]) # deleting by the index



#------------------------------------------------------------
# Exercise 4: Using remove() to Remove an Element by Value
# Write a program to remove a specific element by its value.
# Example: Remove "green" from the list.
# colors = ["red", "green", "blue", "yellow"]
# colors.remove("green")  # Remove by value
# print("Colors after removal: {}".format(colors))

# fruits.remove("durian")

# while True:
#     if "durian" in fruits:
#         fruits.remove("durian")
#     else:
#         break



#------------------------------------------------------------
# Exercise 5: Using pop() to Remove and Retrieve an Element
# Write a program to remove the last element of a list using pop().
# Example: Remove and print the last color.
# colors = ["red", "green", "blue", "yellow"]
# removed_color = colors.pop()  # Remove the last element
# print("Removed color: {}".format(removed_color))
# print("Colors after pop: {}".format(colors))

# lastfruit = fruits.pop() # removes last one and assign to variable
# print(fruits)




#------------------------------------------------------------
# Exercise 6: Modifying Elements in a List
# Write a program to change the second element in a list to "pink."
# colors = ["red", "green", "blue"]
# colors[1] = "pink"  # Modify value at index 1
# print("Modified colors: {}".format(colors))
# print(lastfruit)
# fruits[3] = "spikyfruit" # change the value
# print(fruits)

#------------------------------------------------------------
# Exercise 7: Membership Check
# Write a program to check if "blue" is in the list.
# colors = ["red", "green", "blue"]
# if "blue" in colors:
#     print("Blue is in the list.")
# else:
#     print("Blue is not in the list.")

# validation check - existence check
# checkfruit = input("Enter a fruit name: ")
# if checkfruit in fruits:
#     print(f"{checkfruit} is in the list")
# else:
#     print(f"{checkfruit} is not in the list")

# #------------------------------------------------------------

# ##### to loop through every single item
# for i in fruits:
#     print(i)

# for i in range(5): 