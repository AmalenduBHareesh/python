# #pal
# n=int(input())
# dummy=n
# rev=0
# while dummy>0:
#     rem=dummy%10
#     dummy=dummy//10
#     rev=rev*10+rem
# if rev==n:
#     print('pal')
# else:
#     print('not pal')

# prime,rev should be prime and should not be pal




def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False        

def isPal(n):
    rev=0
    dummmy=n
    while dummmy>0:
        rem=dummmy%10
        dummmy=dummmy//10
        rev=rev*10+rem
    if rev==n:
        return True
    else:
        return False  

rev=0
for i in range(2,101,1) :
    n=i
    rev=0
    while n>0:
        rem=n%10
        n=n//10
        rev=rev*10+rem
        
    
    if isPrime(i) and isPrime(rev) and not isPal(i):
        print(i)


# #coming to singletone

# def Singletone(clsAddress):
#     L=[]
#     def inner():

#      if len(L)==0:
#          MCO=clsAddress()
#          L.append(MCO)
#          return L[0]
#       return inner
# @Singletone
# class Multiplex():
#     def __init__(self,tickets):
#         self.tickets=300
#     def booking(self,n):
#         if n<self.tickets:
#             self.tickets-=n
#             print('booked')
#         else:
#             print('ticket left=',self.tickets)
# krish=Multiplex()
# krish.booking(250)
# print(krish)

# singeletone


# def singletone(clsAddress):
#     l=[]
#     def inner():
#         if len(l)==0:
#             mco=clsAddress()
#             l.append(mco)
#             return l[0]
#         return inner

# @singletone
# class Multiplex():
#     def __init__(self,tickets):
#         self.tickets=300
#     def booking(self,n):
#         if n<self.tickets:
#             self.tickets-=n
#             print('booked')
#         else:
#             print('tickets left',self.tickets)
