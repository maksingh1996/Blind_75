def maxSubarray(arr):
    maxSum = arr[0]
    currSum = 0

    for data in arr:
        if currSum < 0:
            currSum = 0
        currSum += data
        maxSum = max(maxSum, currSum)

    print(maxSum)

maxSubarray([-2,1,-3,4,-1,2,1,-5,4])