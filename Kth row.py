''' Python program to find k such that all elements in k'th row 
	are 0 and k'th column are 1'''

def find(arr): 

	# store length of the array 
	n = len(arr) 

	# start from top right-most corner 
	i = 0
	j = n - 1
	
	# initialise result 
	res = -1

	# find the index (This loop runs at most 2n times, we 
	# either increment row number or decrement column number) 
	while i < n and j >= 0: 

		# if the current element is 0, then this row may be a solution 
		if arr[i][j] == 0: 

			# check for all the elements in this row 
			while j >= 0 and (arr[i][j] == 0 or i == j): 
				j -= 1

			# if all values are 0, update result as row number	 
			if j == -1: 
				res = i 
				break

			# if found a 1 in current row, the row can't be a 
			# solution, increment row number 
			else: i += 1

		# if the current element is 1 
		else: 

			#check for all the elements in this column 
			while i < n and (arr[i][j] == 1 or i == j): 
				i +=1

			# if all elements are 1, update result as col number 
			if i == n: 
				res = j 
				break

			# if found a 0 in current column, the column can't be a 
			# solution, decrement column number 
			else: j -= 1

	# if we couldn't find result in above loop, result doesn't exist 
	if res == -1: 
		return res 

	# check if the above computed res value is valid 
	for i in range(0, n): 
		if res != i and arr[i][res] != 1: 
			return -1
	for j in range(0, j): 
		if res != j and arr[res][j] != 0: 
			return -1; 

	return res; 

# test find(arr) function 
arr = [ [0,0,1,1,0], 
		[0,0,0,1,0], 
		[1,1,1,1,0], 
		[0,0,0,0,0], 
		[1,1,1,1,1] ] 

print (find(arr)) 
