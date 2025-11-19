#WAP to print first 50 primr numbers
n=2 #initialize the while loop from 2
c=0 #initialize the count from 0
while c<50: #while loop starts with the range less than 50
    if n>1: 
        for i in range(2,n//2+1): # for loop starts with the 2 and till the half of the number
            if n%i==0: # if the number is completely divisible  by any of the i values,then break the statements
                break
        else:  # if its not divisible,
            c+=1 # count is inccremented by 1
            print(n)  # print the o/p
    n+=1       # give the updation of the while loop(till it reaches 50)        