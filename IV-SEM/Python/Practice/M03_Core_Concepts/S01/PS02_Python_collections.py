'''#running sum
nums = list(map(int,input().split()))
sum1 = 0
res = []
for i in range(len(nums)):
    sum1 +=nums[i]
    res.append(sum1)
print(res)
# input:1 2 3 4 5
# output:[1, 3, 6, 10, 15]'''
#duplicates
arr = list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]!=arr[i+1]:
        print("false")
    else:
        print(true)
