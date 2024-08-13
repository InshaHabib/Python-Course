# Set Methods
s1 = {2,4,6,8}
s2 = {3,5,6}
# Union()
print(s1.union(s2))
# Update()
s1.update(s2)
print(s1,s2)

name1 = {"apple","banana","cat","doll","egg","fish"}
name2 = {"apple","ball","cat","dog","elephant","fish"}
print(name1.union(name2))
print("\n")
# intersection()
print(name1.intersection(name2))
print("\n")
# symmetric_differnce():- intersection ka beghr wali values ati hein
print(name1.symmetric_difference(name2))
print("\n")
# differnce():- 1st variable mn jo differnt chezyn hon gi wo ayen gi output mn
print(name1.difference(name2))
print("\n")
# isdisjoint() :- koi intersection na ho
print(name1.isdisjoint(name2))
print("\n")
# issuperset():- 1st are subset of 2nd: jo dosra var mn chezyn hein wo phla mn b honi chiyen tb he true hoga
print(name1.issuperset(name2))
print("\n")
# issubset():- 2nd are subset of 1st
print(name1.issubset(name2))
print("\n")
# add()
num1 = {"aaaaa","bbb","cccc","ddddd"}
num1.add("eeeee")
print(num1)
# remove()
num1.remove("bbb")
print(num1)
# discard()
num1.discard("zzz")
print(num1)
# pop():- pop out the last numbr of set
num1.pop()
print(num1)
# clear():-
num1.clear()
print(num1)
""" del:- delete the entire set
del num1
print(num1)"""

info = {"insha", 20,4.9,20,True}
print(info)
if "insha" in info:
    print("present")
else:
    print("not present")