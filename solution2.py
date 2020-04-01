dit=eval(input())
dit1={}
def nesttonormal(dct,ky):
    for j in dct.keys():
         if type(dct[j]) is dict:
             ky1 = ky+"."+j
             nesttonormal(dct[j],ky1)
         else:
            dit1[ky+"."+j]=dct[j]
    return dit1
for i in dit.keys():
    if type(dit[i]) is dict:
        nesttonormal(dit[i],i)
    else:
        dit1[i]=dit[i]
print(dit1)
