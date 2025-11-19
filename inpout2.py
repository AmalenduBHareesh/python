# # input='aaabbddddcccaaab'
# # output='a3b2d4c3a4b1'
# s=input() # take the input
# ns='' # take a new stringto not modify the string
# c=1 # assume the count to be 1
# for ip in range(1,len(s)): # for loop starts with range starting from 1,to the length if the string
#       if s[ip] == s[ip-1]: #if the first element is equal to the 0th element 
#         c+=1 # if its equal ,increment the count
#       else:
#         ns=ns+s[ip-1]+str(c) # print the string with that elemnt and its string value of the count
#         c=1 # restart the count from 1
#       if ip == len(s)-1: # and if the ip is at the last element ,
#         ns=ns+s[ip]+str(c)     #the new string is printed with the alphabet and the previous count
# print(ns)       # print the new string  

###########################################################################################################

# input='a3b2d4c3a4b1'
# output='aaabbddddcccaaab'

s= input()
new=''
for ip in range(0,len(s),2):
   new=new+s[ip]*int(s[ip+1])
print(new)  

