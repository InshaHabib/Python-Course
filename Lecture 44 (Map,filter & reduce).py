# Map, Filter & Reduce:- Advance List Manipulation
# Map
"""def cube(x):
    return x*x*x
print(cube(2))
l=[2,4,6,5,9,3,8]
newl=[]
for item in l:
    newl.append(cube(item))
print(newl)"""

"""def cube(x):
    return x*x*x
print(cube(2))
l=[2,4,6,5,9,3,8]
newl =list(map(cube,l))
print(newl)"""

# Filter:- filter(predicate,iterable)
# predicate:- returns a boolean value & is applied to each element in iterable arguments 
"""l=[2,4,6,5,9,3,8]

newl =list(map(lambda x:x*x*x,l))
print(newl)

def filter_function(a):
    return a>4

newnewl=list(filter(filter_function,l))
print(newnewl)"""

# Reduce:-import function
from functools import reduce
numbers=[2,3,4,5,6,7]
sum=reduce(lambda x,y:x+y, numbers)
print(sum)