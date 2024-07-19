# for loops : execute a group of statement a certain number of times

name = "insha"
for i in name: # all characters in output
    print(i)
    if(i=="h"):
        print("special")


colors = ["black","green","white","golden","grey"]
# iterate list
for color in colors:
    print(color)
    for i in color:
        print(i)

# print number 20000
for a in range(12):
    print(a)
    # print(a+1)

for b in range(1,11):
    print(b)
    # print(b+1)

for d in range(1,12,3): # (start,stop,step)
    print(d)
    # print(d+1)

# for c in range(1,20001):
#     print(c)
#     # print(c+1)
