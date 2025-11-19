#3)WAP to print the sum of first n numbers
a=int(input())# integer input from the user
summ=0# assuming the input is 0
for n in range(1,a+1,1): #for loop starts,range within 1 and a=1
    summ+=n  #the number is added by the next number
print(summ) # print the output  