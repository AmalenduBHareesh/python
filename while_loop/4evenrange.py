#4)WAP ro print even numbers in a given range
a=int(input()) # lower limit  input is taken from the user (1)
b=int(input()) # upper limit  input is taken from the user (30)
while a<b: # the while loop starts with the condition that the lower limit is less that the upper limit 
    if a%2==0: # first iteration starts to check wheather the integer is even or not 
        print(a) # print the o/p
    a+=1 # the updation is given by 1


