# String Methods
# Strings are immutable

# a = "insha"
a = "insha !!!!!!!! insha"
b = "!!!!! insha !!!!!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(b.rstrip("!"))

print(a.replace("insha", "mishal"))
print(b.split(" "))

heading ="introduction to py"
print(heading.capitalize())

print(len(heading))
print(len(heading.center(50)))
print(heading.center(50))

print(a.count("insha")) # 2
print(b.endswith("!!!")) 
print(heading.endswith("to", 11, 15)) 
c= "He's name is ayyan. He is an honest man."
print(c.find("is")) 
print(c.find("sdf")) 
# print(c.index("sdf")) 
s = "WelcomeToTheConsole"
print(s.isalnum()) #alphanumeric (a-z,A-Z,0-9) 
print(s.isalpha())
s1 = "WelcomeToTheConsole456"
print(s1.isalpha())
str1 = "hello world"
print(str1.islower())

str2 = "We wish you a Merry Christmas\n"
print(str2.isprintable())

str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "               #using Tab
print(str2.isspace())

str3 = "World Health Organization" 
print(str3.istitle())

str4 = "To kill a Mocking bird"
print(str4.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())



