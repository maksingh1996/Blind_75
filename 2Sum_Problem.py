#### Approach with Dict ####

def twoSum_first(arr, target):
	tempDict = {}
	flag = 0
	for index, data in enumerate(arr):
		second = target - data
		if second in tempDict:
			print(data, f"present at {index} and", second, f"present at {tempDict[second]}")
			flag = 1
			break
		else:
			tempDict[data] = index

	if flag == 0:
		print(f"Element not found with sum {target}")


def twoSum_second(arr, target):
	last = len(arr) -1
	first = 0
	arr.sort()
	print(arr)
	while first < last:
		sum = arr[first] + arr[last]
		print(sum)
		if sum == target:
			print("yes")
			break
		elif sum < target:
			first += 1
		else:
			last -= 1


# twoSum_first([4,7,2,5,8,3,10], 2)

twoSum_second([4,7,2,5,8,3,10], 2)