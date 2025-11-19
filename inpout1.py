# input=[12,11,17,21,5]
# output=['even','prime','prime','odd','prime']
l=eval(input()) # take the input 
nl=[] # introduce a new list 
for ele in l:# first for loop starts to check each element
    if ele >1: # if ele is greater than 1,run th enext loop otherwise skip
        for i in range(2,ele//2+1): # next for loop starts twith the range starting from 2 
            if ele%i==0: # iteration starts if the condition to check wheather the number is prime or not
                if ele%2==0:  # another iteration starts to check the element is even or not if the abouve iteration skips
                    nl.append('even')  # if its even ,add even string to the new list
                else:
                    nl.append('odd') # if its odd, addthe odd string to the list
                break # berak the loop after getting this
        else: 
            nl.append('prime') # if the number is prime ,add the prime string to the new list
    else:
        nl.append('prime')     # this is for printing prime if the number is 1       
print(nl)       # print the new list as output

