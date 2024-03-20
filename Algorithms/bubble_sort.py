import numpy as np
import time

def min_value(lst, starting_p):
    x = starting_p

    for i in range(x + 1, len(lst)):
        if lst[i] < lst[x]:
            x = i
        return x

def bubble_sort(lst):
    n = len(lst)

    # Loop iterating over each element of the list
    for i in range(n):
        for j in range(n - i - 1):
            # Swap element if the next one is smaller
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

times = []

for i in range(100):
    test = np.random.randint(-5000, 5000, 100)

    start = time.perf_counter_ns()
    sort_test = bubble_sort(test)
    finish = time.perf_counter_ns()

    t = finish - start
    times.append(t)

print(times)
avg = sum(times)/100
print(avg)

# Display data
# data = [-5, 5, 50, 1, 0, -30]
# bubble_sort(data)
# print("Sorted array using bubble sort:")
# print(data)
# List of values for which measurements will be taken
list = [100, 500, 1000, 2000]

times = []

for i in range(100):
    test = np.random.randint(0, 5000, 100)

    start = time.perf_counter_ns()
    sort_test = sorted(test)
    finish = time.perf_counter_ns()

    t = finish - start
    times.append(t)

print(times)
avg = sum(times)/100
print(avg)
