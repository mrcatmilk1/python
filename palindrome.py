# word = input("Word: ")
# letters = list(word)
# for i in range(len(letters)//2):
#         j = -i - 1
#         letters[i], letters[j] = letters[j], letters[i]
#         print(letters)





# if word == ''.join(letters):
#     print("Palindromic")
# else:
#     print("Non-palindromic")

def is_palindromic(num):
    word = str(num)
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            return False
    return True

def solve(nums: list):
    list_palindromic = True
    all_palindromic = True

    for i in range(len(nums)):
        if nums[i] != nums[-i-1]:
            list_palindromic = False
    for num in nums:
        if not is_palindromic(num):
            all_palindromic = False

    return list_palindromic, all_palindromic, sum(nums)


nums = list(map(int, input('nums: ').split()))
list_palindromic, all_palindromic, total = solve(nums)


if list_palindromic and all_palindromic:
    print("e")
elif list_palindromic:
    print("h")
elif all_palindromic:
    print("g")
else:
    print("a")