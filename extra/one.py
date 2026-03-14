# # 3)WAP to print how many vowels are present in the given strings
# s=input()
# vowels='aeiou'
# c=0
# for ele in s:
#     if ele.lower()in vowels:
#         c+=1
# print(c)        


# #consonents

# s=input()
# vowels='aeiou'
# c=0
# for ele in s:
#     if ele.isalpha() and ele.lower() not in vowels:
#         c+=1
# print(c)        

# ams 
# n=int(input())
# p=len(str(n))
# summ=0
# dummy=n
# while dummy>0:
#     rem=dummy%10
#     dummy=dummy//10
#     rem**=p
#     summ+=rem
# if summ==n:
#     print('amstrong')
# else:
#     print('not ams')        


#ams without typecasting

# n=int(input())
# dummy1=n
# dummy2=n
# summ=0
# l=0
# while dummy1>0:
#     dummy1=dummy1//10
#     l+=1
# while dummy2>0:
#     rem=dummy2%10
#     dummy2=dummy2//10
#     summ+=rem**l
# if summ==n:
#     print('ams')
# else:
#     print('not ams')        
    

# disarium
n=int(input())
dummy=n
summ=0
l=len(str(n))
while dummy>0:
    rem=dummy%10
    dummy=dummy//10
    summ+=rem**l
    l-=1
if summ==n:
    print('dis')
else:
    print('not')        
