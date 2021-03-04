from timeit import default_timer as timer


def bubble_sort(list_n):
	iteration_length = len(list_n) - 1
	start_time = timer()
	isSorted = False

	while not isSorted:
		isSorted = True
		for i in range(0, iteration_length):
			if list_n[i] > list_n[i+1]:
				isSorted = False
				list_n[i], list_n[i+1] = list_n[i+1], list_n[i]
	end_time = timer()
	print(end_time-start_time)
	return list_n



