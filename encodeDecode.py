str=input("Enter your string: ")
words=str.split(" ")
encode=False
if(encode):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            rand1="abc"
            rand2="def"
            strnew=rand1+word[1:]+word[0]+rand2
            nwords.append(strnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
    
else:
   nwords=[]
   for word in words:
        if(len(word)>=3):
            strnew=word[3:-3]
            strnew=strnew[-1]+strnew[:-1]
            nwords.append(strnew)
        else:
            nwords.append(word[::-1])
   print(" ".join(nwords))
    