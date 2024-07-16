# if/else statements = used for decision making
a =int(input("Enter your age: "))
print("your age is:", a)
# Conditional Operators
# ==, !=, <=, >=, <, >
print(a>20)
print(a<=20)
print(a!=20)
print(a==20)

if(a<20):
    print("you can drive")
    print("yes")
else:
    print("you cannot drive")
    print("no")
print("yeah!!!") 
# above space is identation fot starting the block of if/else

# Example1 = if,else
price = int(input("Enter the price of apple= "))
print("apple price= ", price)
budget = int(input("Enter the budget= "))
print("budget= ", budget)
if(price<= budget):
    print("add apple")
# if(budget-price<50):
#     print("add apple")
# elif( budget - price>70):
#     print("its okay you can buy")
else:
    print("no addition")

# Example2 = if,elif,else
num = int(input("enter the value of num="))
if(num<0):
    print("num id negative=")
elif(num==0):
    print("num is zero")
elif(num==999):
    print("num is special")
else:
    print("num is positive")
print("i am happy now")

# Example3 = nested if/else
b = int(input("Enter the value of b= "))
if (b < 0):
    print("Number is negative.")
elif (b > 0):
    if (b <= 10):
        print("Number is between 1-10")
    elif (b > 10 and b <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
