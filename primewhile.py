# WAP to check wheather the given number is prime or not with while loop
n=int(input()) # take the user input
if n>1: # if loop starts if n is greater than 1
    a=2 # iunitialization starts with 2
    while a>n//2+1: # while loop starts with  a> than n//2+1
        if n%a==0: # iteration starts by dividing the n by the divisor and checking wheather its 0
            print('its not prime number')# print the o/p
            break # break the statement if the number is not prime
        a+=1  # updation is given by 1 
    else: # else the number is checked to be prime
        print('number is  prime') # print idf the number is prime
else:
     print('number is not prime')# print o/p if the number is not prime(if its 1)
