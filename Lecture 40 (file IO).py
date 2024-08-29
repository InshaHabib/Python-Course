# File IO in Python
"""# Reading a File
# opening a file:-
f=open('inshafile.txt','r')
# print(f)
# read file:-
text=f.read()
print(text)
f.close()"""

# writing a File
# f=open('inshafile.txt','w') # write in file
"""f=open('inshafile.txt','a') # append in file
f.write('Hello World')
f.close()
"""
with open ('inshafile.txt','a') as f:
    f.write('Hey i am insha habib.')