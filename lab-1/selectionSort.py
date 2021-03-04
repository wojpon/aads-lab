from timeit import default_timer as timer


def selection_sort(list_n):
    iteration_length = range(0, len(list_n)-1)
    start_time = timer()

    for i in iteration_length:
        min_value = i

        for j in range(i+1, len(list_n)):
            if list_n[j] < list_n[min_value]:
                min_value = j

        if min_value != i:
            list_n[min_value], list_n[i] = list_n[i], list_n[min_value]
    end_time = timer()
    print(end_time-start_time)
    return list_n

