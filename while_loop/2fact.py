#WAP to print the factorial of the given number using while loop
a=int(input()) # the user input is taken
fact=1 # assume the factorial is 1,that is the factorial of 0 is 1
i=1 # tha loop ins initialized by the value 1
while i<a+1: # while  loop starts 
    fact*=i #the factorial is done by multipying the values
    i+=1 #the count is incremented 
print(fact) # the output is printed
   

# n=int(input()) # we take the output from the user
# fact=1 #assume its zero and its factorial is given as 1
# for f in range(1,n+1):# for loop starts,ranges from 1 to n+1
#     fact*=f #the number is multiplied by the next number
# print(fact)  # print the output  
