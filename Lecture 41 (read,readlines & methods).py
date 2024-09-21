# File Methods
""" f= open('inshafile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"Marks of student {i} in DBMS is {m1*2}")
    print(f"Marks of student {i} in OR is {m2*2}")
    print(f"Marks of student {i} in SQE is {m3*2}")
    print(line) """

"""f = open('inshafile1.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()"""


f = open('inshafile1.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()