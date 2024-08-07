l = [2,8,0,3,20,1,9,11,12,1]
print(l)
print(l.index(1))
print(l.count(1))
m=l.copy()
# m=l
m[0]=0
# print(l)
print(l.insert(1,234))
n=[300,600,900]
k=l+n
print(k)
# l.extend(n)
print(l)

l.append(7) # add digit
print(l)
# l.sort(reverse=True) # arrange digit
# l.reverse()
l.sort()
print(l)


