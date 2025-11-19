#10) WAP to reverse a given string without using slicing
s=input() # take the string input from the user(amalendu)
rev='' # declare a new strimg to not modify the give string
ip=-1 # the while loop os initialized by -1
while ip> -(len(s)+1): # while loop starts with the ip greater -(len(s)+1)
    rev+=s[ip] # the reversed elements are added t the new string
    ip+=-1 #the updation if the string is given as -1
print(rev)  # print the output