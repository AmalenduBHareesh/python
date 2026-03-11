# # 2) WAP TO PRINT HOW MANY TIMES THE GIVEN SUBSTRING IS RESENT IN THE GIVEN STRING
# #       or IMPLEMENT COUNT METHOD LOGIC



# ms=input() # we are taking string input from the user, taking input as 'banana'
# ss=input()# we are taking sub string input from the user,taking as 'an'
# c=0 #assuming the number of substring in the string is 0 by defining with c
# for ele in ms: #for loop starts 
#     if ele == ss: #first iteration 
#         c+=1 #if the sting contains substring ,increment the count  
# print(c)  # printing the output



# ms=input()
# ss=input()
# c=ms.count(ss)
# print(c)

ms=input()
ss=input()
c=0
for i in range(len(ms)-len(ss)+1):
    if ms[i:i+len(ss):]==ss:
        c+=1
print(c)