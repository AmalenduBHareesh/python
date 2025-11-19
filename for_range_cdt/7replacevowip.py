#7)WAP ro replace all the vowels iwith their index positions in a gier sting
s=input() # we give the user input as amalendu 
new='' # we assume the new string as new string to print the value without modifying the string
for ip in range(len(s)): # for loop starts ,with the range of length of s
    if s[ip] in 'aeiouAEIOU': # first iteration starts and define the vowels 
        new+=str(ip)  # if vowel is there replace the vowel with the index position
    else:
        new+=str(s[ip])    # else dont replace the letter
print(new)      # print the new string  