# Dictionary:- ordered collections of data item.
dic = {
    "name": "insha","age":20,"student":"BSSE"
}
print(dic["name"],dic["age"])

dict={
    101:"wasama",
    77:"maryam",
    73:"insha",
    86:"sharjeel"
}
print(dict[73])

info = {'name':'insha', 'age':21, 'eligible':True}
print(info)
print(info['name'])
print(info.get('name')) 
print(info.get('eligible')) 
"""print(info['name2']) # through error
print(info.get('name2')) # no through error """
print("\n")
print(info.keys())
print(info.values())
print("\n")

for key in info.keys():
    # print(info[key])
    print(f"The value corresponding to the {key} is {info[key]}")

print("\n")
print(info.items()) # print key values pair
for key,value in info.items():
  print(f"The value corresponding to the {key} is {info[key]}")