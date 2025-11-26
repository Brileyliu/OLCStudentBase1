'''
Question 1 (Length Check):
Write the input entry and validation code for a program that
needs to accept a 4-digit OTP (One-Time Password)
The OTP must be exactly 4 digits long

If the input is invalid, your code should keep trying
by asking for the input to be entered again.

#########################################

Sample output

Enter OTP: 12
Invalid input. The OTP must be exactly 4 digits.

Enter OTP: 12345

Invalid input. The OTP must be exactly 4 digits

Enter OTP: 1234
OTP accepted

'''

# how to check for length

# pin = "1234"
# print(len(pin))

while True:
    otp = input("Enter a 4 digit OTP: ")

    # validation both for length and for numbers
    if not otp.isdigit():
        print("OTP must be a number")
    elif len(otp) != 4:
        print("OTP must be 4 digits")
    else:
        #otp is valid
         print("OTP is valid")    
         break