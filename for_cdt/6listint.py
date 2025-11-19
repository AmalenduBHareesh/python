#6) WAP to print how many integers are present in the given list
L=eval(input())# taking list input from user [5,6,7,'hai',[2,2]]
c=0 # assuming if there are no integers in the list
for ele in L: # for loop starts 
    if type(ele)== int: # iteration 1,checking the type of element
        c+=1# increment the count if integers are present in th list
print(c)        # print the output