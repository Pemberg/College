import random


class MaxHeap:
    def __init__(self, numbers):
        self.numbers = numbers
        self.build_heap()

    # Function to swap two elements in the list
    def swap(self, i, j):
        self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]

    # Function to "fix" the heap - ensures that every node has a value greater than its children
    def heapify(self, parent_index, end_index):
        largest_index = parent_index
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        # Check if the left child exists and is greater than the parent
        if left_child_index < end_index and self.numbers[left_child_index] > self.numbers[largest_index]:
            largest_index = left_child_index

        # Check if the right child exists and is greater than the parent or the left child
        if right_child_index < end_index and self.numbers[right_child_index] > self.numbers[largest_index]:
            largest_index = right_child_index

        # If the largest element is not the parent, swap parent with the largest child and recursively fix the heap
        if largest_index != parent_index:
            self.swap(parent_index, largest_index)
            self.heapify(largest_index, end_index)

    # Method to build the maximum heap
    def build_heap(self):
        for i in range(len(self.numbers)//2 - 1, -1, -1):
            self.heapify(i, len(self.numbers))

    # Method to print the heap in a pyramid form
    def print_heap_pyramid(self):
        current_index = 0
        level = 0
        level_size = 1

        while current_index < len(self.numbers):
            print(" " * (len(self.numbers)//2 - level), end="")
            for i in range(level_size):
                if current_index < len(self.numbers):
                    print(str(self.numbers[current_index]).center(3), end="")
                    current_index += 1
            print()
            level += 1
            level_size = 2 ** level

# Generate 10 random numbers from 0 to 20
numbers = random.sample(range(21), 10)

# Create a MaxHeap object based on these numbers
heap = MaxHeap(numbers)
print("Maximum heap in pyramid form:")
heap.print_heap_pyramid()

