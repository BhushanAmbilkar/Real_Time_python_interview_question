l1=['sun','mon','tue','wed','thu','fri','sat']
#out="sun#1:mon#2:tue#3:wed#4:thu#5:fri#6:sat#7"
s=""
j=0
for i in l1:
    j+=1
    s+=i+"#"+str(j)+":"
print(s)
l=len(s)
print(s[:l-1])
l=list(range(1,8))
result=map(lambda x,y:x+"#"+str(y),l1,l)
print(":".join(list(result)))

ls=[]
j=1
for i in l1:
    ls.append(i+"#"+str(j))
    j+=1
print(":".join(ls))

