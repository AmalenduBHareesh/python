#2)WAP ro print even numbers in a given range
a=int(input()) # first element integer input from the user
b=int(input()) # end element integer input from the user
for n in range(a,b,1): #for loop starts ,ranges from a and b with updation 1
    if n%2==0:  # checking wheather the number is even or not
        print(n)  # print the output  

        