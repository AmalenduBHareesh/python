 # WAP to print the sum of index positions of all the vowels present in the given string
s=input() # the string input is taken from the user(amalendu)
summ=0 # the sum is assumed to be 0,if there are no vowels are present un the string
ip=0# value is initialized,value 0
while ip < len(s): # while loop started with the condition that is lesser than the length of the string 
    if s[ip] in 'aeiouAEIOU': # first iteration starts ,by cheching th evowels present in the string by defining them (the vowels in  the giver string include aaeu,that are in the ip 0,2,4,7 that gibes a total of 13)
        summ+=ip # the index position is added if there is a vowel inn the string
    ip+=1 #the updation is gven by one
print(summ)    # print th e o/p    
        
