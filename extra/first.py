#hattb3kkk
#vowel,@@@------>digit,$$-----> k,0

s=input()
vowels='AEIOUaeiou'
new=''
for ele in s:
    if ele in vowels:
        new+='@@@'
    elif ele.isdigit():
        new+='$$'   
    elif ele=='k':
        new+='0' 
    else:
        new+=ele     
print(s)          
print(new)        