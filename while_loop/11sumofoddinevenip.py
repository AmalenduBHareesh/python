#11)WAP to print the sum of even digits present in the odd index positions

s=input() # take the string output from the user
summ=0 # assuming the sum is 0
ip=1 # intializing the while loop as 1
while ip<len(s): # while loop starts with the ip less than the length of the string
    if s[ip] in '02468': #   if loop starts with the condition of checking the number includes in even numbers
        summ+=int(s[ip]) # add to the sum of the even numbers if the up is odd
    ip+=2 #increment the count by 2 
print(summ) # print the sum 