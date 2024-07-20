# BREAK(to skip over a part of code) AND CONTINUE

for i in range(12):
    if (i==10):
        break
    print("5 * ",i+1," = ",5*(i+1))
print("Exit this loop")

for i in range(12):
    if (i==10):
        print("skip the iteration")
        continue
    print("5 * ",i," = ",5*i)  

# tut14 continued........

i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
       break