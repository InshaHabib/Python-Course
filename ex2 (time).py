import time

print("Current Time is",time.strftime("%H:%M:%S"))
# print()
h=int(time.strftime("%H"))
print(h)
m=int(time.strftime("%M"))
print(m)
s=int(time.strftime("%S"))
print(s)
if(h<=11 and m<=59):
    print("Good Morning Sir")
elif(h>=11 and m<=59 and h<17):
    print("Good AfterNoon Sir")
elif(h>=17 and m<=59 and h<21):
    print("Good Evening Sir")
else:
    print("Good Night Sir")