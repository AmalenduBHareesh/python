# # l = [8,3,1,6,9,2]

# # #first alp sort in asc,second half in desc
# # mid=len(l)//2
# # first=l[:mid]
# # last=l[mid:]

# # first.sort()
# # last.sort(reverse=True)

# # print(first+last)


# # move vowels to front
# # s='amalendu'
# # vowels=''
# # others=''
# # for ele in s:
# #     if ele in 'aeiouAEIOU':
# #         vowels+=ele
# #         print(vowels)
# #     else:
# #         others+=ele
# #         print(others)
# # print(vowels+others)            



# # Even Left, Odd Right (Maintain Order)
# # l = [1,2,3,4,5,6]
# # even=[]
# # odd=[]
# # for ele in l:
# #     if ele%2==0:
# #         even.append(ele)
# #     else:
# #         odd.append(ele)
# # print(even+odd)            

# # def squares(n):
# #     for i in range(1,n+1):
# #         yield i*i

# # for i in squares(5):
# #     print(i)

# # create a custom iterator to that stops at a vowel

class Stringiterator:
    def __init__(self,s):
        self.s=s
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.s)>self.index:
            ch=self.s[self.index] 
            self.index+=1
            if ch in 'aeiouAEIOU':
                raise StopIteration
            return ch
for i in Stringiterator('python'):
    print(i)        


