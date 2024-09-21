# Seek(), tell() & other functions:-
"""with open('inshafile1.txt','r') as f:
    print(type(f))
    # move to 10th byte in a file
    f.seek(10)
    # read the next 6 byte
    data=f.read(6)
    print(data)"""


"""with open('inshafile1.txt','r') as f:
    print(type(f))
    # move to 10th byte in a file
    f.seek(10)
    # check the current position
    print(f.tell())
    # read the next 6 byte
    data=f.read(6)
    print(data)"""
 

with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(12)
with open('sample.txt', 'r') as f:
  print(f.read())