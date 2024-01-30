"""
first, second, third = input('input 3 words')
print(first)
print(second)
print(third)

one, two, three = input('input 3 words and space').split()
print(one)
print(two)
print(three)
"""

'''
for i in range (3):
    for j in range (3) :
        print('i=', i, '\tj =', j)
'''
    
# multiprication table
'''
for i in range(1, 10):
    for j in range(1, 10) :
        print('\t',i*j, end ='')
    print('')
'''

# flag 
'''while True :
    print('help me')
    choice = input('[1] help him right now\t [2] No')
    
    if choice =='1' : break
    
print('thanks')'''


# Exercise
# ユーザから入力された整数を加算し続けるプログラム / 0 は終了
sum=0 
flag = True
while flag :
    print('整数加算器：')
    integer = int(input('整数を入力してください： '))
    sum += integer
    
    
    if integer == 0 : 
        print('0が入力されました。計算を終了します。\n合計値は',sum,'でした。')
        flag = False
    else :
        print('現在の合計値は',sum,'です')
