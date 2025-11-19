# WAP to check wheather the number is perfect number or not
# divisors sum is eqaul to the number
n=int(input()) # take the user input
sd=0 # assume there are no divisors
for  divisor in range(1,n//2+1): # for loop starts with range starting with 1 to n/2+1
    if n%divisor==0: # iteration starts by dividing the n by the divisor and checking wheather its 0
        sd+=divisor # add the sd with divisor
if n==sd:# the second if loop starts to check wheather the n is eqaul to the sd
    print('n is a perfect number') # print the output 
else:
    print('n is not a perfect number')  # print the output          