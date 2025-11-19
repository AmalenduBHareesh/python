#11)input and output is given
# input:[11,20,'hai123','25',['bye',40],[10]]
# output:56
# input:[2,5,6,'78'[50],'h48']
# output:91
# we need to add the integers and integers inside the string and find the sum

# l=eval(input()) 
# summ=0
# for ele in l:
#     if type(ele)==int:
#         summ+=ele
#     elif type(ele)==str and ele.isdigit():
#         summ+=int(ele)   
# print (summ)         
  
l=eval(input())    # we get the list input from the user [11,20,'hai123','25',['bye',40],[10]]
summ=0    #assuming there is are no integers and integers inside string in the list 
for ele in l: # for loop starts
    if isinstance(ele,int): #iteration 1,to check wheather the element is integer,using isinstance
        summ+=ele  #if yes,inrement the value and add
    elif isinstance(ele,str) and ele.isdigit():    #iteration 2,to check wheather the element is string,using isinstance and then checking wheather it is an integer
        summ+=int(ele)   # if yes add the element
print (summ)    #print the output sum     
