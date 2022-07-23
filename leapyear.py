'''
Purpose: for finding a leapyear
Author: Rounaq
Date: 17-07-2022
'''

def year(x):
    if x % 4 == 0:
        print(x,' is a leap year.')
    else:
        print(x,' is not a leap year.')

enter_year=int(input('YEAR: '))
year(enter_year)