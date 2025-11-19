#2)WAP to print the sum of index positions of all the consonents present in the string
s=input()# we take the string input from the user
summ=0 #assume if there are no consonents present in the string
for ip in range(len(s)): # for loop starts ,with the range of the length of the input
    if  s[ip].isalpha() and s[ip] in 'aeiouAEIOU': # first iteration starts and check wheather they are alphabets and in vowels
        summ+=ip #  add the index positon if its a consonent
print (summ)    #print the output     