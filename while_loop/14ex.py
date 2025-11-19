l=[11,22,33,44,55,66]
ip=0
while ip<len(l):
      l[ip],l[ip+1]=l[ip+1],l[ip]
      ip+=2
print(l)           
