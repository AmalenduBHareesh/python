#40 WAP to find the consenonts present in th givem string
s=input() #we are taking string input from the user, taking input as 'amalendu2307'
c=0 # assuming if there are no vowels
vowels='aeiou' # defining the vowels 
for ele in s :#for loop starts 
    if ele.isalpha() and ele.lower() not in vowels: #first iteration, cheching its alphabet and converting the string into lower case and checking 
        c+=1 # count is incremented by one if alphabets other than  vowels are present 
print (c)    # print the output    