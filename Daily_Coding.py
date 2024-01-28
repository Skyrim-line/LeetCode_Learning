nums = [0, 1, 2, 4, 5, 7]
# ["0->2","4->5","7"]

# ["0","2->4","6","8->9"]
# nums = [0, 2, 3, 4, 6, 8, 9]
# ["0", "2->4", "6", "8->9"]
sample = []
start=0
for i in range(1,len(nums)):
    if nums[i-1]+1!=nums[i]:
        if i-1==start:
            sample.append(str(nums[start]))
        else:
            sample.append(str(nums[start])+'->'+str(nums[i-1]))
        start=i
print(sample)




