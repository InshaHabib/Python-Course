# tuples value not change....
l=(2,7,4,9,6,"Black",True)
# l[0]=45
print(type(l),l)
print(l[0])
print(l[1])
print(l[-2]) # Black
print(l[2])
print(l[3])

if 345 in l:
    print("Yes")
else:
    print("No")

tup=l[1:4]
print(tup)
