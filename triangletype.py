# program to determine whether the triangle is isosceles, scalen or right angled
a = int(input('enter the first side of triangle\n'))
b = int(input('enter the second side of triangle\n'))
c = int(input('enter the third side of triangle\n'))
if a+b>c or b+c>a or c+a>b:
    if a==b or b==c or c==a:
        print("The given triangle is Isosceles Triangle")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print('The given triangle is right angled Triangle')
    else:
        print('The given Triangle is Scalene Triangle')
else:
    print('Enter the valid side of Triangle')
    
