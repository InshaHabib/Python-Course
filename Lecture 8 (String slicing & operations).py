# String slicing and operations
name="insha,habib"
print(name[0:5])
print(len(name))
fruit = "mango"
len1 = len(fruit)
print("mango is a", len1,"character word")

# slicing
fruit = "mango"
letter = len(fruit)
print(letter)
print(fruit[0:4]) # including 0 but not 4
print(fruit[:4])
print(fruit[1:4])
print(fruit[:]) # by-default length
print(fruit[0:len(fruit)-3])

# print(fruit[len(fruit)-1:len(fruit)-3])
print(fruit[len(fruit)-3:len(fruit)-1])

alphabets = "ABCDEFGH"
for character in alphabets:
 print(character) 

# Quiz
nm = "insha"
print(nm[-4:-2]) #print ns