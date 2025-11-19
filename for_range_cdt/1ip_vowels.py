#1)WAP to print the index positions of all the vowels present in the given string
s=input() #taking string input from the user(amalendu)
vowels='aeiouAEIOU'  #defining the vowels
for ip in range(len(s)):#for loop starts in the range of length of s
    if s[ip] in vowels: #first iteration checks weather the vowel is present in the given string
        print(ip) # print the index position where the vowels are  present 
