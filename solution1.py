l=eval(input())
k=int(input())
dt={}
for i in l:
    dt.setdefault(i[0],set())
    dt[i[0]].add(i[1])
l1=list(dt.keys())
lst=[]
j=1
for ky1 in dt.keys():
    for i in range(j,len(l1)):
            lst.append(((ky1,l1[i]),len(dt[ky1].intersection(dt[l1[i]]))))
    j+=1
while(k):
    max=lst[0]
    for i in lst:
        if i[1]>max[1]:
            max=i # IDEA:
    print(max[0])
    lst.remove(max)
    k-=1
