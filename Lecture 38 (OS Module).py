# OS Module
import os

# agr ek folder ka andr koi folder bnana ha tu:-
# os.mkdir("data")

"""
# Create folder:-
if (not os.path.exists("data")):
    os.mkdir("data")
# agr data folder mn 100 or folder bnana ho tu:-
for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")
"""

"""
# Rename folder:-
# then rename a folder
if (not os.path.exists("data")):
    os.mkdir("data")
# agr data folder mn 100 folder ko rename krna ho tu:-
for i in range(0,100):
    os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}")

"""
"""
# List folder:-
folders=os.listdir("data")
print(folders)

for folder in folders:
    # print all folder of data
    print(folder)
    # check subfolder of any folder:-
    print(os.listdir(f"data/{folder}"))
"""

"""check os module on tis link:-
https://docs.python.org/3/library/os.html"""

"""
# print directory name
print(os.getcwd())
# change directory name then check directory
# os.chdir("/Users")
print(os.getcwd())
"""