"""
sum =0
print('Now sum is  ', sum)

get_num1 = input('Please input to integer : ')
sum += int(get_num1)
print('now sum is ', sum)

get_num2 = input('input to float number : ')
sum += float(get_num2)
print('now sum is : ',sum )

test_hoge = 0.1+0.1+0.1
print(test_hoge)
"""
#Report
'''report1
print(int('4')) #str(4) > int 4 change
print(float(555)) #float 0.0 
print(int(6.6))  
'''#report2
print('Welcome to 100 Yen shop')
buy_num = input('input your nums ')
print(buy_num,'is your number')
notax = 100*int(buy_num)
tax = notax//10
sum = notax-tax
print(notax,tax,sum)

'''review
input으로 받은 값은 모두 str형임
int()or float()형으로 바꿔야 사칙연산 가능
a // b  는 소숫점을 다 버림 = int 형으로 간주 가능
그외 특이사항 없음.
'''