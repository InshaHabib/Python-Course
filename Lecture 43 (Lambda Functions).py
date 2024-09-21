# Lambda Function :- function ka variable bnana (for 1 line of code)
# lambda arguments: expression
"""def double(x):
    return x*2
print(double(5))"""

def apply(fx,value):
    return 8 + fx(value)

double=lambda x:x*2 
cube=lambda x:x*x*x
avg=lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(5))
print(avg(2,4,8))
# print(apply(cube,2))
print(apply(lambda x:x*x*x,2))

