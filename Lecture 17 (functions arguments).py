# Functions Arguments:
def average(a,b): #first arguments are imp / last argument by default 1 
    print("The average is ",(a+b)/2)

average(4,8)

# Default Arguments
def average(a=8,b=4): # default ignore function call run
    print("The average is ",(a+b)/2)

average(5,9)

def name(fname,mname="mishal",lname="habib"):
    print("Hello,", fname,mname,lname)
name("miss", "insha")
#   print(type(name))

def average (*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is:", sum/len(numbers))
    # return 7 # (1st return run other not run [ignore it])
    return sum/len(numbers)

c=average(5,6,7,1)
print(c)


def name(**name): # name as dictionary type (**)
  print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"])


name(mname="insha", lname="habib", fname="S")