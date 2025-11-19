# the input given is [11,22,33,44,55,66]
#the out put to be got is ['odd','even','odd,''even......]




l=[11,22,33,44,55,66] # the input is given in a list
new=[]# a new string is defined inorder to not modify the given string
for ip in range(len(l)): # for loop starts with the range of the length of the list
    if l[ip]%2==0:  # first iteration starts , if the number is divisible by 2,its even 
        new+=['even'] # then print even there
    else:
        new+=['odd']  # else print odd 
print(new)    # print the modified list output        
