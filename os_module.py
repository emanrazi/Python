import os
if(not os.path.exists("data")):
 os.mkdir("data")
else: 
 open("data/file.txt", "w").close()
 
folder=os.listdir("data")
print(folder)

os.remove("data/file.txt")
os.removedirs("data")