# is vs ==
# is:- compares the identity of two objects
# ==:- compares the value of objects
a=[2,4,6,8]
b=[2,4,6,8]
c=3 # "insha", (2,4):-tuple
d=3 # "insha", (2,4):-tuple

print(c is d) # exact location of object in memory
print(a is b) # exact location of object in memory
print(a == b) # value

