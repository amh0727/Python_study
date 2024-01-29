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

'''
sum =0
for count in range(5):
    nums = input('st input years : ')
    print(count, nums)
    sum += int(nums)
    
print(sum)

