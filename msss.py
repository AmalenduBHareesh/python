# WAP to check wheather the gives substring is present in the given string
ms=input() # take th input from the user(main string-harshad)
ss=input() #(substring -ha)
c=0 # make the count default by 0
for ip in range (len(ms)): # for loop starts with the condition that the range is length of the mainstring
    if ms[ip:ip+len(ss):]==ss:# if loop starts,first iteration to check the index positions with slicing (to take multiple elements)
        c+=1 # increment the count
print(c) #print the output    (2)    
