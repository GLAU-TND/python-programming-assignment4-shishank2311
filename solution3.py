s=input("enter a query string")
l=eval(input("enter set of strings"))
t=[ ]
for i in l:
      if i.startswith(s):
          t.append(i)
print(t)
