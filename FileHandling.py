""" 
f=open("files/myfile.txt",'a')
f.write("I am from Gujrat")
f=open("files/myfile.txt",'r')
text=f.read()
print(text)
f.close()

while True:
    line=f.readline()
    print(line)
    if not line:
        break
f.close()
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=(line.split(",")[0])
    m2=(line.split(",")[1])
    m3=(line.split(",")[2])
    print(f"City of Student {i} is, {m1}")
    print(f"City of Student {i} is, {m2}")
    print(f"City of Student {i} is, {m3}")
    print(line)
    
    with open("files/myfile.txt",'r') as f:
    line=f.seek(5)
    text=f.tell()
    print(text)

"""

i=0
with open("files/myfile.txt",'w') as f:
     f.write("Hello World")
     f.truncate(5)

 
 
   
   



