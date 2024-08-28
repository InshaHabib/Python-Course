# Dictionary Methods
employee1 = {122:45,123:50,173:85,183:95}
employee2 = {124:59,135:70,193:65}
# update()
employee1.update(employee2)

"""clear()
employee1.clear()""" # for empty dictionary
print(employee1)

# pop()
employee1.pop(122)
print(employee1)

# popitem() :- pop the last item of dictionary
employee2.popitem()
print(employee2)

# del:- delete the entire dictionary
del employee2[135]
print(employee2)
