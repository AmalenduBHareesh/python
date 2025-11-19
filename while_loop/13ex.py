l=[11,22,33,44,55,66]
new=[]
ip=0
while ip<len(l):
    if l[ip]%2==0:
        new+=['even']
    else:
        new+=['odd'] 
    ip+=1
print(new)           
