#5) WAP a profram to find how many digits are present in the given string
s= input()#we are taking string input from the user, taking input as 'amalendu2307'
c=0 # assuming if there are no digits
for ele in s: #for loop starts 
    if ele.isdigit() : #first iteration,checking wheather the given string has digits
        c+=1 # count is incremented by 1 if the condition satisfies
print(c)   #print the output     