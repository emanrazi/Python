list=[1,2,3,4]
print(list)
list.append(8)
print(list)

m=[5,6,7,9]
list.extend(m)
print(list)

k=list+m
print(k)
list.sort()
print(list)

list.sort(reverse=True)
print(list)

for i in list:
    print(i)
