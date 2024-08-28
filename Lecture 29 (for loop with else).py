# For loop with else
for i in range(6):
    print(i)
    if i==4:
        break

else: # else means not a loop break its mean loop completed (else not executed)
    print("break the function")


# While loop with else
i=0
while i<8:
    print(i)
    i=i+1
    # if i==4:
    #     break

else: # else means not a loop break its mean loop completed (else not executed)
    print("break the function")


for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")
    