
"""_summary_
s={2,4,2,6,8,8,10}
print(s)

eman=set()
print(type(eman))
for values in s:
    print(values)
    
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
(s1.update(s2))
print(s1)

s1.intersection_update(s2)
print(s1)
s1.symmetric_difference(s2))
 """

cities1={"Pakistan",'India','ENgland','Tokyo',"Multan"}
cities2={'Pakistan','India'}
print(cities1.isdisjoint(cities2))

print(cities1.issuperset(cities2))

print(cities2.issubset(cities1))

cities1.remove('Tokyo')
print(cities1)

item=cities1.pop()
print(cities1)
print(item)

cities2.clear()
print(cities2)
