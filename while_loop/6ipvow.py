#6)WAP to print all the index positions of all the viwels in the given string
s=input() # the string input is taken from the user
ip=0 #the loop is initialized by 0
while ip<len(s): # while loop starts with condition taht the the ip will be less than the length of the string
    if s[ip] in 'aeiouAEIOU':#if loop starts  ,by checking wheather the elemnts are vowels 
        print (ip)# the output is printed
    ip+=1 # the ip is updated by 1
         