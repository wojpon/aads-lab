from selectionSort import selection_sort
from insertionSort import insertion_sort
from bubbleSort import bubble_sort
from binarySearch import binary_search
import random

random_array = [random.randint(1, 100) for _ in range(100)]

print("Selection sort time:")
selection_sort(random_array)

print(binary_search(random_array, 76))

print("Insertion sort time:")
insertion_sort(random_array)

print("Bubble sort time:")
bubble_sort(random_array)
