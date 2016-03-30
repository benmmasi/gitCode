#Ben Masi, maxHeap program in python version 2.7

def maxHeap(Arr):
	for i in range(len(Arr) // 2, -1, -1):
		maxHeapify(Arr, i)

def maxHeapify(Arr, i):
	l = 2 * i + 1
	r = 2 * i + 2
	heapSize = len(Arr) - 1

	if (l <= heapSize and Arr[l] > Arr[i]):
		largest = l
	else:
		largest = i

	if (r <= heapSize and Arr[r] > Arr[largest]):
		largest = r
	if (largest != i):
		Arr[i], Arr[largest] = Arr[largest], Arr[i]
		maxHeapify(Arr, largest)

def maxHeapAnalysis():
	#in the string below, add the name of 
	#the current text file you are testing
	f = open('random-10000.txt')
	A = f.readlines()
	from time import time
	start_time = time()
	maxHeap(A)
	end_time = time()
	runtime = end_time - start_time
	print runtime
	print A[:15]

maxHeapAnalysis()