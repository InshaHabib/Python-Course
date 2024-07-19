# Do While Loop not in python
# while loop

i=int(input("Enter the number:"))
while(i<=35):
    i=int(input("Enter the number:"))
    print(i)
    # i=i+1
    
    # if not (i%2==0):
    #     break
print("Done with the loop")

c=5
while(c>0): # loop condition check means iteration
    print(c)
    c=c-1
    # c=c+1 #infinite loop
else:
    print("I am inside else")

""" do{
   loop body;
} while(condition); """