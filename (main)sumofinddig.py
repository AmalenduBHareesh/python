# #WAP to print the sum of independent digits of a given number
# logic
# 1)get the reminder by dividing th given number by 10(to get the last digit,modular division %)
# 2)to remove the last digit,divide with 10 and get quotient(floor division //)
# 3) repeat the above steps until the number goes to 0

#program
n=int(input()) # input is gievn from th euser side
dummy=n # the value of n is given to a dummy variable to not to modify the give number
summ=0 # assuming the sum is 0
while dummy>0:  # while loop starts with the condition that the dummy is less than 0
    rem=dummy%10 # divide the number by 10(modular division) to get the reminder
    dummy=dummy//10  # divide the number by 10(floor division) to get the quotient
    summ+=rem # add the reminders 
print(summ)  # print the output