#10)WAP to print the sum of even numbers in the given string
s= input() # we get the string input from the user 
summ=0    #assuming there is are no even numbers in the string
for ele in s: #for loop starts
    if ele.isdigit() and int(ele)%2==0:    # iteration 1 to check wheather the element is digit and an even number,is not skip 
        summ+=1     # if the element is an even number add the element
print(summ)      #print the output      