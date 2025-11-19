# print   
# *****
# *****
# *****
# *****
# *****
# for row in range(1,6):
#     for col in range(1,6):
#         print('*',end=' ')
#     print()    


# *
#  *
#   *
#    *
#     *
# for row in range(1,6):
#     for col in range(1,6):
#         if row==col: 
#          print('*',end=' ')
#         else:
#            print(' ',end=' ')
#     print()   
# 

#     *
#    *
#   *
#  *
# *


# for row in range(1,6):
#     for col in range(1,6):
#         if row+col==6: 
#          print('*',end=' ')
#         else:
#            print(' ',end=' ')
#     print()            



# *   *
#  * *
#   *
#  * *
# *   *
 
# n=int(input('Enter the number:'))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row==col or row+col==n+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')    
#     print()    



# *   
# * * 
# * * *
# * * * *
# * * * * *
# n=int(input('Enter the number:'))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row>=col:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')    
#     print()    



# * * * * * 
#   * * * *
#     * * *
#       * *
#         *
# n=int(input('Enter the number:'))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row<=col:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')    
#     print()    


#         * 
#       * *
#     * * *
#   * * * *
# * * * * *

# n=int(input('Enter the number:'))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         if row+col>=n+1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')    
#     print()    




# * * * * * 
# * * * *
# * * *
# * *
# *

n=int(input('Enter the number:'))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col<=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')    
    print()    
