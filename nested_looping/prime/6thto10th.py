#WAP to print the 10th prime number
n=2 #initialize the while loop from 2
c=0 #initialize the count from 0
while c<10: #start the while loop 
    for i in range(2,n//2+1) :# for loop starts with the 2 and till the half of the number
        if n%i==0:  # if the number is completely divisible  by any of the i values,then break the statements
            break
    else:
        c+=1 # else,increment the count
        if c>=10: # if the count is 6 between 6,print upto when the count is 10
            print(n)
    n+=1 #update the while loop 