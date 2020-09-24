def mergeSort(dataset):
	if len(dataset) > 1:
		mid = len(dataset)//2
		leftSide = dataset[:mid]
		rightSide = dataset[mid:]
		mergeSort(leftSide)
		mergeSort(rightSide)

		i = j = k = 0

		while i < len(leftSide) and j < len(rightSide):
			if leftSide[i] < rightSide[j]:
				dataset[k] = leftSide[i]
				i += 1
			else:
				dataset[k] = rightSide[j]
				j+=1
			k+=1
		while i < len(leftSide):
			dataset[k] = leftSide[i]
			i+=1
			k+=1
		while j < len(rightSide):
			dataset[k] = rightSide[j]
			j+=1
			k+=1
	return dataset

print(mergeSort([2000,309,4,200,-1,0,909,1]))
