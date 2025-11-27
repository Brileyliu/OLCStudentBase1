# A student is writing a program to note down 
# the favourite sports of each of his classmates.
# the program will help check how many students like a certain sport.



# Write a program that will 
# -------------------------------------------------
# 1. ask how many students there are in the class

students = int(input("how many students are there in the class? :"))


# -------------------------------------------------
# 2. for each student, ask what is their favourite sport
	# 2a. Add the sport into a list
sportlist = []
for i in range(students):
    sport = input("what is your favourite sport? :")
    sportlist.append(sport)
    print(sportlist)
# -------------------------------------------------
# 3. After asking all the student's sport, 
	# Ask the user to enter a sport to check how many students like the sport.
check_sport = input("what sport do you want to check :")


# -------------------------------------------------
# 4. if the sport exist, print out how many people like the sport.
	# e.g. # 3 students like the sport
sportcounter = 0

if check_sport in sportlist:
    for sport in sportlist:
        if check_sport == sport:
            sportcounter = sportcounter + 1
        
    print(f"{sportcounter} students like {check_sport}")

     # 5. if the sport does not exist, print out an appropriate message.
else:
    print("nobody likes this sport")
    
# ------------------------------------------------
# ** Assume that all inputs given are in lower case and valid.
# ** the program will work for any number of students.