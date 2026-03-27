# class RangeIterator():
#     def __init__(self,sl,el,up=1):
#         print('__init__')
#         self.sl=sl
#         self.el=el
#         self.up=up
#     def __iter__(self):
#         print('__iter__')   
#         self.i=1
#         return self 
#     def __next__(self):
#         print('__next__')
#         if self.i<=self.el:
#             res=self.i
#             self.i+=self.up
#             return res
#         raise StopIteration  
# RIO=RangeIterator(1,10)   
# for value in RIO:
#     print(value) 


# class RangeIterator():
#     def __init__(self,sl,el,up=1):
#         self.sl=sl
#         self.el=el
#         self.up=up
#     def __iter__(self):
#         self.i=1
#         return self
#     def __next__(self):
#         if self.i<=self.el:
#             res=self.i
#             self.i+=self.up
#             return res               
#         raise StopIteration
# RIO=RangeIterator(1,20)
# for value in RIO:
#     print(value)        


# cubes of numbers

# class CubeIterator():
#     def __init__(self,sl,el,up=1):
#         self.sl=sl
#         self.el=el
#         self.up=up
#     def __iter__(self):
#         self.i=1
#         return self
#     def __next__(self):
#         if self.i<=self.el:
#             res=self.i**3
#             self.i+=self.up
#             return res
#         raise StopIteration
# RCO=CubeIterator(1,20)    
# for value in RCO:
#     print(value)
        

# custom iterator for fibonocci(first n numbers)
# class FiboIterator():
#     def __init__(self,fv,sv,n):
#         self.fv=fv
#         self.sv=sv
#         self.n=n
#     def __iter__(self):
#         self.i=1
#         return self
#     def __next__(self):
#         if self.i<=self.n:
#             self.i+=1
#             result=self.fv
#             self.fv,self.sv=self.sv,self.fv+self.sv
#             return result 
#         raise StopIteration
# RFO=FiboIterator(2,3,10)

# for value in RFO:
#     print(value)
        





# class FiboIterator():
#     def __init__(self,fv,sv,n):
#         self.fv=fv
#         self.sv=sv
#         self.n=n
#     def __iter__(self):
#         self.i=1   
#         return self 
#     def __next__(self):
#         if self.i<=self.n:
#             self.i+=1
#             result=self.fv 
#             self.fv,self.sv=self.sv,self.fv+self.sv
#             return result        
#         raise StopIteration
# RFO=FiboIterator(1,2,10)
# for value in RFO:
#     print(value)        


# custom (range)
# class FiboIterator():
#     def __init__(self,sl,el,n):
#         self.sl=sl
#         self.el=el
#         self.n=n
#     def __iter__(self):
#         self.i=1
#         return self
#     def __next__(self):
#        if self.i<=self.n:
#             self.i+=1
#             res=self.sl
#             self.sl,self.el=self.el,self.sl+self.el
#             return res
#        raise StopIteration

# rio=FiboIterator(20,22,10)

# for value in rio:
#     print(value)    
# 
# 

# class FiboIterator():
#     def __init__(self,fv,sv,n):
#         self.fv=fv
#         self.sv=sv
#         self.n=n
#     def __iter__(self):
#         self.i=1
#         return self
#     def __next__(self):
#         if self.i<self.n:
#             self.i+=1
#             res=self.sv
#             self.fv,self,sv=self.sv,self.fv+self.sv
#             return res
#         raise StopIteration    




















































    


#remove duplicates


# s=input()
# res=''
# for i in s:
#     if i not in res:
#         res+=i
# print(res)        











#fact

# n=int(input())
# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)    

