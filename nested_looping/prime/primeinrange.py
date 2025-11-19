#WAP to print prime numbers in a given range
ll=int(input()) # take the lower limit from the user
ul=int(input()) # take the upper limit
for n in range(ll,ul+1): # take the range to from the starting limit to trh ending limit 
    if n>1:
        for i in range(2,n//2+1):  # to take the prime numbers,take the range starting from 2 and ending in the half of the value of the number
            if n%i==0: # if the user input is divisible by any of the numbers less than that of the given number,break the loop ,since it is not prime
                break
        else:    # else print the statement
         print(n)