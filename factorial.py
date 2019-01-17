#program to find factorial of given number using while loop:-
n = int(input("Enter the no to find factorial\n"))
temp = n
f = 1
while(temp>0):
    f = f*temp
    temp = temp-1
print('factorial of ',n,'is', f)
