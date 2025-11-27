# Task 2

# The following program allows the weights of 15 bags of rice to be input. 
# The correct weight for each bag of rice must be 
# between 4.9 kg and 5.1 kg inclusive.
underweight = 0
overweight = 0
bags_rice = int(input("Enter number bags of rice: "))
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        overweight = overweight + 1
        print("The bag of rice is overweight")
    elif bag_weight < lower_bound:
        underweight = underweight + 1
        print("The bag of rice is underweight")    
    else:
        print("The bag of rice is the correct weight")
    
bags = print(f"{overweight} bags of rice were over weight while {underweight} bags were underweight")




# 7       Edit the program so that it:
# a.       Accepts the weights for only 10 bags of rice.
# [1]

# b.       Prints out the message “The bag of rice is the correct weight” 
# when a weight entered is between 4.9kg and 5.1 kg inclusive.
# [2]

# c.       Prints out the number of bags of rice that were underweight, 
# as well as the number that were overweight, after the weights of all 
# the bags have been entered.
# [5]

# d. Edit your program so that it works for any number of bags of rice.
# [2]
# Save your program.

