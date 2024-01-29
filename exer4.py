#condition
'''
years = input('input your years : ')
age = int(years)

if age < 3 or age >= 70 :
    print('your free')

'''

score = input('input your score : ')
integer_score = int(score)

if  integer_score >= 90 :
    print('S')
elif 90 > integer_score >= 80  :
    print('A')
elif 80 > integer_score >= 70 :
    print('B')
elif 70 > integer_score >= 60 :
    print('C')
else :
    print('D')

    