a =int(input())
l=[]
for i in range(1,a+1):
    l.append(int(input("enter the list Element:")))
print("the list is",l)
c=set(l)
d = list(c)
print("Runner up score is:",d[-2])
