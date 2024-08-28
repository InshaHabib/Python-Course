# Exception Handling

num=input("Enter any number=")
print(f"The multiplication table of {num} is:")
try:
    for i in range(1,11):
        print(f"{int(num)}*{i}={int(num)*i}")
except Exception as e:
    print(e)
    # print("Invalid input")
    
print("Some important lines of code")
print("End of Program")

#------------------------------------------------------
try:
    numbr = int(input("Enter any integer number="))
    a=[3,6]
    print(a[numbr])
except ValueError:
    print("Entered number is not an integer")
except IndexError:
    print("Index Error")



