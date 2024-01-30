'''num =2 

print(num)
print('no',end ='\n')
print('yes', end ='hoge')
print('yes')

--------------

count = 0
num = 10
notcount = 10
while count < num:
    count += 1
    notcount -= 1
    if notcount == 0 :
        print('last')
    else :
        print(notcount)


limit = 10

for count in range(limit) :
    print('for : ', count)
#finish

start = 5
stop = 99
step = 2

for count in range (start, stop, step) : # start ~ stop +step > count
    print('for : ' ,count)


sum =0
count = 1
for count in range(5):
    print(count+1, end='')
    nums = input('st input years : ')
    sum += int(nums)
    
print(sum)

'''

#ここから課題１：Whileを使ってfactorial計算
#課題２：for文を使ってfactorial計算
'''
print('factorialを計算します ',end = '')
base = int(input('基数を入力してください：'))
result = 1
count = 1
num = base

while count < base :
    
    result *= num
    num -= 1
    count += 1
    
if base >= 2 :
    print(base,'のfactorialは',result,'です')
elif base == 0 or base == 1:
    print(base,'のfactorialは1です')
elif base < 0 :
    print('0以上の整数を入力してください')
    
'''
print('factorialを計算します ',end = '')
base = int(input('基数を入力してください：'))
result = 1
count = 1


for count in range(1, base+1, 1) :
    result *= count
    
if base >= 2 :
    print(base,'のfactorialは',result,'です')
elif base == 0 or base == 1:
    print(base,'のfactorialは1です')
elif base < 0 :
    print('0以上の整数を入力してください')
    
