# An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits.
n=int(input()) # take the input from the user side(153 1^3+5)
dummy=n # the value of n is given to a dummy variable to not to modify the give number
p=len(str(n)) # give a value to the length of the n by typecasting to string
summ=0 # assuming the sum is 0
while dummy>0:  # while loop starts with the condition that the dummy is less than 0
    rem=dummy%10 # divide the number by 10(modular division) to get the reminder
    dummy=dummy//10  # divide the number by 10(floor division) to get the quotient
    rem**=p
    summ+=rem # add the reminders 
if summ==n: # if loop starts ,if the guven number is divisible by the sum of the digits
    print('it is a armstrong number') 
else:
    print('its not armstrong number')     
    