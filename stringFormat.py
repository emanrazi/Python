country="Pakistan"
name="Eman"
letter=("Hey my name is {} and I am from {}")
print(letter.format(name,country))

letter=("Hey my name is {1} and I am from {0}")
print(letter.format(country,name))

letter=(f"Hey my name is {name} and I am from {country}")
print(letter)
