#!/usr/bin/env python3

"""
Script Name: 	insertionSort.py
Description: 	Implementation of Insertion Sort on a list-implelmented array of elements, 
				and accompanying main() function that provides a sample array to be sorted.
			 	This implementation was created as part of an introductory course on data 
				structures. 
				The purpose of this particular implementation is to express the Insertion 
				Sort algorithm using a nested for loop structure.
				The reasoning is that such a structure may better illustrate to students 
				how the comparison of the algorithm to the commonly used example of sorting 
				a hand of cards one has been dealt, ends up resulting in O(N²) time complexity.  
Author: 		Lena Kanellou
Date: 			2024
Repository: 	https://github.com/lenakanellou/objsandends
License: 		MIT License (see LICENSE file in the root of the repository)

Usage:
    python3 insertionSort.py

"""


def insertionSort(arr):

	n = len(arr)

	if n == 0 :
		print("Array is empty!")
		return None, -1 

	for i in range(1, n): 
		print(f"i is {i}")
		value = arr[i]
		#j = i-1
		for j in range(i-1, -1, -1): 
			print(f"j is {j}")
			if value < arr[j]:
				arr[j+1] = arr[j]
				arr[j] = value
			else:
				arr[j+1] = value
				break
		print(arr)
				
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
