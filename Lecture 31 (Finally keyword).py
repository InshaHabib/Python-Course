# Finally Keyword:- finally mn hmesha code execute hota either error aye ya nhi.....
def func():
    try:
        l=[2,3,4,6,8,7,10,14]
        i=int(input("Enter any index="))
        print(l[i])
        return 1

    except:
        print("Some error occurred")
        return 0
    
    finally:
        print("I am always executed!!!")
# print("I am always executed!!!")

x = func()
print(x)