for i in range (10,0,-1): 
    print (i)
x = 1
result =1 
while x < 6 : 
    result = x * result
    x+=1 
print(result)
num = 0 
nums = [3, 7, 2, 9, 4, 11, 6] 
for num in nums: 

    if num > 10:
        break
    if num % 2 != 0:
            continue
    else:
        print(num)

