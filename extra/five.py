# prime in range
# ll=int(input())
# ul=int(input())
# for n in range(ll,ul+1):
#     if n>1:
#         for i in range(2,n//2+1):
#             if n%i==0:
#                 break
#         else: 
#             print(n)      


#pal
# n=int(input())
# rev=0
# dummy=n
# while dummy>0:
#     rem=dummy%10
#     dummy=dummy//10
#     rev=rev*10+rem
# if rev==n:
#     print('pal')  
# else:
#     print('not pal')

#rev of string
# s=input()
# rev=''
# for ele in s:
#     rev=ele+rev
# print(rev)    


#fibbonoci

# a=int(input())
# b=int(input())
# n=int(input())
# print(a,b)
# for i in range(n-2):
#     c=a+b
#     print(c)
#     a,b=b,c

# fact
# n=int(input())
# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)    


# print(list(map(lambda n:n%2==0,[20,30,10])))

# print(list(map(lambda n:int(n),['12','13','22','20'])))

# print(list(map(int,input().split())))

#how many spl charas

# s=input()
# c=0
# for ele in s:
#     if not ele.isalnum():
#         c+=1
# print(c)        



#how many alpha,digits,specialchara

# s=input()
# a=0
# b=0
# c=0
# for ele in s:
#     if ele.isalpha():
#         a+=1
#     elif ele.isdigit():
#         b+=1
#     else:
#         c+=1
# print(a)
# print(b)
# print(c)

# abs difference of odd and even
# n=eval(input())
# se=0
# so=0
# for ele in n:
#     if ele%2==0:
#         se+=ele
#     else:
#         so+=ele
# print(abs(se-so))            

