def containsDuplicate(arr):
    # approach 1 with nested loop 
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i] == arr[j]:
    #             print(f"found duplicate at {i} {j} for value {arr[i]}")

    # Approach 2 with sorted Data
    # arr.sort()
    # for i in range(1, len(arr)):
    #     if arr[i] == arr[i-1]:
    #         print(f"yes there is same dublicate value with data as {arr[i]}")

    # approach 3 with dict data
    dataDict = {}
    for index,data in enumerate(arr):
        if data in dataDict:
            print(f"yes there is dublicate value for {data}")
        else:
            dataDict[data] = index

containsDuplicate([4,5,3,1,7,9,2,5,13,13])