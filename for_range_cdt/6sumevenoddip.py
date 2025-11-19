#6)WAP to print the sum of even digits present in the odd index positions
s=input() # take the string input from the user(123456)
sum=0 # assume that there are  no even numbers in even index positions
for eip in range(1,len(s),2):# for loop starts,range with 2 updation
    if s[eip] in '02468': # first iteration starts ,first is 0ip with value 2,second is 1 ip with value 3,likewise take the even values present in the string's odd index position
        sum+=int(s[eip])# sum it if its an even digit in even index position
print (sum)    #print the sum      (12)  
