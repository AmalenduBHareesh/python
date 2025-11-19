#3)WAP to print the sum of even index positions of all the even numbers present in the given string
s=input() # we take the input string from the user 
summ=0 #assume that there are no even numbers present in even index positions
for eip in range(0,len(s),2): #for loop starts 
    if s[eip] in '02468': #first iteration ,if the digit is even or not
        summ+=eip # add teh index position if the number is even in even inedex postion
print (summ)     #print the sum    
