# Shorthand if/else
a=int(input("Enter the value of a="))
b=int(input("Enter the value of b="))
print("A") if a>b else print("B") if a==b else print("C")

c=9 if a>b else 0
print(c)

"""method 1
result = value_if_true if condition else value_if_false

method 2
if condition:
    result = value_if_true
else:
    result = value_if_false"""

