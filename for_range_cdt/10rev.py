#10) WAP to reverse a given string without using slicing
# s=input()
# rev=''
# for ele in s:
#     rev=ele+rev
# print (rev)    


# negetive index position
s=input() # input is taken from the user 
rev='' # a new string is introdced inorder to not modify the given string
for ip in range (-1,-(len(s)+1),-1): # for loop starts with range starting from the -1 ending in -(len(s)+1) and with the updation of -1 
    rev+=s[ip] # add the reversed elment in the new string
print(rev)   # print the output 



# # positive index position  
# s=input()
# rev=''
# for ip in range ((len(s)-1),-1,-1):
#     rev+=s[ip]
# print(rev)  
