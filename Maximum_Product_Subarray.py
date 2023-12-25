def MaxProdSubArray(arr):
    res = max(arr)
    curMin, curMax = 1, 1

    for data in arr:
        if data == 0:
            curMin, curMax = 1, 1
            continue
        tmp = data*curMax
        curMax = max(data*curMax, data*curMin, data)
        curMin = min(data*curMax, data*curMin, data)
        res = max(res, curMax)
    print(res)

MaxProdSubArray([-1,-2,-3,0,4,5])