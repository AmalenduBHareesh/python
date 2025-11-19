# # 12) WAP to find the absolute difference of all even integers and odd integers present in the given list
# l= eval(input()) # we get the list input from the user  [2,3,4,5]
# se=0    #assuming there is are no even numbers in the string
# so=0     #assuming there is are no odd numbers in the string
# for ele in l:      #for loop starts 
#     if ele%2==0:    #iteration 1,checking the element is even,if yes count,and skip teh remaining steps
#         se+=ele     #increment the count by 1
#     else:          #iteration 2,checking element is odd 
#         so+=ele    #increment if its odd
# print (abs(se-so)) #print the output by using abs to find the absolute difference (difference between 6 and 8)  

# OR

l= eval(input())  # we get the list input from the user [2,3,4,5]
se=0   #assuming there is are no even numbers in the string
so=0    #assuming there is are no odd numbers in the string
for ele in l: #for loop starts 
    if ele%2==0:   #iteration 1,checking the element is even,if yes count,and skip teh remaining steps
        se+=ele  #increment the count by 1(adding 2 and 4)
    else:       #iteration 2,checking element is odd 
        so+=ele  #increment if its odd(adding 3 and 5)
    if se>so:   # iteration 3, find which sum is greater
        k=se-so #find the diff  (difference between 6 and 8)
    else:  # iteration 4, find which sum is greater
        k=so-se     #find the diff     (difference between 6 and 8)
      
print (k)    #print the output 
