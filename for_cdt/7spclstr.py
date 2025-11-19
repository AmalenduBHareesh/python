#7) WAP to check how many special characters are present in the given string
s=input()# taking string input from user 'amalendu @2307'
c=0 #assuming if there are no special characters in the list
for ele in s: #for loop starts 
    if not ele.isalnum(): #iteration starts ,cheching that the elements in the string is not alphabets and digits
        c+=1#increment the count by one if the condition satisfies
print (c)      # print the output   