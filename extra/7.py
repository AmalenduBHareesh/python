# # count vowels
# s= input()
# vowels='aeiouAEIOU'
# c=0
# for ele in s:
#     if ele in vowels:
#         c+=1
# print(c)        


#filter even numbers

# l=[1,2,4,3,5,6,7,8,9]
# res=list(filter(lambda n:n%2==0,l))
# print(res)

# l=[1,2,3,4]
# res=list(map(lambda x:x*x,l))
# print(res)

# rev a number

# n= int(input())
# rev=0
# while n>0:
#     rem=n%10
#     n=n//10
#     rev=rev*10+rem
# print (rev)    


# s = input()

# for i in set(s):
#     print(i, s.count(i))

#character count
# s=input()
# res={}
# for ele in s:
#     if ele in res:
#         res[ele]+=1
#     else:
#         res[ele]=1
# print(res)            

# number reverse
# n=12345
# rev=int(str(n)[::-1])
# print(rev)

#reverse a string

# n=input()
# rev=''
# for ele in n:
#     rev=ele+rev
# print(rev)    

# s=input()
# if s==s[::-1]:
#     print('pal')
# else:
#     print('no')    

#anagram
# s1=input()
# s2=input()
# if sorted(s1)==sorted(s2):
#     print('yes')
# else:
#     print('no')    



#amstong

# n=int(input())
# dummy=n
# summ=0
# p=len(str(n))
# while dummy>0:
#     rem=dummy%10
#     dummy=dummy//10
#     summ+=rem**p
# if n==summ:
#     print('ams')
# else:
#     print('no')    


#sum of digits and reverse

# n=int(input())
# summ=0
# dummy=n
# while dummy>0:
#     rem=dummy%10
#     dummy=dummy//10
#     summ+=rem
# print(summ)
# # rev=(str(summ)[::-1])
# # print(summ)


# s=input()
# d={}
# for ele in s:
#     if ele in d:
#         d[ele]+=1
#     else:
#         d[ele]=1
# print(d)       
# 
    
#reverse each word in sentance

# s=input()
# words=s.split()
# res=''
# for w in words:
#     res+=w[::-1]+''
# print(res)    

# s=input()
# words=s.split()
# res=''
# for w in words:
#     res+=w[::-1]+''
# print(res)


# # remove duplicates
# s='programming'
# d={}
# res=''
# for ele in set(s):
#     if ele not in d:
#         res+=ele
# print(res)        

            
# s=input()
# res=''
# for ele in s:
#     if ele not in res:
#         res+=ele
# print(res)        


#Find max, min, second largest

# l=list(map(int,input().split()))

# l=[10, 20, 5, 40, 30]
# first=l[0]
# second=l[0]
# for i in l:
#     if i>first:
#         second=first
#         first=i
#     elif i>second and i!=first:
#         second=i
# print(second)                

#second largest
# l=[2,3,4,6,8,8,7,4]
# n=list(set(l))
# n.sort()
# print(n[-2])

# l=[2,3,4,6,8,8,7,4]
# n=[]
# for ele in l:
#     if ele not in n:
#         n.append(ele)
# print(n)       
# n.sort()
# print(n[-2])     


# l=[64,34,25,12,22]
# n=len(l)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if l[j]>l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
# print(l)            

# rotate the list by k positions
# l=[1,2,3,4,5]
# k=2
# rotated=l[k:]+l[:k]

# a=[1,3,5]
# b=[2,4,6]
# a.extend(b)
# print(a)
# a.sort()
# print(a)


