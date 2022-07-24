# Purpose:Finding sum of numbers given in a list
# Date:24-07-22

list1=[10,89,11,67,53,65,90,70,88,2]
x=0
for num in list1:
    x=x+num
print('Sum of the numbers present in list1: ',x)

greatest_num=list1[0]
for num in list1:
    if num > greatest_num:
        greatest_num=num 
print('Greatest number in list1: ',greatest_num)
    
smallest_num=list1[0]
for num in list1:
    if num < smallest_num:
        smallest_num=num 
print('Smallest number in list1: ',smallest_num)