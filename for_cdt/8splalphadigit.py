#8)Wap to print how many special characters and how many alophabets and how many digits are present in the strings
s=input()# we take the string input from the user as 'ammu2@'
a=0 #assuming there are no alphabets in the string
d=0 # assuming there are no digits in the string
c=0 # assuming there are no special characters in the string
for ele in s: # for loop starts
    if ele.isalpha(): # iteration1 checks a is alpha or not and skips remaining
        a+=1 #count incremnts by 1 qand extends till m,m,u
    elif ele.isdigit():#iteration 2,check 2 is a digit and skips the remaining
        d+=1  # increment the count by 1
    else: #iteration 3,check wheather the other conditions are skipped and only special characters are remaining
        c+=1 #increment the count by one for the special character
print('alphabets',a) # print the output
print('digits',d)                
print('special',c)                               