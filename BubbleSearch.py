#bubble sort
import time

start = time.process_time()
print(start)
def sort(nums):
    for i in range(len(nums)-1,0,-1): #check the number of elements we have . works in this loop
        for j in range(i): #looping over the elememts in the list
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = []
for i in range(0,10000):
    nums.append(i)

sort(nums)

#print(nums)
print("time of perf counter",time.perf_counter())

end = time.process_time()
print(end)
print(end-start)

