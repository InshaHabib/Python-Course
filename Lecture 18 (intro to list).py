# Python List = lists are ordered collection of data items
l = [1,2,3,"insha",True,4,5,7,8,9]
print(l)
print(type(l))
# List Index
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])
# print(l[5]) # error occur

print(l[-3]) # negative index
print(l[len(l)-3]) # positive index
print(l[5-3]) # positive index
print(l[2]) # positive index

if 7 in l:
    print("yes")
else:
    print("no")

if True in l:
    print("yes")
else:
    print("no")

# Same things applies for strings as well !!!
if "sha" in "insha":
    print("yes")
else:
    print("no")
if "ahs" in "insha":
    print("yes")
else:
    print("no")

print(l)
print(l[:])
print(l[1:])
print(l[1:3])
print(l[1:-1])
# jump index
print(l[1:10:2])
print(l[1:10:3])

# List Comprehension
lst = [i for i in range(4)]
print(lst)
lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(10) if (i%2==0)]
print(lst)

