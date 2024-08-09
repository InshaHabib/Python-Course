# f-string:- for string formatting

letter = "My name is {0} and I am from {1}"
name = "InshaHabib"
country = "Pakistan"
# print(letter.format(country,name))
print(f"My name is {name} and I am from {country}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format(price=49.09999))

print(type(f"{2*30}"))
print(f"{2*30}")