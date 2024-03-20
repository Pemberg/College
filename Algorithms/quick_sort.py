from matplotlib import pyplot as plt
import numpy as np
import time
import sys
sys.setrecursionlimit(5000)


def min_value(lst, starting_p):
    x = starting_p

    for i in range(x + 1, len(lst)):
        if lst[i] < lst[x]:
            x = i
        return x

# list of values for which measurements will be taken
list = [100, 500, 1000, 3000, 5000]


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)

# list for execution times
times1 = []

# loop that performs sorting and measures time
for i in list:
    for j in range(10):
        test = np.random.randint(0, 5000, i)

        start = time.perf_counter_ns()
        sort_test = quicksort(test)
        finish = time.perf_counter_ns()

        t = finish - start
        times1.append(t)

    # calculation of the average execution time for a given value of i
    if i == 100:
        srQ1 = sum(times1) / 10
        print(srQ1)
    if i == 500:
        srQ2 = sum(times1) / 10
        print(srQ2)
    if i == 1000:
        srQ3 = sum(times1) / 10
        print(srQ3)
    if i == 3000:
        srQ4 = sum(times1) / 10
        print(srQ4)
    if i == 5000:
        srQ5 = sum(times1) / 10
        print(srQ5)

# List that keeps the average time for value i
scoreQ = [srQ1, srQ2, srQ3, srQ4, srQ5]

# Quick sort pessimistic


def quicksort_pes(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort_pes(left) + [pivot] + quicksort_pes(right)

times2 = []

for i in list:
    for j in range(10):
        test = sorted(np.random.randint(0, 5000, i))

        start = time.perf_counter_ns()
        sort_test = quicksort_pes(test)
        finish = time.perf_counter_ns()

        t = finish - start
        times2.append(t)

    if i == 100:
        srQp1 = sum(times2) / 10
        print(srQp1)
    if i == 500:
        srQp2 = sum(times2) / 10
        print(srQp2)
    if i == 1000:
        srQp3 = sum(times2) / 10
        print(srQp3)
    if i == 3000:
        srQp4 = sum(times2) / 10
        print(srQp4)
    if i == 5000:
        srQp5 = sum(times2) / 10
        print(srQp5)

scoreQp = [srQp1, srQp2, srQp3, srQp4, srQp5]

# Quick sort optimistic


def quicksort_op(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort_op(left) + [pivot] + quicksort_op(right)

times3 = []

for i in list:
    for j in range(10):
        random_value = np.random.randint(0, 5000)
        test = [random_value for _ in range(i)]


        start = time.perf_counter_ns()
        sort_test = quicksort_op(test)
        finish = time.perf_counter_ns()

        t = finish - start
        times3.append(t)


    if i == 100:
        srQo1 = sum(times3)/10
        print(srQo1)
    if i == 500:
        srQo2 = sum(times3)/10
        print(srQo2)
    if i == 1000:
        srQo3 = sum(times3)/10
        print(srQo3)
    if i == 3000:
        srQo4 = sum(times3)/10
        print(srQo4)
    if i == 5000:
        srQo5 = sum(times3)/10
        print(srQo5)

scoreQo = [srQo1, srQo2, srQo3, srQo4, srQo5]

# Displaying function plots
plt.plot(list, scoreQ, label = "Average value Quick sort")
plt.plot(list, scoreQp, label = "Pessimistic value Quick sort")
plt.plot(list, scoreQo, label = "Optimistic value Quick sort")
plt.title("Quick sort")
plt.legend()
plt.xlabel("Number of numbers in the vector")
plt.ylabel("Amount of time")
plt.show()
