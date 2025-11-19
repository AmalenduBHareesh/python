#WAP to print the factorial of the given number
n=int(input()) # we take the output from the user
fact=1 #assume its zero and its factorial is given as 1
for f in range(1,n+1):# for loop starts,ranges from 1 to n+1
    fact*=f #the number is multiplied by the next number
print(fact)  # print the output  