#WAP to print the sum of ip of all the consonents present in the given string
s=input() # input string is taken from the user (ammu)
summ=0 # assuming the sum is 0
ip=0 # intializing the while loop as 0
while ip<len(s): # while loop starts with the ip less than the length of the string
    if s[ip].isalpha() and  s[ip] not in 'aeiouAEIOU': # if loop starts to check weather the element is alphabet and is not in vowels (the 1st and 2nd alphabets are consonents ,so the sum of theie index positions is 3 )
        summ+=ip #adding to the sum if the alphabet is consonent
    ip+=1 # updation of the while loop is given as 1
print(summ)      # sum is printed   