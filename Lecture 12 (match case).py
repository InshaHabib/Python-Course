
a = int(input("Enter the value of a="))
print(a)
match a:
    case 0:
        print("Case is zero")
    case _ if a%2==0:
        print("case 4")
    case 8:
        print("value is positive")
    case _ if a<0:
        print("value is negative")
    case _ if(a!=80):
        print("value not equal 80")
    case _ if a>100:
        print("value is greater ")
    case _:
        print("Default value:",a)
    