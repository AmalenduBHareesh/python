#12) WAP to replace all the vowels with their index positions
s=input() # take the input from the user
new='' # give an emplty string to not modify the given string
ip=0 #initialize the ip with 0
while ip<len(s): # while loop starts with the condition that the ip is less than the length of the given string
    if s[ip] in 'aeiouAEIOU': #first iteration starts with if loop checking the condition wheather it is a vowel or not
        new+=str(ip) # if the alphabet is vowel then replace it with the index positions
    else:
        new+=s[ip] #else dont replace but just be with the current letter
    ip+=1     # update the while loop by 1
print (new)   #print the output        
