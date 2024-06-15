from functools import reduce
cube=lambda x:x*x*x

l=[1,2,3,4,5]
newlist=list(map(lambda x: x*x*x,l))
print(newlist)

newnewlist=list(filter(lambda x: x>2,l))
print(newnewlist)
    
newl=(reduce(lambda x,y:x+y,l))
print(newl)