# Enumerate Function
marks=[45,50,55,75,85,95,43,67]

"""index=0
for mark in marks:
    print(mark)
    if (index==5):
        print("Insha Habib !!!")
    index=index+1"""

for index, mark  in enumerate(marks, start=1):
    print(mark)
    if index==5:
        print("Insha Habib !!!")

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\n")
# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

print("\n")
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')

print("\n")
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)

print("\n")
# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)