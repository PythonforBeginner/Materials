def missingNumber(nums):
    for i in range(0, len(nums)):
        if i not in nums:
            return i
    return len(nums)

if __name__ == '__main__':
    print(missingNumber([3,0,1]))
    print(missingNumber([0,1]))
    print(missingNumber([9,6,4,2,3,5,7,0,1]))
