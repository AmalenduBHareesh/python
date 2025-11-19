#A Disarium number is a number in which the sum of its digits powered with their respective positions is equal to the number itself.
n=int(input()) # take the input from th user side(135)
dummy=n # the value of n is given to a dummy variable to not to modify the give number
l=len(str(n)) # give a value to the length of the n by typecasting to string
summ=0 # assuming the sum is 0
while dummy>0:  # while loop starts with the condition that the dummy is less than 0
    rem=dummy%10 # divide the number by 10(modular division) to get the reminder
    dummy=dummy//10  # divide the number by 10(floor division) to get the quotient
    rem**=l
    summ+=rem # add the reminders 
    l-=1
if summ==n: # if loop starts ,if the guven number is divisible by the sum of the digits
    print('it is a disarium number') 
else:
    print('its not disarium number')     
    