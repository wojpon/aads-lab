from timeit import default_timer as timer


def binary_search(list_n, item):
    start_index = 0
    end_index = len(list_n) - 1
    start_time = timer()

    while start_index <= end_index:
        midpoint = start_index + (end_index - start_index) // 2
        midpoint_value = list_n[midpoint]
        if midpoint_value == item:
            end_time = timer()
            print("Bianry search time: " + str(end_time-start_time))
            return "Element position: " + str(midpoint)
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return "Item not found"
