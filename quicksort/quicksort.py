def countdown(i):
	print(i)
	if i <= 1:
		return
	else:
		countdown(i - 1)

def factorial(i):
	if i == 1:
		return 1
	else:
		return i * factorial(i - 1)

# def quicksort(array):
# 	if len(array) < 2:
# 		return array
# 	else:
# 		# less = []
# 		# greater = []
# 		base = array[0]
# 		# for i in array:
# 		# 	if(i <= base):
# 		# 		less.append(i)
# 		# 	else:
# 		# 		greater.append(i)
# 		less = [i for i in array[1:] if i <= base]
# 		greater = [i for i in array[1:] if i > base]
# 		# print(less)
# 		# print(greater)
# 		return quicksort(less) + [base] + quicksort(greater)

def quicksort(array):
	if len(array) < 2:
		return array
	else:
		less = []
		greater = []
		base = array.pop(0)
		for i in array:
			if(i <= base):
				less.append(i)
			else:
				greater.append(i)
		return quicksort(less) + [base] + quicksort(greater)
print(quicksort([9,8,7,5,10]))