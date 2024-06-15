
"""
dict={
    1:"Eman",
    2:"Razi",
    3:"Aftab Razi",
    4:"Abbas"
}
print(dict[3])
print(dict.get(1))

print(dict.values())
for i in dict:
    print(f"The value corrosponding to the key {i} is {dict[i]}")
# print(dict[i])
    
#print(dict.keys())
"""
ep1={1:100,
    2:340,
    3:600,
    4:450
    }
ep2={
    22:340,
    45:899,
    68:230
}
ep1.update(ep2)
print(ep1)

#ep1.clear()
#print(ep1)

ep1.pop(1)
print(ep1)

ep1.popitem()
print(ep1)

