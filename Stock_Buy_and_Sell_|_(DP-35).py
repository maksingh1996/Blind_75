def stockBuyNSell(arr):
    profit = 0
    minValue = arr[0]

    for i in range(1, len(arr)):
        profit = max(profit, arr[i]- minValue)
        minValue = min(minValue, arr[i])
    print(profit)        

stockBuyNSell([8,4,5,7,9,17])