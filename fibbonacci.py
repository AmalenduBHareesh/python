# fibonnoci series

a= int(input())# take input from the user (first number in the series)
b= int(input())# take input from the user (second number in the series)
n= int(input())# take input from the user (number of elememts needed in the series)
print(a,b)# print the two inputs first
for i in range(n-2):# for loop starts,by n-2 values,since two are already printed
    c=a+b # third value is the sum of previous two values
    print(c)# print the third value
    a,b=b,c # swap the values and continue

    