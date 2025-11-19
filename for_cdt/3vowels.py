# 3)WAP to print how many vowels are present in the given strings
s= input() #we are taking string input from the user, taking input as 'amalendu'
c=0# assuming if there are no vowels
vowels='aeiou' # defining the vowels 
for ele in s:#for loop starts 
    if ele.lower() in vowels: #first iteration, converting the string into lower case using method and checking 
        c+=1 # count is incremented by one if vowels are present 
print (c)        # printing the output