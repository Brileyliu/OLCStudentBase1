# dict1 = {"hamburger": 5, 
#          "pasta": 10, 
#          "fries": 2}

# # add / amend
# dict1["hamburger"] = 10

# for key,value in dict1.items():
#     print(key)
#     print(value)

# for key in dict1:
#     print(key) # key
#     print(dict1[key]) # value

# def oddoreven(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# How to define a dictionary
menu = {"hamburger": "$2.00", "fries": "$1.00", "pasta": "$3.50"}

#retrieve a value from dictionary

priceham = menu["hamburger"]
print(priceham)

# change the value of the key

menu["hamburger"] = "$20.00"
print(menu)

menu["pizza"] = "$30.00"

## delete an item from dictionary

del menu["fries"]
print(menu)

# loop through dictionary
for food, price in menu.items():
    print(f"{food} : {price}")

choice = input("Hello sir, what would u like to eat? ")

if choice in menu:
    print(f"{choice} is {menu[choice]}")
else:
    print("Sorry I do not sell:", choice)

food = input("food to add to the menu: ")
food_price = input("price of food: ")

menu[food] = food_price
print(menu)