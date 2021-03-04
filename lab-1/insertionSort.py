from timeit import default_timer as timer

def insertion_sort(list_n):
    iteration_length = range(1, len(list_n))
    start_time = timer()

    for i in iteration_length:
        value_to_sort = list_n[i]

        while list_n[i-1] > value_to_sort and i > 0:
            list_n[i], list_n[i-1] = list_n[i-1], list_n[i]
            i = i-1
    end_time = timer()
    print(end_time-start_time)
    return list_n
