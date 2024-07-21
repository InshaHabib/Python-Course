# Functions: block of code that performs a specific task (bhot bara program ka function bna kr use krna)
""" Two types of function
1) Built-In function= not defined a def keyword
As: min,max,range,len,um,list,tuple,set
2) User-Defined function= defined a def keyword(jo hum khud bnaty hein (per our needs)) """

def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater")
def islesser(a,b):
    pass # Kuch b run ni hoga isme agla program run hojai ga.....
def name(fname, lname):
    print("Hello", fname, lname)

name("insha", "habib")

a=9
b=8
isGreater(a,b)
""" if(a>b):
    print("first number is greater")
else:
    print("second number is greater") """
calculateGmean(a,b)
# gmean=(a*b)/(a+b)
# print(gmean)
c=6
d=9
isGreater(c,d)
""" if(c>d):
    print("first number is greater")
else:
    print("second number is greater") """
calculateGmean(c,d)
# gmean2=(c*d)/(c+d)
# print(gmean2)

