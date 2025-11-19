#9)WAP to print the sum of even digits present in the even index positions
s=input() # take the string output from the user(0141414)
summ=0 # assuming the sum is 0
ip=0 # intializing the while loop as 0
while ip<len(s): # while loop starts with the ip less than the length of the string
    if s[ip] in '02468': #   if loop starts with the condition of checking the number includes in even numbers
        summ+=int(s[ip]) # add to the sum if the even numbers in even ip 
    ip+=2 #increment the count by 2 
print(summ) # print the sum (12)