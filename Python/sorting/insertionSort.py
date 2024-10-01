def insertionSort(arr):

	n = len(arr)

	if n == 0 :
		print("Array is empty!")
		return None, -1 

	for i in range(1, n) : 
		value = arr[i]
		j = i-1

		while j >= 0:
			if value < arr[j] :
				arr[j+1] = arr[j]
				j = j - 1
			else:
				break

		arr[j+1] = value
				
	return arr, 0




def main():


	arr = [11, 5, 7, 23, 3]

	print(f"Input array is {arr}")
	
	sorted_arr, sorting_result = insertionSort(arr)

	if sorting_result != -1 :
		print(f"Sorted array is {sorted_arr}")
	else:
		print("Erroneous input array.")


if __name__ == "__main__":
    main()
