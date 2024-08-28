# Raising Custom Errors

num=int(input("Enter any number="))
if (num<5 or num>9):
    raise ValueError("Value should be between 5 and 9")

# -------------------------------------------------------------

num=input("Enter any Value=")
if num=='q' or num=='quit':
    exit()
elif (num<5 or num>9):
    raise ValueError("Value should be between 5 and 9")

# -------------------------------------------------------------

digit=input("Enter any digit between 5 and 9=")
if digit=='q' or digit=='quit':
    exit()
elif digit.isalpha():
   raise ValueError("Enter any integer value.....")
elif int(digit)<5 or int(digit)>9:
    raise ValueError("Number is not a value between 5 anf 9")
elif int(digit)>=5 or int(digit)<=9:
    print("Thank you for your input")

