# # # reverse a string


# # s=input()
# # rev=''
# # for ele in s:
# #     rev=ele+rev
# # print(rev)    
# #


# #Remove duplicates from a string


# # s=input()
# # dup=''
# # for ele in s:
# #     if ele not in dup:
# #         dup+=ele
# # print(dup)        






# # s=input()
# # dup=''
# # for ele in s:
# #     if ele not in dup:
# #         dup+=ele
# # print(dup)        



# s=input()
# dup=''
# for ele in s:
#     if ele not in dup:
#         dup+=ele
# print(dup)        



#main in sub

ms=input()
ss=input()
c=0
for ip in range(len(ms)-len(ss)+1):
    if ms[ip:ip+len(ss):]==ss:
        c+=1
print(c)