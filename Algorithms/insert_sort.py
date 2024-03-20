import numpy as np
import time

def min_value(lst, starting_p):
    x = starting_p

    for i in range(x + 1, len(lst)):
        if lst[i] < lst[x]:
            x = i
        return x

def insertionSort(lst):
    for i in range(1, len(lst)):
        # Store the value of the current element and its index
        j = i
        # Shift elements greater to the right by one position
        while j > 0 and lst[j - 1] > lst[j]:
            # Swap the current element with the element to its left
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1

times = []

for i in range(100):
    test = np.random.randint(-5000, 5000, 100)

    start = time.perf_counter_ns()
    sort_test = insertionSort(test)
    finish = time.perf_counter_ns()

    t = finish - start
    times.append(t)

print(times)
avg = sum(times)/100
print(avg)

# Displaying data
# data = [-5, 5, 50, 1, 0, -30]
# insertionSort(data)
# print("Sorted array using insertion sort:")
# print(data)
