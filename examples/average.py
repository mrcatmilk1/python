from random import randint

nums = [randint(1, 1000) for i in range(randint(1, 2000))]


# nums is a list of numbers
# TODO: Find the average of all numbers in nums as well as the largest number

# average: 230.4567
# most frequent: 100

shark = 0
fish = len(nums)
largest = 0
frequent = 0
e = 0
for num in nums:
    shark += num
    if num > largest:
        largest = num
    littlebird = nums.count(num)
    if littlebird > frequent:
        frequent = littlebird
        e = num
average = shark / fish

print(f'average: {average}')
print(f'largest: {largest}')
print(f'{e} came out {frequent} times')
print(nums.count(e))