# 1)program to check wheather the given number is harshad number or not
# An integer which is divisible by sum of its digits then it is called harshad number or niven number
n=int(input()) # take the input from th user side(135)
dummy=n # the value of n is given to a dummy variable to not to modify the give number
summ=0 # assuming the sum is 0
while dummy>0:  # while loop starts with the condition that the dummy is less than 0
    rem=dummy%10 # divide the number by 10(modular division) to get the reminder
    dummy=dummy//10  # divide the number by 10(floor division) to get the quotient
    summ+=rem # add the reminders 
if n%summ==0: # if loop starts ,if the guven number is divisible by the sum of the digits
    print('it is a harshad number') 
else:
    print('its not harshad number')     
    



