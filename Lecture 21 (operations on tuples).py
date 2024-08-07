# example 1
countries = ("Pakistan","Saudia","Turkey","Malaysia","Dubai","Indonesia")
temp=list(countries)
temp.append("england")
temp.pop(3)
temp[4]="Abu-Dhabi"
countries=tuple(temp)
print(countries)

# example 2
countries1 = ("Pakistan","Saudia","Afghanistan","Bangladesh","Turkey")
countries2 = ("Malaysia","Dubai","Indonesia")
SEA = countries1 + countries2
print(SEA)

# example 3
tuple=(2,3,4,5,3,4,6,7,4)
res = tuple.count(4)
print(res)
res1= tuple.index(4)
res1= tuple.index(4,5,7) # element,start,end
print(res1)
res2= len(tuple)
print(res2)


