# Local VS Global Variable
# Local:- variable that is defined in function & is only accessible within that function.
# Global:-variable that is defined outside of function & is accessible fron within any function in code.
x=4
print(x)

def hello():
    x=5
    y=8
    print(f"The local variable x is {x}")
    print("Hello World!!!")

print(f"The global variable x is {x}")
hello()
print(f"The global variable x is {x}")
# print(y) # error bcz not defined in globally, its local variable


a=10
def function():
    global a
    a=4
    b=5
    print(b)

function()
print(a)
# print(b) # error

