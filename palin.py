# to check wheather the number is palindrome or not
n=int(input()) # take the input from th user side(135)
dummy=n # the value of n is given to a dummy variable to not to modify the give number rev=0 # assuming the sreverse value is 0
rev=0
while dummy>0:  # while loop starts with the condition that the dummy is less than 0
    rem=dummy%10 # divide the number by 10(modular division) to get the reminder
    dummy=dummy//10  # divide the number by 10(floor division) to get the quotient rev+=rem # add the reminders 
    rev=rev*10+rem # add the reversed value that is multiplied by 10 to the reminder got
if n==rev: # if loop starts ,if the given number is equal to its reverse
    print('it is a palindrome number') 
else:
    print('its not palindrome number')     