# 1)WAP to check wheather the given number is even or odd,if even print YES otherwise NO from a list
l=[11,22,33,44,55,66] # take the list input
for ele in l: #     for loop starts 
    if ele%2==0: # if loop starts to check wheather the element is even
        print('YES') # print YES if there is even element present in th list
        break # terminate the loop if yes
else:
    print('NO')    # if there is no even element present print NO 