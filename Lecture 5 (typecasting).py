# String type answer 12
# a="1"
# b="2"

""" a=1
b=2
print(a+b) """

# Typecasting = 1 datatype into another datatype
# Type 1 (Explicit Conversion = jisme hum python ko koi datatype convert krna ko kehta hein)
a="1"
# a="1Insha" #error occur
b="2"
# 1st convert into integer then add
print(int(a)+int(b)) 

# Type 2 (Implicit Conversion = automatically python datatype khud he convert krdyta ha)
c = 1.9
d = 8
# c convert to float
print(c+d)
# define type to "type" function
e = 7
print(type(e))
f = a + b 
print(f)
print(type(f))

