# WAP to check wheather the given number is prime or not
n=int(input())# take the user input
if n>1: # if loop starts if n is greater than 1
    for divisor in range(2,n//2+1):  # for loop starts with range starting with 1 to n/2+1
        if n% divisor==0: # iteration starts by dividing the n by the divisor and checking wheather its 0
            print('its not prime number') # print the o/p
            break # break the statement if the number is not prime
    else: # else the number is checked to be prime
        print('number is  prime')
else:
     print('number is not prime')# print o/p if the number is not prime(if its 1)
