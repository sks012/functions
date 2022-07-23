# Purpose:Program for finding factorial of a number.
# Author:Rounaq
# Date:20-07-22


def fact(x):
    a=1
    for z in range(1,(x+1)):
        a=a*z
    print('Factorial of ',x,' is ',a)



num=int(input('Enter any number: '))
fact(num)