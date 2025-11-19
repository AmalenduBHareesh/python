#5)WAP to print the sum of odd index positions of all the even numbers present in the given string
s=input() # we take the input string from the user 
summ=0 #assume that there are no even numbers present in odd index positions
for eip in range(1,len(s),2): #for loop starts 
    if s[eip] in '02468': #first iteration ,if the digit is even or not
        summ+=eip # add the index position if the number is even in odd inedex postion
print (summ)     #print the sum    
