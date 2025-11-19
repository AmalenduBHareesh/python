# WAP to print alternate prime numbers
ll=int(input()) #take the lower limit and upper limit from the user 
ul=int(input())
c=0 # initiate the count as 0
for n in range(ll,ul+1): # take the range of the numbers from lower limit to upper limit+1
    if n>1:
        for i in range (2,n//2+1): # take the for loop with range starting from 2 and ending with the half of the value of the givn number 
            if n%i==0: # if the number is divisible by the range if numbers,break the loop
                break 
        else:
            c+=1     #else,the count is incremented
            if c%2==0: # and if the count is completely divisible by 2, thwn it will be an alternate number
                print(n)   # print the output  