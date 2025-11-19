#WAP to find the sum of digits present in the string 
s= input()# we get the string input from the user 
summ=0 #assuming there is are no integers in the string
for  ele in s: # for loop starts
    if ele.isdigit(): #iteration 1,cheching the element is a digit,if false skip the step and take next element
        summ+=int(ele)  #add the element if it is a digit
print(summ) # print the output