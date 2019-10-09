""" Python program to find runner up score"""
a =int(input())     #Enter the total no values;
l=[]
for i in range(1,a+1):        #loop run a times;
    l.append(int(input("enter the list Element:")))    #it takes the value input;
print("the list is",l)     #it print of input values;
c=set(l)                    #set method convert the list into set and duplicate value removed;
d = list(c)                 #list method convert the set into list;
print("Runner up score is:",d[-2])    #it print the last second value which is the runner up score;
