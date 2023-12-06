# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# def solution(nums):
#     if not nums:
#         return []
#     count = 0
#     total = 0
#     for num in nums:
#         if num > 0:
#             count += 1
#         elif num < 0:
#             total += num
#     return [count, total]

def solution(nums):
    if not nums:
        return []
    positives = []
    negatives = []
    for num in nums:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)
    # print('Postitives:', positives)       
    # print('Negatives:', negatives)       
    count = len(positives)
    total = sum(negatives)
    return [count, total]


print(solution([2, 4, -4, -3, -1, 10, 14, 3, -9]))
