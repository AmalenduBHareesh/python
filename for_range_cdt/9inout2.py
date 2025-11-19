#9) An input is given and the output should be the swapped elemwnts between 2 of them 
# the input is [11,22,33,44,55,66] 
# and the output is[22,11,44,33,66,55]

l=[11,22,33,44,55,66]  # input
for ip in range(0,len(l),2): # for loop starts with the starting index position as 0 ,the ending index position as the length of the list and the updation as 2
      l[ip],l[ip+1]=l[ip+1],l[ip] # the elements are swapped to ewach other  like two-two elements 
print(l)     # output is printed      
